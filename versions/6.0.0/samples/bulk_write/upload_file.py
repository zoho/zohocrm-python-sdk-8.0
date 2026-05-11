from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.bulk_write import BulkWriteOperations, FileBodyWrapper, UploadFileHeader, \
    SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.util import StreamWrapper


class UploadFile(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def upload_file(org_id, file_path):
        """
        This method is used to upload a CSV file in ZIP format for bulk write API. The response contains the file_id.
        :param org_id: The unique ID (zgid) of your organization obtained through the Organization API.
        :param file_path: The absoluteFilePath of the zip file you want to upload.
        """
        """
        example
        org_id = "6045"
        file_path = "/Users/Leads.zip"
        """
        bulk_write_operations = BulkWriteOperations()
        file_body_wrapper = FileBodyWrapper()
        """
        StreamWrapper can be initialized in any of the following ways
        * param 1 -> fileName 
        * param 2 -> Read Stream.
        """
        # stream_wrapper = StreamWrapper(stream=open(absolute_file_path, 'rb'))
        """
        * param 1 -> fileName
        * param 2 -> Read Stream
        * param 3 -> Absolute File Path of the file to be attached
        """
        stream_wrapper = StreamWrapper(file_path=file_path)
        file_body_wrapper.set_file(stream_wrapper)
        header_instance = HeaderMap()
        # Possible parameters for upload_file operation
        header_instance.add(UploadFileHeader.feature, "bulk-write")
        header_instance.add(UploadFileHeader.x_crm_org, org_id)
        # Call upload_file method that takes FileBodyWrapper instance and header_instance as parameter
        response = bulk_write_operations.upload_file(file_body_wrapper, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, SuccessResponse):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())
                elif isinstance(response_object, APIException):
                    if response_object.get_status() is not None:
                        print("Status: " + response_object.get_status().get_value())
                    if response_object.get_code() is not None:
                        print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    if details is not None:
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                    if response_object.get_error_message() is not None:
                        print("Error Message: " + response_object.get_error_message().get_value())
                    print('Error Code: ' + str(response_object.get_error_code()))
                    if response_object.get_x_error() is not None:
                        print('XError: ' + response_object.get_x_error().get_value())
                    if response_object.get_info() is not None:
                        print("Info: " + response_object.get_info().get_value())
                    if response_object.get_x_info() is not None:
                        print("XInfo: " + response_object.get_x_info().get_value())
                    if response_object.get_message() is not None:
                        print("Message: " + response_object.get_message().get_value())
                    print('HttpStatus: ' + str(response_object.get_http_status()))


UploadFile.initialize()
UploadFile.upload_file(org_id="6045", file_path="/Users/Leads.zip")
