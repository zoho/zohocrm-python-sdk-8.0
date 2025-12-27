from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import (
    VariablesOperations, ActionWrapper, ActionResponse, SuccessResponse, 
    APIException, DeleteVariablesParam
)
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class DeleteVariables:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_variables():
        try:
            variables_operations = VariablesOperations()
            param_instance = ParameterMap()
            
            # Specify variable IDs to delete
            param_instance.add(DeleteVariablesParam.ids, "1055806000028566004,1055806000000394002")
            
            response = variables_operations.delete_variables(param_instance)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_responses = response_object.get_variables()
                        for action_response in action_responses:
                            if isinstance(action_response, SuccessResponse):
                                print(f"Status: {action_response.get_status().get_value()}")
                                print(f"Code: {action_response.get_code().get_value()}")
                                print(f"Message: {action_response.get_message()}")
                            elif isinstance(action_response, APIException):
                                print(f"Status: {action_response.get_status().get_value()}")
                                print(f"Code: {action_response.get_code().get_value()}")
                                print(f"Message: {action_response.get_message()}")

        except Exception as e:
            print(f"Error in delete_variables: {e}")

DeleteVariables.initialize()
DeleteVariables.delete_variables()