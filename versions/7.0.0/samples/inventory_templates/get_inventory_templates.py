from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.inventory_templates import InventoryTemplatesOperations, GetInventoryTemplatesParam
from zohocrmsdk.src.com.zoho.crm.api.inventory_templates import ResponseWrapper, APIException
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter


class GetInventoryTemplates:
    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_inventory_templates():
        try:
            inventory_templates_operations = InventoryTemplatesOperations()
            param_instance = ParameterMap()
            param_instance.add(GetInventoryTemplatesParam.module, "Sales_Orders")
            response = inventory_templates_operations.get_inventory_templates(param_instance)
            if response is not None:
                print('Status Code: ' + str(response.get_status_code()))
                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return
                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        inventory_templates = response_object.get_inventory_templates()
                        for inventory_template in inventory_templates:
                            print("InventoryTemplate ID: " + str(inventory_template.get_id()))
                            print("InventoryTemplate Name: " + str(inventory_template.get_name()))
                            print("InventoryTemplate EditorMode: " + str(inventory_template.get_editor_mode()))
                            print("InventoryTemplate Category: " + str(inventory_template.get_category()))
                            print("InventoryTemplate Favorite: " + str(inventory_template.get_favorite()))
                            print("InventoryTemplate Active: " + str(inventory_template.get_active()))
                            print("InventoryTemplate Content: " + str(inventory_template.get_content()))
                            print("InventoryTemplate MailContent: " + str(inventory_template.get_mail_content()))
                            if inventory_template.get_created_time() is not None:
                                print("InventoryTemplate CreatedTime: " + str(inventory_template.get_created_time()))
                            if inventory_template.get_modified_time() is not None:
                                print("InventoryTemplate ModifiedTime: " + str(inventory_template.get_modified_time()))
                            if inventory_template.get_last_usage_time() is not None:
                                print("InventoryTemplate LastUsageTime: " + str(inventory_template.get_last_usage_time()))
                            if inventory_template.get_folder() is not None:
                                folder = inventory_template.get_folder()
                                print("InventoryTemplate Folder ID: " + str(folder.get_id()))
                                print("InventoryTemplate Folder Name: " + str(folder.get_name()))
                            if inventory_template.get_module() is not None:
                                module = inventory_template.get_module()
                                print("InventoryTemplate Module ID: " + str(module.get_id()))
                                print("InventoryTemplate Module APIName: " + str(module.get_api_name()))
                            if inventory_template.get_created_by() is not None:
                                created_by = inventory_template.get_created_by()
                                print("InventoryTemplate CreatedBy ID: " + str(created_by.get_id()))
                                print("InventoryTemplate CreatedBy Name: " + str(created_by.get_name()))
                            if inventory_template.get_modified_by() is not None:
                                modified_by = inventory_template.get_modified_by()
                                print("InventoryTemplate ModifiedBy ID: " + str(modified_by.get_id()))
                                print("InventoryTemplate ModifiedBy Name: " + str(modified_by.get_name()))
                        info = response_object.get_info()
                        if info is not None:
                            print("Info PerPage: " + str(info.get_per_page()))
                            print("Info Page: " + str(info.get_page()))
                            print("Info Count: " + str(info.get_count()))
                            print("Info MoreRecords: " + str(info.get_more_records()))
                    elif isinstance(response_object, APIException):
                        print("Status: " + response_object.get_status().get_value())
                        print("Code: " + response_object.get_code().get_value())
                        print("Details")
                        details = response_object.get_details()
                        for key, value in details.items():
                            print(key + ' : ' + str(value))
                        print("Message: " + response_object.get_message())
        except Exception as e:
            print("Exception when calling get_inventory_templates: " + str(e))


GetInventoryTemplates.initialize()
GetInventoryTemplates.get_inventory_templates()
