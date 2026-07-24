from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.util import Choice
from zohocrmsdk.src.com.zoho.crm.api.variables import (
    VariablesOperations, ActionWrapper, ActionResponse, SuccessResponse, 
    APIException, BodyWrapper, Variable, VariableGroup
)


class CreateVariables:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_variables():
        """
        Create new variables
        
        Returns:
            None (prints the response)
        """
        try:
            variables_operations = VariablesOperations()
            request = BodyWrapper()
            variables_list = []

            # Create variable 1
            variable1 = Variable()
            variable1.set_name("Test Variable")
            variable1.set_api_name("TestVariable")
            variable1.set_type(Choice("text"))
            variable1.set_value("Test Value")
            variable1.set_description("A test variable for demonstration")
            
            # Set variable group (if required)
            variable_group = VariableGroup()
            variable_group.set_id(1055806000010178011)  # Replace with actual variable group ID
            variable1.set_variable_group(variable_group)
            
            variables_list.append(variable1)

            # Create variable 2
            variable2 = Variable()
            variable2.set_name("Another Test Variable")
            variable2.set_api_name("AnotherTestVariable")
            variable2.set_type(Choice("integer"))
            variable2.set_value("123")
            variable2.set_description("Another test variable")
            
            # Set variable group
            variable_group2 = VariableGroup()
            variable_group2.set_id(1055806000000394001)  # Replace with actual variable group ID
            variable2.set_variable_group(variable_group2)
            
            variables_list.append(variable2)

            request.set_variables(variables_list)
            
            response = variables_operations.create_variables(request)
            
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
            print(f"Error in create_variables: {e}")

CreateVariables.initialize()
CreateVariables.create_variables()