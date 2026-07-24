from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.profiles import ProfilesOperations, GetProfilesParam
from zohocrmsdk.src.com.zoho.crm.api.profiles import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetProfiles:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_profiles():
        try:
            profiles_operations = ProfilesOperations()
            param_instance = ParameterMap()
            param_instance.add(GetProfilesParam.include_lite_profile, True)
            
            response = profiles_operations.get_profiles(param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        profiles_list = response_object.get_profiles()
                        for profile in profiles_list:
                            print("Profile DisplayLabel: " + str(profile.get_display_label()))
                            if profile.get_created_time() is not None:
                                print("Profile CreatedTime: " + str(profile.get_created_time()))
                            if profile.get_modified_time() is not None:
                                print("Profile ModifiedTime: " + str(profile.get_modified_time()))
                            print("Profile Name: " + str(profile.get_name()))
                            modified_by = profile.get_modified_by()
                            if modified_by is not None:
                                print("Profile Modified By - Name: " + str(modified_by.get_name()))
                                print("Profile Modified By - ID: " + str(modified_by.get_id()))
                            print("Profile Description: " + str(profile.get_description()))
                            print("Profile ID: " + str(profile.get_id()))
                            print("Profile Category: " + str(profile.get_category()))
                            created_by = profile.get_created_by()
                            if created_by is not None:
                                print("Profile Created By - Name: " + str(created_by.get_name()))
                                print("Profile Created By - ID: " + str(created_by.get_id()))
                            if profile.get_delete() is not None:
                                print("Profile Delete: " + str(profile.get_delete()))
                            if profile.get_default() is not None:
                                print("Profile Default: " + str(profile.get_default()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling get_profiles: " + str(e))


GetProfiles.initialize()
GetProfiles.get_profiles()