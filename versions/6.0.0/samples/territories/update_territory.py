from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, BodyWrapper, ActionWrapper, APIException, Territories


class UpdateTerritory:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_territory(territory_id):
        """
        Update specific territory by ID
        
        Args:
            territory_id (int): The ID of the territory to update
            
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            request = BodyWrapper()
            territories_list = []
            
            territory = Territories()
            territory.set_name("Updated Single Territory")
            territory.set_description("Updated description for single territory")
            territories_list.append(territory)
            
            request.set_territories(territories_list)
            response = territories_operations.update_territory(territory_id, request)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_territories()
                        
                        for action_response in action_response_list:
                            print(f"\n--- Territory Update Response ---")
                            
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
            print(f"Error in update_territory: {e}")

territory_id = 1055806000000394043
UpdateTerritory.initialize()
UpdateTerritory.update_territory(territory_id)