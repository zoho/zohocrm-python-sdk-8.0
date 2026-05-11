from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.duplicate_check_preference_operations import \
    DuplicateCheckPreferenceOperations
from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.response_handler import ResponseHandler
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer


class GetDuplicateCheckPreference:
    @staticmethod
    def get_duplicate_check_preference(module_api_name):
        duplicate_check_preference_operations = DuplicateCheckPreferenceOperations(module_api_name)
        response = duplicate_check_preference_operations.get_duplicate_check_preference()

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseHandler):
                response_wrapper = response_handler

                if hasattr(response_wrapper, 'get_duplicate_check_preference'):
                    duplicate_check_preference = response_wrapper.get_duplicate_check_preference()
                    print("duplicate_check_preference Type : " + duplicate_check_preference.get_type().get_value())
                    type_configurations = duplicate_check_preference.get_type_configurations()

                    if type_configurations is not None:
                        for type_configuration in type_configurations:
                            mapped_module = type_configuration.get_mapped_module()

                            if mapped_module is not None:
                                print("duplicate_check_preference TypeConfiguration MappedModule Id : " + str(
                                    mapped_module.get_id()))
                                print("duplicate_check_preference TypeConfiguration MappedModule Name : " +
                                      mapped_module.get_name())
                                print("duplicate_check_preference TypeConfiguration MappedModule APIName : " +
                                      mapped_module.get_api_name())
                            field_mappings = type_configuration.get_field_mappings()

                            if field_mappings is not None:
                                for field_mapping in field_mappings:
                                    current_field = field_mapping.get_current_field()
                                    if current_field is not None:
                                        print("duplicate_check_preference TypeConfiguration FieldMappings "
                                              "CurrentField Id : " + str(current_field.get_id()))
                                        print("duplicate_check_preference TypeConfiguration FieldMappings "
                                              "CurrentField Name : " + current_field.get_name())
                                        print("duplicate_check_preference TypeConfiguration FieldMappings "
                                              "CurrentField APIName : " + current_field.get_api_name())
                                    mapped_field = field_mapping.get_mapped_field()
                                    if mapped_field is not None:
                                        print("duplicate_check_preference TypeConfiguration FieldMappings MappedField "
                                              "Id : " + str(mapped_field.get_id()))
                                        print("duplicate_check_preference TypeConfiguration FieldMappings MappedField "
                                              "Name : " + mapped_field.get_name())
                                        print("duplicate_check_preference TypeConfiguration FieldMappings MappedField "
                                              "APIName : " + mapped_field.get_api_name())
            elif isinstance(response_handler, APIException):
                exception = response_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")

                for key, value in exception.get_details().items():
                    print(key + ": " + str(value))

                print("Message: " + exception.get_message().get_value())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


GetDuplicateCheckPreference.initialize()
GetDuplicateCheckPreference.get_duplicate_check_preference(module_api_name="Leads")
