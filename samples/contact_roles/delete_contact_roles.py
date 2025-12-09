from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.contact_roles import ContactRolesOperations, DeleteContactRolesParam, ActionWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class DeleteContactRoles(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_contact_roles(contact_role_ids):
        """
        This method is used to delete multiple Contact Roles and print the response.
        :param contact_role_ids: The list of ContactRole IDs to be deleted
        """
        contact_roles_operations = ContactRolesOperations()
        param_instance = ParameterMap()
        
        # Add ids to ParameterMap instance
        for contact_role_id in contact_role_ids:
            param_instance.add(DeleteContactRolesParam.ids, contact_role_id)
        
        response = contact_roles_operations.delete_contact_roles(param_instance)
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


DeleteContactRoles.initialize()
# Example: Delete multiple contact roles
contact_role_ids = ["347706113006072", "347706113006073", "347706113006074"]
DeleteContactRoles.delete_contact_roles(contact_role_ids)