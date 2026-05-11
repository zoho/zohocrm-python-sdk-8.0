from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, CountResponseWrapper, APIException, GetRecordCountForTagParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class GetRecordCountForTag:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_record_count_for_tag(tag_id):
        """
        This method is used to get record count for a tag and print the response.
        
        Args:
            tag_id (int): The ID of the tag
        """
        try:
            tags_operations = TagsOperations()
            
            param_instance = ParameterMap()
            param_instance.add(GetRecordCountForTagParam.module, "Leads")
            
            response = tags_operations.get_record_count_for_tag(tag_id, param_instance)
            
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                
                response_object = response.get_object()
                
                if response_object is not None:
                    if isinstance(response_object, CountResponseWrapper):
                        print("Tag Count: " + str(response_object.get_count()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + " : " + str(value))
                        print("Message: " + response_object.get_message().get_value())
                        
        except Exception as e:
            print("Exception in get_record_count_for_tag: " + str(e))


GetRecordCountForTag.initialize()
GetRecordCountForTag.get_record_count_for_tag(1055806000012588004)