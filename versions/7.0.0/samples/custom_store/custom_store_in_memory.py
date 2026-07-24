from sqlite3 import Error

from zohocrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
from zohocrmsdk.src.com.zoho.crm.api.user_signature import UserSignature

import sqlite3


class CustomStore(TokenStore):
    """
    This class to store user token details to the MySQL DataBase.
    """

    def __init__(self):

        """
        Creates a DBStore class instance with the specified parameters.
        """
        self.db_name = ':memory:'
        self.connection = sqlite3.connect(self.db_name)
        if not self.check_table_exists():
            cursor = self.connection.cursor()
            cursor.execute(
                "CREATE TABLE oauthtoken (id varchar(10) NOT NULL,user_name varchar(255), client_id varchar(255), "
                "client_secret varchar(255), refresh_token varchar(255), access_token varchar(255), grant_token "
                "varchar(255), expiry_time varchar(20), redirect_url varchar(255), api_domain varchar(255), "
                "primary key (id))")
            cursor.close()

    @staticmethod
    def are_all_objects_null(object1):
        for obj in object1:
            if obj is not None:
                return False
        return True

    def find_token(self, token):
        cursor = None
        try:
            if isinstance(token, OAuthToken):
                oauth_token = token
                query = "select * from oauthtoken"
                if oauth_token.get_user_signature() is not None:
                    name = oauth_token.get_user_signature().get_name()
                    if name is not None and len(name) > 0:
                        query = query + " where user_name='" + name + "'"
                elif oauth_token.get_access_token() is not None and self.are_all_objects_null(
                        [oauth_token.get_client_id(), oauth_token.get_client_secret()]):
                    query = query + " where access_token='" + oauth_token.get_access_token() + "'"
                elif oauth_token.get_refresh_token() is not None or oauth_token.get_grant_token() is not None and \
                        oauth_token.get_client_id() is not None and oauth_token.get_client_secret() is not None:
                    if oauth_token.get_grant_token() is not None and len(oauth_token.get_grant_token()) > 0:
                        query = query + " where grant_token='" + oauth_token.get_grant_token() + "'"
                    elif oauth_token.get_refresh_token() is not None and len(oauth_token.get_refresh_token()) > 0:
                        query = query + " where refresh_token='" + oauth_token.get_refresh_token() + "'"
                query = query + " limit 1"
                cursor = self.connection.cursor()
                cursor.execute(query)
                result = cursor.fetchone()
                if result is None:
                    return None
                self.set_merge_data(oauth_token, result)
        except Exception as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_DB_ERROR1, cause=ex)
        finally:
            cursor.close() if cursor is not None else None
        return token

    @staticmethod
    def get_data(next_record):
        return next_record if next_record is not None else None

    @staticmethod
    def set_merge_data(oauth_token, next_record):
        if oauth_token.get_id() is None:
            oauth_token.set_id(CustomStore.get_data(next_record[0]))
        if oauth_token.get_user_signature() is None:
            name = CustomStore.get_data(next_record[1])
            if name is not None:
                oauth_token.set_user_signature(UserSignature(name))
        if oauth_token.get_client_id() is None:
            oauth_token.set_client_id(CustomStore.get_data(next_record[2]))
        if oauth_token.get_client_secret() is None:
            oauth_token.set_client_secret(CustomStore.get_data(next_record[3]))
        if oauth_token.get_refresh_token() is None:
            oauth_token.set_refresh_token(CustomStore.get_data(next_record[4]))
        if oauth_token.get_access_token() is None:
            oauth_token.set_access_token(CustomStore.get_data(next_record[5]))
        if oauth_token.get_grant_token() is None:
            oauth_token.set_grant_token(CustomStore.get_data(next_record[6]))
        if oauth_token.get_expires_in() is None:
            expires_in = CustomStore.get_data(next_record[7])
            if expires_in is not None:
                oauth_token.set_expires_in(str(expires_in))
        if oauth_token.get_redirect_url() is None:
            oauth_token.set_redirect_url(CustomStore.get_data(next_record[8]))
        if oauth_token.get_api_domain() is None:
            oauth_token.set_api_domain(CustomStore.get_data(next_record[9]))

    def save_token(self, token):
        if not isinstance(token, OAuthToken):
            return
        cursor = None
        try:
            oauth_token = token
            query = "update oauthtoken set "
            if oauth_token.get_user_signature() is not None:
                name = oauth_token.get_user_signature().get_name()
                if name is not None and len(name) > 0:
                    query = query + self.set_token(oauth_token) + " where user_name='" + name + "'"
            elif oauth_token.get_access_token() is not None and len(oauth_token.get_access_token()) > 0 and \
                    self.are_all_objects_null([oauth_token.get_client_id(), oauth_token.get_client_secret()]):
                query = query + self.set_token(
                    oauth_token) + " where access_token='" + oauth_token.get_access_token() + "'"
            elif ((oauth_token.get_refresh_token() is not None and len(oauth_token.get_refresh_token()) > 0) or
                  (oauth_token.get_grant_token() is not None and len(oauth_token.get_grant_token()) > 0)) and \
                    oauth_token.get_client_id() is not None and oauth_token.get_client_secret() is not None:
                if oauth_token.get_grant_token() is not None and len(oauth_token.get_grant_token()) > 0:
                    query = query + self.set_token(
                        oauth_token) + " where grant_token='" + oauth_token.get_grant_token() + "'"
                elif oauth_token.get_refresh_token() is not None and len(oauth_token.get_refresh_token()) > 0:
                    query = query + self.set_token(
                        oauth_token) + " where refresh_token='" + oauth_token.get_refresh_token() + "'"
            query = query + " limit 1"
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                if cursor.rowcount <= 0:
                    if oauth_token.get_id() is not None or oauth_token.get_user_signature() is not None:
                        if oauth_token.get_refresh_token() is None and oauth_token.get_grant_token() is None and \
                                oauth_token.get_access_token() is None:
                            raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_DB_ERROR1)
                    if oauth_token.get_id() is None:
                        new_id = str(self.generate_id())
                        oauth_token.set_id(new_id)
                    query = "insert into oauthtoken (id,user_name,client_id,client_secret,refresh_token,access_token," \
                            "grant_token,expiry_time,redirect_url,api_domain) values (?,?,?,?,?,?,?,?,?,?);"
                    val = (token.get_id(),
                           token.get_user_signature().get_name() if token.get_user_signature() is not None else None,
                           token.get_client_id(), token.get_client_secret(), token.get_refresh_token(),
                           token.get_access_token(), token.get_grant_token(), token.get_expires_in(),
                           token.get_redirect_url(), token.get_api_domain())
                    cursor.execute(query, val)
            except Error as e:
                raise e
            finally:
                self.connection.commit()
                cursor.close() if cursor is not None else None
        except Exception as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.SAVE_TOKEN_DB_ERROR, cause=ex)

    @staticmethod
    def set_oauth_token(oauth_token):
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

    def set_token(self, oauth_token):
        query = []
        if oauth_token.get_user_signature() is not None:
            name = oauth_token.get_user_signature().get_name()
            if name is not None and len(name) > 0:
                query.append(self.set_token_info(Constants.USER_NAME, name))
        if oauth_token.get_api_domain() is not None:
            query.append(self.set_token_info(Constants.API_DOMAIN, oauth_token.get_api_domain()))
        if oauth_token.get_client_id() is not None:
            query.append(self.set_token_info(Constants.CLIENT_ID, oauth_token.get_client_id()))
        if oauth_token.get_client_secret() is not None:
            query.append(self.set_token_info(Constants.CLIENT_SECRET, oauth_token.get_client_secret()))
        if oauth_token.get_refresh_token() is not None:
            query.append(self.set_token_info(Constants.REFRESH_TOKEN, oauth_token.get_refresh_token()))
        if oauth_token.get_access_token() is not None:
            query.append(self.set_token_info(Constants.ACCESS_TOKEN, oauth_token.get_access_token()))
        if oauth_token.get_grant_token() is not None:
            query.append(self.set_token_info(Constants.GRANT_TOKEN, oauth_token.get_grant_token()))
        if oauth_token.get_expires_in() is not None:
            query.append(self.set_token_info(Constants.EXPIRY_TIME, oauth_token.get_expires_in()))
        if oauth_token.get_redirect_url() is not None:
            query.append(self.set_token_info(Constants.REDIRECT_URL, oauth_token.get_redirect_url()))
        return str.join(",", query)

    @staticmethod
    def set_token_info(key, value):
        return key + "='" + value + "'"

    def delete_token(self, id):
        cursor = None
        try:
            try:
                cursor = self.connection.cursor()
                query = "delete from oauthtoken where id= " + id + ";"
                cursor.execute(query)
                self.connection.commit()
            except Error as ex:
                raise ex
            finally:
                cursor.close() if cursor is not None else None
        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKEN_DB_ERROR, cause=ex)

    def get_tokens(self):
        cursor = None
        try:
            tokens = []
            try:
                cursor = self.connection.cursor()
                query = "select * from oauthtoken;"
                cursor.execute(query)
                results = cursor.fetchall()
                for result in results:
                    oauth_token = object.__new__(OAuthToken)
                    self.set_oauth_token(oauth_token)
                    self.set_merge_data(oauth_token, result)
                    tokens.append(oauth_token)
                return tokens
            except Error as ex:
                raise ex
            finally:
                cursor.close() if cursor is not None else None
        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKENS_DB_ERROR, cause=ex)

    def delete_tokens(self):
        cursor = None
        try:
            try:
                cursor = self.connection.cursor()
                query = "delete from oauthtoken;"
                cursor.execute(query)
                self.connection.commit()
            except Error as ex:
                raise ex
            finally:
                cursor.close() if cursor is not None else None
        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKENS_DB_ERROR, cause=ex)

    def find_token_by_id(self, id):
        cursor = None
        try:
            try:
                query = "select * from oauthtoken where id='" + id + "'"
                oauth_token = object.__new__(OAuthToken)
                self.set_oauth_token(oauth_token)
                cursor = self.connection.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                if results is None or len(results) <= 0:
                    raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_BY_ID_DB_ERROR)
                for result in results:
                    self.set_merge_data(oauth_token, result)
                    return oauth_token
            except Error as ex:
                raise ex
            finally:
                cursor.close() if cursor is not None else None
        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_BY_ID_DB_ERROR, cause=ex)

    def generate_id(self):
        cursor = None
        try:
            query = "select  max(id) as id from oauthtoken;"
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            max1 = result[0]
            if max1 is None:
                return 1
            else:
                return int(max1) + 1
        except Exception as e1:
            raise SDKException(Constants.TOKEN_STORE, Constants.GENERATE_TOKEN_ID_ERROR, cause=e1)
        finally:
            cursor.close() if cursor is not None else None

    def check_table_exists(self):
        cursor = None
        try:
            cursor = self.connection.cursor()
            # Query to check if table exists
            cursor.execute("SELECT * FROM oauthtoken limit 1")
            table = cursor.fetchone()
            return table is not None
        except Exception:
            return False
        finally:
            cursor.close() if cursor is not None else None
