from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.related_records import APIException
from zohocrmsdk.src.com.zoho.crm.api.related_records import RelatedRecordsOperations, ActionWrapper, SuccessResponse


class DelinkRecord:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delink_record(module_api_name, record_id, related_list_api_name, related_list_id):
        """
        This method is used to delete the association between modules and print the response.
        :param module_api_name: The API Name of the module to delink related record.
        :param record_id: The ID of the record
        :param related_list_api_name: The API name of the related list.
        :param related_list_id: The ID of the related record.
        """
        """
        example
        module_api_name = "Products"
        record_id = 34096430798007
        related_list_api_name = "Price_Books"
        related_list_id = 3409414001
        """
        related_records_operations = RelatedRecordsOperations(related_list_api_name, module_api_name)
        header_instance = HeaderMap()
        response = related_records_operations.delink_record(related_list_id, record_id, header_instance)
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


DelinkRecord.initialize()
DelinkRecord.delink_record(module_api_name="Leads", record_id=4402480774074,
                           related_list_api_name="Notes", related_list_id=440248001495003)
