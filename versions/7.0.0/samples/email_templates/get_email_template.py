from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.email_templates import EmailTemplatesOperations
from zohocrmsdk.src.com.zoho.crm.api.email_templates import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetEmailTemplate:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_email_template(template_id):
        try:
            email_templates_operations = EmailTemplatesOperations()
            response = email_templates_operations.get_email_template(template_id)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        email_templates = response_object.get_email_templates()
                        for email_template in email_templates:
                            print("EmailTemplate ID: " + str(email_template.get_id()))
                            print("EmailTemplate Name: " + str(email_template.get_name()))
                            print("EmailTemplate Subject: " + str(email_template.get_subject()))
                            print("EmailTemplate EditorMode: " + str(email_template.get_editor_mode()))
                            print("EmailTemplate Favorite: " + str(email_template.get_favorite()))
                            print("EmailTemplate Associated: " + str(email_template.get_associated()))
                            print("EmailTemplate ConsentLinked: " + str(email_template.get_consent_linked()))
                            print("EmailTemplate Description: " + str(email_template.get_description()))
                            print("EmailTemplate Category: " + str(email_template.get_category()))
                            print("EmailTemplate Active: " + str(email_template.get_active()))
                            print("EmailTemplate MailContent: " + str(email_template.get_mail_content()))
                            print("EmailTemplate Content: " + str(email_template.get_content()))
                            if email_template.get_created_time() is not None:
                                print("EmailTemplate CreatedTime: " + str(email_template.get_created_time()))
                            if email_template.get_modified_time() is not None:
                                print("EmailTemplate ModifiedTime: " + str(email_template.get_modified_time()))
                            if email_template.get_last_usage_time() is not None:
                                print("EmailTemplate LastUsageTime: " + str(email_template.get_last_usage_time()))
                            if email_template.get_folder() is not None:
                                folder = email_template.get_folder()
                                print("EmailTemplate Folder ID: " + str(folder.get_id()))
                                print("EmailTemplate Folder Name: " + str(folder.get_name()))
                            if email_template.get_module() is not None:
                                module = email_template.get_module()
                                print("EmailTemplate Module ID: " + str(module.get_id()))
                                print("EmailTemplate Module APIName: " + str(module.get_api_name()))
                            if email_template.get_created_by() is not None:
                                created_by = email_template.get_created_by()
                                print("EmailTemplate CreatedBy ID: " + str(created_by.get_id()))
                                print("EmailTemplate CreatedBy Name: " + str(created_by.get_name()))
                            if email_template.get_modified_by() is not None:
                                modified_by = email_template.get_modified_by()
                                print("EmailTemplate ModifiedBy ID: " + str(modified_by.get_id()))
                                print("EmailTemplate ModifiedBy Name: " + str(modified_by.get_name()))
                            if email_template.get_attachments() is not None:
                                attachments = email_template.get_attachments()
                                for attachment in attachments:
                                    print("Attachment ID: " + str(attachment.get_id()))
                                    print("Attachment FileName: " + str(attachment.get_file_name()))
                                    print("Attachment FileId: " + str(attachment.get_file_id()))
                                    print("Attachment Size: " + str(attachment.get_size()))
                            if email_template.get_last_version_statistics() is not None:
                                last_version_statistics = email_template.get_last_version_statistics()
                                print("LastVersionStatistics Tracked: " + str(last_version_statistics.get_tracked()))
                                print("LastVersionStatistics Delivered: " + str(last_version_statistics.get_delivered()))
                                print("LastVersionStatistics Opened: " + str(last_version_statistics.get_opened()))
                                print("LastVersionStatistics Bounced: " + str(last_version_statistics.get_bounced()))
                                print("LastVersionStatistics Sent: " + str(last_version_statistics.get_sent()))
                                print("LastVersionStatistics Clicked: " + str(last_version_statistics.get_clicked()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling get_email_template: " + str(e))


GetEmailTemplate.initialize()
GetEmailTemplate.get_email_template(template_id=1055806000017124014)
