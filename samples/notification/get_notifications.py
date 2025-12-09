from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.notifications import NotificationsOperations, GetNotificationsParam
from zohocrmsdk.src.com.zoho.crm.api.notifications import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetNotifications:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_notifications():
        try:
            notifications_operations = NotificationsOperations()
            param_instance = ParameterMap()
            param_instance.add(GetNotificationsParam.page, 1)
            param_instance.add(GetNotificationsParam.per_page, 20)
            param_instance.add(GetNotificationsParam.module, "Deals")
            param_instance.add(GetNotificationsParam.channel_id, 100000006800211)
            
            response = notifications_operations.get_notifications(param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        notification_list = response_object.get_watch()
                        for notification in notification_list:
                            print("Notification Channel ID: " + str(notification.get_channel_id()))
                            print("Notification Channel Expiry: " + str(notification.get_channel_expiry()))
                            print("Notification Resource URI: " + str(notification.get_resource_uri()))
                            print("Notification Resource ID: " + str(notification.get_resource_id()))
                            print("Notification Resource Name: " + str(notification.get_resource_name()))
                            print("Notification Notify URL: " + str(notification.get_notify_url()))
                            print("Notification Token: " + str(notification.get_token()))
                            if notification.get_notify_on_related_action() is not None:
                                print("Notify On Related Action: " + str(notification.get_notify_on_related_action()))
                            events = notification.get_events()
                            if events is not None:
                                for event in events:
                                    print("Notification Event: " + str(event))
                        info = response_object.get_info()
                        if info is not None:
                            print("Notifications Info Count: " + str(info.get_count()))
                            print("Notifications Info Page: " + str(info.get_page()))
                            print("Notifications Info PerPage: " + str(info.get_per_page()))
                            print("Notifications Info MoreRecords: " + str(info.get_more_records()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling get_notifications: " + str(e))


GetNotifications.initialize()
GetNotifications.get_notifications()