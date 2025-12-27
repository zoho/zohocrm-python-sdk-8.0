from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.custom_views import CustomViewsOperations, GetCustomViewsParam
from zohocrmsdk.src.com.zoho.crm.api.custom_views import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetCustomViews:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_custom_views():
        try:
            custom_views_operations = CustomViewsOperations()
            param_instance = ParameterMap()
            param_instance.add(GetCustomViewsParam.module, "Leads")
            param_instance.add(GetCustomViewsParam.page, 1)
            param_instance.add(GetCustomViewsParam.per_page, 20)
            response = custom_views_operations.get_custom_views(param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        custom_views_list = response_object.get_custom_views()
                        for custom_view in custom_views_list:
                            print("CustomView ID: " + str(custom_view.get_id()))
                            print("CustomView Name: " + str(custom_view.get_name()))
                            print("CustomView DisplayValue: " + str(custom_view.get_display_value()))
                            print("CustomView SystemName: " + str(custom_view.get_system_name()))
                            print("CustomView Category: " + str(custom_view.get_category()))
                            print("CustomView SortBy: " + str(custom_view.get_sort_by()))
                            print("CustomView SortOrder: " + str(custom_view.get_sort_order()))
                            print("CustomView Favorite: " + str(custom_view.get_favorite()))
                            print("CustomView Offline: " + str(custom_view.get_offline()))
                            print("CustomView Default: " + str(custom_view.get_default()))
                            print("CustomView SystemDefined: " + str(custom_view.get_system_defined()))
                            criteria = custom_view.get_criteria()
                            if criteria is not None:
                                print("CustomView Criteria: " + str(criteria))
                            fields = custom_view.get_fields()
                            if fields is not None:
                                for field in fields:
                                    print("Field ID: " + str(field.get_id()))
                                    print("Field APIName: " + str(field.get_api_name()))
                        info = response_object.get_info()
                        if info is not None:
                            if info.get_count() is not None:
                                print('CustomView Info Count: ' + str(info.get_count()))
                            if info.get_page() is not None:
                                print('CustomView Info Page: ' + str(info.get_page()))
                            if info.get_per_page() is not None:
                                print('CustomView Info PerPage: ' + str(info.get_per_page()))
                            if info.get_more_records() is not None:
                                print('CustomView Info MoreRecords: ' + str(info.get_more_records()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling get_custom_views: " + str(e))


GetCustomViews.initialize()
GetCustomViews.get_custom_views()