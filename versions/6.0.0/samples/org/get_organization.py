from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.org import OrgOperations, ResponseWrapper, APIException


class GetOrganization:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="client_id", client_secret="client_secret", grant_token="grant_token")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_organization():
        """
        This method is used to get the organization data and print the response.
        """
        org_operations = OrgOperations()
        # Call get_organization method
        response = org_operations.get_organization()
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    org_list = response_object.get_org()
                    for org in org_list:
                        print("Organization Country: " + str(org.get_country()))
                        hierarchy_preferences = org.get_hierarchy_preferences()
                        if hierarchy_preferences is not None:
                            print("Organization HierarchyPreferences Type: " + str(hierarchy_preferences.get_type()))
                        print("Organization HipaaComplianceEnabled: " + str(org.get_hipaa_compliance_enabled()))
                        print("Organization PhotoId: " + str(org.get_photo_id()))
                        print("Organization City: " + str(org.get_city()))
                        print("Organization Description: " + str(org.get_description()))
                        print("Organization McStatus: " + str(org.get_mc_status()))
                        print("Organization GappsEnabled: " + str(org.get_gapps_enabled()))
                        print("Organization DomainName: " + str(org.get_domain_name()))
                        print("Organization TranslationEnabled: " + str(org.get_translation_enabled()))
                        print("Organization Alias: " + str(org.get_alias()))
                        print("Organization Id: " + str(org.get_id()))
                        print("Organization State: " + str(org.get_state()))
                        print("Organization Fax: " + str(org.get_fax()))
                        print("Organization EmployeeCount: " + str(org.get_employee_count()))
                        print("Organization Zip: " + str(org.get_zip()))
                        print("Organization Website: " + str(org.get_website()))
                        print("Organization CurrencySymbol: " + str(org.get_currency_symbol()))
                        print("Organization Mobile: " + str(org.get_mobile()))
                        print("Organization CurrencyLocale: " + str(org.get_currency_locale()))
                        print("Organization PrimaryZuid: " + str(org.get_primary_zuid()))
                        print("Organization ZiaPortalId: " + str(org.get_zia_portal_id()))
                        print("Organization TimeZone: " + str(org.get_time_zone()))
                        print("Organization Zgid: " + str(org.get_zgid()))
                        print("Organization CountryCode: " + str(org.get_country_code()))
                        license_details = org.get_license_details()
                        if license_details is not None:
                            print("Organization LicenseDetails PaidExpiry: " + str(license_details.get_paid_expiry()))
                            print("Organization LicenseDetails UsersLicensePurchased: " + str(
                                license_details.get_users_license_purchased()))
                            print("Organization LicenseDetails TrialType: " + str(license_details.get_trial_type()))
                            print("Organization LicenseDetails TrialExpiry: " + str(license_details.get_trial_expiry()))
                            print("Organization LicenseDetails Paid: " + str(license_details.get_paid()))
                            print("Organization LicenseDetails PaidType: " + str(license_details.get_paid_type()))
                        print("Organization Phone: " + str(org.get_phone()))
                        print("Organization CompanyName: " + str(org.get_company_name()))
                        print("Organization PrivacySettings: " + str(org.get_privacy_settings()))
                        print("Organization PrimaryEmail: " + str(org.get_primary_email()))
                        print("Organization IsoCode: " + str(org.get_iso_code()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())


GetOrganization.initialize()
GetOrganization.get_organization()
