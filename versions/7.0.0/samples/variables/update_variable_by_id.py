from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import (
    VariablesOperations, ActionWrapper, ActionResponse, SuccessResponse, 
    APIException, BodyWrapper, Variable, UpdateVariableByIDParam
)
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class UpdateVariableByID:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_variable_by_id(variable_id):
        """
        Update specific variable by ID
        
        Args:
            variable_id (int): The ID of the variable to update
            
        Returns:
            None (prints the response)
        """
        try:
            variables_operations = VariablesOperations()
            request = BodyWrapper()
            param_instance = ParameterMap()
            
            # Optional parameters
            # param_instance.add(UpdateVariableByIDParam.group, "General")
            
            variables_list = []
            
            # Update variable
            variable = Variable()
            variable.set_name("Updated Variable Name")
            variable.set_value("Updated Value")
            variable.set_description("Updated description")
            
            variables_list.append(variable)
            request.set_variables(variables_list)
            
            response = variables_operations.update_variable_by_id(variable_id, request, param_instance)
            
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

                    elif isinstance(response_object, APIException):
                        print(f"Status: {response_object.get_status().get_value()}")
                        print(f"Code: {response_object.get_code().get_value()}")
                        print("Details:")

                        details = response_object.get_details()
                        if details is not None:
                            for key, value in details.items():
                                print(f"  {key}: {value}")

                        print(f"Message: {response_object.get_message()}")

        except Exception as e:
            print(f"Error in update_variable_by_id: {e}")


UpdateVariableByID.initialize()
variable_id = 1055806000000394001
UpdateVariableByID.update_variable_by_id(variable_id)