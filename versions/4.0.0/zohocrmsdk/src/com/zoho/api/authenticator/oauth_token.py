try:
    import threading
    import logging
    import enum
    import json
    import time
    import requests
    from .token import Token
    from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
    from ...crm.api.util import APIHTTPConnector
    from ...crm.api.util import Utility
    from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
    from ...crm.api.util.constants import Constants
    from ...crm.api.user_signature import UserSignature
    from zohocrmsdk.src.com.zoho.crm.api.dc.data_center import DataCenter

except Exception as e:
    import threading
    import logging
    import enum
    import json
    import time
    import requests
    from .token import Token
    from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
    from ...crm.api.util import APIHTTPConnector
    from ...crm.api.util import Utility
    from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
    from ...crm.api.util.constants import Constants
    from ...crm.api.dc.data_center import DataCenter


class OAuthToken(Token):
    """
    This class maintains the tokens and authenticates every request.
    """

    logger = logging.getLogger('SDKLogger')
    lock = threading.Lock()

    def __init__(self, client_id=None, client_secret=None, grant_token=None, refresh_token=None, redirect_url=None,
                 id=None, access_token=None, user_signature=None, api_domain=None, find_user=True):

        """
        Creates an OAuthToken class instance with the specified parameters.

        Parameters:
            client_id (str) : A string containing the OAuth client id.
            client_secret (str) : A string containing the OAuth client secret.
            grant_token (str) : A string containing the GRANT token.
            refresh_token (str) : A string containing the REFRESH token.
            redirect_url (str) : A string containing the OAuth redirect URL. Default value is None
            id (str) : A string containing the Id. Default value is None
            user_signature(UserSignature) : An instance of UserSignature
            api_domain(str) : A string containing the api_domain
        """

        error = {}

        if grant_token is None and refresh_token is None and id is None and access_token is None and user_signature is None:
            raise SDKException(code=Constants.MANDATORY_VALUE_ERROR, message=Constants.MANDATORY_KEY_ERROR,
                               details=Constants.OAUTH_MANDATORY_KEYS)

        if id is None and access_token is None and user_signature is None:
            if not isinstance(client_id, str):
                error[Constants.FIELD] = Constants.CLIENT_ID
                error[Constants.EXPECTED_TYPE] = Constants.STRING
                error[Constants.CLASS] = OAuthToken.__name__
                raise SDKException(code=Constants.TOKEN_ERROR, details=error)

            if not isinstance(client_secret, str):
                error[Constants.FIELD] = Constants.CLIENT_SECRET
                error[Constants.EXPECTED_TYPE] = Constants.STRING
                error[Constants.CLASS] = OAuthToken.__name__
                raise SDKException(code=Constants.TOKEN_ERROR, details=error)

            if grant_token is not None and not isinstance(grant_token, str):
                error[Constants.FIELD] = Constants.GRANT_TOKEN
                error[Constants.EXPECTED_TYPE] = Constants.STRING
                error[Constants.CLASS] = OAuthToken.__name__
                raise SDKException(code=Constants.TOKEN_ERROR, details=error)

            if refresh_token is not None and not isinstance(refresh_token, str):
                error[Constants.FIELD] = Constants.REFRESH_TOKEN
                error[Constants.EXPECTED_TYPE] = Constants.STRING
                error[Constants.CLASS] = OAuthToken.__name__
                raise SDKException(code=Constants.TOKEN_ERROR, details=error)

            if redirect_url is not None and not isinstance(redirect_url, str):
                error[Constants.FIELD] = Constants.REDIRECT_URI
                error[Constants.EXPECTED_TYPE] = Constants.STRING
                error[Constants.CLASS] = OAuthToken.__name__
                raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        if id is not None and not isinstance(id, str):
            error[Constants.FIELD] = Constants.ID
            error[Constants.EXPECTED_TYPE] = Constants.STRING
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        if access_token is not None and not isinstance(access_token, str):
            error[Constants.FIELD] = Constants.ACCESS_TOKEN
            error[Constants.EXPECTED_TYPE] = Constants.STRING
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        if user_signature is not None and not isinstance(user_signature, UserSignature):
            error[Constants.FIELD] = Constants.USER_NAME
            error[Constants.EXPECTED_TYPE] = Constants.USER_SIGNATURE_ERROR_MESSAGE
            error[Constants.CLASS] = OAuthToken.__name__
            raise SDKException(code=Constants.TOKEN_ERROR, details=error)

        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__redirect_url = redirect_url
        self.__grant_token = grant_token
        self.__refresh_token = refresh_token
        self.__id = id
        self.__access_token = access_token
        self.__expires_in = None
        self.__user_signature = user_signature
        self.__api_domain = api_domain
        self.__find_user = find_user

    def get_client_id(self):
        """
        This is a getter method to get __client_id.

        Returns:
            string: A string representing __client_id
        """

        return self.__client_id

    def get_client_secret(self):
        """
        This is a getter method to get __client_secret.

        Returns:
            string: A string representing __client_secret
        """

        return self.__client_secret

    def get_redirect_url(self):
        """
        This is a getter method to get __redirect_url.

        Returns:
            string: A string representing __redirect_url
        """

        return self.__redirect_url

    def get_grant_token(self):
        """
        This is a getter method to get __grant_token.

        Returns:
            string: A string representing __grant_token
        """
        return self.__grant_token

    def get_refresh_token(self):
        """
        This is a getter method to get __refresh_token.

        Returns:
            string: A string representing __refresh_token
        """

        return self.__refresh_token

    def get_access_token(self):
        """
        This is a getter method to get __access_token.

        Returns:
            string: A string representing __access_token
        """

        return self.__access_token

    def get_id(self):
        """
        This is a getter method to get __id.

        Returns:
            string: A string representing __id
        """

        return self.__id

    def get_expires_in(self):
        """
        This is a getter method to get __expires_in.

        Returns:
            string: A string representing __expires_in
        """

        return self.__expires_in

    def get_user_signature(self):
        """
        This is a getter method to get __user_signature

        Returns:
            user_signature(UserSignature) : An instance of UserSignature
        """

        return self.__user_signature

    def get_api_domain(self):
        """
        This is a getter method to get api_domain

        Returns:
            string: A string representing __api_domain
        """

        return self.__api_domain

    def set_grant_token(self, grant_token):
        """
        This is a setter method to set __grant_token.

        """
        self.__grant_token = grant_token

    def set_refresh_token(self, refresh_token):
        """
        This is a setter method to set __refresh_token.

        """
        self.__refresh_token = refresh_token

    def set_redirect_url(self, redirect_url):
        """
        This is a setter method to set __redirect_url.

        """
        self.__redirect_url = redirect_url

    def set_access_token(self, access_token):
        """
        This is a setter method to set __access_token.

        """

        self.__access_token = access_token

    def set_client_id(self, client_id):
        """
        This is a setter method to set __client_id.

        """

        self.__client_id = client_id

    def set_client_secret(self, client_secret):
        """
        This is a setter method to set __client_secret.

        """

        self.__client_secret = client_secret

    def set_id(self, id):
        """
        This is a setter method to set __id.

        """

        self.__id = id

    def set_expires_in(self, expires_in):
        """
        This is a setter method to set __expires_in.

        """

        self.__expires_in = expires_in

    def set_user_signature(self, user_signature):
        """
        This is a setter method to set __user_signature.

        """

        self.__user_signature = user_signature

    def set_api_domain(self, api_domain):
        """
        This is a setter method to set __api_domain
        """

        self.__api_domain = api_domain

    def generate_token(self):
        self.get_token()

    def get_token(self):
        initializer = Initializer.get_initializer()
        store = initializer.store

        oauth_token = None
        if self.get_id() is not None:
            oauth_token = store.find_token_by_id(self.get_id())
            self.merge_objects(self, oauth_token)
            oauth_token.__find_user = self.__find_user
        else:
            oauth_token = store.find_token(self)
        if oauth_token is None:
            if self.get_user_signature() is not None:
                self.check_token_details()
            oauth_token = self
        if oauth_token.get_api_domain() is None or len(oauth_token.get_api_domain()) <= 0:
            if initializer.environment is None:
                raise SDKException(Constants.ENVIRONMENT_ERROR_1, Constants.ENVIRONMENT_ERROR_MESSAGE + ":")
            oauth_token.set_api_domain(initializer.environment.url)
        environment = DataCenter.get(oauth_token.get_api_domain())
        if environment is not None:
            try:
                initializer = Initializer.get_initializer()
                setattr(initializer, Constants.ENVIRONMENT, environment)
            except Exception as e:
                raise SDKException(Constants.ENVIRONMENT_ERROR_RESPONSE + ":", cause=e)
        else:
            if initializer.environment is None:
                raise SDKException(Constants.ENVIRONMENT_ERROR_1, Constants.ENVIRONMENT_ERROR_MESSAGE + ":")

        url = initializer.environment.accounts_url
        save = False
        if oauth_token.get_access_token() is None or len(oauth_token.get_access_token()) == 0:
            if oauth_token.get_refresh_token() is not None and len(oauth_token.get_refresh_token()) > 0:
                logging.getLogger("SDKLogger").info(Constants.ACCESS_TOKEN_USING_REFRESH_TOKEN_MESSAGE)
                oauth_token.refresh_access_token(oauth_token, url)
            else:
                logging.getLogger("SDKLogger").info(Constants.ACCESS_TOKEN_USING_GRANT_TOKEN_MESSAGE)
                oauth_token.generate_access_token(oauth_token, url)
            save = True
        elif (oauth_token.get_expires_in() is not None and len(oauth_token.get_expires_in()) > 0 and int(
                oauth_token.get_expires_in()) - int(time.time() * 1000) < 5000):
            logging.getLogger("SDKLogger").info(Constants.REFRESH_TOKEN_MESSAGE)
            oauth_token.refresh_access_token(oauth_token, url)
            save = True
        elif oauth_token.get_expires_in() is None and oauth_token.get_access_token() is not None and \
                oauth_token.get_id() is None:
            
            save = True
        if save:
            try:
                if oauth_token.__user_signature is None and oauth_token.__find_user:
                    try:
                        user_name = Utility().get_user_name(oauth_token.get_access_token())
                        if user_name is not None:
                            oauth_token.set_user_signature(UserSignature(user_name))
                    except SDKException as ex:
                        logging.getLogger("SDKLogger").error(Constants.API_EXCEPTION, ex)
                store.save_token(oauth_token)
            except Exception as ex:
                logging.getLogger("SDKLogger").error(Constants.SAVE_TOKEN_ERROR, ex)
        return oauth_token.get_access_token()

    def check_token_details(self):
        if self.are_all_objects_null([self.__grant_token, self.__refresh_token]):
            raise SDKException(Constants.MANDATORY_VALUE_ERROR, Constants.GET_TOKEN_BY_USER_NAME_ERROR + " - " +
                               str.join(", ", Constants.OAUTH_MANDATORY_KEYS2))
        return True

    @staticmethod
    def are_all_objects_null(object1):
        for obj in object1:
            if obj is not None:
                return False
        return True

    @staticmethod
    def merge_objects(first, second):
        try:
            fields = dir(first)
            for field1 in fields:
                if any(field2 in field1 for field2 in Constants.OAUTH_TOKEN_FIELDS):
                    if not field1.startswith('__'):
                        value1 = getattr(first, field1)
                        value2 = getattr(second, field1)
                        value = value1 if value1 is not None else value2
                        setattr(first, field1, value)

        except Exception as ex:
            raise SDKException(Constants.MERGE_OBJECT, cause=ex)

    def authenticate(self, url_connection):
        if Constants.AUTHORIZATION not in url_connection.headers:
            url_connection.add_header(Constants.AUTHORIZATION, Constants.OAUTH_HEADER_PREFIX + self.get_token())

    def refresh_access_token(self, oauth_token, url):
        try:
            body = {
                Constants.REFRESH_TOKEN: oauth_token.__refresh_token,
                Constants.CLIENT_ID: oauth_token.__client_id,
                Constants.CLIENT_SECRET: oauth_token.__client_secret,
                Constants.GRANT_TYPE: Constants.REFRESH_TOKEN
            }

            response = requests.post(url, data=body, params=None, headers=None, allow_redirects=False).json()
            self.parse_response(oauth_token, response)

        except SDKException as ex:
            raise ex

        except Exception as ex:
            raise SDKException(code=Constants.SAVE_TOKEN_ERROR, cause=ex)

        return oauth_token

    def generate_access_token(self, oauth_token, url):
        try:
            body = {
                Constants.CLIENT_ID: oauth_token.__client_id,
                Constants.CLIENT_SECRET: oauth_token.__client_secret,
                Constants.REDIRECT_URI: oauth_token.__redirect_url if oauth_token.__redirect_url is not None else None,
                Constants.GRANT_TYPE: Constants.GRANT_TYPE_AUTH_CODE,
                Constants.CODE: oauth_token.__grant_token
            }

            headers = dict()
            headers[Constants.USER_AGENT_KEY] = Constants.USER_AGENT
            response = requests.post(url, data=body, params=None, headers=headers, allow_redirects=True).json()
            self.parse_response(oauth_token, response)

        except SDKException as ex:
            raise ex

        except Exception as ex:
            raise SDKException(code=Constants.SAVE_TOKEN_ERROR, cause=ex)

        return self

    def parse_response(self, oauth_token, response):
        initializer = Initializer.get_initializer()
        response_json = dict(response)

        if Constants.ACCESS_TOKEN not in response_json:
            raise SDKException(code=Constants.INVALID_TOKEN_ERROR, message=str(response_json.get(
                Constants.ERROR_KEY)) if Constants.ERROR_KEY in response_json else Constants.NO_ACCESS_TOKEN_ERROR)

        oauth_token.__access_token = response_json.get(Constants.ACCESS_TOKEN)
        oauth_token.__expires_in = str(int(time.time() * 1000) + self.get_token_expires_in(response=response_json))

        if Constants.REFRESH_TOKEN in response_json:
            oauth_token.__refresh_token = response_json.get(Constants.REFRESH_TOKEN)

        if initializer.sdk_config.apply_api_domain_update() and Constants.API_DOMAIN in response_json:
            oauth_token.__api_domain = response_json.get(Constants.API_DOMAIN)

        return oauth_token

    @staticmethod
    def get_token_expires_in(response):
        return int(response[Constants.EXPIRES_IN]) if Constants.EXPIRES_IN_SEC in response else int(
            response[Constants.EXPIRES_IN]) * 1000

    def remove(self):
        try:
            Initializer.get_initializer().store.delete_token(self.get_id())
            return True
        except Exception:
            return False

    def revoke(self, id1):
        try:
            if Initializer.get_initializer() is None:
                raise SDKException(Constants.SDK_UNINITIALIZATION_ERROR, Constants.SDK_UNINITIALIZATION_MESSAGE)
            initializer = Initializer.get_initializer()
            store = initializer.store
            url = initializer.environment.accounts_url
            is_revoke = False
            oauthToken = OAuthToken()
            oauthToken.set_id(id1)
            store.find_token(oauthToken)
            if oauthToken is not None and oauthToken.get_refresh_token() is not None:
                is_revoke = self.revoke_refresh_token(oauthToken.get_refresh_token(), url + Constants.REVOKE_URL)
                logging.getLogger("SDKLogger").info(Constants.ID + " : " + id1 + Constants.REFRESH_TOKEN_REMOVED)
            else:
                logging.getLogger("SDKLogger").info(Constants.ID + " : " + id1 + Constants.TOKEN_NOT_FOUND)

            return is_revoke
        except SDKException as ex:
            raise ex
        except Exception as e1:
            raise SDKException(cause=e1)

    @staticmethod
    def revoke_refresh_token(refreshToken, url):
        try:
            body = {
                Constants.TOKEN: refreshToken
            }
            headers = dict()
            response = requests.post(url, data=body, params=None, headers=headers, allow_redirects=True).json()
            responseJSON = dict(response)
            if (responseJSON is not None and Constants.STATUS in responseJSON and responseJSON.get(
                    Constants.STATUS) == Constants.STATUS_SUCCESS):
                return True
            return False
        except SDKException as ex:
            raise ex
        except Exception as e3:
            raise SDKException(Constants.REVOKE_TOKEN_ERROR, cause=e3)
