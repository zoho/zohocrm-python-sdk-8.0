from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, ExistingTagRequestWrapper, ExistingTag, RecordActionWrapper, RecordSuccessResponse, APIException


class RemoveTagsFromRecord:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def remove_tags_from_record(module_api_name, record_id):
        """
        This method is used to remove tags from a record and print the response.
        
        Args:
            module_api_name (str): The API name of the module
            record_id (int): The ID of the record
        """
        try:
            tags_operations = TagsOperations()
            request = ExistingTagRequestWrapper()
            
            tags_list = []
            
            # Remove tag by ID
            tag = ExistingTag()
            tag.set_name("New Record Tag")
            tags_list.append(tag)
            
            request.set_tags(tags_list)
            
            response = tags_operations.remove_tags(module_api_name, record_id, request)
            
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                
                response_object = response.get_object()
                
                if response_object is not None:
                    if isinstance(response_object, RecordActionWrapper):
                        action_response_list = response_object.get_data()
                        
                        for action_response in action_response_list:
                            if isinstance(action_response, RecordSuccessResponse):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(key + " : " + str(value))
                                print("Message: " + action_response.get_message())
                                
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
            print("Exception in remove_tags_from_record: " + str(e))


RemoveTagsFromRecord.initialize()
RemoveTagsFromRecord.remove_tags_from_record("Leads", 1055806000028347001)