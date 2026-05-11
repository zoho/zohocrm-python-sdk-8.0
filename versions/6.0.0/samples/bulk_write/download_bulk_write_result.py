import os

from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.bulk_write import BulkWriteOperations, FileBodyWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class DownloadBulkWriteResult(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def download_bulk_write_result(download_url, destination_folder):
        """
        This method is used to download the result of bulk write job.
        :param download_url: The URL present in the download_url key in the response of Get Bulk Write Job Details.
        :param destination_folder: The absolute path where downloaded file has to be stored.
        """
        """
        example
        download_url = "https://download-accl.zoho.com/6735/bulk-write/347706122009.zip"
        destination_folder = "/Users/user_name/Documents"
        """
        bulk_write_operations = BulkWriteOperations()
        # Call download_bulk_write_result method that takes download_url as parameter
        response = bulk_write_operations.download_bulk_write_result(download_url)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, FileBodyWrapper):
                    stream_wrapper = response_object.get_file()
                    # Construct the file name by joining the destination_folder and the name from StreamWrapper instance
                    file_name = os.path.join(destination_folder, stream_wrapper.get_name())
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


DownloadBulkWriteResult.initialize()
DownloadBulkWriteResult.download_bulk_write_result(
    download_url="https://download-accl.zoho.com/v2/crm/3477061008.zip", destination_folder="/Users/file")
