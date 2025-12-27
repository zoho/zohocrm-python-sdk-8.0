from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.blueprint import BlueprintOperations, ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetBlueprint(object):

    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_blueprint(module_api_name, record_id):
        """
        This method is used to get a single record's Blueprint details with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to get Blueprint
        """
        """
        example
        module_api_name = "Leads"
        record_id = 3409643000002469044
        """
        blueprint_operations = BlueprintOperations(record_id, module_api_name)
        response = blueprint_operations.get_blueprint()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    blueprint = response_object.get_blueprint()
                    process_info = blueprint.get_process_info()
                    if process_info is not None:
                        print("ProcessInfo ID: " + process_info.get_id())
                        print("ProcessInfo Field-ID: " + str(process_info.get_field_id()))
                        print("ProcessInfo isContinuous: " + str(process_info.get_is_continuous()))
                        print("ProcessInfo API Name: " + process_info.get_api_name())
                        print("ProcessInfo Continuous: " + str(process_info.get_continuous()))
                        print("ProcessInfo FieldLabel: " + process_info.get_field_label())
                        print("ProcessInfo Name: " + process_info.get_name())
                        print("ProcessInfo ColumnName: " + process_info.get_column_name())
                        print("ProcessInfo FieldValue: " + process_info.get_field_value())
                        print("ProcessInfo FieldName: " + process_info.get_field_name())
                        print("ProcessInfo FieldName: " + str(process_info.get_escalation()))
                    transitions = blueprint.get_transitions()
                    for transition in transitions:
                        next_transitions = transition.get_next_transitions()
                        for next_transition in next_transitions:
                            print("NextTransition ID: ")
                            print(next_transition.get_id())
                            print("NextTransition Name: " + next_transition.get_name())
                        data = transition.get_data()
                        if data is not None:
                            print("Record ID: " + str(data.get_id()))
                            created_by = data.get_created_by()
                            if created_by is not None:
                                print("Record Created By - Name: " + created_by.get_name())
                                print("Record Created By - ID: " + created_by.get_id())
                            print("Record CreatedTime: " + str(data.get_created_time()))
                            if data.get_modified_time() is not None:
                                print("Record ModifiedTime: " + str(data.get_modified_time()))
                            modified_by = data.get_modified_by()
                            if modified_by is not None:
                                print("Record Modified By - Name: " + modified_by.get_name())
                                print("Record Modified By - ID: " + modified_by.get_id())
                            tags = data.get_tag()
                            if tags is not None:
                                for tag in tags:
                                    print("Record Tag Name: " + tag.get_name())
                                    print("Record Tag ID: " + tag.get_id())
                            for key, value in data.get_key_values().items():
                                print(key + " : " + str(value))
                        print("Transition NextFieldValue: " + str(transition.get_next_field_value()))
                        print("Transition Name: " + str(transition.get_name()))
                        print("Transition CriteriaMatched: " + str(transition.get_criteria_matched()))
                        print("Transition ID: " + str(transition.get_id()))
                        print("Transition Execution Time: " + str(transition.get_execution_time()))
                        print("Transition CriteriaMessage: " + str(transition.get_criteria_message()))
                        fields = transition.get_fields()
                        print("Transition Fields")
                        for field in fields:
                            print("Webhook: " + str(field.get_webhook()))
                            print("JsonType: " + str(field.get_json_type()))
                            print("DisplayLabel: " + field.get_display_label())
                            print("SystemMandatory: " + str(field.get_system_mandatory()))
                            print("DataType: " + field.get_data_type())
                            print("ColumnName: " + str(field.get_column_name()))
                            print("PersonalityName: " + str(field.get_personality_name()))
                            print("ID: " + str(field.get_id()))
                            print("TransitionSequence: " + str(field.get_transition_sequence()))
                            if field.get_mandatory() is not None:
                                print("Mandatory: " + str(field.get_mandatory()))
                            layout = field.get_layouts()
                            if layout is not None:
                                print("Layout ID: " + str(layout.get_id()))
                                print("Layout Name: " + str(layout.get_name()))
                            print("APIName : " + str(field.get_api_name()))
                            print("Content: " + str(field.get_content()))
                            crypt = field.get_crypt()
                            if crypt is not None:
                                print("Crypt Details")
                                print("Mode: " + crypt.get_mode())
                                print("Column: " + crypt.get_column())
                                print("Table: " + crypt.get_table())
                                print("Status: " + str(crypt.get_status()))
                            print("FieldLabel: " + str(field.get_field_label()))
                            tool_tip = field.get_tooltip()
                            if tool_tip is not None:
                                print("ToolTip Name: " + tool_tip.get_name())
                                print("ToolTip Value: " + tool_tip.get_value())
                            print("CreatedSource: " + str(field.get_created_source()))
                            print("FieldReadOnly: " + str(field.get_field_read_only()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetBlueprint.initialize()
GetBlueprint.get_blueprint(module_api_name="Leads", record_id="1055806000028448052")