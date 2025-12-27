from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.share_records import ShareRecordsOperations, BodyWrapper, ShareRecord
from zohocrmsdk.src.com.zoho.crm.api.users import Users
from zohocrmsdk.src.com.zoho.crm.api.util import Choice
from zohocrmsdk.src.com.zoho.crm.api.share_records import ActionWrapper, SuccessResponse, APIException


class ShareRecordOperations:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def share_record(record_id, module_api_name):
        """
        This method is used to share a record with users.
        
        Args:
            record_id (str): The ID of the record to share
            module_api_name (str): The API name of the module
        """
        try:
            share_records_operations = ShareRecordsOperations(record_id, module_api_name)
            request = BodyWrapper()
            share_record_list = []
            share_record = ShareRecord()
            share_record.set_permission("read_write")  # Options: "read_only", "read_write"
            share_record.set_share_related_records(True)
            user = Users()
            user.set_id(34770615791024)  # Replace with actual user ID
            share_record.set_user(user)
            shared_with = Users()
            shared_with.set_id(1055806000017236002)  # Replace with actual user ID
            shared_with.add_key_value("type", "groups")  # or "groups"
            share_record.set_shared_with(shared_with)
            share_record.set_type(Choice("private"))  # Options: "private", "public_read", "public_read_write"
            share_record_list.append(share_record)
            request.set_share(share_record_list)
            request.set_notify(True)
            response = share_records_operations.share_record(request)
            if response is not None:
                print("Status Code: " + str(response.get_status_code()))
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_share()
                        
                        for action_response in action_response_list:
                            if isinstance(action_response, SuccessResponse):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(key + " : " + str(value))
                                print("Message: " + action_response.get_message().get_value())
                                
                            elif isinstance(action_response, APIException):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(key + " : " + str(value))
                                print("Message: " + action_response.get_message().get_value())
                                
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + " : " + str(value))
                        print("Message: " + response_object.get_message().get_value())
                        
        except Exception as e:
            print(f"Exception occurred: {e}")


ShareRecordOperations.initialize()
ShareRecordOperations.share_record(1055806000028347001, "Leads")