from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, TransferBodyWrapper, ActionWrapper, APIException, TransferTerritory


class TransferAndDeleteTerritory:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def transfer_and_delete_territory(territory_id, transfer_to_territory_id):
        """
        Transfer and delete a specific territory
        
        Args:
            territory_id (int): The ID of the territory to transfer and delete
            transfer_to_territory_id (int): The ID of the territory to transfer records to
            
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            request = TransferBodyWrapper()
            # Set up transfer territory details
            transfer_territory = TransferTerritory()
            transfer_territory.set_id(transfer_to_territory_id)
            transfer_territory.set_delete_previous_forecasts(False)
            request.set_territories([transfer_territory])
            response = territories_operations.transfer_and_delete_territory(territory_id, request)
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_territories()
                        
                        for action_response in action_response_list:
                            print(f"\n--- Territory Transfer and Delete Response ---")
                            
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
            print(f"Error in transfer_and_delete_territory: {e}")


TransferAndDeleteTerritory.initialize()
territory_to_delete_id = 1055806000000394047
transfer_to_territory_id = 1055806000000394043
TransferAndDeleteTerritory.transfer_and_delete_territory(territory_to_delete_id, transfer_to_territory_id)