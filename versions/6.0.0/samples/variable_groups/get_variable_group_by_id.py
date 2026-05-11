from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.variable_groups import VariableGroupsOperations, ResponseWrapper, APIException


class GetVariableGroupById:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_variable_group_by_id(group_id):
        """
        Get specific variable group by ID
        
        Args:
            group_id (str): The ID of the variable group to retrieve
            
        Returns:
            None (prints the response)
        """
        try:
            variable_groups_operations = VariableGroupsOperations()
            
            response = variable_groups_operations.get_variable_group_by_id(group_id)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        variable_groups_list = response_object.get_variable_groups()
                        if variable_groups_list is not None:
                            for variable_group in variable_groups_list:
                                print(f"\n--- Variable Group Details ---")
                                print(f"Variable Group ID: {variable_group.get_id()}")
                                print(f"Variable Group Name: {variable_group.get_name()}")
                                print(f"API Name: {variable_group.get_api_name()}")
                                print(f"Display Label: {variable_group.get_display_label()}")
                                print(f"Description: {variable_group.get_description()}")
                                
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
            print(f"Error in get_variable_group_by_id: {e}")


group_id = "1055806000010178011"

GetVariableGroupById.initialize()
GetVariableGroupById.get_variable_group_by_id(group_id)