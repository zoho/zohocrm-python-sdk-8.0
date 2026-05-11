from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, DeleteRecordsParam, ActionWrapper, \
    SuccessResponse, APIException


class DeleteRecords:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def delete_records(module_api_name, record_ids):
        """
        This method is used to delete multiple records of a module and print the response.
        :param module_api_name: The API Name of the module to delete records.
        :param record_ids: The list of record IDs to be deleted
        """
        """
        example
        module_api_name = "Contacts";
        record_ids = [34096430756050,
            34096430729017, 34096430729009]
        """
        record_operations = RecordOperations(module_api_name)
        param_instance = ParameterMap()
        # Possible parameters for Delete Records operation
        param_instance.add(DeleteRecordsParam.wf_trigger, True)
        for record_id in record_ids:
            param_instance.add(DeleteRecordsParam.ids, record_id)
        header_instance = HeaderMap()
        # header_instance.add(DeleteRecordsHeader.x_external, "Leads.External")
        # Call deleteRecords method that takes param_instance and module_api_name as parameter.
        response = record_operations.delete_records(param_instance, header_instance)
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


DeleteRecords.initialize()
DeleteRecords.delete_records(module_api_name="Leads", record_ids=[3234234234234, 342343434223])
