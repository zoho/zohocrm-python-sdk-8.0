from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import UsersOperations, ResponseWrapper, APIException, GetUserHeader
from zohocrmsdk.src.com.zoho.crm.api import HeaderMap


class GetUser:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_user(user_id):
        """
        Get specific user by ID
        
        Args:
            user_id (int): The ID of the user to retrieve
            
        Returns:
            None (prints the response)
        """
        try:
            users_operations = UsersOperations()
            header_instance = HeaderMap()
            
            # Optional headers
            # header_instance.add(GetUserHeader.if_modified_since, datetime(2023, 1, 1))
            
            response = users_operations.get_user(user_id, header_instance)
            
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        users_list = response_object.get_users()
                        if users_list is not None:
                            for user in users_list:
                                print(f"\n--- User Details ---")
                                print(f"User ID: {user.get_id()}")
                                print(f"User Name: {user.get_name()}")
                                print(f"First Name: {user.get_first_name()}")
                                print(f"Last Name: {user.get_last_name()}")
                                print(f"Email: {user.get_email()}")
                                print(f"Status: {user.get_status()}")
                                print(f"Phone: {user.get_phone()}")
                                print(f"Mobile: {user.get_mobile()}")
                                print(f"Website: {user.get_website()}")
                                print(f"Language: {user.get_language()}")
                                print(f"Locale: {user.get_locale()}")
                                print(f"Time Zone: {user.get_time_zone()}")
                                
                                # Get profile details
                                profile = user.get_profile()
                                if profile is not None:
                                    print(f"Profile ID: {profile.get_id()}")
                                    print(f"Profile Name: {profile.get_name()}")
                                
                                # Get role details
                                role = user.get_role()
                                if role is not None:
                                    print(f"Role ID: {role.get_id()}")
                                    print(f"Role Name: {role.get_name()}")
                                
                                print(f"Created Time: {user.get_created_time()}")
                                print(f"Modified Time: {user.get_modified_time()}")
                                
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
            print(f"Error in get_user: {e}")


user_id = 1055806000028567024
GetUser.initialize()
GetUser.get_user(user_id)