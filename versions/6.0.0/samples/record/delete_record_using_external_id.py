from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, DeleteRecordParam, DeleteRecordHeader, \
    ActionWrapper, SuccessResponse, APIException


class DeleteRecordUsingExternalID:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_record_using_external_id(module_api_name, external_field_value):
        """
        This method is used to delete a single record of a module with ID and print the response.
        :param module_api_name: The API Name of the record's module.
        :param external_field_value:
        """
        """
        example
        module_api_name = 'Leads'
        external_field_value = '34770603276'
        """
        record_operations = RecordOperations(module_api_name)
        param_instance = ParameterMap()
        # Possible parameters for Delete Record operation
        param_instance.add(DeleteRecordParam.wf_trigger, True)
        header_instance = HeaderMap()
        header_instance.add(DeleteRecordHeader.x_external, "Leads.External")
        # Call delete_record_using_external_id method that takes external_field_value, module_api_name,
        # param_instance and header_instance as parameter.
        response = record_operations.delete_record_using_external_id(external_field_value, param_instance,
                                                                     header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_data()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


DeleteRecordUsingExternalID.initialize()
DeleteRecordUsingExternalID.delete_record_using_external_id(module_api_name="Leads",
                                                            external_field_value="3243532423232")
