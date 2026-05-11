from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.action_wrapper import ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.duplicate_check_preference_operations import \
    DuplicateCheckPreferenceOperations
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.success_response import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer


class DeleteDuplicateCheckPreference:
    @staticmethod
    def delete_duplicate_check_preference(module_api_name):
        duplicate_check_preference_operations = DuplicateCheckPreferenceOperations(module_api_name)
        response = duplicate_check_preference_operations.delete_duplicate_check_preference()

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            action_handler = response.get_object()

            if isinstance(action_handler, ActionWrapper):
                action_wrapper = action_handler
                action_response = action_wrapper.get_duplicate_check_preference()

                if isinstance(action_response, SuccessResponse):
                    success_response = action_response
                    print("Status: " + success_response.get_status().get_value())
                    print("Code: " + success_response.get_code().get_value())
                    print("Details: ")
                    for key, value in success_response.get_details().items():
                        print(f"{key}: {value}")
                    print("Message: " + success_response.get_message())

                elif isinstance(action_response, APIException):
                    exception = action_response
                    print("Status: " + exception.get_status().get_value())
                    print("Code: " + exception.get_code().get_value())
                    print("Details: ")
                    for key, value in exception.get_details().items():
                        print(f"{key}: {value}")
                    print("Message: " + exception.get_message().get_value())

            elif isinstance(action_handler, APIException):
                exception = action_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")
                for key, value in exception.get_details().items():
                    print(f"{key}: {value}")
                print("Message: " + exception.get_message().get_value())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


DeleteDuplicateCheckPreference.initialize()
DeleteDuplicateCheckPreference.delete_duplicate_check_preference(module_api_name="Leads")
