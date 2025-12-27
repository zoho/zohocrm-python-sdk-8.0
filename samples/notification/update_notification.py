from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.notifications import NotificationsOperations, BodyWrapper, Notification
from zohocrmsdk.src.com.zoho.crm.api.notifications import ActionWrapper, APIException, SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class UpdateNotification:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_notification():
        try:
            notifications_operations = NotificationsOperations()
            body_wrapper = BodyWrapper()
            notifications = []
            
            notification = Notification()
            notification.set_channel_id("100000006800211")
            notification.set_events(['Leads.create'])
            notification.set_notify_url("https://www.single-updated-example.com/webhook")
            notifications.append(notification)
            
            body_wrapper.set_watch(notifications)
            
            response = notifications_operations.update_notification(body_wrapper)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ActionWrapper):
                        action_response_list = response_object.get_watch()
                        for action_response in action_response_list:
                            if isinstance(action_response, SuccessResponse):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                for key, value in details.items():
                                    if isinstance(value, list):
                                        for event in value:
                                            print("Notification ChannelId: " + str(event.get_channel_id()))
                                            print("Notification ChannelExpiry: " + str(event.get_channel_expiry()))
                                            print("Notification ResourceUri: " + str(event.get_resource_uri()))
                                            print("Notification ResourceId: " + str(event.get_resource_id()))
                                            print("Notification ResourceName: " + str(event.get_resource_name()))
                                    else:
                                        print(key + ' : ' + str(value))
                                print("Message: " + action_response.get_message().get_value())
                            elif isinstance(action_response, APIException):
                                print("Status: " + action_response.get_status().get_value())
                                print("Code: " + action_response.get_code().get_value())
                                print("Details")
                                details = action_response.get_details()
                                for key, value in details.items():
                                    print(key + ' : ' + str(value))
                                print("Message: " + action_response.get_message())
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling update_notification: " + str(e))


UpdateNotification.initialize()
UpdateNotification.update_notification()