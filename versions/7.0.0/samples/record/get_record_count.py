from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.record import RecordOperations, RecordCountParam, CountWrapper, APIException


class GetRecordCount:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_record_count(module_api_name):
        record_operations = RecordOperations(module_api_name)
        param_instance = ParameterMap()
        param_instance.add(RecordCountParam.phone, "(990) 0-0")
        response = record_operations.record_count(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            count_handler = response.get_object()
            if count_handler is not None:
                if isinstance(count_handler, CountWrapper):
                    count_wrapper = count_handler
                    print("Record Count: " + str(count_wrapper.get_count()))
                elif isinstance(count_handler, APIException):
                    print("Status: " + count_handler.get_status().get_value())
                    print("Code: " + count_handler.get_code().get_value())
                    print("Details")
                    details = count_handler.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + count_handler.get_message().get_value())


GetRecordCount.initialize()
GetRecordCount.get_record_count(module_api_name="Leads")
