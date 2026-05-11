from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.user_groups import UserGroupsOperations, AssociationWrapper, APIException


class GetAssociations(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_associations(group_id):
        user_group_operations = UserGroupsOperations()
        response = user_group_operations.get_associations(group_id)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, AssociationWrapper):
                association_wrapper = response_object
                associations = association_wrapper.get_associations()
                if associations is not None:
                    for association_response in associations:
                        print("Associations Type:  " + association_response.get_type())
                        resource = association_response.get_resource()
                        if resource is not None:
                            print("Associations Resource Id: " + str(resource.get_id()))
                            print("Associations Resource Name : " + resource.get_name())
                        detail = association_response.get_detail()
                        if detail is not None:
                            module = detail.get_module()
                            if module is not None:
                                print("Associations Module Id : " + str(module.get_id()))
                                print("Associations Module api_name : " + module.get_api_name())
                                print("Associations Module : " + module.get_module())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message())


GetAssociations.initialize()
GetAssociations.get_associations(group_id=44028001326019)
