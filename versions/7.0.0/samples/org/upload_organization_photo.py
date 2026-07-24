from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.org import OrgOperations, FileBodyWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import StreamWrapper


class UploadOrganizationPhoto:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def upload_organization_photo(file_path):
        """
        This method is used to upload the brand logo or image of the organization and print the response.
        :param file_path: The absolute file path of the file to be attached
        """
        """
        example
        absolute_file_path = "/Users/logo.png";
        """
        org_operations = OrgOperations()
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
        # Call upload_organization_photo method that takes FileBodyWrapper instance as parameter
        response = org_operations.upload_organization_photo(request)
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
                    print("Message: " + response_object.get_message())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


UploadOrganizationPhoto.initialize()
UploadOrganizationPhoto.upload_organization_photo(file_path="/Users/test.png")
