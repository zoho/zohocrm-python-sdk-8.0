from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.assignment_rules.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.assignment_rules.assignment_rules_operations import AssignmentRulesOperations, GetAssignmentRuleParam
from zohocrmsdk.src.com.zoho.crm.api.assignment_rules.response_handler import ResponseHandler
from zohocrmsdk.src.com.zoho.crm.api.assignment_rules.response_wrapper import ResponseWrapper
from zohocrmsdk.src.com.zoho.crm.api.dc.in_data_center import INDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap


class GetAssignmentRule:

    @staticmethod
    def initialize():
        environment = INDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_assignment_rule(id):
        assignment_rules_operations = AssignmentRulesOperations()
        param_instance = ParameterMap()
        param_instance.add(GetAssignmentRuleParam.module, "Leads")
        response = assignment_rules_operations.get_assignment_rule(id, param_instance)

        if response is not None:
            print("Status Code: " + str(response.get_status_code()))

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseHandler):
                response_wrapper = response_handler

                if isinstance(response_wrapper, ResponseWrapper):
                    assignment_rules = response_wrapper.get_assignment_rules()

                    if assignment_rules is not None:
                        for assignment_rule in assignment_rules:
                            print("AssignmentRule Id: " + str(assignment_rule.get_id()))
                            print("AssignmentRule Name: " + str(assignment_rule.get_name()))
                            print("AssignmentRule ApiName: " + str(assignment_rule.get_api_name()))
                            print("AssignmentRule Description: " + str(assignment_rule.get_description()))
                            print("AssignmentRule CreatedTime: " + str(assignment_rule.get_created_time()))
                            print("AssignmentRule ModifiedTime: " + str(assignment_rule.get_modified_time()))
                            module = assignment_rule.get_module()
                            if module is not None:
                                print("AssignmentRule Module Id: " + str(module.get_id()))
                                print("AssignmentRule Module APIName: " + str(module.get_api_name()))
                            created_by = assignment_rule.get_created_by()
                            if created_by is not None:
                                print("AssignmentRule CreatedBy Id: " + str(created_by.get_id()))
                                print("AssignmentRule CreatedBy Name: " + str(created_by.get_name()))
                            modified_by = assignment_rule.get_modified_by()
                            if modified_by is not None:
                                print("AssignmentRule ModifiedBy Id: " + str(modified_by.get_id()))
                                print("AssignmentRule ModifiedBy Name: " + str(modified_by.get_name()))
                            default_assignee = assignment_rule.get_default_assignee()
                            if default_assignee is not None:
                                print("AssignmentRule DefaultAssignee Id: " + str(default_assignee.get_id()))
                                print("AssignmentRule DefaultAssignee Name: " + str(default_assignee.get_name()))

            elif isinstance(response_handler, APIException):
                exception = response_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")

                for key, value in exception.get_details().items():
                    print(key + ": " + str(value))

                print("Message: " + exception.get_message().get_value())


GetAssignmentRule.initialize()
GetAssignmentRule.get_assignment_rule(1055806000018924001)
