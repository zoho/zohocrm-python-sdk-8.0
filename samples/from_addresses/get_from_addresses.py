from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.from_addresses import FromAddressesOperations, ResponseWrapper, APIException


class GetFromAddresses:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_from_addresses(user_id=None):
        """
        This method is used to get the from addresses configured for sending emails.

        Args:
            user_id (str): The ID of the user (optional)
        """
        try:
            from_addresses_operations = FromAddressesOperations(user_id)
            response = from_addresses_operations.get_from_addresses()
            if response is not None:
                print("Status Code: " + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print("No Content" if response.get_status_code() == 204 else "Not Modified")
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        from_addresses = response_object.get_from_addresses()
                        if from_addresses is not None:
                            for from_address in from_addresses:
                                print("From Address Email: " + str(from_address.get_email()))
                                print("From Address Type: " + str(from_address.get_type()))
                                print("From Address ID: " + str(from_address.get_id()))
                                print("From Address UserName: " + str(from_address.get_user_name()))
                                print("From Address Default: " + str(from_address.get_default()))
                                print()

                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + " : " + str(value))
                        print("Message: " + response_object.get_message())

        except Exception as e:
            print(f"Exception occurred: {e}")


GetFromAddresses.initialize()
GetFromAddresses.get_from_addresses("1055806000000173021")
