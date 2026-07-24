from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.wizards import (
    WizardsOperations, ResponseWrapper, APIException, GetWizardByIDParam
)
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap


class GetWizardByID:
    @staticmethod
    def initialize():
        """Initialize the SDK with authentication credentials"""
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_wizard_by_id(wizard_id):
        """
        Get specific wizard by ID

        Args:
            wizard_id (str): The ID of the wizard to retrieve

        Returns:
            None (prints the response)
        """
        try:
            wizards_operations = WizardsOperations()
            param_instance = ParameterMap()

            # Optional parameters
            param_instance.add(GetWizardByIDParam.layout_id, "1055806000000091055")

            response = wizards_operations.get_wizard_by_id(wizard_id, param_instance)

            if response is not None:
                print(f"Status Code: {response.get_status_code()}")

                if response.get_status_code() in [204, 304]:
                    print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                    return

                response_object = response.get_object()
                if response_object is not None:
                    if isinstance(response_object, ResponseWrapper):
                        wizards_list = response_object.get_wizards()
                        if wizards_list is not None:
                            for wizard in wizards_list:
                                print(f"\n--- Wizard Details ---")
                                print(f"Wizard ID: {wizard.get_id()}")
                                print(f"Wizard Name: {wizard.get_name()}")
                                print(f"Active: {wizard.get_active()}")
                                print(f"Draft: {wizard.get_draft()}")
                                print(f"Created Time: {wizard.get_created_time()}")
                                print(f"Modified Time: {wizard.get_modified_time()}")

                                # Get module details
                                module = wizard.get_module()
                                if module is not None:
                                    print(f"Module ID: {module.get_id()}")
                                    print(f"Module API Name: {module.get_api_name()}")

                                # Get created by details
                                created_by = wizard.get_created_by()
                                if created_by is not None:
                                    print(f"Created By ID: {created_by.get_id()}")
                                    print(f"Created By Name: {created_by.get_name()}")

                                # Get modified by details
                                modified_by = wizard.get_modified_by()
                                if modified_by is not None:
                                    print(f"Modified By ID: {modified_by.get_id()}")
                                    print(f"Modified By Name: {modified_by.get_name()}")

                                # Get profiles
                                profiles = wizard.get_profiles()
                                if profiles is not None:
                                    for profile in profiles:
                                        print(f"Profile ID: {profile.get_id()}")
                                        print(f"Profile Name: {profile.get_name()}")

                                # Get containers
                                containers = wizard.get_containers()
                                if containers is not None:
                                    for container in containers:
                                        print(f"\n  --- Container ---")
                                        print(f"  Container ID: {container.get_id()}")

                                        # Get layout
                                        layout = container.get_layout()
                                        if layout is not None:
                                            print(f"  Layout ID: {layout.get_id()}")
                                            print(f"  Layout Name: {layout.get_name()}")

                                        # Get screens
                                        screens = container.get_screens()
                                        if screens is not None:
                                            for screen in screens:
                                                print(f"\n    --- Screen ---")
                                                print(f"    Screen ID: {screen.get_id()}")
                                                print(f"    Display Label: {screen.get_display_label()}")
                                                print(f"    API Name: {screen.get_api_name()}")
                                                print(f"    Reference ID: {screen.get_reference_id()}")

                                                # Get conditional rules
                                                conditional_rules = screen.get_conditional_rules()
                                                if conditional_rules is not None:
                                                    for rule in conditional_rules:
                                                        print(f"\n      --- Conditional Rule ---")
                                                        print(f"      Query ID: {rule.get_query_id()}")
                                                        print(f"      Execute On: {rule.get_execute_on()}")

                                                        criteria = rule.get_criteria()
                                                        if criteria is not None:
                                                            print(f"      Comparator: {criteria.get_comparator()}")
                                                            print(f"      Group Operator: {criteria.get_group_operator()}")
                                                            print(f"      Value: {criteria.get_value()}")

                                                            field = criteria.get_field()
                                                            if field is not None:
                                                                print(f"      Field ID: {field.get_id()}")
                                                                print(f"      Field API Name: {field.get_api_name()}")

                                                        actions = rule.get_actions()
                                                        if actions is not None:
                                                            for action in actions:
                                                                print(f"      Action: {action}")

                                                # Get segments
                                                segments = screen.get_segments()
                                                if segments is not None:
                                                    for segment in segments:
                                                        print(f"\n      --- Segment ---")
                                                        print(f"      Segment ID: {segment.get_id()}")
                                                        print(f"      Display Label: {segment.get_display_label()}")
                                                        print(f"      Sequence Number: {segment.get_sequence_number()}")
                                                        print(f"      Type: {segment.get_type()}")
                                                        print(f"      Column Count: {segment.get_column_count()}")

                                                        # Get fields
                                                        fields = segment.get_fields()
                                                        if fields is not None:
                                                            for field in fields:
                                                                print(f"      Field ID: {field.get_id()}")
                                                                print(f"      Field API Name: {field.get_api_name()}")

                                                        # Get buttons
                                                        buttons = segment.get_buttons()
                                                        if buttons is not None:
                                                            for button in buttons:
                                                                print(f"      Button ID: {button.get_id()}")
                                                                print(f"      Button Display Label: {button.get_display_label()}")
                                                                print(f"      Button Type: {button.get_type()}")
                                                                print(f"      Button Color: {button.get_color()}")
                                                                print(f"      Button Shape: {button.get_shape()}")
                                                                print(f"      Button Background Color: {button.get_background_color()}")
                                                                print(f"      Button Visibility: {button.get_visibility()}")
                                                                print(f"      Button Sequence Number: {button.get_sequence_number()}")
                                                                print(f"      Button Category: {button.get_category()}")
                                                                print(f"      Button Reference ID: {button.get_reference_id()}")

                                                                transition = button.get_transition()
                                                                if transition is not None:
                                                                    print(f"      Transition ID: {transition.get_id()}")
                                                                    print(f"      Transition Name: {transition.get_name()}")

                                                                target_screen = button.get_target_screen()
                                                                if target_screen is not None:
                                                                    print(f"      Target Screen ID: {target_screen.get_id()}")
                                                                    print(f"      Target Screen Display Label: {target_screen.get_display_label()}")

                                                                message = button.get_message()
                                                                if message is not None:
                                                                    print(f"      Message Title: {message.get_title()}")
                                                                    print(f"      Message Content: {message.get_content()}")

                                                        # Get elements
                                                        elements = segment.get_elements()
                                                        if elements is not None:
                                                            for element in elements:
                                                                print(f"      Element Type: {element.get_type()}")

                                                                resource = element.get_resource()
                                                                if resource is not None:
                                                                    print(f"      Resource ID: {resource.get_id()}")
                                                                    print(f"      Resource Name: {resource.get_name()}")

                                        # Get chart data
                                        chart_data = container.get_chart_data()
                                        if chart_data is not None:
                                            print(f"  Canvas Width: {chart_data.get_canvas_width()}")
                                            print(f"  Canvas Height: {chart_data.get_canvas_height()}")

                                            color_palette = chart_data.get_color_palette()
                                            if color_palette is not None:
                                                print(f"  Color Palette: {color_palette.get_button_background()}")

                                            nodes = chart_data.get_nodes()
                                            if nodes is not None:
                                                for node in nodes:
                                                    print(f"    Node Pos X: {node.get_pos_x()}")
                                                    print(f"    Node Pos Y: {node.get_pos_y()}")
                                                    print(f"    Start Node: {node.get_start_node()}")

                                                    node_screen = node.get_screen()
                                                    if node_screen is not None:
                                                        print(f"    Node Screen ID: {node_screen.get_id()}")
                                                        print(f"    Node Screen Display Label: {node_screen.get_display_label()}")

                                            connections = chart_data.get_connections()
                                            if connections is not None:
                                                for connection in connections:
                                                    print(f"    Connection ID: {connection.get_id()}")

                                                    source_button = connection.get_source_button()
                                                    if source_button is not None:
                                                        print(f"    Source Button ID: {source_button.get_id()}")
                                                        print(f"    Source Button Display Label: {source_button.get_display_label()}")

                                                    target_screen = connection.get_target_screen()
                                                    if target_screen is not None:
                                                        print(f"    Target Screen ID: {target_screen.get_id()}")
                                                        print(f"    Target Screen Display Label: {target_screen.get_display_label()}")

                                # Get portal user types
                                portal_user_types = wizard.get_portal_user_types()
                                if portal_user_types is not None:
                                    for portal_user_type in portal_user_types:
                                        print(f"\n  --- Portal User Type ---")
                                        print(f"  Portal User Type ID: {portal_user_type.get_id()}")

                                # Get exempted portal user types
                                exempted_portal_user_types = wizard.get_exempted_portal_user_types()
                                if exempted_portal_user_types is not None:
                                    for exempted_type in exempted_portal_user_types:
                                        print(f"  Exempted Portal User Type ID: {exempted_type.get_id()}")

                                # Get parent wizard
                                parent_wizard = wizard.get_parent_wizard()
                                if parent_wizard is not None:
                                    print(f"Parent Wizard ID: {parent_wizard.get_id()}")
                                    print(f"Parent Wizard Name: {parent_wizard.get_name()}")

                                print("---")

                    elif isinstance(response_object, APIException):
                        print(f"Status: {response_object.get_status().get_value()}")
                        print(f"Code: {response_object.get_code().get_value()}")
                        print("Details:")

                        details = response_object.get_details()
                        if details is not None:
                            for key, value in details.items():
                                print(f"  {key}: {value}")

                        print(f"Message: {response_object.get_message()}")

        except Exception as e:
            print(f"Error in get_wizard_by_id: {e}")


GetWizardByID.initialize()
GetWizardByID.get_wizard_by_id("1055806000009497009")  # Replace with actual wizard ID
