try:
    import os
    import csv
    from zohocrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
    from ....crm.api.util.constants import Constants
    from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from zohocrmsdk.src.com.zoho.crm.api.user_signature import UserSignature

except Exception as e:
    import os
    import csv
    from .token_store import TokenStore
    from ..oauth_token import OAuthToken
    from ....crm.api.util.constants import Constants
    from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException


class FileStore(TokenStore):
    """
    The class to store user token details to the file.
    """

    def __init__(self, file_path):

        """
        Creates an FileStore class instance with the specified parameters.

        Parameters:
            file_path (str) : A string containing the absolute file path of the file to store tokens

        """

        self.file_path = file_path
        is_create = False
        self.headers = [Constants.ID, Constants.USER_NAME, Constants.CLIENT_ID, Constants.CLIENT_SECRET,
                        Constants.REFRESH_TOKEN, Constants.ACCESS_TOKEN, Constants.GRANT_TOKEN, Constants.EXPIRY_TIME,
                        Constants.REDIRECT_URI, Constants.API_DOMAIN]

        if (os.path.exists(file_path) and os.stat(file_path).st_size == 0) or not os.path.exists(file_path):
            is_create = True
            with open(self.file_path, mode='w', newline='') as token_file:
                csv_writer = csv.writer(token_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

                csv_writer.writerow(self.headers)
        if not is_create:
            with open(file_path, 'r') as file:
                csvReader = csv.reader(file)
                allContents = list(csvReader)
                headers = allContents[0]
                if len(headers) == 9:
                    allContents = [arr + [''] for arr in allContents]
                    allContents[0] = self.headers
                    with open(file_path, 'w', newline='') as file1:
                        csvWriter = csv.writer(file1)
                        csvWriter.writerows(allContents)

    def find_token(self, token):
        if not isinstance(token, OAuthToken):
            return token
        try:
            oauth_token = token
            is_row_present = False
            with open(self.file_path, mode='r') as f:
                data = csv.reader(f, delimiter=",")
                next(data, None)
                for next_record in data:
                    if len(next_record) == 0:
                        continue
                    is_row_present = self.check_condition(oauth_token, next_record)
                    if is_row_present:
                        self.set_merge_data(oauth_token, next_record)
                        return oauth_token
                if not is_row_present:
                    return None
        except IOError as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKEN_FILE_ERROR, cause=ex)
        finally:
            f.close()

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
            expiresIn = self.get_data(next_record[7])
            if expiresIn is not None:
                oauth_token.set_expires_in(str(expiresIn))
        if oauth_token.get_redirect_url() is None:
            oauth_token.set_redirect_url(self.get_data(next_record[8]))
        if oauth_token.get_api_domain() is None:
            oauth_token.set_api_domain(self.get_data(next_record[9]))

    def check_condition(self, oauth_token, next_record):
        is_row_present = False
        if oauth_token.get_user_signature() is not None:
            name = oauth_token.get_user_signature().get_name()
            userName = self.get_data(next_record[1])
            if name is not None and len(name) > 0 and userName is not None and len(userName) > 0 and name == userName:
                is_row_present = True
        elif oauth_token.get_access_token() is not None and self.are_all_objects_null(
                [oauth_token.get_client_id(), oauth_token.get_client_secret()]):
            accessToken = self.get_data(next_record[5])
            if accessToken is not None and len(accessToken) > 0 and len(
                    oauth_token.get_access_token()) > 0 and oauth_token.get_access_token() == accessToken:
                is_row_present = True
        elif (oauth_token.get_refresh_token() is not None or oauth_token.get_grant_token() is not None) and \
                oauth_token.get_client_id() is not None and oauth_token.get_client_secret() is not None:
            grantToken = self.get_data(next_record[6])
            refreshToken = self.get_data(next_record[4])
            if grantToken is not None and len(grantToken) > 0 and oauth_token.get_grant_token() is not None and len(
                    oauth_token.get_grant_token()) > 0 and oauth_token.get_grant_token() == grantToken:
                is_row_present = True
            elif refreshToken is not None and len(
                    refreshToken) > 0 and oauth_token.get_refresh_token() is not None and len(
                    oauth_token.get_refresh_token()) > 0 and oauth_token.get_refresh_token() == refreshToken:
                is_row_present = True
        return is_row_present

    def save_token(self, token):
        if isinstance(token, OAuthToken):
            try:
                is_row_present = False
                oauth_token = token
                with open(self.file_path, mode="r") as f:
                    data = csv.reader(f, delimiter=",")
                    all_contents = list()
                    for next_record in list(data):
                        if len(next_record) > 0:
                            all_contents.append(next_record)
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
                            newId = self.generate_id(all_contents)
                            oauth_token.set_id(newId)
                        all_contents.append(self.set_token(oauth_token))
                    with open(self.file_path, mode='w', newline='') as file1:
                        csv_writer = csv.writer(file1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csv_writer.writerows(all_contents)
            except IOError as ex:
                raise SDKException(code=Constants.TOKEN_STORE, message=Constants.SAVE_TOKEN_FILE_ERROR, cause=ex)
            except Exception as error:
                raise error
            finally:
                f.close()

    @staticmethod
    def set_token(oauth_token):
        data = []
        data.insert(0, oauth_token.get_id())
        data.insert(1, oauth_token.get_user_signature().get_name() if oauth_token.get_user_signature() is not None else "")
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
            with open(self.file_path, mode='r') as f:
                data = csv.reader(f, delimiter=',')
                all_contents = list(data)
                for i in range(len(all_contents)):
                    next_record = all_contents[i]
                    if len(next_record) > 1:
                        recordId = self.get_data(next_record[0])
                        if recordId is not None and recordId == id:
                            is_row_present = True
                            all_contents.pop(i)
                            break
            with open(self.file_path, mode='w') as f:
                csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerows(all_contents)
            if not is_row_present:
                raise SDKException(Constants.TOKEN_STORE, Constants.TOKEN_BY_ID_FILE_ERROR)
        except SDKException as ex:
            raise ex
        except Exception as e2:
            raise SDKException(Constants.TOKEN_STORE, Constants.DELETE_TOKENS_FILE_ERROR, cause=e2)

    def get_tokens(self):
        tokens = []

        try:
            with open(self.file_path, mode='r') as f:
                data = csv.reader(f, delimiter=',')
                next(data, None)
                for next_record in data:
                    if len(next_record) > 0:
                        oauth_token = object.__new__(OAuthToken)
                        self.set_oauth_token(oauth_token)
                        self.set_merge_data(oauth_token, next_record)
                        tokens.append(oauth_token)
            return tokens
        except Exception as ex:
            raise SDKException(code=Constants.TOKEN_STORE, message=Constants.GET_TOKENS_FILE_ERROR, cause=ex)

    def delete_tokens(self):
        try:
            with open(self.file_path, mode='w') as token_file:
                csv_writer = csv.writer(token_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(self.headers)
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

            with open(self.file_path, mode='r') as f:
                data = csv.reader(f, delimiter=',')
                all_contents = list(data)
                for content in all_contents:
                    if len(content) > 0 and content[0] == id:
                        self.set_merge_data(oauth_token, content)
                        return oauth_token
            if not is_row_present:
                raise SDKException(Constants.TOKEN_STORE, Constants.GET_TOKEN_BY_ID_FILE_ERROR)
        except SDKException as ex:
            raise ex
        except Exception as ex:
            raise SDKException(Constants.TOKEN_STORE, Constants.TOKEN_BY_ID_FILE_ERROR, cause=ex)
        finally:
            f.close()
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
        maxValue = 0
        if len(all_contents) > 0:
            for i in range(len(all_contents) - 1):
                next_record = all_contents[i + 1]
                if next_record is not None and len(next_record) > 1 and len(next_record[0]) > 0:
                    if maxValue < int(next_record[0]):
                        maxValue = int(next_record[0])
        return str(maxValue + 1)
