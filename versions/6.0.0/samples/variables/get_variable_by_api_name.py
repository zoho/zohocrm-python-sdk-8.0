from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variables import (
    VariablesOperations, ResponseWrapper, APIException, GetVariableByAPINameParam
)
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class GetVariableByAPIName:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_variable_by_api_name(api_name):
        """
        Get specific variable by API name
        
        Args:
            api_name (str): The API name of the variable to retrieve
            
        Returns:
            None (prints the response)
        """
        try:
            variables_operations = VariablesOperations()
            param_instance = ParameterMap()
            
            # Optional parameters
            # param_instance.add(GetVariableByAPINameParam.group, "General")
            
            response = variables_operations.get_variable_by_apiname(api_name, param_instance)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        variables_list = response_object.get_variables()
                        if variables_list is not None:
                            for variable in variables_list:
                                print(f"\n--- Variable Details ---")
                                print(f"Variable ID: {variable.get_id()}")
                                print(f"Variable Name: {variable.get_name()}")
                                print(f"API Name: {variable.get_api_name()}")
                                print(f"Type: {variable.get_type()}")
                                print(f"Value: {variable.get_value()}")
                                print(f"Description: {variable.get_description()}")
                                
                                # Get variable group details
                                variable_group = variable.get_variable_group()
                                if variable_group is not None:
                                    print(f"Variable Group: {variable_group.get_name()}")
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
            print(f"Error in get_variable_by_api_name: {e}")

GetVariableByAPIName.initialize()
api_name = "TestVariable"  # Replace with actual variable API name
GetVariableByAPIName.get_variable_by_api_name(api_name)