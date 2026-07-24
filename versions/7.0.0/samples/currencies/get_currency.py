from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.currencies import CurrenciesOperations, ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetCurrency:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_currency(currency_id):
        try:
            currencies_operations = CurrenciesOperations()
            response = currencies_operations.get_currency(currency_id)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        currencies_list = response_object.get_currencies()
                        for currency in currencies_list:
                            print("Currency Id: " + str(currency.get_id()))
                            print("Currency IsoCode: " + str(currency.get_iso_code()))
                            print("Currency Symbol: " + str(currency.get_symbol()))
                            print("Currency CreatedTime: " + str(currency.get_created_time()))
                            print("Currency IsActive: " + str(currency.get_is_active()))
                            print("Currency ExchangeRate: " + str(currency.get_exchange_rate()))
                            format = currency.get_format()
                            if format is not None:
                                print("Currency Format DecimalSeparator: " + str(format.get_decimal_separator()))
                                print("Currency Format ThousandSeparator: " + str(format.get_thousand_separator()))
                                print("Currency Format DecimalPlaces: " + str(format.get_decimal_places()))
                            created_by = currency.get_created_by()
                            if created_by is not None:
                                print("Currency Created By - Name: " + created_by.get_name())
                                print("Currency Created By - ID: " + str(created_by.get_id()))
                                print("Currency Created By - Email: " + str(created_by.get_email()))
                            modified_by = currency.get_modified_by()
                            if modified_by is not None:
                                print("Currency Modified By - Name: " + modified_by.get_name())
                                print("Currency Modified By - ID: " + str(modified_by.get_id()))
                                print("Currency Modified By - Email: " + str(modified_by.get_email()))
                            print("Currency PrefixSymbol: " + str(currency.get_prefix_symbol()))
                            print("Currency IsBase: " + str(currency.get_is_base()))
                            print("Currency ModifiedTime: " + str(currency.get_modified_time()))
                            print("Currency Name: " + currency.get_name())
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling get_currency: " + str(e))


GetCurrency.initialize()
GetCurrency.get_currency(1055806000005657003)