from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.cadences_execution.action_wrapper import ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.cadences_execution.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.cadences_execution.body_wrapper import BodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.cadences_execution.cadences_execution_operations import CadencesExecutionOperations
from zohocrmsdk.src.com.zoho.crm.api.cadences_execution.success_response import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer


class EnrollCadences:

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)
    @staticmethod
    def enroll_cadences(module_api_name):
        cadences_execution_operations = CadencesExecutionOperations()
        request = BodyWrapper()

        cadences_ids = ["34770785001"]
        request.set_cadences_ids(cadences_ids)

        ids = ["34770650001"]
        request.set_ids(ids)

        response = cadences_execution_operations.enroll_cadences(module_api_name, request)

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            action_handler = response.get_object()

            if isinstance(action_handler, ActionWrapper):
                action_wrapper = action_handler
                action_responses = action_wrapper.get_data()

                for action_response in action_responses:
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
                        print("Message: " + exception.get_message())

            elif isinstance(action_handler, APIException):
                exception = action_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")
                for key, value in exception.get_details().items():
                    print(f"{key}: {value}")
                print("Message: " + exception.get_message())


EnrollCadences.initialize()
EnrollCadences.enroll_cadences(module_api_name="Leads")
