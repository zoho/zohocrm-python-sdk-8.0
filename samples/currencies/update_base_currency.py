from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.currencies import CurrenciesOperations, BaseCurrencyWrapper, BaseCurrency, Format
from zohocrmsdk.src.com.zoho.crm.api.currencies import BaseCurrencyActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import Choice
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class UpdateBaseCurrency:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_base_currency():
        try:
            currencies_operations = CurrenciesOperations()
            request = BaseCurrencyWrapper()
            currency = BaseCurrency()
            currency.set_id(3409643000002293001)
            currency.set_prefix_symbol(True)
            currency.set_symbol("Af")
            currency.set_exchange_rate("1.000000000")
            currency.set_is_active(True)
            format = Format()
            format.set_decimal_separator(Choice('Period'))
            format.set_thousand_separator(Choice('Comma'))
            format.set_decimal_places(Choice('3'))
            currency.set_format(format)
            request.set_base_currency(currency)
            response = currencies_operations.update_base_currency(request)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, BaseCurrencyActionWrapper):
                        action_response = response_object.get_base_currency()
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " + action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " + action_response.get_message().get_value())
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling update_base_currency: " + str(e))


UpdateBaseCurrency.initialize()
UpdateBaseCurrency.update_base_currency()