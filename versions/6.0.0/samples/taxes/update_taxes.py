from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.taxes import TaxesOperations, BodyWrapper, ActionWrapper, APIException, Tax, OrgTax

class UpdateTaxes:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_taxes():
        try:
            taxes_operations = TaxesOperations()
            request = BodyWrapper()
            org_tax = OrgTax()
            tax_list = []
            tax1 = Tax()
            tax1.set_id(1055806000023782001)  # Existing tax ID to update (replace with actual ID)
            tax1.set_name("Updated GST")
            tax1.set_sequence_number(1)
            tax1.set_value(18.0)
            tax_list.append(tax1)
            # Set the taxes list to org_tax
            org_tax.set_taxes(tax_list)
            # Set the org_tax to request
            request.set_org_taxes(org_tax)
            # Call update_taxes method that takes BodyWrapper instance as parameter
            response = taxes_operations.update_taxes(request)

            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                # Get object from response
                response_object = response.get_object()

                if response_object is not None:
                    # Check if expected ActionWrapper instance is received
                    if isinstance(response_object, ActionWrapper):

                        # Get the list of obtained ActionResponse instances
                        action_response_list = response_object.get_org_taxes()

                        for i, action_response in enumerate(action_response_list):
                            print(f"\n--- Tax {i+1} Update Response ---")

                            # Check if the request is successful
                            if hasattr(action_response, 'get_status'):
                                print(f"Status: {action_response.get_status().get_value()}")
                                print(f"Code: {action_response.get_code().get_value()}")

                                print("Details:")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(f"  {key}: {value}")

                                print(f"Message: {action_response.get_message().get_value()}")

                            # Check if the request returned an exception
                            elif isinstance(action_response, APIException):
                                print(f"Status: {action_response.get_status().get_value()}")
                                print(f"Code: {action_response.get_code().get_value()}")

                                print("Details:")
                                details = action_response.get_details()
                                if details is not None:
                                    for key, value in details.items():
                                        print(f"  {key}: {value}")

                                print(f"Message: {action_response.get_message().get_value()}")

                    # Check if the request returned an exception
                    elif isinstance(response_object, APIException):
                        print(f"Status: {response_object.get_status().get_value()}")
                        print(f"Code: {response_object.get_code().get_value()}")

                        print("Details:")
                        details = response_object.get_details()
                        if details is not None:
                            for key, value in details.items():
                                print(f"  {key}: {value}")

                        print(f"Message: {response_object.get_message().get_value()}")

        except Exception as e:
            print(f"Error in update_taxes: {e}")

UpdateTaxes.initialize()
UpdateTaxes.update_taxes()