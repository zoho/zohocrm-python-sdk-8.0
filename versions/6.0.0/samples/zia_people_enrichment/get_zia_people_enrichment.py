from zohocrmsdk.src.com.zoho.api.authenticator.oauth_token import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api.dc.us_data_center import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.api_exception import APIException
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.response_wrapper import ResponseWrapper
from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.zia_people_enrichment_operations import \
    ZiaPeopleEnrichmentOperations


class GetZiaPeopleEnrichment:
    @staticmethod
    def get_zia_people_enrichment(zia_people_enrichment_id):
        zia_people_enrichment_operations = ZiaPeopleEnrichmentOperations()
        response = zia_people_enrichment_operations.get_zia_people_enrichment(zia_people_enrichment_id)

        if response:
            print("Status Code: " + str(response.get_status_code()))

            if response.get_status_code() == 204:
                print("No Content")
                return

            response_handler = response.get_object()

            if isinstance(response_handler, ResponseWrapper):
                response_wrapper = response_handler
                zia_people_enrichment_list = response_wrapper.get_zia_people_enrichment()

                if zia_people_enrichment_list:
                    for zia_people_enrichment in zia_people_enrichment_list:
                        enriched_data = zia_people_enrichment.get_enriched_data()

                        if enriched_data:
                            print("zia_people_enrichment EnrichedData Website: " + str(enriched_data.get_website()))

                            email_infos = enriched_data.get_email_infos()
                            if email_infos:
                                for email_info in email_infos:
                                    print(
                                        "zia_people_enrichment EnrichedData EmailInfo Type: " + email_info.get_type())
                                    print(
                                        "zia_people_enrichment EnrichedData EmailInfo Email: " + email_info.get_email())

                            print("zia_people_enrichment EnrichedData Gender: " + str(enriched_data.get_gender()))

                            company_info = enriched_data.get_company_info()
                            if company_info:
                                print(
                                    "zia_people_enrichment EnrichedData CompanyInfo Name: " + company_info.get_name())

                                industries = company_info.get_industries()
                                if industries:
                                    for industry in industries:
                                        print(
                                            "zia_people_enrichment EnrichedData CompanyInfo Industries Name: " + industry.get_name())
                                        print(
                                            "zia_people_enrichment EnrichedData CompanyInfo Industries Description: " + industry.get_description())

                                experiences = company_info.get_experiences()
                                if experiences:
                                    for experience in experiences:
                                        print(
                                            "zia_people_enrichment EnrichedData CompanyInfo Experience EndDate: " + experience.get_end_date())
                                        print(
                                            "zia_people_enrichment EnrichedData CompanyInfo Experience CompanyName: " + experience.get_company_name())
                                        print(
                                            "zia_people_enrichment EnrichedData CompanyInfo Experience Title: " + experience.get_title())
                                        print(
                                            "zia_people_enrichment EnrichedData CompanyInfo Experience StartDate: " + experience.get_start_date())
                                        print(
                                            "zia_people_enrichment EnrichedData CompanyInfo Experience Primary: " + experience.get_primary())

                            print("zia_people_enrichment EnrichedData LastName: " + str(enriched_data.get_last_name()))

                            educations = enriched_data.get_educations()
                            if educations:
                                print("zia_people_enrichment EnrichedData Educations: ")
                                print(educations)

                            print(
                                "zia_people_enrichment EnrichedData MiddleName: " + enriched_data.get_middle_name())

                            skills = enriched_data.get_skills()
                            if skills:
                                print("zia_people_enrichment EnrichedData Skills: ")
                                print(skills)

                            other_contacts = enriched_data.get_other_contacts()
                            if other_contacts:
                                for other_contact in other_contacts:
                                    print("zia_people_enrichment EnrichedData OtherContacts: " + other_contact)

                            address_list_info = enriched_data.get_address_list_info()
                            if address_list_info:
                                for address in address_list_info:
                                    print(
                                        "zia_people_enrichment EnrichedData AddressListInfo Continent: " + address.get_continent())
                                    print(
                                        "zia_people_enrichment EnrichedData AddressListInfo Country: " + address.get_country())
                                    print(
                                        "zia_people_enrichment EnrichedData AddressListInfo Name: " + address.get_name())
                                    print(
                                        "zia_people_enrichment EnrichedData AddressListInfo Region: " + address.get_region())
                                    print(
                                        "zia_people_enrichment EnrichedData AddressListInfo Primary: " + address.get_primary())

                            primary_address_info = enriched_data.get_primary_address_info()
                            if primary_address_info:
                                print(
                                    "zia_people_enrichment EnrichedData PrimaryAddressInfo Continent: " + primary_address_info.get_continent())
                                print(
                                    "zia_people_enrichment EnrichedData PrimaryAddressInfo Country: " + primary_address_info.get_country())
                                print(
                                    "zia_people_enrichment EnrichedData PrimaryAddressInfo Name: " + primary_address_info.get_name())
                                print(
                                    "zia_people_enrichment EnrichedData PrimaryAddressInfo Region: " + primary_address_info.get_region())
                                print(
                                    "zia_people_enrichment EnrichedData PrimaryAddressInfo Primary: " + primary_address_info.get_primary())

                            print("zia_people_enrichment EnrichedData Name: " + enriched_data.get_name())
                            print(
                                "zia_people_enrichment EnrichedData SecondaryContact: " + enriched_data.get_secondary_contact())
                            print(
                                "zia_people_enrichment EnrichedData PrimaryEmail: " + enriched_data.get_primary_email())
                            print(
                                "zia_people_enrichment EnrichedData Designation: " + enriched_data.get_designation())
                            print("zia_people_enrichment EnrichedData Id: " + enriched_data.get_id())

                            interests = enriched_data.get_interests()
                            if interests:
                                print("zia_people_enrichment EnrichedData Interests: ")
                                print(interests)

                            print("zia_people_enrichment EnrichedData FirstName: " + enriched_data.get_first_name())
                            print(
                                "zia_people_enrichment EnrichedData PrimaryContact: " + enriched_data.get_primary_contact())

                            social_media = enriched_data.get_social_media()
                            if social_media:
                                for social in social_media:
                                    print(
                                        "zia_people_enrichment EnrichedData SocialMedia MediaType: " + social.get_media_type())
                                    media_urls = social.get_media_url()
                                    if media_urls:
                                        for url in media_urls:
                                            print("zia_people_enrichment EnrichedData SocialMedia MediaUrl: " + url)

                        enrich_based_on = zia_people_enrichment.get_enrich_based_on()
                        if enrich_based_on:
                            social = enrich_based_on.get_social()
                            if social:
                                print(
                                    "zia_people_enrichment EnrichBasedOn Social Facebook: " + social.get_facebook())
                                print(
                                    "zia_people_enrichment EnrichBasedOn Social Linkedin: " + social.get_linkedin())
                                print("zia_people_enrichment EnrichBasedOn Social Twitter: " + social.get_twitter())

                            print("zia_people_enrichment EnrichBasedOn Name: " + enrich_based_on.get_name())

                            company = enrich_based_on.get_company()
                            if company:
                                print(
                                    "zia_people_enrichment EnrichBasedOn Company Website: " + company.get_website())
                                print("zia_people_enrichment EnrichBasedOn Company Name: " + company.get_name())

                            print("zia_people_enrichment EnrichBasedOn Email: " + enrich_based_on.get_email())

                        print("zia_people_enrichment Id: " + str(zia_people_enrichment.get_id()))
                        print("zia_people_enrichment Status: " + zia_people_enrichment.get_status())

            elif isinstance(response_handler, APIException):
                exception = response_handler
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


GetZiaPeopleEnrichment.initialize()
GetZiaPeopleEnrichment.get_zia_people_enrichment(zia_people_enrichment_id=727200561001)
