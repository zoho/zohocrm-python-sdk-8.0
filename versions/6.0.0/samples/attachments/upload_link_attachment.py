from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.attachments import AttachmentsOperations, UploadUrlAttachmentsParam, ActionWrapper, \
    SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class UploadLinkAttachment(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def upload_link_attachment(module_api_name, record_id, attachment_url):
        """
        This method is used to upload link attachment and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to upload Link attachment
        :param attachment_url: The attachment url of the doc or image link to be attached
        """
        """
        example
        module_api_name = "Leads";
        record_id = 3409643002267003
        attachment_url = "https://5.imimg.com/data5/KJ/UP/MY-8655440/zoho-crm-500x500.png";
        """
        attachments_operations = AttachmentsOperations()
        param_instance = ParameterMap()
        param_instance.add(UploadUrlAttachmentsParam.attachmenturl, attachment_url)
        response = attachments_operations.upload_url_attachments(record_id, module_api_name, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message())
                        elif isinstance(action_response, APIException):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


UploadLinkAttachment.initialize()
UploadLinkAttachment.upload_link_attachment(module_api_name="Leads", record_id=3477001,
                                            attachment_url="https://5.imimg.com/data5/KJ/UP/MY-860/zoho-crm-500x500.png"
                                            )
