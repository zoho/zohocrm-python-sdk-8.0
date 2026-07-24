from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.roles import RolesOperations, BodyWrapper, Role, ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser


class CreateRoles:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_roles():
        """
        This method is used to create roles and print the response.
        """
        try:
            roles_operations = RolesOperations()
            request = BodyWrapper()
            roles_list = []

            role = Role()
            role.set_name("Sample Role Name")
            role.set_display_label("Sample Role Display Label")
            role.set_description("Sample role description")
            role.set_share_with_peers(True)

            reporting_to = MinifiedUser()
            reporting_to.set_id(440248001431017)
            role.set_reporting_to(reporting_to)

            roles_list.append(role)
            request.set_roles(roles_list)

            response = roles_operations.create_roles(request)

            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))

                response_object = response.get_object()

                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_roles()

                        for action_response in action_response_list:
                            if isinstance(action_response, SuccessResponse):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                for key, value in details.items():
                                    print(key + ' : ' + str(value))
                                print("Message: " + action_response.get_message())

                            elif isinstance(action_response, APIException):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                for key, value in details.items():
                                    print(key + ' : ' + str(value))
                                print("Message: " + action_response.get_message())

                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())

        except Exception as e:
            print("Exception in create_roles: " + str(e))


CreateRoles.initialize()
CreateRoles.create_roles()