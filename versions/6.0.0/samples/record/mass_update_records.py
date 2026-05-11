from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import MassUpdateBodyWrapper, RecordOperations, Record, Field, \
    MassUpdateTerritory, MassUpdateActionWrapper, MassUpdateSuccessResponse, APIException


class MassUpdateRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def mass_update_records(module_api_name):
        """
        This method is used to update the values of specific fields for multiple records and print the response.
        :param module_api_name: The API Name of the module to mass update records.
        """
        """
        example
        module_api_name = "Contacts"
        """
        record_operations = RecordOperations(module_api_name)
        request = MassUpdateBodyWrapper()
        # List to hold Record instances
        records_list = []
        record = Record()
        record.add_field_value(Field.Leads.city(), 'HOO')
        # Add the record instance to list
        records_list.append(record)
        request.set_data(records_list)
        request.set_cvid('34096430087537')
        ids = [3409643002049003, 3409643002043003, 3409643001881002]
        request.set_ids(ids)
        request.set_over_write(True)
        territory = MassUpdateTerritory()
        territory.set_id(34096430505351)
        territory.set_include_child(True)
        request.set_territory(territory)
        # Call mass_update_records method that takes MassUpdateBodyWrapper instance, module_api_name as parameter.
        response = record_operations.mass_update_records(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, MassUpdateActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, MassUpdateSuccessResponse):
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


MassUpdateRecords.initialize()
MassUpdateRecords.mass_update_records(module_api_name="Leads")
