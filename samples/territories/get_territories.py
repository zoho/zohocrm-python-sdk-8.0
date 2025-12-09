from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, ResponseWrapper, APIException, GetTerritoriesParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class GetTerritories:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_territories():
        """
        Get all territories with optional parameters
        
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            param_instance = ParameterMap()
            
            # Optional parameters
            param_instance.add(GetTerritoriesParam.page, 1)
            param_instance.add(GetTerritoriesParam.per_page, 10)
            # param_instance.add(GetTerritoriesParam.filters, "name:starts_with:Territory")
            # param_instance.add(GetTerritoriesParam.include, "managers,criteria")
            # param_instance.add(GetTerritoriesParam.ids, "1055806000000394043,1055806000000394044")
            
            response = territories_operations.get_territories(param_instance)
            
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
                                
                                # Get created by details
                                created_by = territory.get_created_by()
                                if created_by is not None:
                                    print(f"Created By: {created_by.get_name()}")
                                
                                print(f"Created Time: {territory.get_created_time()}")
                                print(f"Modified Time: {territory.get_modified_time()}")
                                print("---")
                                
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
            print(f"Error in get_territories: {e}")


GetTerritories.initialize()
GetTerritories.get_territories()