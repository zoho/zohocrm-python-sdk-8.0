from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.users import UsersOperations, ResponseWrapper, APIException, GetUsersParam, GetUsersHeader
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class GetUsers:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_users():
        """
        Get all users with optional parameters
        
        Returns:
            None (prints the response)
        """
        try:
            users_operations = UsersOperations()
            param_instance = ParameterMap()
            header_instance = HeaderMap()
            
            # Optional parameters for filtering and pagination
            param_instance.add(GetUsersParam.type, "ActiveUsers")  # AllUsers, ActiveUsers, DeactiveUsers, ConfirmedUsers, NotConfirmedUsers, DeletedUsers
            param_instance.add(GetUsersParam.page, 1)
            param_instance.add(GetUsersParam.per_page, 10)
            # param_instance.add(GetUsersParam.ids, "1055806000000394001,1055806000000394002")
            
            # Optional headers
            # header_instance.add(GetUsersHeader.if_modified_since, datetime(2023, 1, 1))
            
            response = users_operations.get_users(param_instance, header_instance)
            
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
                            print(f"\nTotal Users Retrieved: {len(users_list)}")
                            for user in users_list:
                                print(f"\n--- User Details ---")
                                print(f"User ID: {user.get_id()}")
                                print(f"User Name: {user.get_name()}")
                                print(f"First Name: {user.get_first_name()}")
                                print(f"Last Name: {user.get_last_name()}")
                                print(f"Email: {user.get_email()}")
                                print(f"Status: {user.get_status()}")
                                
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
            print(f"Error in get_users: {e}")


GetUsers.initialize()
GetUsers.get_users()