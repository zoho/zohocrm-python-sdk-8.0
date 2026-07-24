from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, BodyWrapper, ActionWrapper, APIException, Territories


class CreateTerritories:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_territories():
        """
        Create new territories
        
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            request = BodyWrapper()
            territories_list = []
            
            # Create first territory
            territory1 = Territories()
            territory1.set_name("New Territory 1")
            territory1.set_description("Description for New Territory 1")
            territories_list.append(territory1)
            
            # Create second territory
            territory2 = Territories()
            territory2.set_name("New Territory 2") 
            territory2.set_description("Description for New Territory 2")
            territories_list.append(territory2)
            
            request.set_territories(territories_list)
            response = territories_operations.create_territories(request)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_territories()
                        
                        for i, action_response in enumerate(action_response_list):
                            print(f"\n--- Territory {i+1} Creation Response ---")
                            
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
            print(f"Error in create_territories: {e}")

CreateTerritories.initialize()
CreateTerritories.create_territories()