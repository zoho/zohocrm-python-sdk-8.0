from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles import DealContactRolesOperations, \
    DeleteAssociatedContactRolesParam
from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles import ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class DeleteAssociatedContactRoles:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_associated_contact_roles(deal_id, contact_ids):
        try:
            deal_contact_roles_operations = DealContactRolesOperations()
            param_instance = ParameterMap()
            if contact_ids:
                param_instance.add(DeleteAssociatedContactRolesParam.ids, ",".join(map(str, contact_ids)))
            response = deal_contact_roles_operations.delete_associated_contact_roles(deal_id, param_instance)
            if response is not None:
                print("Status Code: " + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print("No Content" if response.get_status_code() == 204 else "Not Modified")
                    return
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
            print("Exception when calling delete_associated_contact_roles: " + str(e))


DeleteAssociatedContactRoles.initialize()
DeleteAssociatedContactRoles.delete_associated_contact_roles(1055806000028482009, [1055806000028482004])