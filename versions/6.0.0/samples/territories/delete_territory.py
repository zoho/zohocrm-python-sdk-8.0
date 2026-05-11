from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, ActionWrapper, APIException, DeleteTerritoryParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class DeleteTerritory:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_territory(territory_id):
        """
        Delete specific territory by ID
        
        Args:
            territory_id (int): The ID of the territory to delete
            
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            param_instance = ParameterMap()
            
            # Optional: Delete previous forecasts associated with territory
            param_instance.add(DeleteTerritoryParam.delete_previous_forecasts, "true")
            
            response = territories_operations.delete_territory(territory_id, param_instance)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_territories()
                        
                        for action_response in action_response_list:
                            print(f"\n--- Territory Deletion Response ---")
                            
                            if hasattr(action_response, 'get_status'):
                                print(f"Status: {action_response.get_status().get_value()}")
                                print(f"Code: {action_response.get_code().get_value()}")
                                
                                print("Details:")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(f"  {key}: {value}")
                                
                                print(f"Message: {action_response.get_message().get_value()}")
                            
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
            print(f"Error in delete_territory: {e}")


territory_id = 1055806000000394047
DeleteTerritory.initialize()
DeleteTerritory.delete_territory(territory_id)