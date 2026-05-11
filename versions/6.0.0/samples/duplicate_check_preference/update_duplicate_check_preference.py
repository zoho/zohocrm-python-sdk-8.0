from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.action_wrapper import ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.body_wrapper import BodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.current_field import CurrentField
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.duplicate_check_preference import \
    DuplicateCheckPreference
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.duplicate_check_preference_operations import \
    DuplicateCheckPreferenceOperations
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.field_mappings import FieldMappings
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.mapped_field import MappedField
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.mapped_module import MappedModule
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.success_response import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.type_configuration import TypeConfiguration
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer


class UpdateDuplicateCheckPreference:
    @staticmethod
    def update_duplicate_check_preference(module_api_name):
        duplicate_check_preference_operations = DuplicateCheckPreferenceOperations(module_api_name)
        request = BodyWrapper()
        duplicate_check_preference = DuplicateCheckPreference()
        duplicate_check_preference.type = 'converted_records'

        type_configurations = []
        type_configuration = TypeConfiguration()
        mapped_module = MappedModule()
        mapped_module.id = '347706102175'
        mapped_module.api_name = 'Leads'
        type_configuration.mapped_module = mapped_module

        field_mappings = []
        field_mapping = FieldMappings()
        current_field = CurrentField()
        current_field.id = '3477061000570001'
        current_field.api_name = 'Email_1'
        field_mapping.current_field = current_field

        mapped_field = MappedField()
        mapped_field.id = '347706123537018'
        mapped_field.api_name = 'Email_2'
        field_mapping.mapped_field = mapped_field

        field_mappings.append(field_mapping)
        type_configuration.field_mappings = field_mappings
        type_configurations.append(type_configuration)
        duplicate_check_preference.type_configurations = type_configurations

        request.duplicate_check_preference = duplicate_check_preference
        response = duplicate_check_preference_operations.update_duplicate_check_preference(request)

        if response is not None:
            print("Status Code:", response.get_status_code())

            action_handler = response.get_object()
            if isinstance(action_handler, ActionWrapper):
                action_wrapper = action_handler
                action_response = action_wrapper.get_duplicate_check_preference()

                if isinstance(action_response, SuccessResponse):
                    success_response = action_response
                    print("Status:", success_response.get_status())
                    print("Code:", success_response.get_code())
                    print("Details:")
                    for key, value in success_response.get_details().items():
                        print(f"{key}: {value}")
                    print("Message:", success_response.get_message())

                elif isinstance(action_response, APIException):
                    exception = action_response
                    print("Status:", exception.get_status())
                    print("Code:", exception.get_code())
                    print("Details:")
                    for key, value in exception.get_details().items():
                        print(f"{key}: {value}")
                    print("Message:", exception.get_message())

            elif isinstance(action_handler, APIException):
                exception = action_handler
                print("Status:", exception.get_status())
                print("Code:", exception.get_code())
                print("Details:")
                for key, value in exception.get_details().items():
                    print(f"{key}: {value}")
                print("Message:", exception.get_message())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


UpdateDuplicateCheckPreference.initialize()
UpdateDuplicateCheckPreference.update_duplicate_check_preference(module_api_name="Leads")
