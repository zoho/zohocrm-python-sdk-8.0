from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.response_wrapper import ResponseWrapper
from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.zia_org_enrichment_operations import ZiaOrgEnrichmentOperations


class GetZiaOrgEnrichment:
    @staticmethod
    def get_zia_org_enrichment(zia_org_enrichment_id):
        zia_org_enrichment_operations = ZiaOrgEnrichmentOperations()
        response = zia_org_enrichment_operations.get_zia_org_enrichment(zia_org_enrichment_id)

        if response is not None:
            print(f"Status Code: {response.get_status_code()}")

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseWrapper):
                response_wrapper = response_handler
                zia_org_enrichment_list = response_wrapper.get_zia_org_enrichment()

                if zia_org_enrichment_list:
                    for zia_org_enrichment in zia_org_enrichment_list:
                        enriched_data = zia_org_enrichment.get_enriched_data()

                        if enriched_data:
                            print(f"zia_org_enrichment EnrichedData OrgStatus : {enriched_data.get_org_status()}")

                            descriptions = enriched_data.get_description()
                            if descriptions:
                                for desc in descriptions:
                                    print(f"zia_org_enrichment EnrichedData Title : {desc.get_title()}")
                                    print(f"zia_org_enrichment EnrichedData Description : {desc.get_description()}")

                            print(f"zia_org_enrichment EnrichedData CEO : {enriched_data.get_ceo()}")
                            print(f"zia_org_enrichment EnrichedData SecondaryEmail : "
                                  f"{enriched_data.get_secondary_email()}")
                            print(f"zia_org_enrichment EnrichedData Revenue : {enriched_data.get_revenue()}")
                            print(f"zia_org_enrichment EnrichedData YearsInIndustry : "
                                  f"{enriched_data.get_years_in_industry()}")

                            other_contacts = enriched_data.get_other_contacts()
                            if other_contacts:
                                for contact in other_contacts:
                                    print(f"zia_org_enrichment EnrichedData OtherContacts : {contact}")

                            print(f"zia_org_enrichment EnrichedData TechnoGraphicData : "
                                  f"{enriched_data.get_techno_graphic_data()}")
                            print(f"zia_org_enrichment EnrichedData Logo : {enriched_data.get_logo()}")
                            print(f"zia_org_enrichment EnrichedData SecondaryContact : "
                                  f"{enriched_data.get_secondary_contact()}")
                            print(f"zia_org_enrichment EnrichedData Id: {enriched_data.get_id()}")

                            other_emails = enriched_data.get_other_emails()
                            if other_emails:
                                for email in other_emails:
                                    print(f"zia_org_enrichment EnrichedData OtherEmails : {email}")

                            print(f"zia_org_enrichment EnrichedData SignIn : {enriched_data.get_sign_in()}")
                            print(f"zia_org_enrichment EnrichedData Website : {enriched_data.get_website()}")

                            addresses = enriched_data.get_address()
                            if addresses:
                                for address in addresses:
                                    print(f"zia_org_enrichment EnrichedData Address Country : {address.get_country()}")
                                    print(f"zia_org_enrichment EnrichedData Address City : {address.get_city()}")
                                    print(f"zia_org_enrichment EnrichedData Address PinCode : {address.get_pin_code()}")
                                    print(f"zia_org_enrichment EnrichedData Address State : {address.get_state()}")
                                    print(f"zia_org_enrichment EnrichedData Address FillAddress : "
                                          f"{address.get_fill_address()}")

                            print(f"zia_org_enrichment EnrichedData SignUp : {enriched_data.get_sign_up()}")
                            print(f"zia_org_enrichment EnrichedData OrgType : {enriched_data.get_org_type()}")

                            head_quarters = enriched_data.get_head_quarters()
                            if head_quarters:
                                for head_quarter in head_quarters:
                                    print(f"zia_org_enrichment EnrichedData HeadQuarters Country : "
                                          f"{head_quarter.get_country()}")
                                    print(f"zia_org_enrichment EnrichedData HeadQuarters City : "
                                          f"{head_quarter.get_city()}")
                                    print(f"zia_org_enrichment EnrichedData HeadQuarters PinCode : "
                                          f"{head_quarter.get_pin_code()}")
                                    print(f"zia_org_enrichment EnrichedData HeadQuarters State : "
                                          f"{head_quarter.get_state()}")
                                    print(f"zia_org_enrichment EnrichedData HeadQuarters FillAddress : "
                                          f"{head_quarter.get_fill_address()}")

                            print(f"zia_org_enrichment EnrichedData NoOfEmployees : "
                                  f"{enriched_data.get_no_of_employees()}")

                            territory_list = enriched_data.get_territory_list()
                            if territory_list:
                                for territory in territory_list:
                                    print(f"zia_org_enrichment EnrichedData TerritoryList : {territory}")

                            print(f"zia_org_enrichment EnrichedData FoundingYear : {enriched_data.get_founding_year()}")

                            industries = enriched_data.get_industries()
                            if industries:
                                for industry in industries:
                                    print(f"zia_org_enrichment EnrichedData Industries Name : {industry.get_name()}")
                                    print(f"zia_org_enrichment EnrichedData Industries Description : "
                                          f"{industry.get_description()}")

                            print(f"zia_org_enrichment EnrichedData Name : {enriched_data.get_name()}")
                            print(f"zia_org_enrichment EnrichedData PrimaryEmail : {enriched_data.get_primary_email()}")

                            business_model = enriched_data.get_business_model()
                            if business_model:
                                for model in business_model:
                                    print(f"zia_org_enrichment EnrichedData BusinessModel : {model}")

                            print(f"zia_org_enrichment EnrichedData PrimaryContact : "
                                  f"{enriched_data.get_primary_contact()}")

                            social_media = enriched_data.get_social_media()
                            if social_media:
                                for media in social_media:
                                    print(f"zia_org_enrichment EnrichedData SocialMedia MediaType : "
                                          f"{media.get_media_type()}")
                                    media_urls = media.get_media_url()
                                    if media_urls:
                                        for url in media_urls:
                                            print(f"zia_org_enrichment EnrichedData SocialMedia MediaUrl: {url}")

                        enrich_based_on = zia_org_enrichment.get_enrich_based_on()
                        if enrich_based_on:
                            print(f"zia_org_enrichment EnrichBasedOn Name : {enrich_based_on.get_name()}")
                            print(f"zia_org_enrichment EnrichBasedOn Email : {enrich_based_on.get_email()}")
                            print(f"zia_org_enrichment EnrichBasedOn Website : {enrich_based_on.get_website()}")

                        print(f"zia_org_enrichment Id : {zia_org_enrichment.get_id()}")
                        print(f"zia_org_enrichment Status : {zia_org_enrichment.get_status()}")

            elif isinstance(response_handler, APIException):
                exception = response_handler
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


GetZiaOrgEnrichment.initialize()
GetZiaOrgEnrichment.get_zia_org_enrichment(zia_org_enrichment_id=72722561001)
