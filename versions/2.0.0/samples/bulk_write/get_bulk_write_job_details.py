from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.bulk_write import BulkWriteOperations, BulkWriteResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetBulkWriteJobDetails(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_bulk_write_job_details(job_id):
        """
        This method is used to get the details of a bulk write job performed previously.
        :param job_id: The unique ID of the bulk write job.
        """
        """
        example
        job_id = 3477061005615003
        """
        bulk_write_operations = BulkWriteOperations()
        # Call get_bulk_write_job_details method that takes job_id as parameter
        response = bulk_write_operations.get_bulk_write_job_details(job_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, BulkWriteResponse):
                    print("Bulk write Job Status: " + response_object.get_status())
                    print("Bulk write CharacterEncoding: ")
                    print(response_object.get_character_encoding())
                    resources = response_object.get_resource()
                    if resources is not None:
                        for resource in resources:
                            print("Bulk write Resource Status: " + resource.get_status().get_value())
                            print("Bulk write Resource Type: " + resource.get_type().get_value())
                            print("Bulk write Resource Module: ")
                            print(resource.get_module().get_id())
                            print("Bulk write Resource Module: " + resource.get_module().get_api_name())
                            field_mappings = resource.get_field_mappings()
                            if field_mappings is not None:
                                for field_mapping in field_mappings:
                                    print("Bulk write Resource FieldMapping Module: " + field_mapping.get_api_name())
                                    if field_mapping.get_index() is not None:
                                        print(
                                            "Bulk write Resource FieldMapping Index: " + str(field_mapping.get_index()))
                                    if field_mapping.get_format() is not None:
                                        print("Bulk write Resource FieldMapping Format: " + field_mapping.get_format())
                                    if field_mapping.get_find_by() is not None:
                                        print("Bulk write Resource FieldMapping FindBy: " + field_mapping.get_find_by())
                                    if field_mapping.get_module() is not None:
                                        print("Bulk write Resource FieldMapping module: " + field_mapping.get_module())
                                    default_value = field_mapping.get_default_value()
                                    if default_value is not None:
                                        print('Default values' + default_value.get_value())

                            file = resource.get_file()
                            if file is not None:
                                print("Bulk write Resource File Status: " + file.get_status().get_value())
                                print("Bulk write Resource File Name: " + file.get_name())
                                print("Bulk write Resource File AddedCount: " + str(file.get_added_count()))
                                print("Bulk write Resource File SkippedCount: " + str(file.get_skipped_count()))
                                print("Bulk write Resource File UpdatedCount: " + str(file.get_updated_count()))
                                print("Bulk write Resource File TotalCount: " + str(file.get_total_count()))
                    callback = response_object.get_callback()
                    if callback is not None:
                        print("Bulk write CallBack Url: " + callback.get_url())
                        print("Bulk write CallBack Method: " + callback.get_method().get_value())
                    print("Bulk write ID: " + str(response_object.get_id()))
                    result = response_object.get_result()
                    if result is not None:
                        print("Bulk write DownloadUrl: " + result.get_download_url())
                    created_by = response_object.get_created_by()
                    if created_by is not None:
                        print("Bulk write Created By - Name: " + created_by.get_name())
                        print("Bulk write Created By - ID: " + str(created_by.get_id()))
                    print("Bulk write Operation: " + response_object.get_operation())
                    print("Bulk write File CreatedTime: " + str(response_object.get_created_time()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetBulkWriteJobDetails.initialize()
GetBulkWriteJobDetails.get_bulk_write_job_details(job_id="3477084002")
