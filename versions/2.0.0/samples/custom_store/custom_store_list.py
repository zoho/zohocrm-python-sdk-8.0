from zohocrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
from zohocrmsdk.src.com.zoho.crm.api.user_signature import UserSignature


class CustomStoreList(TokenStore):

    def __init__(self):
        self.store = []

    def find_token(self, token):
        if not isinstance(token, OAuthToken):
            return token
        try:
            oauth_token = token
            is_row_present = False
            data = self.store
            for next_record in data:
                if len(next_record) == 0:
                    continue
                is_row_present = self.check_condition(oauth_token, next_record)
                if is_row_present:
                    self.set_merge_data(oauth_token, next_record)
                    return oauth_token
            if not is_row_present:
                return None
        except Exception as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_FILE_ERROR, cause=ex)

    def set_merge_data(self, oauth_token, next_record):
        if oauth_token.get_id() is None:
            oauth_token.set_id(self.get_data(next_record[0]))
        if oauth_token.get_user_signature() is None:
            name = self.get_data(next_record[1])
            if name is not None:
                oauth_token.set_user_signature(UserSignature(name))
        if oauth_token.get_client_id() is None:
            oauth_token.set_client_id(self.get_data(next_record[2]))
        if oauth_token.get_client_secret() is None:
            oauth_token.set_client_secret(self.get_data(next_record[3]))
        if oauth_token.get_refresh_token() is None:
            oauth_token.set_refresh_token(self.get_data(next_record[4]))
        if oauth_token.get_access_token() is None:
            oauth_token.set_access_token(self.get_data(next_record[5]))
        if oauth_token.get_grant_token() is None:
            oauth_token.set_grant_token(self.get_data(next_record[6]))
        if oauth_token.get_expires_in() is None:
            expires_in = self.get_data(next_record[7])
            if expires_in is not None:
                oauth_token.set_expires_in(str(expires_in))
        if oauth_token.get_redirect_url() is None:
            oauth_token.set_redirect_url(self.get_data(next_record[8]))
        if oauth_token.get_api_domain() is None:
            oauth_token.set_api_domain(self.get_data(next_record[9]))

    def check_condition(self, oauth_token, next_record):
        is_row_present = False
        if oauth_token.get_user_signature() is not None:
            name = oauth_token.get_user_signature().get_name()
            user_name = self.get_data(next_record[1])
            if name is not None and len(name) > 0 and user_name is not None and len(user_name) > 0 \
                    and name == user_name:
                is_row_present = True
        elif oauth_token.get_access_token() is not None and self.are_all_objects_null(
                [oauth_token.get_client_id(), oauth_token.get_client_secret()]):
            access_token = self.get_data(next_record[5])
            if access_token is not None and len(access_token) > 0 and len(
                    oauth_token.get_access_token()) > 0 and oauth_token.get_access_token() == access_token:
                is_row_present = True
        elif (oauth_token.get_refresh_token() is not None or oauth_token.get_grant_token() is not None) and \
                oauth_token.get_client_id() is not None and oauth_token.get_client_secret() is not None:
            grant_token = self.get_data(next_record[6])
            refresh_token = self.get_data(next_record[4])
            if grant_token is not None and len(grant_token) > 0 and oauth_token.get_grant_token() is not None and len(
                    oauth_token.get_grant_token()) > 0 and oauth_token.get_grant_token() == grant_token:
                is_row_present = True
            elif refresh_token is not None and len(refresh_token) > 0 and oauth_token.get_refresh_token() is not None \
                    and len(oauth_token.get_refresh_token()) > 0 and oauth_token.get_refresh_token() == refresh_token:
                is_row_present = True
        return is_row_present

    def save_token(self, token):
        if isinstance(token, OAuthToken):
            try:
                is_row_present = False
                oauth_token = token
                all_contents = self.store
                for next_record in all_contents:
                    if len(next_record) > 0:
                        if oauth_token.get_id() is not None:
                            id = self.get_data(next_record[0])
                            if id is not None and oauth_token.get_id() is not None and id == oauth_token.get_id():
                                is_row_present = True
                        else:
                            is_row_present = self.check_condition(oauth_token, next_record)
                        if is_row_present:
                            self.set_merge_data(oauth_token, next_record)
                            i = all_contents.index(next_record)
                            all_contents[i] = self.set_token(oauth_token)
                            break
                    else:
                        all_contents.remove(next_record)
                if not is_row_present:
                    if oauth_token.get_id() is not None or oauth_token.get_user_signature() is not None:
                        if (oauth_token.get_refresh_token() is None and oauth_token.get_grant_token() is None
                                and oauth_token.get_access_token() is None):
                            raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_FILE_ERROR1)
                    if oauth_token.get_id() is None:
                        new_id = self.generate_id(all_contents)
                        oauth_token.set_id(new_id)
                    all_contents.append(self.set_token(oauth_token))
                self.store = all_contents
            except Exception as error:
                raise SDKException(code=Constants.TOKEN_STORE, message=Constants.SAVE_TOKEN_FILE_ERROR, cause=error)

    @staticmethod
    def set_token(oauth_token):
        data = []
        data.insert(0, oauth_token.get_id())
        data.insert(1,
                    oauth_token.get_user_signature().get_name() if oauth_token.get_user_signature() is not None else "")
        data.insert(2, oauth_token.get_client_id())
        data.insert(3, oauth_token.get_client_secret())
        data.insert(4, oauth_token.get_refresh_token())
        data.insert(5, oauth_token.get_access_token())
        data.insert(6, oauth_token.get_grant_token())
        data.insert(7, oauth_token.get_expires_in())
        data.insert(8, oauth_token.get_redirect_url())
        data.insert(9, oauth_token.get_api_domain())
        return data

    def delete_token(self, id):
        try:
            is_row_present = False
            all_contents = self.store
            for i in range(len(all_contents)):
                next_record = all_contents[i]
                if len(next_record) > 1:
                    record_id = self.get_data(next_record[0])
                    if record_id is not None and record_id == id:
                        is_row_present = True
                        all_contents.pop(i)
                        break
            self.store = all_contents
            if not is_row_present:
                raise SDKException(Constants.TOKEN_STORE, Constants.TOKEN_BY_ID_FILE_ERROR)
        except SDKException as ex:
            raise ex
        except Exception as e2:
            raise SDKException(Constants.TOKEN_STORE, Constants.DELETE_TOKENS_FILE_ERROR, cause=e2)

    def get_tokens(self):
        tokens = []
        try:
            for next_record in self.store:
                oauth_token = object.__new__(OAuthToken)
                self.set_oauth_token(oauth_token)
                self.set_merge_data(oauth_token, next_record)
                tokens.append(oauth_token)
            return tokens
        except Exception as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKENS_FILE_ERROR, cause=ex)

    def delete_tokens(self):
        try:
            self.store = []
        except Exception as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.DELETE_TOKENS_FILE_ERROR, cause=ex)

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

    def find_token_by_id(self, id):
        try:
            is_row_present = False
            oauth_token = object.__new__(OAuthToken)
            self.set_oauth_token(oauth_token)
            all_contents = self.store
            for content in all_contents:
                if content[0] == id:
                    is_row_present = True
                    self.set_merge_data(oauth_token, content)
                    return oauth_token
            if not is_row_present:
                raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_BY_ID_FILE_ERROR)
        except SDKException as ex:
            raise ex
        except Exception as e:
            raise SDKException(Constants.TOKEN_STORE, Constants.TOKEN_BY_ID_FILE_ERROR, cause=e)
        return None

    @staticmethod
    def get_data(value):
        return value if (value is not None and len(value) > 0) else None

    @staticmethod
    def are_all_objects_null(object1):
        for obj in object1:
            if obj is not None:
                return False
        return True

    @staticmethod
    def generate_id(all_contents):
        max_value = 0
        if len(all_contents) > 0:
            for i in range(len(all_contents) - 1):
                next_record = all_contents[i + 1]
                if next_record is not None and len(next_record) > 1 and len(next_record[0]) > 0:
                    if max_value < int(next_record[0]):
                        max_value = int(next_record[0])
        return str(max_value + 1)
