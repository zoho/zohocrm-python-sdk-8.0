from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.response_wrapper import ResponseWrapper
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.zia_org_enrichment_operations import ZiaOrgEnrichmentOperations


class GetZiaOrgEnrichments:
    @staticmethod
    def get_zia_org_enrichments():
        zia_org_enrichment_operations = ZiaOrgEnrichmentOperations()
        param_instance = ParameterMap()
        response = zia_org_enrichment_operations.get_zia_org_enrichments(param_instance)

        if response is not None:
            print("Status Code:", response.get_status_code())

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseWrapper):
                response_wrapper = response_handler
                zia_org_enrichment_list = response_wrapper.get_zia_org_enrichment()

                if zia_org_enrichment_list:
                    for zia_org_enrichment in zia_org_enrichment_list:
                        print("ZiaOrgEnrichment CreatedTime:", zia_org_enrichment.get_created_time())
                        print("ZiaOrgEnrichment Id:", zia_org_enrichment.get_id())
                        user = zia_org_enrichment.get_created_by()

                        if user:
                            print("ZiaOrgEnrichment User Id:", user.get_id())
                            print("ZiaOrgEnrichment User Name:", user.get_name())

                        print("ZiaOrgEnrichment Status:", zia_org_enrichment.get_status())

                info = response_wrapper.get_info()
                if info:
                    if info.get_per_page() is not None:
                        print("ZiaOrgEnrichment Info PerPage:", info.get_per_page())
                    if info.get_count() is not None:
                        print("ZiaOrgEnrichment Info Count:", info.get_count())
                    if info.get_page() is not None:
                        print("ZiaOrgEnrichment Info Page:", info.get_page())
                    if info.get_more_records() is not None:
                        print("ZiaOrgEnrichment Info MoreRecords:", info.get_more_records())

            elif isinstance(response_handler, APIException):
                exception = response_handler
                print("Status:", exception.get_status().get_value())
                print("Code:", exception.get_code().get_value())
                print("Details:")
                if exception.get_details() is not None:
                    for key, value in exception.get_details().items():
                        print(f"{key}: {value}")
                print("Message:", exception.get_message())

    @staticmethod
    def initialize():
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
            Initializer.initialize(environment, token)
        except Exception as e:
            print(e)


GetZiaOrgEnrichments.initialize()
GetZiaOrgEnrichments.get_zia_org_enrichments()
