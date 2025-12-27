from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.currencies import CurrenciesOperations, BodyWrapper, Currency, Format
from zohocrmsdk.src.com.zoho.crm.api.currencies import ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.util import Choice
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class UpdateCurrencies:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_currencies():
        try:
            currencies_operations = CurrenciesOperations()
            request = BodyWrapper()
            currencies_list = []
            currency = Currency()
            currency.set_id(3409643000002293037)
            currency.set_prefix_symbol(True)
            currency.set_exchange_rate("28.000000000")
            currency.set_is_active(True)
            format = Format()
            format.set_decimal_separator(Choice('Period'))
            format.set_thousand_separator(Choice('Comma'))
            format.set_decimal_places(Choice('2'))
            currency.set_format(format)
            currencies_list.append(currency)
            request.set_currencies(currencies_list)
            response = currencies_operations.update_currencies(request)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_currencies()
                        for action_response in action_response_list:
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
            print("Exception when calling update_currencies: " + str(e))


UpdateCurrencies.initialize()
UpdateCurrencies.update_currencies()