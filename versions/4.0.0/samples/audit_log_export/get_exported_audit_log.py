from zohocrmsdk.src.com.zoho.crm.api.audit_log_export import ResponseWrapper
from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.audit_log_export_operations import AuditLogExportOperations
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer


class GetExportedAuditLog:

    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_exported_auditlog(id1):
        audit_log_export_operations = AuditLogExportOperations()
        response = audit_log_export_operations.get_exported_auditlog(id1)

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseWrapper):
                response_wrapper = response_handler
                audit_log_export = response_wrapper.get_audit_log_export()

                if audit_log_export is not None:
                    for audit_log_export1 in audit_log_export:
                        criteria = audit_log_export1.get_criteria()
                        if criteria is not None:
                            GetExportedAuditLog.print_criteria(criteria)
                        print("AuditLogExport Id : " + str(audit_log_export1.get_id()))
                        print("AuditLogExport Status : " + str(audit_log_export1.get_status()))
                        created_by = audit_log_export1.get_created_by()
                        if created_by is not None:
                            print("AuditLogExport User Id : " + str(created_by.get_id()))
                            print("AuditLogExport User Name : " + str(created_by.get_name()))
                        download_links = audit_log_export1.get_download_links()
                        if download_links != None:
                            for link in download_links:
                                print("AuditLogExport DownloadLink : " + link)
                            print("AuditLogExport JobStartTime : " + str(audit_log_export1.get_job_start_time()))
                            print("AuditLogExport JobEndTime : " + str(audit_log_export1.get_job_end_time()))
                            print("AuditLogExport ExpiryDate : " + str(audit_log_export1.get_expiry_date()))

            elif isinstance(response_handler, APIException):
                exception = response_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")
                for key, value in exception.get_details().items():
                    print(key + ": " + str(value))
                print("Message: " + exception.get_message())

    @staticmethod
    def print_criteria(criteria):
        if criteria.get_comparator() is not None:
            print("ExportedAuditlogs Criteria Comparator: " + criteria.get_comparator())
        if criteria.get_value() is not None:
            print("ExportedAuditlogs Criteria Value: " + str(criteria.get_value()))
        if criteria.get_field() is not None:
            print("ExportedAuditlogs Criteria field name: " + criteria.get_field().get_api_name())
        criteria_group = criteria.get_group()
        if criteria_group is not None:
            for criteria1 in criteria_group:
                GetExportedAuditLog.print_criteria(criteria1)
        if criteria.get_group_operator() is not None:
            print("ExportedAuditlogs Criteria Group Operator: " + criteria.get_group_operator())


GetExportedAuditLog.initialize()
id = 72722554001
GetExportedAuditLog.get_exported_auditlog(id)
