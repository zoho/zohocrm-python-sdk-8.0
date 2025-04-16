from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.body_wrapper import BodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.mass_delete import MassDelete
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.mass_delete_tags_operations import MassDeleteTagsOperations
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.module import Module
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.success_response import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.tag import Tag


class MassDeleteTags:
    @staticmethod
    def mass_delete_tags():
        mass_delete_tags_operations = MassDeleteTagsOperations()

        # Create an instance of BodyWrapper
        request = BodyWrapper()

        # Create a list of MassDelete instances
        mass_delete_list = []

        # Create an instance of MassDelete
        mass_delete1 = MassDelete()

        # Set Module to the instance of MassDelete
        module = Module()
        module.set_api_name("Leads")
        module.set_id(72722537)
        mass_delete1.set_module(module)

        # Create a list of Tag instances
        tags = []

        tag1 = Tag()
        tag1.set_id(7272250558034)
        tags.append(tag1)

        tag2 = Tag()
        tag2.set_id(727220558035)
        tags.append(tag2)

        mass_delete1.set_tags(tags)

        mass_delete_list.append(mass_delete1)

        request.set_mass_delete(mass_delete_list)

        # Call mass_delete_tags method
        response = mass_delete_tags_operations.mass_delete_tags(request)

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            action_response = response.get_object()

            if isinstance(action_response, SuccessResponse):
                success_response = action_response
                print("Status: " + success_response.get_status().get_value())
                print("Code: " + success_response.get_code().get_value())
                print("Details: ")
                for key, value in success_response.get_details().items():
                    print(f"{key}: {value}")
                print("Message: " + success_response.get_message())

            elif isinstance(action_response, APIException):
                exception = action_response
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")
                if exception.get_details() is not None:
                    for key, value in exception.get_details().items():
                        print(f"{key}: {value}")
                print("Message: " + exception.get_message())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


MassDeleteTags.initialize()
MassDeleteTags.mass_delete_tags()
