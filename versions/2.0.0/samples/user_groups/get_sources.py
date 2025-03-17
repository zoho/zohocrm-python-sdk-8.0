from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap, Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.user_groups import UserGroupsOperations, SourcesWrapper, APIException


class GetSources(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_sources(group_id):
        user_group_operations = UserGroupsOperations()
        param_instance = ParameterMap()
        response = user_group_operations.get_sources(group_id, param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, SourcesWrapper):
                sources = response_object.get_sources()
                for source in sources:
                    source1 = source.get_source()
                    if source1 is not None:
                        print("Source user_name: " + source1.get_name())
                        print("Source user_id: " + str(source1.get_id()))
                    print("Sources Type : " + source.get_type().get_value())
                    print("Sources Subordinates: " + str(source.get_subordinates()))
                info = response_object.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("Sources Info PerPage: " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("Sources Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("Sources Info Page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("Sources Info MoreRecords: " + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetSources.initialize()
GetSources.get_sources(group_id=44028001219057)
