try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Org(object):
	def __init__(self):
		"""Creates an instance of Org"""

		self.__country = None
		self.__photo_id = None
		self.__city = None
		self.__description = None
		self.__mc_status = None
		self.__gapps_enabled = None
		self.__translation_enabled = None
		self.__street = None
		self.__domain_name = None
		self.__alias = None
		self.__currency = None
		self.__id = None
		self.__state = None
		self.__fax = None
		self.__zip = None
		self.__employee_count = None
		self.__website = None
		self.__currency_symbol = None
		self.__mobile = None
		self.__currency_locale = None
		self.__primary_zuid = None
		self.__zia_portal_id = None
		self.__time_zone = None
		self.__zgid = None
		self.__country_code = None
		self.__deletable_org_account = None
		self.__license_details = None
		self.__hierarchy_preferences = None
		self.__phone = None
		self.__company_name = None
		self.__privacy_settings = None
		self.__primary_email = None
		self.__iso_code = None
		self.__hipaa_compliance_enabled = None
		self.__lite_users_enabled = None
		self.__max_per_page = None
		self.__ezgid = None
		self.__call_icon = None
		self.__oauth_presence = None
		self.__zia_zgid = None
		self.__checkin_preferences = None
		self.__type = None
		self.__created_time = None
		self.__key_modified = dict()

	def get_country(self):
		"""
		The method to get the country

		Returns:
			string: A string representing the country
		"""

		return self.__country

	def set_country(self, country):
		"""
		The method to set the value to country

		Parameters:
			country (string) : A string representing the country
		"""

		if country is not None and not isinstance(country, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: country EXPECTED TYPE: str', None, None)
		
		self.__country = country
		self.__key_modified['country'] = 1

	def get_photo_id(self):
		"""
		The method to get the photo_id

		Returns:
			string: A string representing the photo_id
		"""

		return self.__photo_id

	def set_photo_id(self, photo_id):
		"""
		The method to set the value to photo_id

		Parameters:
			photo_id (string) : A string representing the photo_id
		"""

		if photo_id is not None and not isinstance(photo_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: photo_id EXPECTED TYPE: str', None, None)
		
		self.__photo_id = photo_id
		self.__key_modified['photo_id'] = 1

	def get_city(self):
		"""
		The method to get the city

		Returns:
			string: A string representing the city
		"""

		return self.__city

	def set_city(self, city):
		"""
		The method to set the value to city

		Parameters:
			city (string) : A string representing the city
		"""

		if city is not None and not isinstance(city, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: city EXPECTED TYPE: str', None, None)
		
		self.__city = city
		self.__key_modified['city'] = 1

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

	def get_mc_status(self):
		"""
		The method to get the mc_status

		Returns:
			bool: A bool representing the mc_status
		"""

		return self.__mc_status

	def set_mc_status(self, mc_status):
		"""
		The method to set the value to mc_status

		Parameters:
			mc_status (bool) : A bool representing the mc_status
		"""

		if mc_status is not None and not isinstance(mc_status, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mc_status EXPECTED TYPE: bool', None, None)
		
		self.__mc_status = mc_status
		self.__key_modified['mc_status'] = 1

	def get_gapps_enabled(self):
		"""
		The method to get the gapps_enabled

		Returns:
			bool: A bool representing the gapps_enabled
		"""

		return self.__gapps_enabled

	def set_gapps_enabled(self, gapps_enabled):
		"""
		The method to set the value to gapps_enabled

		Parameters:
			gapps_enabled (bool) : A bool representing the gapps_enabled
		"""

		if gapps_enabled is not None and not isinstance(gapps_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: gapps_enabled EXPECTED TYPE: bool', None, None)
		
		self.__gapps_enabled = gapps_enabled
		self.__key_modified['gapps_enabled'] = 1

	def get_translation_enabled(self):
		"""
		The method to get the translation_enabled

		Returns:
			bool: A bool representing the translation_enabled
		"""

		return self.__translation_enabled

	def set_translation_enabled(self, translation_enabled):
		"""
		The method to set the value to translation_enabled

		Parameters:
			translation_enabled (bool) : A bool representing the translation_enabled
		"""

		if translation_enabled is not None and not isinstance(translation_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: translation_enabled EXPECTED TYPE: bool', None, None)
		
		self.__translation_enabled = translation_enabled
		self.__key_modified['translation_enabled'] = 1

	def get_street(self):
		"""
		The method to get the street

		Returns:
			string: A string representing the street
		"""

		return self.__street

	def set_street(self, street):
		"""
		The method to set the value to street

		Parameters:
			street (string) : A string representing the street
		"""

		if street is not None and not isinstance(street, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: street EXPECTED TYPE: str', None, None)
		
		self.__street = street
		self.__key_modified['street'] = 1

	def get_domain_name(self):
		"""
		The method to get the domain_name

		Returns:
			string: A string representing the domain_name
		"""

		return self.__domain_name

	def set_domain_name(self, domain_name):
		"""
		The method to set the value to domain_name

		Parameters:
			domain_name (string) : A string representing the domain_name
		"""

		if domain_name is not None and not isinstance(domain_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: domain_name EXPECTED TYPE: str', None, None)
		
		self.__domain_name = domain_name
		self.__key_modified['domain_name'] = 1

	def get_alias(self):
		"""
		The method to get the alias

		Returns:
			string: A string representing the alias
		"""

		return self.__alias

	def set_alias(self, alias):
		"""
		The method to set the value to alias

		Parameters:
			alias (string) : A string representing the alias
		"""

		if alias is not None and not isinstance(alias, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: alias EXPECTED TYPE: str', None, None)
		
		self.__alias = alias
		self.__key_modified['alias'] = 1

	def get_currency(self):
		"""
		The method to get the currency

		Returns:
			string: A string representing the currency
		"""

		return self.__currency

	def set_currency(self, currency):
		"""
		The method to set the value to currency

		Parameters:
			currency (string) : A string representing the currency
		"""

		if currency is not None and not isinstance(currency, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency EXPECTED TYPE: str', None, None)
		
		self.__currency = currency
		self.__key_modified['currency'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string representing the id
		"""

		if id is not None and not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string representing the state
		"""

		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string representing the state
		"""

		if state is not None and not isinstance(state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: str', None, None)
		
		self.__state = state
		self.__key_modified['state'] = 1

	def get_fax(self):
		"""
		The method to get the fax

		Returns:
			string: A string representing the fax
		"""

		return self.__fax

	def set_fax(self, fax):
		"""
		The method to set the value to fax

		Parameters:
			fax (string) : A string representing the fax
		"""

		if fax is not None and not isinstance(fax, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fax EXPECTED TYPE: str', None, None)
		
		self.__fax = fax
		self.__key_modified['fax'] = 1

	def get_zip(self):
		"""
		The method to get the zip

		Returns:
			string: A string representing the zip
		"""

		return self.__zip

	def set_zip(self, zip):
		"""
		The method to set the value to zip

		Parameters:
			zip (string) : A string representing the zip
		"""

		if zip is not None and not isinstance(zip, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zip EXPECTED TYPE: str', None, None)
		
		self.__zip = zip
		self.__key_modified['zip'] = 1

	def get_employee_count(self):
		"""
		The method to get the employee_count

		Returns:
			string: A string representing the employee_count
		"""

		return self.__employee_count

	def set_employee_count(self, employee_count):
		"""
		The method to set the value to employee_count

		Parameters:
			employee_count (string) : A string representing the employee_count
		"""

		if employee_count is not None and not isinstance(employee_count, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: employee_count EXPECTED TYPE: str', None, None)
		
		self.__employee_count = employee_count
		self.__key_modified['employee_count'] = 1

	def get_website(self):
		"""
		The method to get the website

		Returns:
			string: A string representing the website
		"""

		return self.__website

	def set_website(self, website):
		"""
		The method to set the value to website

		Parameters:
			website (string) : A string representing the website
		"""

		if website is not None and not isinstance(website, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: website EXPECTED TYPE: str', None, None)
		
		self.__website = website
		self.__key_modified['website'] = 1

	def get_currency_symbol(self):
		"""
		The method to get the currency_symbol

		Returns:
			string: A string representing the currency_symbol
		"""

		return self.__currency_symbol

	def set_currency_symbol(self, currency_symbol):
		"""
		The method to set the value to currency_symbol

		Parameters:
			currency_symbol (string) : A string representing the currency_symbol
		"""

		if currency_symbol is not None and not isinstance(currency_symbol, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency_symbol EXPECTED TYPE: str', None, None)
		
		self.__currency_symbol = currency_symbol
		self.__key_modified['currency_symbol'] = 1

	def get_mobile(self):
		"""
		The method to get the mobile

		Returns:
			string: A string representing the mobile
		"""

		return self.__mobile

	def set_mobile(self, mobile):
		"""
		The method to set the value to mobile

		Parameters:
			mobile (string) : A string representing the mobile
		"""

		if mobile is not None and not isinstance(mobile, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mobile EXPECTED TYPE: str', None, None)
		
		self.__mobile = mobile
		self.__key_modified['mobile'] = 1

	def get_currency_locale(self):
		"""
		The method to get the currency_locale

		Returns:
			string: A string representing the currency_locale
		"""

		return self.__currency_locale

	def set_currency_locale(self, currency_locale):
		"""
		The method to set the value to currency_locale

		Parameters:
			currency_locale (string) : A string representing the currency_locale
		"""

		if currency_locale is not None and not isinstance(currency_locale, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency_locale EXPECTED TYPE: str', None, None)
		
		self.__currency_locale = currency_locale
		self.__key_modified['currency_locale'] = 1

	def get_primary_zuid(self):
		"""
		The method to get the primary_zuid

		Returns:
			string: A string representing the primary_zuid
		"""

		return self.__primary_zuid

	def set_primary_zuid(self, primary_zuid):
		"""
		The method to set the value to primary_zuid

		Parameters:
			primary_zuid (string) : A string representing the primary_zuid
		"""

		if primary_zuid is not None and not isinstance(primary_zuid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: primary_zuid EXPECTED TYPE: str', None, None)
		
		self.__primary_zuid = primary_zuid
		self.__key_modified['primary_zuid'] = 1

	def get_zia_portal_id(self):
		"""
		The method to get the zia_portal_id

		Returns:
			string: A string representing the zia_portal_id
		"""

		return self.__zia_portal_id

	def set_zia_portal_id(self, zia_portal_id):
		"""
		The method to set the value to zia_portal_id

		Parameters:
			zia_portal_id (string) : A string representing the zia_portal_id
		"""

		if zia_portal_id is not None and not isinstance(zia_portal_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zia_portal_id EXPECTED TYPE: str', None, None)
		
		self.__zia_portal_id = zia_portal_id
		self.__key_modified['zia_portal_id'] = 1

	def get_time_zone(self):
		"""
		The method to get the time_zone

		Returns:
			string: A string representing the time_zone
		"""

		return self.__time_zone

	def set_time_zone(self, time_zone):
		"""
		The method to set the value to time_zone

		Parameters:
			time_zone (string) : A string representing the time_zone
		"""

		self.__time_zone = time_zone
		self.__key_modified['time_zone'] = 1

	def get_zgid(self):
		"""
		The method to get the zgid

		Returns:
			string: A string representing the zgid
		"""

		return self.__zgid

	def set_zgid(self, zgid):
		"""
		The method to set the value to zgid

		Parameters:
			zgid (string) : A string representing the zgid
		"""

		if zgid is not None and not isinstance(zgid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zgid EXPECTED TYPE: str', None, None)
		
		self.__zgid = zgid
		self.__key_modified['zgid'] = 1

	def get_country_code(self):
		"""
		The method to get the country_code

		Returns:
			string: A string representing the country_code
		"""

		return self.__country_code

	def set_country_code(self, country_code):
		"""
		The method to set the value to country_code

		Parameters:
			country_code (string) : A string representing the country_code
		"""

		if country_code is not None and not isinstance(country_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: country_code EXPECTED TYPE: str', None, None)
		
		self.__country_code = country_code
		self.__key_modified['country_code'] = 1

	def get_deletable_org_account(self):
		"""
		The method to get the deletable_org_account

		Returns:
			bool: A bool representing the deletable_org_account
		"""

		return self.__deletable_org_account

	def set_deletable_org_account(self, deletable_org_account):
		"""
		The method to set the value to deletable_org_account

		Parameters:
			deletable_org_account (bool) : A bool representing the deletable_org_account
		"""

		if deletable_org_account is not None and not isinstance(deletable_org_account, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deletable_org_account EXPECTED TYPE: bool', None, None)
		
		self.__deletable_org_account = deletable_org_account
		self.__key_modified['deletable_org_account'] = 1

	def get_license_details(self):
		"""
		The method to get the license_details

		Returns:
			LicenseDetails: An instance of LicenseDetails
		"""

		return self.__license_details

	def set_license_details(self, license_details):
		"""
		The method to set the value to license_details

		Parameters:
			license_details (LicenseDetails) : An instance of LicenseDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.org.license_details import LicenseDetails
		except Exception:
			from .license_details import LicenseDetails

		if license_details is not None and not isinstance(license_details, LicenseDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: license_details EXPECTED TYPE: LicenseDetails', None, None)
		
		self.__license_details = license_details
		self.__key_modified['license_details'] = 1

	def get_hierarchy_preferences(self):
		"""
		The method to get the hierarchy_preferences

		Returns:
			HierarchyPreferences: An instance of HierarchyPreferences
		"""

		return self.__hierarchy_preferences

	def set_hierarchy_preferences(self, hierarchy_preferences):
		"""
		The method to set the value to hierarchy_preferences

		Parameters:
			hierarchy_preferences (HierarchyPreferences) : An instance of HierarchyPreferences
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.org.hierarchy_preferences import HierarchyPreferences
		except Exception:
			from .hierarchy_preferences import HierarchyPreferences

		if hierarchy_preferences is not None and not isinstance(hierarchy_preferences, HierarchyPreferences):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: hierarchy_preferences EXPECTED TYPE: HierarchyPreferences', None, None)
		
		self.__hierarchy_preferences = hierarchy_preferences
		self.__key_modified['hierarchy_preferences'] = 1

	def get_phone(self):
		"""
		The method to get the phone

		Returns:
			string: A string representing the phone
		"""

		return self.__phone

	def set_phone(self, phone):
		"""
		The method to set the value to phone

		Parameters:
			phone (string) : A string representing the phone
		"""

		if phone is not None and not isinstance(phone, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: phone EXPECTED TYPE: str', None, None)
		
		self.__phone = phone
		self.__key_modified['phone'] = 1

	def get_company_name(self):
		"""
		The method to get the company_name

		Returns:
			string: A string representing the company_name
		"""

		return self.__company_name

	def set_company_name(self, company_name):
		"""
		The method to set the value to company_name

		Parameters:
			company_name (string) : A string representing the company_name
		"""

		if company_name is not None and not isinstance(company_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: company_name EXPECTED TYPE: str', None, None)
		
		self.__company_name = company_name
		self.__key_modified['company_name'] = 1

	def get_privacy_settings(self):
		"""
		The method to get the privacy_settings

		Returns:
			bool: A bool representing the privacy_settings
		"""

		return self.__privacy_settings

	def set_privacy_settings(self, privacy_settings):
		"""
		The method to set the value to privacy_settings

		Parameters:
			privacy_settings (bool) : A bool representing the privacy_settings
		"""

		if privacy_settings is not None and not isinstance(privacy_settings, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: privacy_settings EXPECTED TYPE: bool', None, None)
		
		self.__privacy_settings = privacy_settings
		self.__key_modified['privacy_settings'] = 1

	def get_primary_email(self):
		"""
		The method to get the primary_email

		Returns:
			string: A string representing the primary_email
		"""

		return self.__primary_email

	def set_primary_email(self, primary_email):
		"""
		The method to set the value to primary_email

		Parameters:
			primary_email (string) : A string representing the primary_email
		"""

		if primary_email is not None and not isinstance(primary_email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: primary_email EXPECTED TYPE: str', None, None)
		
		self.__primary_email = primary_email
		self.__key_modified['primary_email'] = 1

	def get_iso_code(self):
		"""
		The method to get the iso_code

		Returns:
			string: A string representing the iso_code
		"""

		return self.__iso_code

	def set_iso_code(self, iso_code):
		"""
		The method to set the value to iso_code

		Parameters:
			iso_code (string) : A string representing the iso_code
		"""

		if iso_code is not None and not isinstance(iso_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: iso_code EXPECTED TYPE: str', None, None)
		
		self.__iso_code = iso_code
		self.__key_modified['iso_code'] = 1

	def get_hipaa_compliance_enabled(self):
		"""
		The method to get the hipaa_compliance_enabled

		Returns:
			bool: A bool representing the hipaa_compliance_enabled
		"""

		return self.__hipaa_compliance_enabled

	def set_hipaa_compliance_enabled(self, hipaa_compliance_enabled):
		"""
		The method to set the value to hipaa_compliance_enabled

		Parameters:
			hipaa_compliance_enabled (bool) : A bool representing the hipaa_compliance_enabled
		"""

		if hipaa_compliance_enabled is not None and not isinstance(hipaa_compliance_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: hipaa_compliance_enabled EXPECTED TYPE: bool', None, None)
		
		self.__hipaa_compliance_enabled = hipaa_compliance_enabled
		self.__key_modified['hipaa_compliance_enabled'] = 1

	def get_lite_users_enabled(self):
		"""
		The method to get the lite_users_enabled

		Returns:
			bool: A bool representing the lite_users_enabled
		"""

		return self.__lite_users_enabled

	def set_lite_users_enabled(self, lite_users_enabled):
		"""
		The method to set the value to lite_users_enabled

		Parameters:
			lite_users_enabled (bool) : A bool representing the lite_users_enabled
		"""

		if lite_users_enabled is not None and not isinstance(lite_users_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lite_users_enabled EXPECTED TYPE: bool', None, None)
		
		self.__lite_users_enabled = lite_users_enabled
		self.__key_modified['lite_users_enabled'] = 1

	def get_max_per_page(self):
		"""
		The method to get the max_per_page

		Returns:
			int: An int representing the max_per_page
		"""

		return self.__max_per_page

	def set_max_per_page(self, max_per_page):
		"""
		The method to set the value to max_per_page

		Parameters:
			max_per_page (int) : An int representing the max_per_page
		"""

		if max_per_page is not None and not isinstance(max_per_page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: max_per_page EXPECTED TYPE: int', None, None)
		
		self.__max_per_page = max_per_page
		self.__key_modified['max_per_page'] = 1

	def get_ezgid(self):
		"""
		The method to get the ezgid

		Returns:
			string: A string representing the ezgid
		"""

		return self.__ezgid

	def set_ezgid(self, ezgid):
		"""
		The method to set the value to ezgid

		Parameters:
			ezgid (string) : A string representing the ezgid
		"""

		if ezgid is not None and not isinstance(ezgid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ezgid EXPECTED TYPE: str', None, None)
		
		self.__ezgid = ezgid
		self.__key_modified['ezgid'] = 1

	def get_call_icon(self):
		"""
		The method to get the call_icon

		Returns:
			string: A string representing the call_icon
		"""

		return self.__call_icon

	def set_call_icon(self, call_icon):
		"""
		The method to set the value to call_icon

		Parameters:
			call_icon (string) : A string representing the call_icon
		"""

		if call_icon is not None and not isinstance(call_icon, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: call_icon EXPECTED TYPE: str', None, None)
		
		self.__call_icon = call_icon
		self.__key_modified['call_icon'] = 1

	def get_oauth_presence(self):
		"""
		The method to get the oauth_presence

		Returns:
			bool: A bool representing the oauth_presence
		"""

		return self.__oauth_presence

	def set_oauth_presence(self, oauth_presence):
		"""
		The method to set the value to oauth_presence

		Parameters:
			oauth_presence (bool) : A bool representing the oauth_presence
		"""

		if oauth_presence is not None and not isinstance(oauth_presence, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: oauth_presence EXPECTED TYPE: bool', None, None)
		
		self.__oauth_presence = oauth_presence
		self.__key_modified['oauth_presence'] = 1

	def get_zia_zgid(self):
		"""
		The method to get the zia_zgid

		Returns:
			int: An int representing the zia_zgid
		"""

		return self.__zia_zgid

	def set_zia_zgid(self, zia_zgid):
		"""
		The method to set the value to zia_zgid

		Parameters:
			zia_zgid (int) : An int representing the zia_zgid
		"""

		if zia_zgid is not None and not isinstance(zia_zgid, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zia_zgid EXPECTED TYPE: int', None, None)
		
		self.__zia_zgid = zia_zgid
		self.__key_modified['zia_zgid'] = 1

	def get_checkin_preferences(self):
		"""
		The method to get the checkin_preferences

		Returns:
			CheckinPreferences: An instance of CheckinPreferences
		"""

		return self.__checkin_preferences

	def set_checkin_preferences(self, checkin_preferences):
		"""
		The method to set the value to checkin_preferences

		Parameters:
			checkin_preferences (CheckinPreferences) : An instance of CheckinPreferences
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.org.checkin_preferences import CheckinPreferences
		except Exception:
			from .checkin_preferences import CheckinPreferences

		if checkin_preferences is not None and not isinstance(checkin_preferences, CheckinPreferences):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: checkin_preferences EXPECTED TYPE: CheckinPreferences', None, None)
		
		self.__checkin_preferences = checkin_preferences
		self.__key_modified['checkin_preferences'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (Choice) : An instance of Choice
		"""

		if type is not None and not isinstance(type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: Choice', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
