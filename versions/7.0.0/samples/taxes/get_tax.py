from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.taxes import TaxesOperations, ResponseWrapper, APIException

class GetTax:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_tax(tax_id):
        try:
            taxes_operations = TaxesOperations()
            response = taxes_operations.get_tax(tax_id)
            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        org_tax = response_object.get_org_taxes()
                        if org_tax is not None:
                                print("\n--- Organization Tax Details ---")
                                taxes = org_tax.get_taxes()
                                if taxes is not None:
                                    for tax in taxes:
                                        print(f"Tax ID: {tax.get_id()}")
                                        print(f"Tax Name: {tax.get_name()}")
                                        print(f"Display Label: {tax.get_display_label()}")
                                        print(f"Value: {tax.get_value()}")
                                        print(f"Sequence Number: {tax.get_sequence_number()}")
                                        print("---")
                                preference = org_tax.get_preference()
                                if preference is not None:
                                    print(f"Auto Populate Tax: {preference.get_auto_populate_tax()}")
                                    print(f"Modify Tax Rates: {preference.get_modify_tax_rates()}")
                    elif isinstance(response_object, APIException):
                        print(f"Status: {response_object.get_status().get_value()}")
                        print(f"Code: {response_object.get_code().get_value()}")
                        print("Details:")

                        details = response_object.get_details()
                        if details is not None:
                            for key, value in details.items():
                                print(f"{key}: {value}")

                        print(f"Message: {response_object.get_message().get_value()}")

        except Exception as e:
            print(f"Error in get_tax: {e}")

GetTax.initialize()
GetTax.get_tax(1055806000023782001)