from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.attachments import AttachmentsOperations, ActionWrapper, SuccessResponse, \
    APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class DeleteAttachment:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_attachment(module_api_name, record_id, attachment_id):
        """
        This method is used to delete an attachment of a single record with ID and attachment ID and print the response
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to delete attachment
        :param attachment_id: The ID of the attachment to be deleted
        """
        """
        example
        module_api_name = "Leads";
        record_id = 3409643002267003
        attachment_id = 3409643002267024
        """
        attachments_operations = AttachmentsOperations()
        response = attachments_operations.delete_attachment(attachment_id, record_id, module_api_name)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
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
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message())
                        elif isinstance(action_response, APIException):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())


DeleteAttachment.initialize()
DeleteAttachment.delete_attachment(module_api_name="Leads", record_id=3477613001, attachment_id=3477576001)
