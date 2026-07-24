from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.apis.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.apis.apis_operations import APIsOperations
from zohocrmsdk.src.com.zoho.crm.api.apis.response_handler import ResponseHandler
from zohocrmsdk.src.com.zoho.crm.api.apis.response_wrapper import ResponseWrapper
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer


class GetSupportedAPI:

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_supported_api():
        filters = None
        apis_operations = APIsOperations(filters)
        response = apis_operations.get_supported_api()

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseHandler):
                response_wrapper = response_handler

                if isinstance(response_wrapper, ResponseWrapper):
                    apis = response_wrapper.get_apis()

                    if apis is not None:
                        for api in apis:
                            print("API Path: " + api.get_path())
                            operation_types = api.get_operation_types()

                            for operation_type in operation_types:
                                print("API Operation Method: " + operation_type.get_method())
                                print("API Operation OAuthScope: " + operation_type.get_oauth_scope())
                                print("API Operation MaxCredits: " + str(operation_type.get_max_credits()))
                                print("API Operation MinCredits: " + str(operation_type.get_min_credits()))
            elif isinstance(response_handler, APIException):
                exception = response_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")

                for key, value in exception.get_details().items():
                    print(key + ": " + str(value))

                print("Message: " + exception.get_message())


GetSupportedAPI.initialize()
GetSupportedAPI.get_supported_api()
