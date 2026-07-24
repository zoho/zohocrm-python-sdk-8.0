from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.fields import FieldsOperations, GetFieldParam
from zohocrmsdk.src.com.zoho.crm.api.fields import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetField:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_field(field_id):
        try:
            fields_operations = FieldsOperations()
            param_instance = ParameterMap()
            param_instance.add(GetFieldParam.module, "Leads")
            response = fields_operations.get_field(field_id, param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        fields_list = response_object.get_fields()
                        for field in fields_list:
                            print("Field ID: " + str(field.get_id()))
                            print("Field APIName: " + str(field.get_api_name()))
                            print("Field DataType: " + str(field.get_data_type()))
                            print("Field DisplayLabel: " + str(field.get_display_label()))
                            print("Field SystemMandatory: " + str(field.get_system_mandatory()))
                            print("Field Visible: " + str(field.get_visible()))
                            print("Field Length: " + str(field.get_length()))
                            print("Field ReadOnly: " + str(field.get_read_only()))
                            print("Field CustomField: " + str(field.get_custom_field()))
                            print("Field QuickSequenceNumber: " + str(field.get_quick_sequence_number()))
                            print("Field SequenceNumber: " + str(field.get_sequence_number()))
                            if field.get_default_value() is not None:
                                print("Field DefaultValue: " + str(field.get_default_value()))
                            if field.get_tooltip() is not None:
                                print("Field Tooltip: " + str(field.get_tooltip().get_name()))
                            if field.get_created_source() is not None:
                                print("Field CreatedSource: " + str(field.get_created_source()))
                            if field.get_field_label() is not None:
                                print("Field Label: " + str(field.get_field_label()))
                            if field.get_pick_list_values() is not None:
                                pick_list_values = field.get_pick_list_values()
                                for pick_list_value in pick_list_values:
                                    print("PickList Value ID: " + str(pick_list_value.get_id()))
                                    print("PickList Value Display Value: " + str(pick_list_value.get_display_value()))
                                    print("PickList Value Actual Value: " + str(pick_list_value.get_actual_value()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling get_field: " + str(e))


GetField.initialize()
GetField.get_field(1055806000028209027)