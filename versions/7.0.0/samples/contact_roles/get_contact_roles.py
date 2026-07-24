from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.contact_roles import ContactRolesOperations, ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetContactRoles(object):

    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_contact_roles():
        """
        This method is used to get all the Contact Roles and print the response.
        """
        contact_roles_operations = ContactRolesOperations()
        response = contact_roles_operations.get_roles()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    contact_roles_list = response_object.get_contact_roles()
                    for contact_role in contact_roles_list:
                        print("ID: " + str(contact_role.get_id()))
                        print("Name: " + str(contact_role.get_name()))
                        print("Sequence Number: " + str(contact_role.get_sequence_number()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetContactRoles.initialize()
GetContactRoles.get_contact_roles()