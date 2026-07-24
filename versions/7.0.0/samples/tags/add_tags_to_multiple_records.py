from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, NewTagRequestWrapper, Tag, RecordActionWrapper, RecordSuccessResponse, APIException, AddTagsToMultipleRecordsParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class AddTagsToMultipleRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def add_tags_to_multiple_records(module_api_name):
        """
        This method is used to add tags to multiple records and print the response.
        
        Args:
            module_api_name (str): The API name of the module
        """
        try:
            tags_operations = TagsOperations()
            request = NewTagRequestWrapper()
            
            tags_list = []
            
            # Add tag to multiple records
            tag = Tag()
            tag.set_name("Bulk Tag")
            tags_list.append(tag)
            
            request.set_tags(tags_list)
            request.set_ids([1055806000028448052])
            param_instance = ParameterMap()
            param_instance.add(AddTagsToMultipleRecordsParam.over_write, "false")
            
            response = tags_operations.add_tags_to_multiple_records(module_api_name, request, param_instance)
            
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
            print("Exception in add_tags_to_multiple_records: " + str(e))


AddTagsToMultipleRecords.initialize()
AddTagsToMultipleRecords.add_tags_to_multiple_records("Leads")