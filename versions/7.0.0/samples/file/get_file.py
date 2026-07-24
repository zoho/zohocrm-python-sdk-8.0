from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.files import FilesOperations, GetFileParam
from zohocrmsdk.src.com.zoho.crm.api.files import FileBodyWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetFile:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_file(file_id):
        try:
            files_operations = FilesOperations()
            param_instance = ParameterMap()
            param_instance.add(GetFileParam.id, file_id)

            response = files_operations.get_file(param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, FileBodyWrapper):
                        with open("./" + response_object.get_file().get_name(), "wb") as f:
                            for chunk in response_object.get_file().get_stream():
                                f.write(chunk)
                        print("File downloaded successfully")
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling get_file: " + str(e))


GetFile.initialize()
GetFile.get_file("51147aee5c9390e6100059c4991231485a9144bc37137bda53c2590cda59be9ea09aad02531e1e8c1c4bdfb9c3378ee5")