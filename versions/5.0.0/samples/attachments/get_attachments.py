from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.attachments import AttachmentsOperations, GetAttachmentsParam, ResponseWrapper, \
    APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetAttachments(object):

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_attachments(module_api_name, record_id):
        """
        This method is used to get a single record's attachments' details with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to get attachments
        """
        """
        example
        module_api_name = 'Leads'
        record_id = 3409643002267003
        """
        attachments_operations = AttachmentsOperations()
        param_instance = ParameterMap()
        param_instance.add(GetAttachmentsParam.page, 1)
        param_instance.add(GetAttachmentsParam.per_page, 10)
        param_instance.add(GetAttachmentsParam.fields, "Company")
        response = attachments_operations.get_attachments(record_id, module_api_name, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    attachments_list = response_object.get_data()
                    for attachment in attachments_list:
                        print('Attachment ID : ' + str(attachment.get_id()))
                        owner = attachment.get_owner()
                        if owner is not None:
                            print("Attachment Owner - Name: " + owner.get_name())
                            print("Attachment Owner - ID: " + str(owner.get_id()))
                            print("Attachment Owner - Email: " + owner.get_email())
                        print("Attachment Modified Time: " + str(attachment.get_modified_time()))
                        print("Attachment File Name: " + str(attachment.get_file_name()))
                        print("Attachment Created Time: " + str(attachment.get_created_time()))
                        print("Attachment File Size: " + str(attachment.get_size()))
                        parent_id = attachment.get_parent_id()
                        if parent_id is not None:
                            print("Attachment parent record Name: " + parent_id.get_key_value("name"))
                            print("Attachment parent record ID: " + str(parent_id.get_id()))
                        print("Attachment is Editable: " + str(attachment.get_editable()))
                        print("Attachment File ID: " + str(attachment.get_file_id()))
                        print("Attachment File Type: " + str(attachment.get_type()))
                        print("Attachment Type: " + str(attachment.get_attachment_type()))
                        print("Attachment SharingPermission: " + str(attachment.get_sharing_permission()))
                        print("Attachment seModule: " + str(attachment.get_se_module()))
                        modified_by = attachment.get_modified_by()
                        if modified_by is not None:
                            print("Attachment Modified By - Name: " + modified_by.get_name())
                            print("Attachment Modified By - ID: " + str(modified_by.get_id()))
                            print("Attachment Modified By - Email: " + modified_by.get_email())
                        print("Attachment State: " + str(attachment.get_state()))
                        created_by = attachment.get_created_by()
                        if created_by is not None:
                            print("Attachment Created By - Name: " + created_by.get_name())
                            print("Attachment Created By - ID: " + str(created_by.get_id()))
                            print("Attachment Created By - Email: " + created_by.get_email())
                        print("Attachment LinkUrl: " + str(attachment.get_link_url()))
                    info = response_object.get_info()
                    if info is not None:
                        if info.get_per_page() is not None:
                            print('Attachment Info PerPage: ' + str(info.get_per_page()))
                        if info.get_page() is not None:
                            print('Attachment Info Page: ' + str(info.get_page()))
                        if info.get_count() is not None:
                            print('Attachment Info Count: ' + str(info.get_count()))
                        if info.get_more_records() is not None:
                            print('Attachment Info MoreRecords: ' + str(info.get_more_records()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    if details is not None:
                        if details is not None:
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


GetAttachments.initialize()
GetAttachments.get_attachments(module_api_name="Leads", record_id=347713001)
