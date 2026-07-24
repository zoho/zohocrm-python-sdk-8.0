from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, ResponseWrapper, APIException, GetChildTerritoryParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class GetChildTerritory:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_child_territory(parent_territory_id):
        """
        Get child territories of a parent territory
        
        Args:
            parent_territory_id (int): The ID of the parent territory
            
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            param_instance = ParameterMap()
            
            # Optional parameters for pagination and filtering
            param_instance.add(GetChildTerritoryParam.page, 1)
            param_instance.add(GetChildTerritoryParam.per_page, 10)
            # param_instance.add(GetChildTerritoryParam.filters, "name:starts_with:Child")
            
            response = territories_operations.get_child_territory(parent_territory_id, param_instance)
            
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
                            print(f"\nFound {len(territories_list)} child territories for parent ID {parent_territory_id}:")
                            
                            for territory in territories_list:
                                print(f"\n--- Child Territory Details ---")
                                print(f"Territory ID: {territory.get_id()}")
                                print(f"Territory Name: {territory.get_name()}")
                                print(f"Territory Description: {territory.get_description()}")
                                
                                # Get manager details
                                manager = territory.get_manager()
                                if manager is not None:
                                    print(f"Manager ID: {manager.get_id()}")
                                    print(f"Manager Name: {manager.get_name()}")
                                
                                # Get parent territory details
                                parent = territory.get_parent_territory()
                                if parent is not None:
                                    print(f"Parent Territory: {parent.get_name()}")
                                
                                print(f"Created Time: {territory.get_created_time()}")
                                print("---")
                        else:
                            print(f"No child territories found for parent ID {parent_territory_id}")
                                
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
            print(f"Error in get_child_territory: {e}")


parent_territory_id = 1055806000000394043
GetChildTerritory.initialize()
GetChildTerritory.get_child_territory(parent_territory_id)