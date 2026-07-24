from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import Record, Field
from zohocrmsdk.src.com.zoho.crm.api.related_records import RelatedRecordsOperations, BodyWrapper, ActionWrapper, \
    SuccessResponse, APIException


class UpdateRelatedRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_related_records(module_api_name, record_id, related_list_api_name):
        """
        This method is used to update the relation between the records and print the response.
        :param module_api_name: The API Name of the module to update related record.
        :param record_id: The ID of the record to be update Related List.
        :param related_list_api_name: The API name of the related list.
        """
        """
        example
        module_api_name = "Products"
        record_id = 34096430798007
        related_list_api_name = "Price_Books"
        """
        related_records_operations = RelatedRecordsOperations(related_list_api_name, module_api_name)
        request = BodyWrapper()
        # List to hold Record instances
        records_list = []
        record_1 = Record()
        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        # record_1.set_id(3409643002414001)
        #
        # record_1.add_key_value('list_price', 50.56)
        record_1.add_field_value(Field.Notes.id(), 4402480750028)
        record_1.add_field_value(Field.Notes.note_content(), "updated")
        # Add Record instance to the list
        records_list.append(record_1)

        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        # record_2.set_id(3477061010927068)
        #
        # record_2.add_key_value('list_price', 100.56)
        #
        # # Add Record instance to the list
        # records_list.append(record_2)
        request.set_data(records_list)
        header_instance = HeaderMap()
        response = related_records_operations.update_related_records(record_id, request, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
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
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
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


UpdateRelatedRecords.initialize()
UpdateRelatedRecords.update_related_records(module_api_name="Leads", record_id=3242342342343,
                                            related_list_api_name="Notes")
