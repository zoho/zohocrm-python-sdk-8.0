"""
Multi-Database Support for Zoho CRM SDK via SQLAlchemy
Matches official MySQL DBStore behavior but supports any SQL database
"""

try:
    from zohocrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
    from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from zohocrmsdk.src.com.zoho.crm.api.user_signature import UserSignature

except Exception:
    from .token_store import TokenStore
    from ..oauth_token import OAuthToken
    from ....crm.api.util.constants import Constants
    from ....crm.api.exception.sdk_exception import SDKException
    from ....crm.api.user_signature import UserSignature

try:
    from sqlalchemy import Column, String, Integer, Index, create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker, Session
    from sqlalchemy.engine import URL
    from sqlalchemy.sql import func
except ImportError:
    raise ImportError(Constants.SQLALCHEMY_IMPORT_ERROR)

from typing import Optional, List
import logging
import uuid

logger = logging.getLogger(__name__)

Base = declarative_base()


class ZohoOAuthToken(Base):
    """
    SQLAlchemy model for storing Zoho OAuth tokens.
    Schema matches official MySQL implementation exactly.
    """

    __tablename__ = "oauthtoken"

    # Fields match official MySQL schema
    id = Column(String(36), primary_key=True)
    user_name = Column(String(255), nullable=True)
    client_id = Column(String(255), nullable=True)
    client_secret = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    access_token = Column(String(255), nullable=True)
    grant_token = Column(String(255), nullable=True)
    expiry_time = Column(String(20), nullable=True)
    redirect_url = Column(String(255), nullable=True)
    api_domain = Column(String(255), nullable=True)

    __table_args__ = (
        Index('idx_user_name', 'user_name'),
        Index('idx_grant_token', 'grant_token'),
        Index('idx_refresh_token', 'refresh_token'),
        Index('idx_access_token', 'access_token'),
    )

    def __repr__(self):
        return f"<ZohoOAuthToken(id={self.id}, user_name={self.user_name})>"


