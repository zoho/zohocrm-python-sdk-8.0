from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.modules import APIException, SuccessResponse, ActionWrapper, ModulesOperations, \
    Modules, BodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.profiles import MinifiedProfile


class UpdateModuleById:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_module_by_id(module_id):
        """
        This method is used to update module details using module id and print the response.
        :param module_id: The id of the module to update
        """
        """
        example
        module_id = 34096430252001
        """
        modules_operations = ModulesOperations()
        modules_list = []
        profiles_list = []
        profile = MinifiedProfile()
        # To set the Profile id
        profile.set_id(440280031160)
        # profile.set_delete(True)
        # Add Profile instance to the list
        profiles_list.append(profile)
        module = Modules()
        module.set_profiles(profiles_list)
        # Add the Module instance to list
        modules_list.append(module)
        request = BodyWrapper()
        request.set_modules(modules_list)
        # Call update_module_by_id method that takes BodyWrapper instance and module_id as parameter
        response = modules_operations.update_module(module_id, request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_modules()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
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


UpdateModuleById.initialize()
UpdateModuleById.update_module_by_id(module_id=347485367)
