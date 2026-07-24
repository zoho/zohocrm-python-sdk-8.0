from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.user_groups import UserGroupsOperations, AssociatedUserCount, APIException, \
    GetAssociatedUsersCountParam, Criteria, Field
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class GetAssociatedUsersCount(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.DEVELOPER()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_associated_users_count():
        user_groups_operations = UserGroupsOperations()
        param_instance = ParameterMap()
        param_instance.add(GetAssociatedUsersCountParam.page, "1")
        param_instance.add(GetAssociatedUsersCountParam.per_page, "10")
        criteria = Criteria()
        criteria.set_group_operator(Choice("OR"))
        group = []
        group1 = Criteria()
        group1.set_comparator("equal")
        group1.set_value("test group")
        field1 = Field()
        field1.set_api_name("name")
        group1.set_field(field1)
        group.append(group1)

        group2 = Criteria()
        group2.set_comparator("equal")
        group2.set_value("Tier2")
        field2 = Field()
        field2.set_api_name("name")
        group2.set_field(field2)
        group.append(group2)

        criteria.set_group(group)
        param_instance.add(GetAssociatedUsersCountParam.filters, criteria)
        response = user_groups_operations.get_associated_users_count(param_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, AssociatedUserCount):
                associated_users_count = response_object.get_associated_users_count()
                if associated_users_count is not None:
                    for associated_user in associated_users_count:
                        print("AssociatedUSer count " + str(associated_user.get_count()))
                        user_group = associated_user.get_user_group()
                        if user_group is not None:
                            print("Associated Name: " + user_group.get_name())
                            print("AssociatedUser Id: " + str(user_group.get_id()))
                info = response_object.get_info()
                if info is not None:
                    if info.get_per_page() is not None:
                        print("User Info PerPage: " + str(info.get_per_page()))
                    if info.get_count() is not None:
                        print("User Info Count: " + str(info.get_count()))
                    if info.get_page() is not None:
                        print("User Info Page: " + str(info.get_page()))
                    if info.get_more_records() is not None:
                        print("User Info MoreRecords: " + str(info.get_more_records()))
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetAssociatedUsersCount.initialize()
GetAssociatedUsersCount.get_associated_users_count()
