from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.share_records import ShareRecordsOperations
from zohocrmsdk.src.com.zoho.crm.api.share_records import DeleteActionWrapper, SuccessResponse, APIException


class RevokeSharedRecord:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def revoke_shared_record(record_id, module_api_name):
        """
        This method is used to revoke access to a shared record.
        
        Args:
            record_id (str): The ID of the record to revoke sharing for
            module_api_name (str): The API name of the module
        """
        try:
            share_records_operations = ShareRecordsOperations(record_id, module_api_name)
            response = share_records_operations.revoke_shared_record()
            if response is not None:
                print("Status Code: " + str(response.get_status_code()))
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, DeleteActionWrapper):
                        action_response = response_object.get_share()
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


RevokeSharedRecord.initialize()
RevokeSharedRecord.revoke_shared_record(1055806000028347001, "Leads")