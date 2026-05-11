import os

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, FileBodyWrapper, APIException


class GetPhoto:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_photo(module_api_name, record_id, destination_folder):
        """
        This method is used to download a photo associated with a record.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record
        :param destination_folder: The absolute path of the destination folder to store the photo.
        """
        """
        example
        module_api_name = "Contacts"
        record_id = 3409643002034003
        destination_folder = "/Users/user-name/Documents"
        """
        record_operations = RecordOperations(module_api_name)
        # Call getPhoto method that takes module_api_name and record_id as parameters
        response = record_operations.get_photo(record_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, FileBodyWrapper):
                    stream_wrapper = response_object.get_file()
                    # Construct the file name by joining the destinationFolder and the name from StreamWrapper instance
                    file_name = os.path.join(
                        destination_folder, stream_wrapper.get_name())
                    # Open the destination file where the file needs to be written in 'wb' mode
                    with open(file_name, 'wb') as f:
                        for chunk in stream_wrapper.get_stream():
                            f.write(chunk)
                        f.close()
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


module_api_name = "Leads"
record_id = 44028001507174
destination_folder = "/users/sample/file"
GetPhoto.initialize()
GetPhoto.get_photo(module_api_name, record_id, destination_folder)
