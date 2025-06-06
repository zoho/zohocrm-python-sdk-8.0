from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
from zohocrmsdk.src.com.zoho.crm.api import Param
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.functions import APIException
from zohocrmsdk.src.com.zoho.crm.api.functions import FileBodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.functions import FunctionsOperations
from zohocrmsdk.src.com.zoho.crm.api.functions import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.util import StreamWrapper


class ExecuteFunctionUsingFile:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def execute_function_using_file():
        functionName = "get_record_lead"
        authType = "oauth"

        functionsOperations = FunctionsOperations(functionName, authType)

        fileBodyWrapper = FileBodyWrapper()
        streamWrapper = StreamWrapper("./sample.txt")
        fileBodyWrapper.set_inputfile(streamWrapper)

        paramInstance = ParameterMap()
        param = dict()
        param["1221"] = "2111221"
        param["15221"] = "21113221"
        param["12421"] = "211341221"
        paramInstance.add(Param("Python", dict.__class__.__name__), param)
        headerInstance = HeaderMap()
        response = functionsOperations.execute_function_using_file(fileBodyWrapper, paramInstance, headerInstance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                response_wrapper = response.get_object()
                if isinstance(response_wrapper, SuccessResponse):
                    print("Code: " + response_wrapper.get_code().get_value())
                    print("Details")
                    details = response_wrapper.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_wrapper.get_message().get_value())
                elif isinstance(response_wrapper, APIException):
                    print("Status: " + response_wrapper.get_status().get_value())
                    print("Code: " + response_wrapper.get_code().get_value())
                    print("Details")
                    details = response_wrapper.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_wrapper.get_message().get_value())


ExecuteFunctionUsingFile.initialize()
ExecuteFunctionUsingFile.execute_function_using_file()
