from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.share_records import ShareRecordsOperations, GetSharedRecordDetailsParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.share_records import ResponseWrapper, APIException


class GetSharedRecordDetails:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_shared_record_details(record_id, module_api_name):
        """
        This method is used to get the details of a shared record.
        
        Args:
            record_id (str): The ID of the record to get shared details for
            module_api_name (str): The API name of the module
        """
        try:
            share_records_operations = ShareRecordsOperations(record_id, module_api_name)
            param_instance = ParameterMap()
            param_instance.add(GetSharedRecordDetailsParam.view, "summary")
            
            # Add parameter for sharedTo (optional)
            # param_instance.add(GetSharedRecordDetailsParam.sharedto, "user_id")
            response = share_records_operations.get_shared_record_details(param_instance)
            if response is not None:
                print("Status Code: " + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print("No Content" if response.get_status_code() == 204 else "Not Modified")
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        share_records = response_object.get_share()
                        if share_records is not None:
                            for share_record in share_records:
                                print("ShareRecord Permission: " + str(share_record.get_permission()))
                                # Get user details
                                user = share_record.get_user()
                                if user is not None:
                                    print("ShareRecord User-ID: " + str(user.get_id()))
                                    print("ShareRecord User-Name: " + str(user.get_name()))
                                    print("ShareRecord User-Email: " + str(user.get_email()))
                                
                                # Get shared with details
                                shared_with = share_record.get_shared_with()
                                if shared_with is not None:
                                    print("SharedWith User-ID: " + str(shared_with.get_id()))
                                    print("SharedWith User-Name: " + str(shared_with.get_name()))
                                
                                # Check if shared with related records
                                print("ShareRecord ShareRelatedRecords: " + str(share_record.get_share_related_records()))
                                print("ShareRecord Type: " + str(share_record.get_type().get_value()))
                                
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


GetSharedRecordDetails.initialize()
GetSharedRecordDetails.get_shared_record_details(1055806000028347001, "Leads")