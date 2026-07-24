from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.wizards import (
    WizardsOperations, ResponseWrapper, APIException
)


class GetWizards:
    @staticmethod
    def initialize():
        """Initialize the SDK with authentication credentials"""
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_wizards():
        """
        Get all wizards

        Returns:
            None (prints the response)
        """
        try:
            wizards_operations = WizardsOperations()

            response = wizards_operations.get_wizards()

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
                            print(f"\nTotal Wizards Retrieved: {len(wizards_list)}")
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

                                            # Get nodes
                                            nodes = chart_data.get_nodes()
                                            if nodes is not None:
                                                for node in nodes:
                                                    print(f"    Node Pos X: {node.get_pos_x()}")
                                                    print(f"    Node Pos Y: {node.get_pos_y()}")
                                                    print(f"    Start Node: {node.get_start_node()}")

                                            # Get connections
                                            connections = chart_data.get_connections()
                                            if connections is not None:
                                                for connection in connections:
                                                    print(f"    Connection ID: {connection.get_id()}")

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
            print(f"Error in get_wizards: {e}")


GetWizards.initialize()
GetWizards.get_wizards()
