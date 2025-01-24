from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.pick_list_values.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.pick_list_values.pick_list_values_operations import PickListValuesOperations
from zohocrmsdk.src.com.zoho.crm.api.pick_list_values.response_wrapper import ResponseWrapper


class GetPickListValues:
    @staticmethod
    def get_pick_list_values(field_id, module_api_name):
        pick_list_values_operations = PickListValuesOperations(field_id, module_api_name)

        response = pick_list_values_operations.get_pick_list_values()

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseWrapper):
                response_wrapper = response_handler
                pick_list_values = response_wrapper.get_pick_list_values()

                if pick_list_values is not None:
                    for pick_list_value in pick_list_values:
                        print("PickListValues SequenceNumber: " + str(pick_list_value.get_sequence_number()))
                        print("PickListValues DisplayValue: " + str(pick_list_value.get_display_value()))
                        print("PickListValues ReferenceValue: " + str(pick_list_value.get_reference_value()))
                        print("PickListValues ColourCode: " + str(pick_list_value.get_colour_code()))
                        print("PickListValues ActualValue: " + str(pick_list_value.get_actual_value()))
                        print("PickListValues Id: " + str(pick_list_value.get_id()))
                        print("PickListValues Type: " + str(pick_list_value.get_type()))

                        layout_associations = pick_list_value.get_layout_associations()
                        if layout_associations is not None:
                            for layout_association in layout_associations:
                                print("PickListValues LayoutAssociation Id: " + str(layout_association.get_id()))
                                print("PickListValues LayoutAssociation Name: " + str(layout_association.get_name()))
                                print("PickListValues LayoutAssociation APIName: " + str(
                                    layout_association.get_api_name()))

            elif isinstance(response_handler, APIException):
                exception = response_handler
                print("Status: " + str(exception.get_status().get_value()))
                print("Code: " + str(exception.get_code().get_value()))
                print("Details: ")

                if exception.get_details() is not None:
                    for key, value in exception.get_details().items():
                        print(f"{key}: {value}")

                print("Message: " + str(exception.get_message()))

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)


GetPickListValues.initialize()
GetPickListValues.get_pick_list_values(field_id=7272235322, module_api_name="Deals")
