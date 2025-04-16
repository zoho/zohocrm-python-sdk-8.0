"""
Copyright (c) 2021, ZOHO CORPORATION PRIVATE LIMITED 
All rights reserved. 
 
   Licensed under the Apache License, Version 2.0 (the "License"); 
   you may not use this file except in compliance with the License. 
   You may obtain a copy of the License at 
 
       http://www.apache.org/licenses/LICENSE-2.0 
 
   Unless required by applicable law or agreed to in writing, software 
   distributed under the License is distributed on an "AS IS" BASIS, 
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
   See the License for the specific language governing permissions and 
   limitations under the License.
"""

try:
    import logging
    import os
    import json
    import threading
    from zohocrmsdk.src.com.zoho.crm.api.user_signature import UserSignature
    from zohocrmsdk.src.com.zoho.api.authenticator.store.token_store import TokenStore
    from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from zohocrmsdk.src.com.zoho.crm.api.dc.data_center import DataCenter
    from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zohocrmsdk.src.com.zoho.api.authenticator.token import Token
    from zohocrmsdk.src.com.zoho.api.logger import Logger, SDKLogger
    from zohocrmsdk.src.com.zoho.crm.api.request_proxy import RequestProxy
    from zohocrmsdk.src.com.zoho.crm.api.sdk_config import SDKConfig

except Exception:
    import logging
    import os
    import json
    import threading
    from ..api.user_signature import UserSignature
    from ...api.authenticator.store.token_store import TokenStore
    from ..api.exception import SDKException
    from ..api.dc.data_center import DataCenter
    from ..api.util.constants import Constants
    from ...api.authenticator.token import Token
    from ...api.logger import Logger, SDKLogger
    from .request_proxy import RequestProxy
    from .sdk_config import SDKConfig


