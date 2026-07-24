from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import (
    UsersOperations, ActionWrapper, APIException, 
    SuccessResponse, BodyWrapper, Users, Profile, Role
)


class CreateUsers:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_users():
        """
        Create new users
        
        Returns:
            None (prints the response)
        """
        try:
            users_operations = UsersOperations()
            request = BodyWrapper()
            users_list = []

            # Create user 1
            user1 = Users()
            user1.set_first_name("Test")
            user1.set_last_name("User")
            user1.set_email("testuser@example.com")
            
            # Set profile (mandatory)
            profile = Profile()
            profile.set_id(1055806000000026011)  # Replace with actual profile ID
            user1.set_profile(profile)
            
            # Set role (mandatory)
            role = Role()
            role.set_id(1055806000000026005)  # Replace with actual role ID
            user1.set_role(role)
            user1.set_website("https://example.com")
            user1.set_language("en_US")
            user1.set_locale("en_US")
            user1.set_time_zone("America/New_York")
            
            users_list.append(user1)
            request.set_users(users_list)
            
            response = users_operations.create_users(request)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_responses = response_object.get_users()
                        for action_response in action_responses:
                            if isinstance(action_response, SuccessResponse):
                                print(f"Status: {action_response.get_status().get_value()}")
                                print(f"Code: {action_response.get_code().get_value()}")
                                print("Details:")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(f"  {key}: {value}")
                                print(f"Message: {action_response.get_message()}")
                                
                            elif isinstance(action_response, APIException):
                                print(f"Status: {action_response.get_status().get_value()}")
                                print(f"Code: {action_response.get_code().get_value()}")
                                print("Details:")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(f"  {key}: {value}")
                                print(f"Message: {action_response.get_message()}")
                    
                    elif isinstance(response_object, APIException):
                        print(f"Status: {response_object.get_status().get_value()}")
                        print(f"Code: {response_object.get_code().get_value()}")
                        print(f"Message: {response_object.get_message()}")

        except Exception as e:
            print(f"Error in create_users: {e}")


CreateUsers.initialize()
CreateUsers.create_users()