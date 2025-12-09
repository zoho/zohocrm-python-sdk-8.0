from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import (
    VariablesOperations, ActionWrapper, ActionResponse, SuccessResponse, 
    APIException, BodyWrapper, Variable
)


class UpdateVariables:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_variables():
        """
        Update multiple variables
        
        Returns:
            None (prints the response)
        """
        try:
            variables_operations = VariablesOperations()
            request = BodyWrapper()
            variables_list = []

            # Update variable 1
            variable1 = Variable()
            variable1.set_id(1055806000000394001)  # Replace with actual variable ID
            variable1.set_name("Updated Variable Name")
            variable1.set_value("Updated Value")
            variable1.set_description("Updated description")
            
            variables_list.append(variable1)

            request.set_variables(variables_list)
            
            response = variables_operations.update_variables(request)
            
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
                                print("Details:")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(f"  {key}: {value}")
                                print(f"Message: {action_response.get_message()}")
                                
                            elif isinstance(action_response, APIException):
                                print(f"Status: {action_response.get_status().get_value()}")
                                print(f"Code: {action_response.get_code().get_value()}")
                                print("Details:")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(f"  {key}: {value}")
                                print(f"Message: {action_response.get_message()}")

        except Exception as e:
            print(f"Error in update_variables: {e}")


UpdateVariables.initialize()
UpdateVariables.update_variables()