from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.business_hours import BusinessHoursOperations, BodyWrapper, BusinessHours, \
    BreakHoursCustomTiming, ActionWrapper, SuccessResponse, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.util import Choice


class UpdateBusinessHours(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def update_business_hours():
        business_hours_operations = BusinessHoursOperations()
        request = BodyWrapper()
        business_hours = BusinessHours()
        business_days = [Choice("Monday")]
        business_hours.set_business_days(business_days)
        business_hours.set_week_starts_on(Choice("Monday"))
        business_hours.set_same_as_everyday(False)  # when same_as_everyday is true
        business_hours.set_id(44028001017425)
        bhct = BreakHoursCustomTiming()
        bhct.set_days(Choice("Monday"))
        business_timings = ["09:00", "17:00"]
        bhct.set_business_timing(business_timings)

        bhct1 = BreakHoursCustomTiming()
        bhct1.set_days(Choice("Tuesday"))
        business_timing1 = ["10:30", "17:00"]
        bhct1.set_business_timing(business_timing1)

        bhct2 = BreakHoursCustomTiming()
        bhct2.set_days(Choice("Wednesday"))
        business_timing2 = ["10:30", "17:00"]
        bhct2.set_business_timing(business_timing2)

        custom_timing = [bhct, bhct1, bhct2]
        business_hours.set_custom_timing(custom_timing)
        daily_timing = ["10:00", "11:00"]
        business_hours.set_daily_timing(daily_timing)

        business_hours.set_type(Choice("custom"))
        request.set_business_hours(business_hours)
        response = business_hours_operations.update_business_hours(request)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ActionWrapper):
                    action_response = response_object.get_business_hours()
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


UpdateBusinessHours.initialize()
UpdateBusinessHours.update_business_hours()
