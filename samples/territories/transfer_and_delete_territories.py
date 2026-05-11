from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, TransferBodyWrapper, ActionWrapper, APIException, TransferTerritory


class TransferAndDeleteTerritories:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def transfer_and_delete_territories():
        """
        Transfer and delete multiple territories

        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            request = TransferBodyWrapper()
            transfer_territory = TransferTerritory()
            transfer_territory.set_id(323243123123)
            transfer_territory.set_transfer_to_id(32322131232)
            transfer_territory.set_delete_previous_forecasts(False)
            request.set_territories([transfer_territory])
            response = territories_operations.transfer_and_delete_territories(request)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_territories()
                        
                        for i, action_response in enumerate(action_response_list):
                            print(f"\n--- Territory {i+1} Transfer and Delete Response ---")
                            
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
            print(f"Error in transfer_and_delete_territories: {e}")

TransferAndDeleteTerritories.initialize()
TransferAndDeleteTerritories.transfer_and_delete_territories()