from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.bulk_write import BulkWriteOperations, RequestWrapper, CallBack, Resource, \
    FieldMapping, SuccessResponse, APIException, DefaultValue
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class CreateBulkWriteJob(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_bulk_write_job(module_api_name, file_id):
        """
        This method is used to create bulk write job with the uploaded file ID
        :param module_api_name: The API Name of the module.
        :param file_id: The ID of the uploaded file to create BulkWrite Job.
        example
        module_api_name = 'Leads'
        file_id = 3409643002212140
        """
        bulk_write_operations = BulkWriteOperations()
        request = RequestWrapper()
        call_back = CallBack()
        call_back.set_url("https://www.example.com/callback")
        call_back.set_method(Choice('post'))
        # The Bulk Read Job's details is posted to this URL on successful completion / failure of the job.
        request.set_callback(call_back)
        request.set_character_encoding('UTF-8')
        # To set the type of operation you want to perform on the bulk write job.
        request.set_operation(Choice('update'))
        request.set_ignore_empty(True)
        resources = []
        resource = Resource()
        # To set the type of module that you want to import. The value is data.
        resource.set_type(Choice('data'))
        # To set API name of the module that you select for bulk write job.
        # Specifies the API Name of the module to be read.
        module = MinifiedModule()
        module.set_api_name(module_api_name)
        resource.set_module(module)
        # To set the fileId obtained from file upload API.
        resource.set_file_id(file_id)
        # To set a field as a unique field or ID of a record.
        resource.set_find_by('id')
        field_mappings = []
        field_mapping = FieldMapping()
        # To set API name of the field present in Zoho module object that you want to import.
        field_mapping.set_api_name('Email')
        # To set the column index of the field you want to map to the CRM field.
        field_mapping.set_index(1)
        field_mappings.append(field_mapping)
        field_mapping = FieldMapping()
        # To set API name of the field present in Zoho module object that you want to import.
        field_mapping.set_api_name('Company')
        # To set the column index of the field you want to map to the CRM field.
        field_mapping.set_index(2)
        field_mappings.append(field_mapping)
        field_mapping = FieldMapping()
        # To set API name of the field present in Zoho module object that you want to import.
        field_mapping.set_api_name('Last_Name')
        # To set the column index of the field you want to map to the CRM field.
        field_mapping.set_index(0)
        field_mappings.append(field_mapping)
        # field_mapping = FieldMapping()
        # # To set API name of the field present in Zoho module object that you want to import.
        # field_mapping.set_api_name('Phone')
        # # To set the column index of the field you want to map to the CRM field.
        # field_mapping.set_index(3)
        # field_mappings.append(field_mapping)
        field_mapping = FieldMapping()
        field_mapping.set_api_name('id')
        field_mapping.set_index(4)
        field_mappings.append(field_mapping)
        field_mapping = FieldMapping()
        field_mapping.set_api_name('Website')
        default_value = DefaultValue()
        default_value.set_value("www.zohoapis.com")
        # To set the default value for an empty column in the uploaded file.
        field_mapping.set_default_value(default_value)
        field_mappings.append(field_mapping)
        resource.set_field_mappings(field_mappings)
        module = MinifiedModule()
        module.set_api_name(module_api_name)
        resource.set_module(module)
        resources.append(resource)
        request.set_resource(resources)
        # Call create_bulk_write_job method that takes RequestWrapper instance as parameter
        response = bulk_write_operations.create_bulk_write_job(request)
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


CreateBulkWriteJob.initialize()
CreateBulkWriteJob.create_bulk_write_job(module_api_name="Leads", file_id="34775486001")
