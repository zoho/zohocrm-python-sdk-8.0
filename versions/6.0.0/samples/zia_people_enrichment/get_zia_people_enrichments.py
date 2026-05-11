from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.response_wrapper import ResponseWrapper
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.zia_people_enrichment_operations import \
    ZiaPeopleEnrichmentOperations


class GetZiaPeopleEnrichments:
    @staticmethod
    def get_zia_people_enrichments():
        zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()
        param_instance = ParameterMap()
        response = zia_people_enrichment_operations.get_zia_people_enrichments(param_instance)

        if response is not None:
            print("Status Code:", response.get_status_code())

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseWrapper):
                response_wrapper = response_handler
                zia_people_enrichment_list = response_wrapper.get_zia_people_enrichment()

                if zia_people_enrichment_list:
                    for zia_people_enrichment in zia_people_enrichment_list:
                        print("zia_people_enrichment CreatedTime:", zia_people_enrichment.get_created_time())
                        print("zia_people_enrichment Id:", zia_people_enrichment.get_id())
                        user = zia_people_enrichment.get_created_by()

                        if user:
                            print("zia_people_enrichment User Id:", user.get_id())
                            print("zia_people_enrichment User Name:", user.get_name())

                        print("zia_people_enrichment Status:", zia_people_enrichment.get_status())

                info = response_wrapper.get_info()
                if info:
                    if info.get_per_page() is not None:
                        print("zia_people_enrichment Info PerPage:", info.get_per_page())
                    if info.get_count() is not None:
                        print("zia_people_enrichment Info Count:", info.get_count())
                    if info.get_page() is not None:
                        print("zia_people_enrichment Info Page:", info.get_page())
                    if info.get_more_records() is not None:
                        print("zia_people_enrichment Info MoreRecords:", info.get_more_records())

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


GetZiaPeopleEnrichments.initialize()
GetZiaPeopleEnrichments.get_zia_people_enrichments()
