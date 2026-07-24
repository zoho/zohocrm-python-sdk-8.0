from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.tags import TagsOperations, MergeWrapper, ConflictWrapper, ActionWrapper, SuccessResponse, APIException


class MergeTags:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def merge_tags(tag_id):
        """
        This method is used to merge tags and print the response.
        
        Args:
            tag_id (int): The ID of the tag to merge into
        """
        try:
            tags_operations = TagsOperations()
            request = MergeWrapper()
            # Create list of tags to merge
            tags_list = []
            tag1 = ConflictWrapper()
            tag1.set_conflict_id("1055806000028567008")  # Replace with actual tag ID to merge
            tags_list.append(tag1)
            request.set_tags(tags_list)
            response = tags_operations.merge_tags(tag_id, request)
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
            print("Exception in merge_tags: " + str(e))


MergeTags.initialize()
MergeTags.merge_tags(1055806000028561006)