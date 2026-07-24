from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment import ZiaOrgEnrichment
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.action_wrapper import ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.body_wrapper import BodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.enrich_based_on import EnrichBasedOn
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.success_response import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.zia_org_enrichment_operations import CreateZiaOrgEnrichmentParam
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.zia_org_enrichment_operations import ZiaOrgEnrichmentOperations


class CreateZiaOrgEnrichment:
    @staticmethod
    def create_zia_org_enrichment():
        zia_org_enrichment_operations = ZiaOrgEnrichmentOperations()
        request = BodyWrapper()
        zia_org_enrichment_list = []

        zia_org_enrichment = ZiaOrgEnrichment()
        enrich_based_on = EnrichBasedOn()
        enrich_based_on.set_name("zoho")
        enrich_based_on.set_email("sales@zohocorp.com")
        enrich_based_on.set_website("www.zoho.com")
        zia_org_enrichment.set_enrich_based_on(enrich_based_on)

        zia_org_enrichment_list.append(zia_org_enrichment)
        request.set_zia_org_enrichment(zia_org_enrichment_list)

        param_instance = ParameterMap()
        param_instance.add(CreateZiaOrgEnrichmentParam.module, "Leads")
        response = zia_org_enrichment_operations.create_zia_org_enrichment(request, param_instance)

        if response:
            print("Status Code: " + str(response.get_status_code()))

            action_handler = response.get_object()

            if isinstance(action_handler, ActionWrapper):
                action_wrapper = action_handler
                action_responses = action_wrapper.get_zia_org_enrichment()

                for action_response in action_responses:
                    if isinstance(action_response, SuccessResponse):
                        success_response = action_response
                        print("Status: " + success_response.get_status().get_value())
                        print("Code: " + success_response.get_code().get_value())
                        print("Details: ")

                        if success_response.get_details():
                            for key, value in success_response.get_details().items():
                                print(f"{key}: {value}")

                        print("Message: " + success_response.get_message().get_value())

                    elif isinstance(action_response, APIException):
                        exception = action_response
                        print("Status: " + exception.get_status().get_value())
                        print("Code: " + exception.get_code().get_value())
                        print("Details: ")

                        if exception.get_details():
                            for key, value in exception.get_details().items():
                                print(f"{key}: {value}")

                        print("Message: " + exception.get_message().get_value())

            elif isinstance(action_handler, APIException):
                exception = action_handler
                print("Status: " + exception.get_status().get_value())
                print("Code: " + exception.get_code().get_value())
                print("Details: ")

                if exception.get_details():
                    for key, value in exception.get_details().items():
                        print(f"{key}: {value}")

                print("Message: " + exception.get_message().get_value())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


CreateZiaOrgEnrichment.initialize()
CreateZiaOrgEnrichment.create_zia_org_enrichment()
