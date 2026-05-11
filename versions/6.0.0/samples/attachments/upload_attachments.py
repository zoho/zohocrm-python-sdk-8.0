from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.attachments import AttachmentsOperations, FileBodyWrapper, ActionWrapper, \
    SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.util import StreamWrapper


class UploadAttachments(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def upload_attachments(module_api_name, record_id, file_path):
        """
        This method is used to upload attachments and print the response
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to upload attachment
        :param file_path: The absolute file path of the file to be attached
        """
        """
        example
        module_api_name= "Leads"
        record_id = 3409643002267003
        file_path = "../image.jpg";
        """
        attachments_operations = AttachmentsOperations()
        file_body_wrapper = FileBodyWrapper()
        """
        StreamWrapper can be initialized in any of the following ways
        * param 1 -> fileName 
        * param 2 -> Read Stream.
        """
        # stream_wrapper = StreamWrapper(stream=open(file_path, 'rb'))
        """
        * param 1 -> fileName
        * param 2 -> Read Stream
        * param 3 -> Absolute File Path of the file to be attached
        """
        stream_wrapper = StreamWrapper(file_path=file_path)
        file_body_wrapper.set_file(stream_wrapper)
        response = attachments_operations.upload_attachments(record_id, module_api_name, file_body_wrapper)
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


UploadAttachments.initialize()
UploadAttachments.upload_attachments(module_api_name="Leads", record_id=3477001, file_path="./sample.txt")