class MultiDBStore(TokenStore):
    """
    Multi-database token store supporting any SQL database via SQLAlchemy.
    Provides same functionality as official MySQL DBStore with broader database support.

    Supported databases: PostgreSQL, MySQL, SQLite, MariaDB, Oracle, SQL Server, etc.

    Example:
        ##### PostgreSQL
        store = MultiDBStore(
            database_driver='postgresql+psycopg2',
            database_host='localhost',
            database_name='zoho_crm',
            database_user_name='postgres',
            database_password='password',
            database_port='5432'
        )

        ##### MySQL
        store = MultiDBStore(
            database_driver='mysql+pymysql',
            database_host='localhost',
            database_name='zohooauth',
            database_user_name='root',
            database_password='password',
            database_port='3306'
        )

        ##### SQLite
        store = MultiDBStore(
            database_driver='sqlite',
            database_host='',
            database_name='zoho_tokens.db',
            database_user_name='',
            database_password=''
        )
    """

    def __init__(
        self,
        database_driver: str,
        database_host: str,
        database_name: str,
        database_user_name: str,
        database_password: str = "",
        database_port: str = None,
        table_name: str = "oauthtoken"
    ):
        """
        Creates a MultiDBStore class instance with the specified parameters.

        Parameters:
            database_driver (str): SQLAlchemy driver (e.g., 'postgresql+psycopg2', 'mysql+pymysql')
            database_host (str): Database host address
            database_name (str): Database name
            database_user_name (str): Database username
            database_password (str): Database password. Default value is an empty string
            database_port (str): Database port. Uses driver default if None
            table_name (str): Table name for storing tokens. Default value is 'oauthtoken'
        """

        self.__database_driver = database_driver
        self.__database_host = database_host
        self.__database_name = database_name
        self.__database_user_name = database_user_name
        self.__database_password = database_password
        self.__database_port = database_port
        self.__table_name = table_name

        # Build database URL
        try:
            if database_driver.startswith('sqlite'):
                database_url = f"{database_driver}:///{database_name}"
            else:
                database_url = URL.create(
                    drivername=database_driver,
                    username=database_user_name,
                    password=database_password,
                    host=database_host,
                    port=int(database_port) if database_port else None,
                    database=database_name
                )

            # Create engine with connection pooling
            self.__engine = create_engine(
                database_url,
                pool_size=10,
                max_overflow=20,
                pool_pre_ping=True,
                pool_recycle=3600
            )

            # Create session factory
            self.__session_factory = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.__engine
            )

            # Create tables if they don't exist
            Base.metadata.create_all(bind=self.__engine)

            logger.info(f"MultiDBStore initialized with {database_driver} database")

        except Exception as ex:
            logger.error(f"Failed to initialize MultiDBStore: {str(ex)}", exc_info=True)
            raise SDKException(
                code=Constants.TOKEN_STORE,
                message=f"Database initialization failed: {str(ex)}",
                cause=ex
            )

    def get_database_driver(self) -> str:
        """
        This is a getter method to get database driver.

        Returns:
            string: A string representing database driver
        """
        return self.__database_driver

    def get_database_host(self) -> str:
        """
        This is a getter method to get database host.

        Returns:
            string: A string representing database host
        """
        return self.__database_host

    def get_database_name(self) -> str:
        """
        This is a getter method to get database name.

        Returns:
            string: A string representing database name
        """
        return self.__database_name

    def get_database_user_name(self) -> str:
        """
        This is a getter method to get database user name.

        Returns:
            string: A string representing database user name
        """
        return self.__database_user_name

    def get_database_password(self) -> str:
        """
        This is a getter method to get database password.

        Returns:
            string: A string representing database password
        """
        return self.__database_password

    def get_database_port(self) -> str:
        """
        This is a getter method to get database port.

        Returns:
            string: A string representing database port
        """
        return self.__database_port

    def get_table_name(self) -> str:
        """
        This is a getter method to get table name.

        Returns:
            string: A string representing table name
        """
        return self.__table_name

    @staticmethod
    def are_all_objects_null(objects: List) -> bool:
        """
        Check if all objects in list are None.

        Parameters:
            objects (list): List of objects to check

        Returns:
            bool: True if all objects are None, False otherwise
        """
        return all(obj is None for obj in objects)

    @staticmethod
    def set_merge_data(oauth_token: OAuthToken, record: ZohoOAuthToken) -> None:
        """
        Merge database record into token object.
        Only populates fields that are None in the token object.
        Matches official MySQL implementation behavior.

        Parameters:
            oauth_token (OAuthToken): Token object to populate
            record (ZohoOAuthToken): Database record
        """
        if record is None:
            return

        if oauth_token.get_id() is None and record.id is not None:
            oauth_token.set_id(record.id)

        if oauth_token.get_user_signature() is None and record.user_name is not None:
            oauth_token.set_user_signature(UserSignature(record.user_name))

        if oauth_token.get_client_id() is None and record.client_id is not None:
            oauth_token.set_client_id(record.client_id)

        if oauth_token.get_client_secret() is None and record.client_secret is not None:
            oauth_token.set_client_secret(record.client_secret)

        if oauth_token.get_refresh_token() is None and record.refresh_token is not None:
            oauth_token.set_refresh_token(record.refresh_token)

        if oauth_token.get_access_token() is None and record.access_token is not None:
            oauth_token.set_access_token(record.access_token)

        if oauth_token.get_grant_token() is None and record.grant_token is not None:
            oauth_token.set_grant_token(record.grant_token)

        if oauth_token.get_expires_in() is None and record.expiry_time is not None:
            oauth_token.set_expires_in(record.expiry_time)

        if oauth_token.get_redirect_url() is None and record.redirect_url is not None:
            oauth_token.set_redirect_url(record.redirect_url)

        if oauth_token.get_api_domain() is None and record.api_domain is not None:
            oauth_token.set_api_domain(record.api_domain)

    @staticmethod
    def set_oauth_token_empty(oauth_token: OAuthToken) -> None:
        """
        Initialize all token fields to None.
        Matches official implementation.

        Parameters:
            oauth_token (OAuthToken): Token object to initialize
        """
        oauth_token.set_id(None)
        oauth_token.set_user_signature(None)
        oauth_token.set_client_id(None)
        oauth_token.set_client_secret(None)
        oauth_token.set_refresh_token(None)
        oauth_token.set_access_token(None)
        oauth_token.set_grant_token(None)
        oauth_token.set_redirect_url(None)
        oauth_token.set_expires_in(None)
        oauth_token.set_api_domain(None)

    def find_token(self, token: OAuthToken) -> Optional[OAuthToken]:
        """
        Retrieve token from database matching official MySQL logic.

        Lookup priority (matches official implementation):
        1. user_signature (if present)
        2. access_token (if client_id AND client_secret are both NULL)
        3. grant_token (if present with client_id AND client_secret)
        4. refresh_token (if present with client_id AND client_secret)

        Parameters:
            token (OAuthToken): Token object with search criteria

        Returns:
            OAuthToken: Populated token object, or None if not found

        Raises:
            SDKException: If database operation fails
        """
        db = self.__session_factory()
        try:
            if not isinstance(token, OAuthToken):
                return None

            query = db.query(ZohoOAuthToken)

            # Priority 1: Lookup by user_signature
            if token.get_user_signature() is not None:
                name = token.get_user_signature().get_name()
                if name and len(name) > 0:
                    query = query.filter(ZohoOAuthToken.user_name == name)

            # Priority 2: Lookup by access_token (ONLY if client_id AND client_secret are BOTH None)
            elif (token.get_access_token() is not None and
                  self.are_all_objects_null([token.get_client_id(), token.get_client_secret()])):
                query = query.filter(ZohoOAuthToken.access_token == token.get_access_token())

            # Priority 3: Lookup by grant_token or refresh_token (with client credentials)
            elif ((token.get_refresh_token() is not None or token.get_grant_token() is not None) and
                  token.get_client_id() is not None and token.get_client_secret() is not None):

                if token.get_grant_token() is not None and len(token.get_grant_token()) > 0:
                    query = query.filter(ZohoOAuthToken.grant_token == token.get_grant_token())
                elif token.get_refresh_token() is not None and len(token.get_refresh_token()) > 0:
                    query = query.filter(ZohoOAuthToken.refresh_token == token.get_refresh_token())

            # Add LIMIT 1 (matches official MySQL query)
            result = query.first()

            if result is not None:
                self.set_merge_data(token, result)
                return token

            return None

        except Exception as ex:
            logger.error(f"Error finding token: {str(ex)}", exc_info=True)
            raise SDKException(code=Constants.TOKEN_STORE,
                             message=Constants.GET_TOKEN_DB_ERROR1,
                             cause=ex)
        finally:
            db.close()

    def find_token_by_id(self, token_id: str) -> Optional[OAuthToken]:
        """
        Retrieve token by ID from database.
        Matches official behavior - throws exception if not found.

        Parameters:
            token_id (str): Token ID as string

        Returns:
            OAuthToken: Populated token object

        Raises:
            SDKException: If token not found or database operation fails
        """
        db = self.__session_factory()
        try:
            result = db.query(ZohoOAuthToken).filter(
                ZohoOAuthToken.id == token_id
            ).first()

            if result is None:
                raise SDKException(code=Constants.TOKEN_STORE,
                                 message=Constants.GET_TOKEN_BY_ID_DB_ERROR)

            oauth_token = object.__new__(OAuthToken)
            self.set_oauth_token_empty(oauth_token)
            self.set_merge_data(oauth_token, result)

            return oauth_token

        except SDKException:
            raise
        except Exception as ex:
            logger.error(f"Error finding token by id {token_id}: {str(ex)}", exc_info=True)
            raise SDKException(code=Constants.TOKEN_STORE,
                             message=Constants.GET_TOKEN_BY_ID_DB_ERROR,
                             cause=ex)
        finally:
            db.close()

    def save_token(self, token: OAuthToken) -> None:
        """
        Save token to database matching official MySQL update/insert logic.

        Logic (matches official implementation):
        1. Try UPDATE first based on lookup criteria
        2. If no rows updated, INSERT new record

        Parameters:
            token (OAuthToken): Token object to save

        Raises:
            SDKException: If token validation fails or database operation fails
        """
        db = self.__session_factory()
        try:
            if not isinstance(token, OAuthToken):
                return

            existing_token = None

            # Priority 1: user_signature
            if token.get_user_signature() is not None:
                name = token.get_user_signature().get_name()
                if name and len(name) > 0:
                    existing_token = db.query(ZohoOAuthToken).filter(
                        ZohoOAuthToken.user_name == name
                    ).first()

            # Priority 2: access_token (if client credentials are None)
            elif (token.get_access_token() is not None and len(token.get_access_token()) > 0 and
                  self.are_all_objects_null([token.get_client_id(), token.get_client_secret()])):
                existing_token = db.query(ZohoOAuthToken).filter(
                    ZohoOAuthToken.access_token == token.get_access_token()
                ).first()

            # Priority 3: grant_token or refresh_token (with client credentials)
            elif ((token.get_refresh_token() is not None and len(token.get_refresh_token()) > 0) or
                  (token.get_grant_token() is not None and len(token.get_grant_token()) > 0)) and \
                  token.get_client_id() is not None and token.get_client_secret() is not None:

                if token.get_grant_token() is not None and len(token.get_grant_token()) > 0:
                    existing_token = db.query(ZohoOAuthToken).filter(
                        ZohoOAuthToken.grant_token == token.get_grant_token()
                    ).first()
                elif token.get_refresh_token() is not None and len(token.get_refresh_token()) > 0:
                    existing_token = db.query(ZohoOAuthToken).filter(
                        ZohoOAuthToken.refresh_token == token.get_refresh_token()
                    ).first()

            if existing_token:
                # UPDATE existing token
                if token.get_user_signature() is not None:
                    existing_token.user_name = token.get_user_signature().get_name()
                if token.get_client_id() is not None:
                    existing_token.client_id = token.get_client_id()
                if token.get_client_secret() is not None:
                    existing_token.client_secret = token.get_client_secret()
                if token.get_refresh_token() is not None:
                    existing_token.refresh_token = token.get_refresh_token()
                if token.get_access_token() is not None:
                    existing_token.access_token = token.get_access_token()
                if token.get_grant_token() is not None:
                    existing_token.grant_token = token.get_grant_token()
                if token.get_expires_in() is not None:
                    existing_token.expiry_time = token.get_expires_in()
                if token.get_redirect_url() is not None:
                    existing_token.redirect_url = token.get_redirect_url()
                if token.get_api_domain() is not None:
                    existing_token.api_domain = token.get_api_domain()

                db.commit()
                token.set_id(existing_token.id)
                logger.debug(f"Updated token with id {existing_token.id}")

            else:
                # INSERT new token
                if (token.get_refresh_token() is None and
                    token.get_grant_token() is None and
                    token.get_access_token() is None):
                    raise SDKException(code=Constants.TOKEN_STORE,
                                     message=Constants.GET_TOKEN_DB_ERROR1)

                # Generate UUID if not present
                if token.get_id() is None:
                    new_id = str(uuid.uuid4())
                    token.set_id(new_id)

                new_token = ZohoOAuthToken(
                    id=token.get_id(),
                    user_name=token.get_user_signature().get_name() if token.get_user_signature() else None,
                    client_id=token.get_client_id(),
                    client_secret=token.get_client_secret(),
                    refresh_token=token.get_refresh_token(),
                    access_token=token.get_access_token(),
                    grant_token=token.get_grant_token(),
                    expiry_time=token.get_expires_in(),
                    redirect_url=token.get_redirect_url(),
                    api_domain=token.get_api_domain()
                )

                db.add(new_token)
                db.commit()
                logger.debug(f"Inserted new token with id {new_token.id}")

        except SDKException:
            db.rollback()
            raise
        except Exception as ex:
            db.rollback()
            logger.error(f"Error saving token: {str(ex)}", exc_info=True)
            raise SDKException(code=Constants.TOKEN_STORE,
                             message=Constants.SAVE_TOKEN_DB_ERROR,
                             cause=ex)
        finally:
            db.close()

    def delete_token(self, token_id: str) -> None:
        """
        Delete token by ID from database.

        Parameters:
            token_id (str): Token ID to delete

        Raises:
            SDKException: If database operation fails
        """
        db = self.__session_factory()
        try:
            db.query(ZohoOAuthToken).filter(
                ZohoOAuthToken.id == token_id
            ).delete()
            db.commit()
            logger.debug(f"Deleted token with id {token_id}")

        except Exception as ex:
            db.rollback()
            logger.error(f"Error deleting token {token_id}: {str(ex)}", exc_info=True)
            raise SDKException(code=Constants.TOKEN_STORE,
                             message=Constants.DELETE_TOKEN_DB_ERROR,
                             cause=ex)
        finally:
            db.close()

    def get_tokens(self) -> List[OAuthToken]:
        """
        Retrieve all tokens from database.

        Returns:
            list: List of OAuthToken objects

        Raises:
            SDKException: If database operation fails
        """
        db = self.__session_factory()
        try:
            results = db.query(ZohoOAuthToken).all()
            tokens = []

            for result in results:
                oauth_token = object.__new__(OAuthToken)
                self.set_oauth_token_empty(oauth_token)
                self.set_merge_data(oauth_token, result)
                tokens.append(oauth_token)

            logger.debug(f"Retrieved {len(tokens)} tokens from database")
            return tokens

        except Exception as ex:
            logger.error(f"Error retrieving tokens: {str(ex)}", exc_info=True)
            raise SDKException(code=Constants.TOKEN_STORE,
                             message=Constants.GET_TOKENS_DB_ERROR,
                             cause=ex)
        finally:
            db.close()

    def delete_tokens(self) -> None:
        """
        Delete all tokens from database.

        Raises:
            SDKException: If database operation fails
        """
        db = self.__session_factory()
        try:
            db.query(ZohoOAuthToken).delete()
            db.commit()
            logger.debug("Deleted all tokens from database")

        except Exception as ex:
            db.rollback()
            logger.error(f"Error deleting all tokens: {str(ex)}", exc_info=True)
            raise SDKException(code=Constants.TOKEN_STORE,
                             message=Constants.DELETE_TOKENS_DB_ERROR,
                             cause=ex)
        finally:
            db.close()

    def close(self) -> None:
        """
        Close database engine and cleanup resources.
        Call this when shutting down the application.
        """
        try:
            self.__engine.dispose()
            logger.info("MultiDBStore engine disposed successfully")
        except Exception as ex:
            logger.error(f"Error closing database engine: {str(ex)}", exc_info=True)