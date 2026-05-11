from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.modules import ModulesOperations, ResponseWrapper, APIException


class GetModule:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_module_by_api_name(module_api_name):
        """
        This method is used to get metadata about single module with its API Name and print the response.
        :param module_api_name: The API Name of the module to obtain metadata
        """
        """
        example
        module_api_name = "Leads";
        """
        modules_operations = ModulesOperations()
        # Call get_module method that takes module_api_name as parameter
        response = modules_operations.get_module_by_api_name(module_api_name)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    modules_list = response_object.get_modules()
                    for module in modules_list:
                        print("Module ID: " + str(module.get_id()))
                        print("Module API Name: " + str(module.get_api_name()))
                        print("Module Name: " + str(module.get_module_name()))
                        print("Module Is Convertable: " + str(bool(module.get_convertable())))
                        print("Module Is editable: " + str(bool(module.get_editable())))
                        print("Module Is deletable: " + str(bool(module.get_deletable())))
                        print("Module Web Link: " + str(module.get_web_link()))
                        print("Module Singular Label: " + str(module.get_singular_label()))
                        if module.get_modified_time() is not None:
                            print("Module Modified Time: " + str(module.get_modified_time()))
                        print("Module Is viewable: " + str(bool(module.get_viewable())))
                        print("Module Is API supported: " + str(bool(module.get_api_supported())))
                        print("Module Is creatable: " + str(module.get_creatable()))
                        print("Module Plural Label: " + str(bool(module.get_plural_label())))
                        print("Module Generated Type: " + str(bool(module.get_generated_type())))
                        print("Module Is blueprint supported: " + str(bool(module.get_isblueprintsupported())))
                        print("Module is Visible: " + str(bool(module.get_visible())))
                        om_demand_properties = module.get_on_demand_properties()
                        if om_demand_properties is not None:
                            for om_demand_property in om_demand_properties:
                                print("\n Module onDemandProperties Fields: ")
                                print(om_demand_property)
                        arguments = module.get_arguments()
                        if arguments is not None:
                            for argument in arguments:
                                print('Module Argument Name: ' + argument.get_name())
                                print("Module Argument Value: " + argument.get_value())
                        modified_by_user = module.get_modified_by()
                        if modified_by_user is not None:
                            print("Module Modified By User-ID: " + str(modified_by_user.get_id()))
                            print("Module Modified By User-Name: " + str(modified_by_user.get_name()))
                        print("Module Is Global Search Supported: " + str(bool(module.get_global_search_supported())))
                        print("Module Presence Sub Menu: " + str(bool(module.get_presence_sub_menu())))
                        print("Module Is Triggers Supported: " + str(bool(module.get_triggers_supported())))
                        print("Module Is Feeds Required: " + str(bool(module.get_feeds_required())))
                        print("Module Is Scoring Supported: " + str(bool(module.get_scoring_supported())))
                        print("Module Is Web form Supported: " + str(bool(module.get_webform_supported())))
                        print("Module Is Kanban view: " + str(bool(module.get_kanban_view())))
                        if module.get_kanban_view_supported() is not None:
                            print("Module Is Kanban view Supported: " + str(bool(module.get_kanban_view_supported())))
                        print("Module Show as tab: " + str(bool(module.get_show_as_tab())))
                        print("Module Filter Status: " + str(bool(module.get_filter_status())))
                        print("Module Quick Create: " + str(bool(module.get_quick_create())))
                        print("Module Is email template Supported: " + str(bool(module.get_emailtemplate_support())))
                        print("Module Is inventory template Supported: " + str(
                            bool(module.get_inventory_template_supported())))
                        print("Module Description: " + str(module.get_description()))
                        print("Module Display Field: " + str(module.get_display_field()))
                        print("Module Visibility: " + str(module.get_visibility()))
                        print("Module Business card field limit: " + str(module.get_business_card_field_limit()))
                        print("Module Per page: " + str(module.get_per_page()))
                        print("Module Sequence Number: " + str(module.get_sequence_number()))
                        custom_view = module.get_custom_view()
                        if custom_view is not None:
                            GetModule.print_custom_view(custom_view)
                        profiles = module.get_profiles()
                        if profiles is not None and len(profiles) > 0:
                            for profile in profiles:
                                print('Name: ' + str(profile.get_name()))
                                print('ID: ' + str(profile.get_id()))
                        search_layout_fields = module.get_search_layout_fields()
                        if search_layout_fields is not None:
                            print("Module SearchLayoutFields Fields: ")
                            for field in search_layout_fields:
                                print(field, end=",")
                            print('\n')
                        related_list_properties = module.get_related_list_properties()
                        if related_list_properties is not None:
                            print('Module RelatedListProperties Sort By:' + str(related_list_properties.get_sort_by()))
                            print('Module RelatedListProperties Sort Order:' + str(
                                related_list_properties.get_sort_order()))
                            fields = related_list_properties.get_fields()
                            if fields is not None:
                                print('Module RelatedListProperties Fields')
                                for field in fields:
                                    print(field, end=",")
                                print('\n')
                        properties = module.get_properties()
                        if properties is not None:
                            print("Module Properties Fields: ")
                            for property1 in properties:
                                print(property1, end=',')
                            print('\n')
                        parent_module = module.get_parent_module()
                        if parent_module is not None and parent_module.get_api_name() is not None:
                            print('Module Parent Module Id: ' + str(parent_module.get_id()))
                            print('Module Parent Module Name: ' + str(parent_module.get_api_name()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message())

    @staticmethod
    def print_custom_view(custom_view):
        print('CustomView ID: ' + str(custom_view.get_id()))
        print('CustomView Name: ' + str(custom_view.get_name()))
        print('CustomView System Name: ' + str(custom_view.get_system_name()))
        print('CustomView Display Value: ' + str(custom_view.get_display_value()))
        print('CustomView Is default: ' + str(custom_view.get_default()))
        print('CustomView SortBy: ' + str(custom_view.get_sort_by()))
        if custom_view.get_sort_order() is not None:
            print('CustomView SortOrder: ' + str(custom_view.get_sort_order()))
        print('CustomView Is System Defined: ' + str(custom_view.get_system_defined()))
        if custom_view.get_favorite() is not None:
            print('CustomView Favorite: ' + str(custom_view.get_favorite()))
        criteria = custom_view.get_criteria()
        if criteria is not None:
            GetModule.print_criteria(criteria)
        fields = custom_view.get_fields()
        if fields is not None:
            print('Fields')
            for field in fields:
                print(field.get_api_name())

    @staticmethod
    def print_criteria(criteria):
        if criteria.get_comparator() is not None:
            print('CustomView Criteria Comparator: ' + criteria.get_comparator())
        if criteria.get_field() is not None:
            print('CustomView Criteria Field api name: ' + criteria.get_field().get_api_name())
        if criteria.get_value() is not None:
            print('CustomView Criteria Value: ' + str(criteria.get_value()))
        criteria_group = criteria.get_group()
        if criteria_group is not None:
            for each_criteria in criteria_group:
                GetModule.print_criteria(each_criteria)
        if criteria.get_group_operator() is not None:
            print('CustomView Criteria Group Operator: ' + criteria.get_group_operator().get_value())


GetModule.initialize()
GetModule.get_module_by_api_name(module_api_name="Leads")
