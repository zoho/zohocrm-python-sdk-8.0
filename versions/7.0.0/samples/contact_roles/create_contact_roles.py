from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.contact_roles import ContactRolesOperations, BodyWrapper, ContactRole, ResponseWrapper, ActionWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class CreateContactRoles(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_contact_roles():
        """
        This method is used to create Contact Roles and print the response.
        """
        contact_roles_operations = ContactRolesOperations()
        request = BodyWrapper()
        
        # List to hold ContactRole instances
        contact_roles_list = []
        
        contact_role = ContactRole()
        contact_role.set_name("Sample Contact Role")
        contact_role.set_sequence_number(1)
        
        contact_roles_list.append(contact_role)
        
        request.set_contact_roles(contact_roles_list)
        
        response = contact_roles_operations.create_roles(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_contact_roles()
                    for action_response in action_response_list:
                        if hasattr(action_response, 'get_status'):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


CreateContactRoles.initialize()
CreateContactRoles.create_contact_roles()