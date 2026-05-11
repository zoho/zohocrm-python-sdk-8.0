from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, BodyWrapper, Record, Field, UpsertRecordsHeader, \
    APIException, SuccessResponse, ActionWrapper


class UpsertRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def upsert_records(module_api_name):
        """
        This method is used to Upsert records of a module and print the response.
        :param module_api_name: The API Name of the module to upsert records.
        """
        """
        example
        module_api_name = 'Leads'
        """
        record_operations = RecordOperations(module_api_name)
        request = BodyWrapper()
        # List to hold Record instances
        records_list = []
        record_1 = Record()
        """Call add_field_value method that takes two arguments Import the zcrmsdk.src.com.zoho.crm.api.record.field 
        file 1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field 
        name from the displayed list. 2 -> Value"""
        record_1.add_field_value(Field.Leads.last_name(), 'Python SDK')
        record_1.add_field_value(Field.Leads.first_name(), 'New')
        record_1.add_field_value(Field.Leads.company(), 'Zoho')
        record_1.add_field_value(Field.Leads.city(), 'City')
        record_1.add_field_value(Field.Leads.annual_revenue(), 1432.1)
        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        record_1.add_key_value('Custom_field', 'Value')
        record_1.add_key_value('Custom_field_2', 12)
        # Add Record instance to the list
        # records_list.append(record_1)
        record_2 = Record()
        # Value to Record's fields can be provided in any of the following ways
        """
        Call add_field_value method that takes two arguments
        Import the zcrmsdk.src.com.zoho.crm.api.record.field file
        1 -> Call Field "." and choose the module from the displayed list and press "." and choose the field name 
             from the displayed list.
        2 -> Value
        """
        record_2.add_field_value(Field.Leads.last_name(), 'Boyle')
        record_2.add_field_value(Field.Leads.first_name(), 'Patricia')
        record_2.add_field_value(Field.Leads.company(), 'Law')
        record_2.add_field_value(Field.Leads.city(), 'Man')
        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        record_2.add_key_value('Custom_field', 'Value')
        record_2.add_key_value('Custom_field_2', 12)
        # Add Record instance to the list
        records_list.append(record_2)
        # request.set_data(records_list)
        duplicate_check_fields = ["City", "Last_Name", "First_Name"]
        request.set_duplicate_check_fields(duplicate_check_fields)
        header_instance = HeaderMap()
        header_instance.add(UpsertRecordsHeader.x_external, "Leads.External")
        # Call upsertRecords method that takes BodyWrapper instance and module_api_name as parameters.
        response = record_operations.upsert_records(request, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


UpsertRecords.initialize()
UpsertRecords.upsert_records(module_api_name="Leads")
