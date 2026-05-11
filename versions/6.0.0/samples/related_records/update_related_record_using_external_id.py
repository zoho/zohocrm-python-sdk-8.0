from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import Record
from zohocrmsdk.src.com.zoho.crm.api.related_records import RelatedRecordsOperations, BodyWrapper, ActionWrapper, \
    SuccessResponse, APIException, UpdateRelatedRecordUsingExternalIDHeader


class UpdateRelatedRecordUsingExternalId:

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_related_record_using_external_id(module_api_name, external_value, related_list_api_name,
                                                external_field_value):
        """
        This method is used to update a single related record with ID and print the response.
        :param module_api_name: The API Name of the module to update related record.
        :param external_value:
        :param related_list_api_name: The API name of the related list.
        :param external_field_value:
        """
        """
        example
        module_api_name = "Products"
        external_value = "34096430798007"
        related_list_api_name = "Price_Books"
        external_field_value = "3409643002414001"
        """
        x_external = "Leads.External,Products.Products_External"
        related_records_operations = RelatedRecordsOperations(related_list_api_name, module_api_name)
        request = BodyWrapper()
        # List to hold Record instances
        records_list = []
        record = Record()
        """
        Call add_key_value method that takes two arguments
        1 -> A string that is the Field's API Name
        2 -> Value
        """
        record.add_key_value('list_price', 90.90)
        # Add Record instance to the list
        records_list.append(record)
        request.set_data(records_list)
        header_instance = HeaderMap()
        header_instance.add(UpdateRelatedRecordUsingExternalIDHeader.x_external, x_external)
        response = related_records_operations.update_related_record_using_external_id(external_field_value,
                                                                                      external_value, request,
                                                                                      header_instance)
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


UpdateRelatedRecordUsingExternalId.initialize()
UpdateRelatedRecordUsingExternalId.update_related_record_using_external_id(module_api_name="Leads",
                                                                           external_value="external",
                                                                           related_list_api_name="Notes",
                                                                           external_field_value="32142342343")
