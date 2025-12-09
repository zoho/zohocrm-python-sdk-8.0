from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.roles import RolesOperations, ResponseWrapper, APIException


class GetRole:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_role(role_id):
        """
        This method is used to retrieve the data of single role with ID and print the response.
        :param role_id: The ID of the role to be obtained
        """
        try:
            roles_operations = RolesOperations()
            response = roles_operations.get_role(role_id)

            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return

                response_object = response.get_object()

                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        roles_list = response_object.get_roles()

                        if roles_list is not None:
                            for role in roles_list:
                                print("Role DisplayLabel: " + str(role.get_display_label()))

                                forecast_manager = role.get_forecast_manager()
                                if forecast_manager is not None:
                                    print("Role Forecast Manager User-ID: " + str(forecast_manager.get_id()))
                                    print("Role Forecast Manager User-Name: " + str(forecast_manager.get_name()))

                                print("Role ShareWithPeers: " + str(role.get_share_with_peers()))
                                print("Role Name: " + role.get_name())
                                print("Role Description: " + str(role.get_description()))
                                print("Role ID: " + str(role.get_id()))

                                reporting_to = role.get_reporting_to()
                                if reporting_to is not None:
                                    print("Role ReportingTo User-ID: " + str(reporting_to.get_id()))
                                    print("Role ReportingTo User-Name: " + str(reporting_to.get_name()))

                                print("Role AdminUser: " + str(role.get_admin_user()))
                                print()

                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())

        except Exception as e:
            print("Exception in get_role: " + str(e))


GetRole.initialize()
GetRole.get_role(1055806000028405017)