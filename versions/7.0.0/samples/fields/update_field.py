from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.fields import FieldsOperations, UpdateFieldParam
from zohocrmsdk.src.com.zoho.crm.api.fields import BodyWrapper, Fields, PickListValue
from zohocrmsdk.src.com.zoho.crm.api.fields import ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class UpdateField:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_field(field_id):
        try:
            fields_operations = FieldsOperations()
            request = BodyWrapper()
            fields_list = []
            field = Fields()
            field.set_display_label("Updated Custom Field Label")
            field.set_visible(True)
            pick_list_values = []
            pick_list_value1 = PickListValue()
            pick_list_value1.set_display_value("Updated Option 1")
            pick_list_value1.set_actual_value("updated_option1")
            pick_list_values.append(pick_list_value1)
            pick_list_value2 = PickListValue()
            pick_list_value2.set_display_value("Updated Option 2")
            pick_list_value2.set_actual_value("updated_option2")
            pick_list_values.append(pick_list_value2)
            pick_list_value3 = PickListValue()
            pick_list_value3.set_display_value("New Option 3")
            pick_list_value3.set_actual_value("new_option3")
            pick_list_values.append(pick_list_value3)
            field.set_pick_list_values(pick_list_values)
            fields_list.append(field)
            request.set_fields(fields_list)
            param_instance = ParameterMap()
            param_instance.add(UpdateFieldParam.module, "Leads")
            response = fields_operations.update_field(field_id, request, param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_fields()
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
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling update_field: " + str(e))


UpdateField.initialize()
UpdateField.update_field(123456789)