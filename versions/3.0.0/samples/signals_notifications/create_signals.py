from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.signals_notifications import SignalsNotificationsOperations
from zohocrmsdk.src.com.zoho.crm.api.signals_notifications import ActionWrapper, Signals
from zohocrmsdk.src.com.zoho.crm.api.signals_notifications import APIException
from zohocrmsdk.src.com.zoho.crm.api.signals_notifications import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.signals_notifications import BodyWrapper


class CreateSignals:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_signals():
        signals_notifications_operations = SignalsNotificationsOperations()
        body_wrapper = BodyWrapper()
        signals = list()
        signal = Signals()
        signal.set_signal_namespace("mailchimp.open")
        signal.set_subject("Java SDK Test")
        signal.set_id(34770605001)
        signal.set_module("Leads")
        signal.set_message("This is SDK sample code")
        signals.append(signal)
        body_wrapper.set_signals(signals)

        response = signals_notifications_operations.create_signals(body_wrapper)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response_list = response_object.get_signals()
                    for action_response in action_response_list:
                        if isinstance(action_response, SuccessResponse):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                        elif isinstance(action_response, APIException):
                            print("Status: " +
                                  action_response.get_status().get_value())
                            print("Code: " + action_response.get_code().get_value())
                            print("Details")
                            details = action_response.get_details()
                            for key, value in details.items():
                                print(key + ' : ' + str(value))
                            print("Message: " +
                                  action_response.get_message().get_value())
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


CreateSignals.initialize()
CreateSignals.create_signals()
