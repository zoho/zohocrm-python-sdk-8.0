from datetime import datetime

from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export import AuditLogExport
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.action_wrapper import ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.audit_log_export_operations import AuditLogExportOperations
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.body_wrapper import BodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.criteria import Criteria
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.field import Field as AuditField
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.success_response import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer


class CreateAuditlogExport:

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def create_auditlog_export():
        audit_log_export_operations = AuditLogExportOperations()
        request = BodyWrapper()
        audit_log_export = []

        audit_log_export1 = AuditLogExport()
        criteria = Criteria()
        criteria.set_comparator("between")

        field = AuditField()
        field.set_api_name("audited_time")
        criteria.set_field(field)

        values = [
            datetime(2024, 1, 2, 10, 0, 0, 0),
            datetime(2024, 1, 3, 10, 0, 0, 0)
        ]
        criteria.set_value(values)

        audit_log_export1.set_criteria(criteria)
        audit_log_export.append(audit_log_export1)
        request.set_audit_log_export(audit_log_export)

        response = audit_log_export_operations.create_auditlog_export(request)

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            action_handler = response.get_object()

            if isinstance(action_handler, ActionWrapper):
                action_wrapper = action_handler
                action_responses = action_wrapper.get_audit_log_export()

                for action_response in action_responses:
                    if isinstance(action_response, SuccessResponse):
                        success_response = action_response
                        print("Status: " + success_response.get_status().get_value())
                        print("Code: " + success_response.get_code().get_value())
                        print("Details: ")
                        for key, value in success_response.get_details().items():
                            print(f"{key}: {value}")
                        print("Message: " + success_response.get_message())
                    elif isinstance(action_response, APIException):
                        exception = action_response
                        print("Status: " + exception.get_status().get_value())
                        print("Code: " + exception.get_code().get_value())
                        print("Details: ")
                        for key, value in exception.get_details().items():
                            print(f"{key}: {value}")
                        print("Message: " + exception.get_message())
            elif isinstance(action_handler, APIException):
                exception = action_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")
                for key, value in exception.get_details().items():
                    print(f"{key}: {value}")
                print("Message: " + exception.get_message())


CreateAuditlogExport.initialize()
CreateAuditlogExport.create_auditlog_export()
