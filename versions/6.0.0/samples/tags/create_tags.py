from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, BodyWrapper, Tag, ActionWrapper, SuccessResponse, APIException, CreateTagsParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class CreateTags:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_tags():
        """
        This method is used to create new tags and print the response.
        """
        try:
            tags_operations = TagsOperations()
            request = BodyWrapper()
            
            tags_list = []
            
            # Create Tag 1
            tag1 = Tag()
            tag1.set_name("Important Lead")
            tag1.set_color_code("#FF5733")
            tags_list.append(tag1)
            
            # Create Tag 2
            tag2 = Tag()
            tag2.set_name("High Priority")
            tag2.set_color_code("#33FF57")
            tags_list.append(tag2)
            
            request.set_tags(tags_list)
            
            param_instance = ParameterMap()
            param_instance.add(CreateTagsParam.module, "Leads")
            param_instance.add(CreateTagsParam.color_code, "#FF5733")
            
            response = tags_operations.create_tags(request, param_instance)
            
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
            print("Exception in create_tags: " + str(e))


CreateTags.initialize()
CreateTags.create_tags()