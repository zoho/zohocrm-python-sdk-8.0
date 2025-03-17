try:
    from zohocrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
    from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from zohocrmsdk.src.com.zoho.crm.api.user_signature import UserSignature

except Exception as e:
    from .token_store import TokenStore
    from ..oauth_token import OAuthToken
    from ....crm.api.util.constants import Constants
    from ....crm.api.exception.sdk_exception import SDKException
    from ....crm.api.user_signature import UserSignature


class DBStore(TokenStore):

    """
    This class to store user token details to the MySQL DataBase.
    """

    def __init__(self, host=Constants.MYSQL_HOST, database_name=Constants.MYSQL_DATABASE_NAME,
                 user_name=Constants.MYSQL_USER_NAME, password="", port_number=Constants.MYSQL_PORT_NUMBER,
                 table_name=Constants.MYSQL_TABLE_NAME):

        """
        Creates a DBStore class instance with the specified parameters.

        Parameters:
            host (str) : A string containing the DataBase host name. Default value is localhost
            database_name (str) : A string containing the DataBase name. Default value is zohooauth
            user_name (str) : A string containing the DataBase user name. Default value is root
            password (str) : A string containing the DataBase password. Default value is an empty string
            port_number (str) : A string containing the DataBase port number. Default value is 3306
        """

        self.__host = host
        self.__database_name = database_name
        self.__user_name = user_name
        self.__password = password
        self.__port_number = port_number
        self.__table_name = table_name

    def get_host(self):
        """
        This is a getter method to get __host.

        Returns:
            string: A string representing __host
        """

        return self.__host

    def get_database_name(self):
        """
        This is a getter method to get __database_name.

        Returns:
            string: A string representing __database_name
        """

        return self.__database_name

    def get_user_name(self):
        """
        This is a getter method to get __user_name.

        Returns:
            string: A string representing __user_name
        """

        return self.__user_name

    def get_password(self):
        """
        This is a getter method to get __password.

        Returns:
            string: A string representing __password
        """
        return self.__password

    def get_port_number(self):
        """
        This is a getter method to get __port_number.

        Returns:
            string: A string representing __port_number
        """

        return self.__port_number

    def get_table_name(self):
        """
        This is a getter method to get __table_name.

        Returns:
            string: A string representing __table_name
        """

        return self.__table_name

    @staticmethod
    def are_all_objects_null(object1):
        for obj in object1:
            if obj is not None:
                return False
        return True

    def find_token(self, token):
        try:
            import mysql.connector
            from mysql.connector import Error
        except Exception:
            import mysql.connector
            from mysql.connector import Error
        cursor = None
        connection = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)
            if isinstance(token, OAuthToken):
                oauth_token = token
                query = "select * from " + self.__table_name
                if oauth_token.get_user_signature() is not None:
                    name = oauth_token.get_user_signature().get_name()
                    if name is not None and len(name) > 0:
                        query = query + " where user_name='" + name + "'"
                elif oauth_token.get_access_token() is not None and self.are_all_objects_null([oauth_token.get_client_id(), oauth_token.get_client_secret()]):
                    query= query + " where access_token='" + oauth_token.get_access_token() + "'"
                elif oauth_token.get_refresh_token() is not None or oauth_token.get_grant_token() is not None and oauth_token.get_client_id() is not None and oauth_token.get_client_secret() is not None:
                    if oauth_token.get_grant_token() is not None and len(oauth_token.get_grant_token()) > 0:
                        query = query + " where grant_token='" + oauth_token.get_grant_token() + "'"
                    elif oauth_token.get_refresh_token() is not None and len(oauth_token.get_refresh_token()) > 0:
                        query = query + " where refresh_token='" + oauth_token.get_refresh_token() + "'"
                query = query + " limit 1"
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchone()
                if result is None:
                    return None
                self.set_merge_data(oauth_token, result)

        except Exception as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_DB_ERROR1, cause=ex)

        finally:
            cursor.close() if cursor is not None else None
            connection.close() if connection is not None else None
        return token

    @staticmethod
    def get_data(next_record):
        return next_record if next_record is not None else None

    @staticmethod
    def set_merge_data(oauth_token, nextRecord):
        if oauth_token.get_id() is None:
            oauth_token.set_id(DBStore.get_data(nextRecord[0]))
        if oauth_token.get_user_signature() is None:
            name = DBStore.get_data(nextRecord[1])
            if name is not None:
                oauth_token.set_user_signature(UserSignature(name))
        if oauth_token.get_client_id() is None:
            oauth_token.set_client_id(DBStore.get_data(nextRecord[2]))
        if oauth_token.get_client_secret() is None:
            oauth_token.set_client_secret(DBStore.get_data(nextRecord[3]))
        if oauth_token.get_refresh_token() is None:
            oauth_token.set_refresh_token(DBStore.get_data(nextRecord[4]))
        if oauth_token.get_access_token() is None:
            oauth_token.set_access_token(DBStore.get_data(nextRecord[5]))
        if oauth_token.get_grant_token() is None:
            oauth_token.set_grant_token(DBStore.get_data(nextRecord[6]))
        if oauth_token.get_expires_in() is None:
            expiresIn = DBStore.get_data(nextRecord[7])
            if expiresIn is not None:
                oauth_token.set_expires_in(str(expiresIn))
        if oauth_token.get_redirect_url() is None:
            oauth_token.set_redirect_url(DBStore.get_data(nextRecord[8]))
        if oauth_token.get_api_domain() is None:
            oauth_token.set_api_domain(DBStore.get_data(nextRecord[9]))

    def save_token(self, token):
        try:
            import mysql.connector
            from mysql.connector import Error
        except Exception:
            import mysql.connector
            from mysql.connector import Error
        cursor = None
        if not isinstance(token, OAuthToken):
            return
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name,password=self.__password, port=self.__port_number)
            oauthToken = token
            query = "update " + self.__table_name + " set "
            if oauthToken.get_user_signature() is not None:
                name = oauthToken.get_user_signature().get_name()
                if name is not None and len(name) > 0:
                    query = query + self.set_token(oauthToken) + " where user_name='" + name + "'"
            elif oauthToken.get_access_token() is not None and len(oauthToken.get_access_token()) > 0 and \
                    self.are_all_objects_null([oauthToken.get_client_id(), oauthToken.get_client_secret()]):
                query = query + self.set_token(oauthToken) + " where access_token='" + oauthToken.get_access_token() + "'"
            elif ((oauthToken.get_refresh_token() is not None and len(oauthToken.get_refresh_token()) > 0) or
                  (oauthToken.get_grant_token() is not None and len(oauthToken.get_grant_token()) > 0)) and oauthToken.get_client_id() is not None and oauthToken.get_client_secret() is not None:
                if oauthToken.get_grant_token() is not None and len(oauthToken.get_grant_token()) > 0:
                    query = query + self.set_token(oauthToken) + " where grant_token='" + oauthToken.get_grant_token() + "'"
                elif oauthToken.get_refresh_token() is not None and len(oauthToken.get_refresh_token()) > 0:
                    query = query + self.set_token(oauthToken) + " where refresh_token='" + oauthToken.get_refresh_token() + "'"
            query = query + " limit 1"
            try:
                cursor = connection.cursor()
                cursor.execute(query)
                if cursor.rowcount <= 0:
                    if oauthToken.get_id() is not None or oauthToken.get_user_signature() is not None:
                        if oauthToken.get_refresh_token() is None and oauthToken.get_grant_token() is None and oauthToken.get_access_token() is None:
                            raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_DB_ERROR1)
                    if oauthToken.get_id() is None:
                        newId = str(self.generate_id())
                        oauthToken.set_id(newId)
                    query = "insert into " + self.__table_name + " (id,user_name,client_id,client_secret,refresh_token,access_token,grant_token,expiry_time,redirect_url,api_domain) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    val = (token.get_id(), token.get_user_signature().get_name() if token.get_user_signature() is not None else None, token.get_client_id(), token.get_client_secret(), token.get_refresh_token(), token.get_access_token(), token.get_grant_token(), token.get_expires_in(), token.get_redirect_url(), token.get_api_domain())
                    cursor.execute(query, val)
            except Error as e:
                raise e
            finally:
                connection.commit()
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None
        except Exception as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.SAVE_TOKEN_DB_ERROR, cause=ex)

    @staticmethod
    def set_oauth_token(oauthToken):
        oauthToken.set_id(None)
        oauthToken.set_user_signature(None)
        oauthToken.set_client_id(None)
        oauthToken.set_client_secret(None)
        oauthToken.set_refresh_token(None)
        oauthToken.set_access_token(None)
        oauthToken.set_grant_token(None)
        oauthToken.set_redirect_url(None)
        oauthToken.set_expires_in(None)
        oauthToken.set_api_domain(None)

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
        try:
            import mysql.connector
            from mysql.connector import Error
        except Exception:
            import mysql.connector
            from mysql.connector import Error
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)

            try:
                cursor = connection.cursor()
                query = "delete from " + self.__table_name + " where id= " + id + ";"
                cursor.execute(query)
                connection.commit()

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKEN_DB_ERROR, cause=ex)

    def get_tokens(self):
        try:
            import mysql.connector
            from mysql.connector import Error
        except Exception:
            import mysql.connector
            from mysql.connector import Error
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)
            tokens = []

            try:
                cursor = connection.cursor()
                query = 'select * from ' + self.__table_name + ";"
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
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKENS_DB_ERROR, cause=ex)

    def delete_tokens(self):
        try:
            import mysql.connector
            from mysql.connector import Error
        except Exception:
            import mysql.connector
            from mysql.connector import Error
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)

            try:
                cursor = connection.cursor()
                query = 'delete from ' + self.__table_name + ";"
                cursor.execute(query)
                connection.commit()

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None
        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKENS_DB_ERROR, cause=ex)

    def find_token_by_id(self, id):
        try:
            import mysql.connector
            from mysql.connector import Error
        except Exception:
            import mysql.connector
            from mysql.connector import Error
        cursor = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)
            try:
                query = "select * from " + self.__table_name + " where id='" + id + "'"
                oauthToken = object.__new__(OAuthToken)
                self.set_oauth_token(oauthToken)
                cursor = connection.cursor()
                cursor.execute(query)
                results = cursor.fetchall()
                if results is None or len(results) <= 0:
                    raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_BY_ID_DB_ERROR)
                for result in results:
                    self.set_merge_data(oauthToken, result)
                    return oauthToken

            except Error as ex:
                raise ex

            finally:
                cursor.close() if cursor is not None else None
                connection.close() if connection is not None else None

        except Error as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_BY_ID_DB_ERROR, cause=ex)

    def generate_id(self):
        try:
            import mysql.connector
            from mysql.connector import Error
        except Exception:
            import mysql.connector
            from mysql.connector import Error
        cursor = None
        connection = None
        try:
            connection = mysql.connector.connect(host=self.__host, database=self.__database_name, user=self.__user_name, password=self.__password, port=self.__port_number)
            query = "select  max(id) as id from " + self.__table_name + ";"
            cursor = connection.cursor()
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
            cursor.close() if connection is not None else None
            connection.close() if connection is not None else None