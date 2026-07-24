from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles import DealContactRolesOperations
from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles import ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class DeleteContactRoleRelation:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_contact_role_relation(deal_id, contact_id):
        try:
            deal_contact_roles_operations = DealContactRolesOperations()
            # Call API
            response = deal_contact_roles_operations.delete_contact_role_relation(contact_id, deal_id)
            if response is not None:
                print("Status Code: " + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print("No Content" if response.get_status_code() == 204 else "Not Modified")
                    return
                # Check if expected response is received
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_data()
                        for action_response in action_response_list:
                            if isinstance(action_response, SuccessResponse):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(key + " : " + str(value))
                                print("Message: " + action_response.get_message())
                            elif isinstance(action_response, APIException):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(key + " : " + str(value))
                                print("Message: " + action_response.get_message())
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + " : " + str(value))
                        print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling delete_contact_role_relation: " + str(e))


DeleteContactRoleRelation.initialize()
DeleteContactRoleRelation.delete_contact_role_relation(1055806000028482009, 1055806000028482004)