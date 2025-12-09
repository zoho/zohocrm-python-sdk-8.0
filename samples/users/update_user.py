from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import (
    UsersOperations, ActionWrapper, APIException, 
    SuccessResponse, BodyWrapper, Users
)


class UpdateUser:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_user(user_id):
        """
        Update a specific user by ID
        
        Args:
            user_id (int): The ID of the user to update
            
        Returns:
            None (prints the response)
        """
        try:
            users_operations = UsersOperations()
            request = BodyWrapper()
            users_list = []

            # Update user
            user = Users()
            user.set_first_name("Updated")
            user.set_website("https://updated-example.com")
            user.set_language("en_US")
            user.set_locale("en_US")
            user.set_time_zone("America/Los_Angeles")
            
            users_list.append(user)
            request.set_users(users_list)
            
            response = users_operations.update_user(user_id, request)
            
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

        except Exception as e:
            print(f"Error in update_user: {e}")


user_id = 1055806000028567024
UpdateUser.initialize()
UpdateUser.update_user(user_id)