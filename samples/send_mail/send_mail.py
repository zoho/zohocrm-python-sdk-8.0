from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.send_mail import SendMailOperations, BodyWrapper, Data, From, To, Cc, Attachment, InReplyTo, Owner, InventoryDetails, InventoryTemplate, DataSubjectRequest, LinkedRecord, LinkedModule, ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class SendMail:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def send_mail(record_id, module_api_name):
        """
        This method is used to send an email from a record.

        Args:
            record_id (int): The ID of the record from which to send mail
            module_api_name (str): The API name of the module
        """
        try:
            send_mail_operations = SendMailOperations(record_id, module_api_name)
            request = BodyWrapper()
            data_list = []
            data = Data()

            # Set From
            from_address = From()
            from_address.set_user_name("sender_name")
            from_address.set_email("sender@example.com")
            data.set_from(from_address)

            # Set To
            to_list = []
            to_address = To()
            to_address.set_user_name("recipient_name")
            to_address.set_email("recipient@example.com")
            to_list.append(to_address)
            data.set_to(to_list)

            # Set Cc
            cc_list = []
            cc_address = Cc()
            cc_address.set_user_name("cc_name")
            cc_address.set_email("cc@example.com")
            cc_list.append(cc_address)
            data.set_cc(cc_list)

            # Set Bcc
            bcc_list = []
            bcc_address = Cc()
            bcc_address.set_user_name("bcc_name")
            bcc_address.set_email("bcc@example.com")
            bcc_list.append(bcc_address)
            data.set_bcc(bcc_list)

            # Set Reply To
            reply_to = To()
            reply_to.set_user_name("reply_name")
            reply_to.set_email("reply@example.com")
            data.set_reply_to(reply_to)

            # Set Org Email
            data.set_org_email(True)

            # Set Mail Format
            data.set_mail_format(Choice("html"))

            # Set Subject and Content
            data.set_subject("Test Email Subject")
            data.set_content("<h3>Email Content</h3><p>This is a test email sent via Zoho CRM SDK.</p>")

            # Set Consent Email
            data.set_consent_email(False)

            # Set In Reply To (optional - for replying to an existing email)
            in_reply_to = InReplyTo()
            in_reply_to.set_message_id("message_id")
            owner = Owner()
            owner.set_id(1055806000017236002)  # Replace with actual owner ID
            owner.set_name("owner_name")
            in_reply_to.set_owner(owner)
            data.set_in_reply_to(in_reply_to)

            # Set Inventory Details (optional)
            inventory_details = InventoryDetails()
            inventory_template = InventoryTemplate()
            inventory_template.set_id(1055806000028347001)  # Replace with actual template ID
            inventory_template.set_name("template_name")
            inventory_details.set_inventory_template(inventory_template)
            data.set_inventory_details(inventory_details)

            # Set Data Subject Request (optional)
            data_subject_request = DataSubjectRequest()
            data_subject_request.set_id(1055806000028347001)  # Replace with actual ID
            data_subject_request.set_type("Leads")
            data.set_data_subject_request(data_subject_request)

            # Set Attachments (optional)
            attachment_list = []
            attachment = Attachment()
            attachment.set_id("attachment_id")  # Replace with actual attachment ID
            attachment_list.append(attachment)
            data.set_attachments(attachment_list)

            data_list.append(data)
            request.set_data(data_list)
            response = send_mail_operations.send_mail(request)
            if response is not None:
                print("Status Code: " + str(response.get_status_code()))
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_data()
                        for action_response in action_response_list:
                            if isinstance(action_response, SuccessResponse):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(key + " : " + str(value))
                                print("Message: " + action_response.get_message())

                            elif isinstance(action_response, APIException):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(key + " : " + str(value))
                                print("Message: " + action_response.get_message())

                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        if details is not None:
                            for key, value in details.items():
                                print(key + " : " + str(value))
                        print("Message: " + response_object.get_message())

        except Exception as e:
            print(f"Exception occurred: {e}")


SendMail.initialize()
SendMail.send_mail(1055806000028347001, "Leads")
