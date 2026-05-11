from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.mass_delete_details import MassDeleteDetails
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.mass_delete_tags_operations import GetStatusParam
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.mass_delete_tags_operations import MassDeleteTagsOperations
from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.status_response_wrapper import StatusResponseWrapper


class GetStatus:
    @staticmethod
    def get_status():
        mass_delete_tags_operations = MassDeleteTagsOperations()
        param_instance = ParameterMap()
        param_instance.add(GetStatusParam.job_id, "72722573001")
        response = mass_delete_tags_operations.get_status(param_instance)

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            response_handler = response.get_object()

            if isinstance(response_handler, StatusResponseWrapper):
                status_response_wrapper = response_handler
                status_action_response = status_response_wrapper.get_mass_delete()

                for status_action_response1 in status_action_response:
                    if isinstance(status_action_response1, MassDeleteDetails):
                        mass_delete_detail = status_action_response1
                        print("Status JobId: " + str(mass_delete_detail.get_job_id()))
                        print("Status TotalCount: " + str(mass_delete_detail.get_total_count()))
                        print("Status FailedCount: " + str(mass_delete_detail.get_failed_count()))
                        print("Status DeletedCount: " + str(mass_delete_detail.get_deleted_count()))
                        print("Job Status: " + mass_delete_detail.get_status().get_value())

                    elif isinstance(status_action_response1, APIException):
                        exception = status_action_response1
                        print("Status: " + exception.get_status().get_value())
                        print("Code: " + exception.get_code().get_value())
                        print("Details: ")
                        if exception.get_details() is not None:
                            for key, value in exception.get_details().items():
                                print(f"{key}: {value}")
                        print("Message: " + exception.get_message())

            elif isinstance(response_handler, APIException):
                exception = response_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")
                if exception.get_details() is not None:
                    for key, value in exception.get_details().items():
                        print(f"{key}: {value}")
                print("Message: " + exception.get_message())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)

        except Exception as e:
            print(e)


GetStatus.initialize()
GetStatus.get_status()
