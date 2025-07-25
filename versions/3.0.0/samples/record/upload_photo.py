from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, FileBodyWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import StreamWrapper


class UploadPhoto:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def upload_photo(module_api_name, record_id, file_path):
        """
        This method is used to attach a photo to a record. You must include the file in the request
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record
        :param file_path: The absolute file path of the file to be uploaded
        """
        """
        example
        module_api_name = "Contacts"
        record_id = 3409643002034003
        absolute_file_path = "/Users/user_name/Desktop/image.png"
        """
        record_operations = RecordOperations(module_api_name)
        request = FileBodyWrapper()
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
        request.set_file(stream_wrapper)
        # Call uploadPhoto method that takes FileBodyWrapper instance, module_api_name and record_id as parameter
        response = record_operations.upload_photo(record_id, request)
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
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


UploadPhoto.initialize()
UploadPhoto.upload_photo(module_api_name="Leads", record_id=44028001507174, file_path="/Users/test.png")
