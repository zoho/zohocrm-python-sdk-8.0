"""
ZOHO CRM SDK v8 - Tags Operations: Update Tags
This sample demonstrates how to update multiple tags.
"""

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, BodyWrapper, Tag, ActionWrapper, SuccessResponse, APIException, UpdateTagsParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class UpdateTags:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_tags():
        """
        This method is used to update multiple tags and print the response.
        """
        try:
            tags_operations = TagsOperations()
            request = BodyWrapper()
            
            tags_list = []
            
            # Update existing tag
            tag = Tag()
            tag.set_id(1055806000028567008)  # Replace with actual tag ID
            tag.set_name("Updated Tag Name")
            tag.set_color_code("#3366FF")
            tags_list.append(tag)
            
            request.set_tags(tags_list)
            
            param_instance = ParameterMap()
            param_instance.add(UpdateTagsParam.module, "Leads")
            
            response = tags_operations.update_tags(request, param_instance)
            
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                
                response_object = response.get_object()
                
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_tags()
                        
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
            print("Exception in update_tags: " + str(e))


UpdateTags.initialize()
UpdateTags.update_tags()