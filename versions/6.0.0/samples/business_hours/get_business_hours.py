from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.business_hours import BusinessHoursOperations, ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter


class GetBusinessHours(object):
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_business_hours():
        business_hours_operations = BusinessHoursOperations()
        response = business_hours_operations.get_business_hours()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if isinstance(response_object, ResponseWrapper):
                response_wrapper = response_object
                business_hours = response_wrapper.get_business_hours()
                business_days = business_hours.get_business_days()
                if business_days is not None:
                    print("business days : ")
                    for business_day in business_days:
                        print(business_day)
                else:
                    print("business days : None")
                custom_timing = business_hours.get_custom_timing()
                if custom_timing is not None:
                    print("custom_timing :")
                    for bhct in custom_timing:
                        print("days: " + bhct.get_days().get_value())
                        business_timings = bhct.get_business_timing()
                        for business_timing in business_timings:
                            print("business_timings : " + business_timing)
                else:
                    print("custom_timing : None")
                daily_timing = business_hours.get_daily_timing()
                if daily_timing is not None:
                    print("daily_timings : ")
                    for daily_timing1 in daily_timing:
                        print(daily_timing1)
                else:
                    print("daily_timings : None")
                print("week_starts_on : " + business_hours.get_week_starts_on().get_value())
                print("same_as_everyday : " + str(business_hours.get_same_as_everyday()))
                print("businesshours_id : " + str(business_hours.get_id()))
                print("businesshours_type : " + business_hours.get_type().get_value())
            elif isinstance(response_object, APIException):
                print("Status: " + response_object.get_status().get_value())
                print("Code: " + response_object.get_code().get_value())
                print("Details")
                details = response_object.get_details()
                for key, value in details.items():
                    print(key + ' : ' + str(value))
                print("Message: " + response_object.get_message().get_value())


GetBusinessHours.initialize()
GetBusinessHours.get_business_hours()
