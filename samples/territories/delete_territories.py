from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, ActionWrapper, APIException, DeleteTerritoriesParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class DeleteTerritories:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_territories(territory_ids):
        """
        Delete multiple territories
        
        Args:
            territory_ids (list): List of territory IDs to delete
            
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            param_instance = ParameterMap()
            
            # Add territory IDs to delete
            for territory_id in territory_ids:
                param_instance.add(DeleteTerritoriesParam.ids, territory_id)
            
            # Optional: Delete previous forecasts associated with territories
            param_instance.add(DeleteTerritoriesParam.delete_previous_forecasts, "true")
            
            response = territories_operations.delete_territories(param_instance)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_territories()
                        
                        for i, action_response in enumerate(action_response_list):
                            print(f"\n--- Territory {i+1} Deletion Response ---")
                            
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
            print(f"Error in delete_territories: {e}")


DeleteTerritories.initialize()
territory_ids = [1055806000000394045, 1055806000000394046]
DeleteTerritories.delete_territories(territory_ids)