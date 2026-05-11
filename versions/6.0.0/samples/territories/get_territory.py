from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, ResponseWrapper, APIException


class GetTerritory:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_territory(territory_id):
        """
        Get specific territory by ID
        
        Args:
            territory_id (int): The ID of the territory to retrieve
            
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            response = territories_operations.get_territory(territory_id)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        territories_list = response_object.get_territories()
                        if territories_list is not None:
                            for territory in territories_list:
                                print(f"\n--- Territory Details ---")
                                print(f"Territory ID: {territory.get_id()}")
                                print(f"Territory Name: {territory.get_name()}")
                                print(f"Territory Description: {territory.get_description()}")
                                
                                # Get manager details
                                manager = territory.get_manager()
                                if manager is not None:
                                    print(f"Manager ID: {manager.get_id()}")
                                    print(f"Manager Name: {manager.get_name()}")
                                
                                print(f"Created Time: {territory.get_created_time()}")
                                print(f"Modified Time: {territory.get_modified_time()}")
                                
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
            print(f"Error in get_territory: {e}")


territory_id = 1055806000003051397

GetTerritory.initialize()
GetTerritory.get_territory(territory_id)