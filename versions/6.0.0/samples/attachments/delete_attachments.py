from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.attachments import AttachmentsOperations, DeleteAttachmentsParam, ActionWrapper, \
    SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class DeleteAttachments(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_attachments(module_api_name, record_id, attachment_ids):
        """
        This method is used to Delete attachments of a single record with ID and print the response.
        :param module_api_name: The API Name of the record's module
        :param record_id: The ID of the record to delete attachments
        :param attachment_ids: The list of attachment IDs to be deleted
        """
        """
        example
        module_api_name= "Leads"
        record_id = 3409267003
        attachment_ids = ["34092267012", "3409643002267018", "3409643002267010"]
        """
        attachments_operations = AttachmentsOperations()
        param_instance = ParameterMap()
        # Add the ids to parameter map instance
        for attachment_id in attachment_ids:
            param_instance.add(DeleteAttachmentsParam.ids, attachment_id)
        # Call delete_attachments method that takes paramInstance as parameter
        response = attachments_operations.delete_attachments(record_id, module_api_name, param_instance)
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


DeleteAttachments.initialize()
DeleteAttachments.delete_attachments(module_api_name="Leads",
                                     record_id=34713001, attachment_ids=["347577001", "3477578001"])
