from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.roles import RolesOperations, DeleteRoleParam, ActionWrapper, SuccessResponse, APIException


class DeleteRole:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_role(role_id, transfer_to_id=None):
        """
        This method is used to delete a role and print the response.
        :param role_id: The ID of the role to be deleted
        :param transfer_to_id: The ID of the role to which users should be transferred
        """
        try:
            roles_operations = RolesOperations()
            param_instance = ParameterMap()

            if transfer_to_id is not None:
                param_instance.add(DeleteRoleParam.transfer_to_id, transfer_to_id)

            response = roles_operations.delete_role(role_id, param_instance)

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
            print("Exception in delete_role: " + str(e))


DeleteRole.initialize()
DeleteRole.delete_role(44024801431002, 44024801431017)