class Initializer(object):

    """
    The class to initialize Zoho CRM SDK.
    """

    def __init__(self):
        self.environment = None
        self.store = None
        self.token = None
        self.sdk_config = None
        self.request_proxy = None
        self.resource_path = None

    json_details = None
    initializer = None
    LOCAL = threading.local()
    LOCAL.init = None

    @staticmethod
    def initialize(environment, token, store=None, sdk_config=None, resource_path=None, logger=None, proxy=None):

        """
        The method to initialize the SDK.

        Parameters:
            environment (DataCenter.Environment) : An Environment class instance containing the CRM API base URL and Accounts URL.
            token (Token) : A Token class instance containing the OAuth client application information.
            store (TokenStore) : A TokenStore class instance containing the token store information.
            sdk_config (SDKConfig) : A SDKConfig class instance containing the configuration.
            resource_path (str) : A String containing the absolute directory path to store user specific JSON files containing module fields information.
            logger (Logger): A Logger class instance containing the log file path and Logger type.
            proxy (RequestProxy) : A RequestProxy class instance containing the proxy properties of the user.
        """

        try:
            if not isinstance(token, Token):
                error = {Constants.FIELD: Constants.TOKEN, Constants.EXPECTED_TYPE: Token.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.TOKEN_ERROR_MESSAGE, details=error)

            if store is not None and not isinstance(store, TokenStore):
                error = {Constants.FIELD: Constants.STORE, Constants.EXPECTED_TYPE: TokenStore.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.STORE_ERROR_MESSAGE, details=error)

            if sdk_config is not None and not isinstance(sdk_config, SDKConfig):
                error = {Constants.FIELD: Constants.SDK_CONFIG, Constants.EXPECTED_TYPE: SDKConfig.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.SDK_CONFIG_ERROR_MESSAGE, details=error)

            if proxy is not None and not isinstance(proxy, RequestProxy):
                error = {Constants.FIELD: Constants.USER_PROXY, Constants.EXPECTED_TYPE: RequestProxy.__module__}

                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.REQUEST_PROXY_ERROR_MESSAGE, details=error)

            if store is None:
                try:
                    from zohocrmsdk.src.com.zoho.api.authenticator.store.file_store import FileStore
                except Exception:
                    from ...api.authenticator.store.file_store import FileStore

                store = FileStore(os.path.join(os.getcwd(), Constants.TOKEN_FILE))
            
            if sdk_config is None:
                sdk_config = SDKConfig()
            
            if resource_path is None or len(resource_path) == 0:
                resource_path = os.getcwd()
            
            if logger is None:
                logger = Logger(Logger.Levels.NOTSET, None)

            SDKLogger.initialize(logger)

            if not os.path.isdir(resource_path):
                raise SDKException(Constants.INITIALIZATION_ERROR, Constants.RESOURCE_PATH_INVALID_ERROR_MESSAGE)

            try:
                json_details_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', Constants.JSON_DETAILS_FILE_PATH)
                if Initializer.json_details is None or len(Initializer.json_details) == 0:
                    with open(json_details_path, mode='r') as JSON:
                        Initializer.json_details = json.load(JSON)
            except Exception as e:
                raise SDKException(code=Constants.JSON_DETAILS_ERROR, cause=e)

            initializer = Initializer()

            initializer.environment = environment
            initializer.store = store
            initializer.sdk_config = sdk_config
            initializer.resource_path = resource_path
            initializer.request_proxy = proxy
            Initializer.initializer = initializer
            initializer.token = token
            if token is not None:
                token.generate_token()
            initializer.token = token
            Initializer.initializer = initializer
            Initializer.LOCAL.init = initializer

            logging.getLogger('SDKLogger').info(Constants.INITIALIZATION_SUCCESSFUL + initializer.__str__())

        except SDKException as e:
            raise e

    def __str__(self):
        return Constants.IN_ENVIRONMENT + Initializer.get_initializer().environment.url + '.'

    @staticmethod
    def get_initializer():

        """
        The method to get Initializer class instance.

        Returns:
            Initializer : An instance of Initializer
        """

        if getattr(Initializer.LOCAL, 'init', None) is not None:
            return getattr(Initializer.LOCAL, 'init')

        return Initializer.initializer

    @staticmethod
    def get_json(file_path):
        with open(file_path, mode="r") as JSON:
            file_contents = json.load(JSON)
            JSON.close()

        return file_contents

    @staticmethod
    def switch_user(environment=None, token=None, sdk_config=None, proxy=None):

        """
        The method to switch the different user in SDK environment.

        Parameters:
            environment (DataCenter.Environment) : An Environment class instance containing the CRM API base URL and Accounts URL.
            token (Token) : A Token class instance containing the OAuth client application information.
            sdk_config (SDKConfig) : A SDKConfig class instance containing the configuration.
            proxy (RequestProxy) : A RequestProxy class instance containing the proxy properties of the user.
        """

        if Initializer.initializer is None:
            raise SDKException(Constants.SDK_UNINITIALIZATION_ERROR, Constants.SDK_UNINITIALIZATION_MESSAGE)

        if environment is not None and not isinstance(environment, DataCenter.Environment):
            error = {Constants.FIELD: Constants.ENVIRONMENT,
                     Constants.EXPECTED_TYPE: DataCenter.Environment.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.ENVIRONMENT_ERROR_MESSAGE, details=error)

        if token is not None and not isinstance(token, Token):
            error = {Constants.FIELD: Constants.TOKEN, Constants.EXPECTED_TYPE: Token.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.TOKEN_ERROR_MESSAGE, details=error)

        if sdk_config is not None and not isinstance(sdk_config, SDKConfig):
            error = {Constants.FIELD: Constants.SDK_CONFIG, Constants.EXPECTED_TYPE: SDKConfig.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.SDK_CONFIG_ERROR_MESSAGE, details=error)

        if proxy is not None and not isinstance(proxy, RequestProxy):
            error = {Constants.FIELD: Constants.USER_PROXY, Constants.EXPECTED_TYPE: RequestProxy.__module__}

            raise SDKException(Constants.SWITCH_USER_ERROR, Constants.REQUEST_PROXY_ERROR_MESSAGE, details=error)

        previous_initializer = Initializer.get_initializer()

        initializer = Initializer()
        initializer.environment = previous_initializer.environment if environment is None else environment
        initializer.sdk_config = previous_initializer.sdk_config if sdk_config is None else sdk_config
        initializer.store = Initializer.initializer.store
        initializer.resource_path = Initializer.initializer.resource_path
        initializer.request_proxy = proxy
        initializer.token = token
        if token is not None:
            token.generate_token()
        initializer.token = token
        Initializer.LOCAL.init = initializer

        logging.getLogger('SDKLogger').info(Constants.INITIALIZATION_SWITCHED + initializer.__str__())
