from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.territories import TerritoriesOperations, ResponseWrapper, APIException


class GetAssociatedUserCount:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_associated_user_count():
        """
        Get count of users associated with territories
        
        Returns:
            None (prints the response)
        """
        try:
            territories_operations = TerritoriesOperations()
            response = territories_operations.get_associated_user_count()
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        print("\n--- Associated User Count Details ---")
                        
                        # The exact response structure may vary, so we handle it generically
                        print(f"Response object type: {type(response_object)}")
                        
                        # Try to access common attributes
                        if hasattr(response_object, 'get_territories'):
                            territories = response_object.get_territories()
                            if territories:
                                print(f"Number of territories with user associations: {len(territories)}")
                                for territory in territories:
                                    print(f"Territory: {territory}")
                        
                        if hasattr(response_object, 'get_count'):
                            count = response_object.get_count()
                            print(f"Total associated user count: {count}")
                        
                        if hasattr(response_object, 'get_info'):
                            info = response_object.get_info()
                            if info:
                                print(f"Additional info: {info}")
                        
                        # Print the entire response for debugging
                        print(f"Full response: {response_object}")
                                
                    elif isinstance(response_object, APIException):
                        print(f"Status: {response_object.get_status().get_value()}")
                        print(f"Code: {response_object.get_code().get_value()}")
                        print("Details:")

                        details = response_object.get_details()
                        if details is not None:
                            for key, value in details.items():
                                print(f"  {key}: {value}")

                        print(f"Message: {response_object.get_message()}")
                    
                    else:
                        print(f"Unexpected response type: {type(response_object)}")
                        print(f"Response: {response_object}")

        except Exception as e:
            print(f"Error in get_associated_user_count: {e}")


GetAssociatedUserCount.initialize()
GetAssociatedUserCount.get_associated_user_count()