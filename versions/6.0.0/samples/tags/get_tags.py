from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, ResponseWrapper, APIException, GetTagsParam
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class GetTags:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_tags():
        """
        This method is used to get all tags and print the response.
        """
        try:
            tags_operations = TagsOperations()
            param_instance = ParameterMap()
            
            # Add parameters
            param_instance.add(GetTagsParam.module, "Leads")
            param_instance.add(GetTagsParam.my_tags, "true")
            # param_instance.add(GetTagsParam.include, "used_count")
            
            response = tags_operations.get_tags(param_instance)
            
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                
                response_object = response.get_object()
                
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        tags_list = response_object.get_tags()
                        
                        if tags_list is not None:
                            for tag in tags_list:
                                print("Tag ID: " + str(tag.get_id()))
                                print("Tag Name: " + str(tag.get_name()))
                                print("Tag ColorCode: " + str(tag.get_color_code()))
                                print("Tag CreatedTime: " + str(tag.get_created_time()))
                                
                                created_by = tag.get_created_by()
                                if created_by is not None:
                                    print("Tag CreatedBy User-ID: " + str(created_by.get_id()))
                                    print("Tag CreatedBy User-Name: " + str(created_by.get_name()))
                                
                                print("Tag ModifiedTime: " + str(tag.get_modified_time()))
                                
                                modified_by = tag.get_modified_by()
                                if modified_by is not None:
                                    print("Tag ModifiedBy User-ID: " + str(modified_by.get_id()))
                                    print("Tag ModifiedBy User-Name: " + str(modified_by.get_name()))
                                
                                print()
                                
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + " : " + str(value))
                        print("Message: " + response_object.get_message().get_value())
                        
        except Exception as e:
            print("Exception in get_tags: " + str(e))


GetTags.initialize()
GetTags.get_tags()