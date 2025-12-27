from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.layouts import LayoutsOperations, GetLayoutsParam
from zohocrmsdk.src.com.zoho.crm.api.layouts import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetLayouts:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_layouts():
        try:
            layouts_operations = LayoutsOperations()
            param_instance = ParameterMap()
            param_instance.add(GetLayoutsParam.module, "Leads")
            response = layouts_operations.get_layouts(param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        layouts_list = response_object.get_layouts()
                        for layout in layouts_list:
                            print("Layout ID: " + str(layout.get_id()))
                            print("Layout Name: " + str(layout.get_name()))
                            print("Layout DisplayLabel: " + str(layout.get_display_label()))
                            print("Layout Visible: " + str(layout.get_visible()))
                            print("Layout Status: " + str(layout.get_status()))
                            print("Layout CreatedTime: " + str(layout.get_created_time()))
                            print("Layout ModifiedTime: " + str(layout.get_modified_time()))
                            if layout.get_created_by() is not None:
                                print("Layout CreatedBy Name: " + str(layout.get_created_by().get_name()))
                            if layout.get_modified_by() is not None:
                                print("Layout ModifiedBy Name: " + str(layout.get_modified_by().get_name()))
                            sections = layout.get_sections()
                            if sections is not None:
                                for section in sections:
                                    print("Section Name: " + str(section.get_name()))
                                    print("Section DisplayLabel: " + str(section.get_display_label()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message().get_value())
        except Exception as e:
            print("Exception when calling get_layouts: " + str(e))


GetLayouts.initialize()
GetLayouts.get_layouts()