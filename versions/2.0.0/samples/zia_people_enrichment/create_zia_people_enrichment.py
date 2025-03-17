from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment import ZiaPeopleEnrichment
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.action_wrapper import ActionWrapper
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.body_wrapper import BodyWrapper
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.company import Company
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.enrich_based_on import EnrichBasedOn
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.social import Social
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.success_response import SuccessResponse
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.zia_people_enrichment_operations import \
    CreateZiaPeopleEnrichmentParam
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.zia_people_enrichment_operations import \
    ZiaPeopleEnrichmentOperations


class CreateZiaPeopleEnrichment:
    @staticmethod
    def create_zia_people_enrichment():
        zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()

        request = BodyWrapper()
        zia_people_enrichment = []

        zia_people_enrichment1 = ZiaPeopleEnrichment()

        enrich_based_on = EnrichBasedOn()
        enrich_based_on.set_name("zoho")
        enrich_based_on.set_email("sales@zohocorp.com")

        company = Company()
        company.set_name("zoho")
        company.set_website("www.zoho.com")
        enrich_based_on.set_company(company)

        social = Social()
        social.set_facebook("facebook.com/zoho")
        social.set_linkedin("linkedin.com/zoho")
        social.set_twitter("twitter.com/zoho")
        enrich_based_on.set_social(social)

        zia_people_enrichment1.set_enrich_based_on(enrich_based_on)
        zia_people_enrichment.append(zia_people_enrichment1)
        request.set_zia_people_enrichment(zia_people_enrichment)

        param_instance = ParameterMap()
        param_instance.add(CreateZiaPeopleEnrichmentParam.module, "Vendors")

        response = zia_people_enrichment_operations.create_zia_people_enrichment(request, param_instance)

        if response is not None:
            print(f"Status Code: {response.get_status_code()}")

            action_handler = response.get_object()

            if isinstance(action_handler, ActionWrapper):
                action_wrapper = action_handler
                action_responses = action_wrapper.get_zia_people_enrichment()

                for action_response in action_responses:
                    if isinstance(action_response, SuccessResponse):
                        success_response = action_response
                        print(f"Status: {success_response.get_status().get_value()}")
                        print(f"Code: {success_response.get_code().get_value()}")
                        print("Details: ")
                        for key, value in success_response.get_details().items():
                            print(f"{key}: {value}")
                        print(f"Message: {success_response.get_message()}")

                    elif isinstance(action_response, APIException):
                        exception = action_response
                        print(f"Status: {exception.get_status().get_value()}")
                        print(f"Code: {exception.get_code().get_value()}")
                        print("Details: ")
                        for key, value in exception.get_details().items():
                            print(f"{key}: {value}")
                        print(f"Message: {exception.get_message()}")

            elif isinstance(action_handler, APIException):
                exception = action_handler
                print(f"Status: {exception.get_status().get_value()}")
                print(f"Code: {exception.get_code().get_value()}")
                print("Details: ")
                for key, value in exception.get_details().items():
                    print(f"{key}: {value}")
                print(f"Message: {exception.get_message()}")

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


CreateZiaPeopleEnrichment.initialize()
CreateZiaPeopleEnrichment.create_zia_people_enrichment()
