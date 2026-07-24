from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.layouts import LayoutsOperations, DeactivateCustomLayoutParam
from zohocrmsdk.src.com.zoho.crm.api.layouts import ActionWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class DeactivateCustomLayout:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def deactivate_custom_layout(layout_id):
        try:
            layouts_operations = LayoutsOperations()
            param_instance = ParameterMap()
            param_instance.add(DeactivateCustomLayoutParam.module, "Leads")
            param_instance.add(DeactivateCustomLayoutParam.transfer_to, "transfer_layout_id")
            
            response = layouts_operations.deactivate_custom_layout(layout_id, param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_layouts()
                        for action_response in action_response_list:
                            if hasattr(action_response, 'get_status'):
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
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling deactivate_custom_layout: " + str(e))


DeactivateCustomLayout.initialize()
DeactivateCustomLayout.deactivate_custom_layout(1055806000000091055)