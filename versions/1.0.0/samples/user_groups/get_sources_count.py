from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.user_groups import UserGroupsOperations, SourcesCountWrapper, APIException


class GetSourcesCount:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_sources_count(group_id):
        user_group_operations = UserGroupsOperations()
        response = user_group_operations.get_sources_count(group_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, SourcesCountWrapper):
                sources_count = response_object.get_sources_count()
                for count in sources_count:
                    print("sources Count Territories: " + str(count.get_territories()))
                    print("sources Count Roles: " + str(count.get_roles()))
                    print("sources Count Groups: " + str(count.get_groups()))
                    users = count.get_users()
                    if users is not None:
                        print("Sources Users Inactive: " + str(users.get_inactive()))
                        print("Sources Users Deleted: " + str(users.get_deleted()))
                        print("Sources Users Groups: " + str(users.get_active()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetSourcesCount.initialize()
GetSourcesCount.get_sources_count(group_id=347706117236002)
