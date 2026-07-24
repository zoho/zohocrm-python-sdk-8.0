try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
	from zohocrmsdk.src.com.zoho.crm.api.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants
	from ..record import Record


class Users(Record):
	def __init__(self):
		"""Creates an instance of Users"""
		super().__init__()


	def get_country(self):
		"""
		The method to get the country

		Returns:
			string: A string representing the country
		"""

		return self.get_key_value('country')

	def set_country(self, country):
		"""
		The method to set the value to country

		Parameters:
			country (string) : A string representing the country
		"""

		if country is not None and not isinstance(country, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: country EXPECTED TYPE: str', None, None)
		
		self.add_key_value('country', country)

	def get_language(self):
		"""
		The method to get the language

		Returns:
			string: A string representing the language
		"""

		return self.get_key_value('language')

	def set_language(self, language):
		"""
		The method to set the value to language

		Parameters:
			language (string) : A string representing the language
		"""

		if language is not None and not isinstance(language, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: language EXPECTED TYPE: str', None, None)
		
		self.add_key_value('language', language)

	def get_microsoft(self):
		"""
		The method to get the microsoft

		Returns:
			bool: A bool representing the microsoft
		"""

		return self.get_key_value('microsoft')

	def set_microsoft(self, microsoft):
		"""
		The method to set the value to microsoft

		Parameters:
			microsoft (bool) : A bool representing the microsoft
		"""

		if microsoft is not None and not isinstance(microsoft, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: microsoft EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('microsoft', microsoft)

	def get_shift_effective_from(self):
		"""
		The method to get the shift_effective_from

		Returns:
			Object: A Object representing the shift_effective_from
		"""

		return self.get_key_value('$shift_effective_from')

	def set_shift_effective_from(self, shift_effective_from):
		"""
		The method to set the value to shift_effective_from

		Parameters:
			shift_effective_from (Object) : A Object representing the shift_effective_from
		"""

		self.add_key_value('$shift_effective_from', shift_effective_from)

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.get_key_value('id')

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.add_key_value('id', id)

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string representing the state
		"""

		return self.get_key_value('state')

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string representing the state
		"""

		if state is not None and not isinstance(state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: str', None, None)
		
		self.add_key_value('state', state)

	def get_fax(self):
		"""
		The method to get the fax

		Returns:
			string: A string representing the fax
		"""

		return self.get_key_value('fax')

	def set_fax(self, fax):
		"""
		The method to set the value to fax

		Parameters:
			fax (string) : A string representing the fax
		"""

		if fax is not None and not isinstance(fax, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fax EXPECTED TYPE: str', None, None)
		
		self.add_key_value('fax', fax)

	def get_country_locale(self):
		"""
		The method to get the country_locale

		Returns:
			string: A string representing the country_locale
		"""

		return self.get_key_value('country_locale')

	def set_country_locale(self, country_locale):
		"""
		The method to set the value to country_locale

		Parameters:
			country_locale (string) : A string representing the country_locale
		"""

		if country_locale is not None and not isinstance(country_locale, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: country_locale EXPECTED TYPE: str', None, None)
		
		self.add_key_value('country_locale', country_locale)

	def get_zip(self):
		"""
		The method to get the zip

		Returns:
			string: A string representing the zip
		"""

		return self.get_key_value('zip')

	def set_zip(self, zip):
		"""
		The method to set the value to zip

		Parameters:
			zip (string) : A string representing the zip
		"""

		if zip is not None and not isinstance(zip, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zip EXPECTED TYPE: str', None, None)
		
		self.add_key_value('zip', zip)

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.get_key_value('created_time')

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.add_key_value('created_time', created_time)

	def get_time_format(self):
		"""
		The method to get the time_format

		Returns:
			Choice: An instance of Choice
		"""

		return self.get_key_value('time_format')

	def set_time_format(self, time_format):
		"""
		The method to set the value to time_format

		Parameters:
			time_format (Choice) : An instance of Choice
		"""

		if time_format is not None and not isinstance(time_format, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: time_format EXPECTED TYPE: Choice', None, None)
		
		self.add_key_value('time_format', time_format)

	def get_offset(self):
		"""
		The method to get the offset

		Returns:
			int: An int representing the offset
		"""

		return self.get_key_value('offset')

	def set_offset(self, offset):
		"""
		The method to set the value to offset

		Parameters:
			offset (int) : An int representing the offset
		"""

		if offset is not None and not isinstance(offset, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: offset EXPECTED TYPE: int', None, None)
		
		self.add_key_value('offset', offset)

	def get_imap_status(self):
		"""
		The method to get the imap_status

		Returns:
			bool: A bool representing the imap_status
		"""

		return self.get_key_value('imap_status')

	def set_imap_status(self, imap_status):
		"""
		The method to set the value to imap_status

		Parameters:
			imap_status (bool) : A bool representing the imap_status
		"""

		if imap_status is not None and not isinstance(imap_status, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: imap_status EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('imap_status', imap_status)

	def get_image_link(self):
		"""
		The method to get the image_link

		Returns:
			string: A string representing the image_link
		"""

		return self.get_key_value('image_link')

	def set_image_link(self, image_link):
		"""
		The method to set the value to image_link

		Parameters:
			image_link (string) : A string representing the image_link
		"""

		if image_link is not None and not isinstance(image_link, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: image_link EXPECTED TYPE: str', None, None)
		
		self.add_key_value('image_link', image_link)

	def get_ezuid(self):
		"""
		The method to get the ezuid

		Returns:
			string: A string representing the ezuid
		"""

		return self.get_key_value('ezuid')

	def set_ezuid(self, ezuid):
		"""
		The method to set the value to ezuid

		Parameters:
			ezuid (string) : A string representing the ezuid
		"""

		if ezuid is not None and not isinstance(ezuid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ezuid EXPECTED TYPE: str', None, None)
		
		self.add_key_value('ezuid', ezuid)

	def get_profile(self):
		"""
		The method to get the profile

		Returns:
			Profile: An instance of Profile
		"""

		return self.get_key_value('profile')

	def set_profile(self, profile):
		"""
		The method to set the value to profile

		Parameters:
			profile (Profile) : An instance of Profile
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.profile import Profile
		except Exception:
			from .profile import Profile

		if profile is not None and not isinstance(profile, Profile):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: profile EXPECTED TYPE: Profile', None, None)
		
		self.add_key_value('profile', profile)

	def get_role(self):
		"""
		The method to get the role

		Returns:
			Role: An instance of Role
		"""

		return self.get_key_value('role')

	def set_role(self, role):
		"""
		The method to set the value to role

		Parameters:
			role (Role) : An instance of Role
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.role import Role
		except Exception:
			from .role import Role

		if role is not None and not isinstance(role, Role):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: role EXPECTED TYPE: Role', None, None)
		
		self.add_key_value('role', role)

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.get_key_value('created_by')

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.minified_user import MinifiedUser
		except Exception:
			from .minified_user import MinifiedUser

		if created_by is not None and not isinstance(created_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.add_key_value('created_by', created_by)

	def get_full_name(self):
		"""
		The method to get the full_name

		Returns:
			string: A string representing the full_name
		"""

		return self.get_key_value('full_name')

	def set_full_name(self, full_name):
		"""
		The method to set the value to full_name

		Parameters:
			full_name (string) : A string representing the full_name
		"""

		if full_name is not None and not isinstance(full_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: full_name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('full_name', full_name)

	def get_zuid(self):
		"""
		The method to get the zuid

		Returns:
			string: A string representing the zuid
		"""

		return self.get_key_value('zuid')

	def set_zuid(self, zuid):
		"""
		The method to set the value to zuid

		Parameters:
			zuid (string) : A string representing the zuid
		"""

		if zuid is not None and not isinstance(zuid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zuid EXPECTED TYPE: str', None, None)
		
		self.add_key_value('zuid', zuid)

	def get_phone(self):
		"""
		The method to get the phone

		Returns:
			string: A string representing the phone
		"""

		return self.get_key_value('phone')

	def set_phone(self, phone):
		"""
		The method to set the value to phone

		Parameters:
			phone (string) : A string representing the phone
		"""

		if phone is not None and not isinstance(phone, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: phone EXPECTED TYPE: str', None, None)
		
		self.add_key_value('phone', phone)

	def get_dob(self):
		"""
		The method to get the dob

		Returns:
			date: An instance of date
		"""

		return self.get_key_value('dob')

	def set_dob(self, dob):
		"""
		The method to set the value to dob

		Parameters:
			dob (date) : An instance of date
		"""

		from datetime import date as date1

		if dob is not None and not isinstance(dob, date1):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: dob EXPECTED TYPE: date1', None, None)
		
		self.add_key_value('dob', dob)

	def get_status(self):
		"""
		The method to get the status

		Returns:
			string: A string representing the status
		"""

		return self.get_key_value('status')

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (string) : A string representing the status
		"""

		if status is not None and not isinstance(status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: str', None, None)
		
		self.add_key_value('status', status)

	def get_customize_info(self):
		"""
		The method to get the customize_info

		Returns:
			CustomizeInfo: An instance of CustomizeInfo
		"""

		return self.get_key_value('customize_info')

	def set_customize_info(self, customize_info):
		"""
		The method to set the value to customize_info

		Parameters:
			customize_info (CustomizeInfo) : An instance of CustomizeInfo
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.customize_info import CustomizeInfo
		except Exception:
			from .customize_info import CustomizeInfo

		if customize_info is not None and not isinstance(customize_info, CustomizeInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: customize_info EXPECTED TYPE: CustomizeInfo', None, None)
		
		self.add_key_value('customize_info', customize_info)

	def get_city(self):
		"""
		The method to get the city

		Returns:
			string: A string representing the city
		"""

		return self.get_key_value('city')

	def set_city(self, city):
		"""
		The method to set the value to city

		Parameters:
			city (string) : A string representing the city
		"""

		if city is not None and not isinstance(city, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: city EXPECTED TYPE: str', None, None)
		
		self.add_key_value('city', city)

	def get_signature(self):
		"""
		The method to get the signature

		Returns:
			string: A string representing the signature
		"""

		return self.get_key_value('signature')

	def set_signature(self, signature):
		"""
		The method to set the value to signature

		Parameters:
			signature (string) : A string representing the signature
		"""

		if signature is not None and not isinstance(signature, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: signature EXPECTED TYPE: str', None, None)
		
		self.add_key_value('signature', signature)

	def get_sort_order_preference__s(self):
		"""
		The method to get the sort_order_preference__s

		Returns:
			string: A string representing the sort_order_preference__s
		"""

		return self.get_key_value('sort_order_preference__s')

	def set_sort_order_preference__s(self, sort_order_preference__s):
		"""
		The method to set the value to sort_order_preference__s

		Parameters:
			sort_order_preference__s (string) : A string representing the sort_order_preference__s
		"""

		if sort_order_preference__s is not None and not isinstance(sort_order_preference__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_order_preference__s EXPECTED TYPE: str', None, None)
		
		self.add_key_value('sort_order_preference__s', sort_order_preference__s)

	def get_category(self):
		"""
		The method to get the category

		Returns:
			string: A string representing the category
		"""

		return self.get_key_value('category')

	def set_category(self, category):
		"""
		The method to set the value to category

		Parameters:
			category (string) : A string representing the category
		"""

		if category is not None and not isinstance(category, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: str', None, None)
		
		self.add_key_value('category', category)

	def get_date_format(self):
		"""
		The method to get the date_format

		Returns:
			Choice: An instance of Choice
		"""

		return self.get_key_value('date_format')

	def set_date_format(self, date_format):
		"""
		The method to set the value to date_format

		Parameters:
			date_format (Choice) : An instance of Choice
		"""

		if date_format is not None and not isinstance(date_format, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: date_format EXPECTED TYPE: Choice', None, None)
		
		self.add_key_value('date_format', date_format)

	def get_confirm(self):
		"""
		The method to get the confirm

		Returns:
			bool: A bool representing the confirm
		"""

		return self.get_key_value('confirm')

	def set_confirm(self, confirm):
		"""
		The method to set the value to confirm

		Parameters:
			confirm (bool) : A bool representing the confirm
		"""

		if confirm is not None and not isinstance(confirm, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: confirm EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('confirm', confirm)

	def get_decimal_separator(self):
		"""
		The method to get the decimal_separator

		Returns:
			Choice: An instance of Choice
		"""

		return self.get_key_value('decimal_separator')

	def set_decimal_separator(self, decimal_separator):
		"""
		The method to set the value to decimal_separator

		Parameters:
			decimal_separator (Choice) : An instance of Choice
		"""

		if decimal_separator is not None and not isinstance(decimal_separator, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: decimal_separator EXPECTED TYPE: Choice', None, None)
		
		self.add_key_value('decimal_separator', decimal_separator)

	def get_number_separator(self):
		"""
		The method to get the number_separator

		Returns:
			Choice: An instance of Choice
		"""

		return self.get_key_value('number_separator')

	def set_number_separator(self, number_separator):
		"""
		The method to set the value to number_separator

		Parameters:
			number_separator (Choice) : An instance of Choice
		"""

		if number_separator is not None and not isinstance(number_separator, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: number_separator EXPECTED TYPE: Choice', None, None)
		
		self.add_key_value('number_separator', number_separator)

	def get_time_zone(self):
		"""
		The method to get the time_zone

		Returns:
			string: An instance of string
		"""

		return self.get_key_value('time_zone')

	def set_time_zone(self, time_zone):
		"""
		The method to set the value to time_zone

		Parameters:
			time_zone (string) : An instance of string
		"""

		self.add_key_value('time_zone', time_zone)

	def get_last_name(self):
		"""
		The method to get the last_name

		Returns:
			string: A string representing the last_name
		"""

		return self.get_key_value('last_name')

	def set_last_name(self, last_name):
		"""
		The method to set the value to last_name

		Parameters:
			last_name (string) : A string representing the last_name
		"""

		if last_name is not None and not isinstance(last_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('last_name', last_name)

	def get_mobile(self):
		"""
		The method to get the mobile

		Returns:
			string: A string representing the mobile
		"""

		return self.get_key_value('mobile')

	def set_mobile(self, mobile):
		"""
		The method to set the value to mobile

		Parameters:
			mobile (string) : A string representing the mobile
		"""

		if mobile is not None and not isinstance(mobile, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mobile EXPECTED TYPE: str', None, None)
		
		self.add_key_value('mobile', mobile)

	def get_current_shift(self):
		"""
		The method to get the current_shift

		Returns:
			Shift: An instance of Shift
		"""

		return self.get_key_value('$current_shift')

	def set_current_shift(self, current_shift):
		"""
		The method to set the value to current_shift

		Parameters:
			current_shift (Shift) : An instance of Shift
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.shift import Shift
		except Exception:
			from .shift import Shift

		if current_shift is not None and not isinstance(current_shift, Shift):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: current_shift EXPECTED TYPE: Shift', None, None)
		
		self.add_key_value('$current_shift', current_shift)

	def get_reporting_to(self):
		"""
		The method to get the reporting_to

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.get_key_value('Reporting_To')

	def set_reporting_to(self, reporting_to):
		"""
		The method to set the value to reporting_to

		Parameters:
			reporting_to (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.minified_user import MinifiedUser
		except Exception:
			from .minified_user import MinifiedUser

		if reporting_to is not None and not isinstance(reporting_to, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reporting_to EXPECTED TYPE: MinifiedUser', None, None)
		
		self.add_key_value('Reporting_To', reporting_to)

	def get_currency(self):
		"""
		The method to get the currency

		Returns:
			string: A string representing the currency
		"""

		return self.get_key_value('Currency')

	def set_currency(self, currency):
		"""
		The method to set the value to currency

		Parameters:
			currency (string) : A string representing the currency
		"""

		if currency is not None and not isinstance(currency, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Currency', currency)

	def get_next_shift(self):
		"""
		The method to get the next_shift

		Returns:
			Shift: An instance of Shift
		"""

		return self.get_key_value('$next_shift')

	def set_next_shift(self, next_shift):
		"""
		The method to set the value to next_shift

		Parameters:
			next_shift (Shift) : An instance of Shift
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.shift import Shift
		except Exception:
			from .shift import Shift

		if next_shift is not None and not isinstance(next_shift, Shift):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: next_shift EXPECTED TYPE: Shift', None, None)
		
		self.add_key_value('$next_shift', next_shift)

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.get_key_value('Modified_Time')

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.add_key_value('Modified_Time', modified_time)

	def get_website(self):
		"""
		The method to get the website

		Returns:
			string: A string representing the website
		"""

		return self.get_key_value('website')

	def set_website(self, website):
		"""
		The method to set the value to website

		Parameters:
			website (string) : A string representing the website
		"""

		if website is not None and not isinstance(website, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: website EXPECTED TYPE: str', None, None)
		
		self.add_key_value('website', website)

	def get_status_reason__s(self):
		"""
		The method to get the status_reason__s

		Returns:
			string: A string representing the status_reason__s
		"""

		return self.get_key_value('status_reason__s')

	def set_status_reason__s(self, status_reason__s):
		"""
		The method to set the value to status_reason__s

		Parameters:
			status_reason__s (string) : A string representing the status_reason__s
		"""

		if status_reason__s is not None and not isinstance(status_reason__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status_reason__s EXPECTED TYPE: str', None, None)
		
		self.add_key_value('status_reason__s', status_reason__s)

	def get_email(self):
		"""
		The method to get the email

		Returns:
			string: A string representing the email
		"""

		return self.get_key_value('email')

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (string) : A string representing the email
		"""

		if email is not None and not isinstance(email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: str', None, None)
		
		self.add_key_value('email', email)

	def get_first_name(self):
		"""
		The method to get the first_name

		Returns:
			string: A string representing the first_name
		"""

		return self.get_key_value('first_name')

	def set_first_name(self, first_name):
		"""
		The method to set the value to first_name

		Parameters:
			first_name (string) : A string representing the first_name
		"""

		if first_name is not None and not isinstance(first_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: first_name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('first_name', first_name)

	def get_sandboxdeveloper(self):
		"""
		The method to get the sandboxdeveloper

		Returns:
			bool: A bool representing the sandboxdeveloper
		"""

		return self.get_key_value('sandboxDeveloper')

	def set_sandboxdeveloper(self, sandboxdeveloper):
		"""
		The method to set the value to sandboxdeveloper

		Parameters:
			sandboxdeveloper (bool) : A bool representing the sandboxdeveloper
		"""

		if sandboxdeveloper is not None and not isinstance(sandboxdeveloper, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sandboxdeveloper EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('sandboxDeveloper', sandboxdeveloper)

	def get_alias(self):
		"""
		The method to get the alias

		Returns:
			string: A string representing the alias
		"""

		return self.get_key_value('alias')

	def set_alias(self, alias):
		"""
		The method to set the value to alias

		Parameters:
			alias (string) : A string representing the alias
		"""

		if alias is not None and not isinstance(alias, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: alias EXPECTED TYPE: str', None, None)
		
		self.add_key_value('alias', alias)

	def get_street(self):
		"""
		The method to get the street

		Returns:
			string: A string representing the street
		"""

		return self.get_key_value('street')

	def set_street(self, street):
		"""
		The method to set the value to street

		Parameters:
			street (string) : A string representing the street
		"""

		if street is not None and not isinstance(street, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: street EXPECTED TYPE: str', None, None)
		
		self.add_key_value('street', street)

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.get_key_value('Modified_By')

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.minified_user import MinifiedUser
		except Exception:
			from .minified_user import MinifiedUser

		if modified_by is not None and not isinstance(modified_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.add_key_value('Modified_By', modified_by)

	def get_isonline(self):
		"""
		The method to get the isonline

		Returns:
			bool: A bool representing the isonline
		"""

		return self.get_key_value('Isonline')

	def set_isonline(self, isonline):
		"""
		The method to set the value to isonline

		Parameters:
			isonline (bool) : A bool representing the isonline
		"""

		if isonline is not None and not isinstance(isonline, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: isonline EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Isonline', isonline)

	def get_locale(self):
		"""
		The method to get the locale

		Returns:
			string: A string representing the locale
		"""

		return self.get_key_value('locale')

	def set_locale(self, locale):
		"""
		The method to set the value to locale

		Parameters:
			locale (string) : A string representing the locale
		"""

		if locale is not None and not isinstance(locale, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locale EXPECTED TYPE: str', None, None)
		
		self.add_key_value('locale', locale)

	def get_name_format__s(self):
		"""
		The method to get the name_format__s

		Returns:
			Choice: An instance of Choice
		"""

		return self.get_key_value('name_format__s')

	def set_name_format__s(self, name_format__s):
		"""
		The method to set the value to name_format__s

		Parameters:
			name_format__s (Choice) : An instance of Choice
		"""

		if name_format__s is not None and not isinstance(name_format__s, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name_format__s EXPECTED TYPE: Choice', None, None)
		
		self.add_key_value('name_format__s', name_format__s)

	def get_personal_account(self):
		"""
		The method to get the personal_account

		Returns:
			bool: A bool representing the personal_account
		"""

		return self.get_key_value('personal_account')

	def set_personal_account(self, personal_account):
		"""
		The method to set the value to personal_account

		Parameters:
			personal_account (bool) : A bool representing the personal_account
		"""

		if personal_account is not None and not isinstance(personal_account, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: personal_account EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('personal_account', personal_account)

	def get_default_tab_group(self):
		"""
		The method to get the default_tab_group

		Returns:
			string: A string representing the default_tab_group
		"""

		return self.get_key_value('default_tab_group')

	def set_default_tab_group(self, default_tab_group):
		"""
		The method to set the value to default_tab_group

		Parameters:
			default_tab_group (string) : A string representing the default_tab_group
		"""

		if default_tab_group is not None and not isinstance(default_tab_group, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_tab_group EXPECTED TYPE: str', None, None)
		
		self.add_key_value('default_tab_group', default_tab_group)

	def get_theme(self):
		"""
		The method to get the theme

		Returns:
			Theme: An instance of Theme
		"""

		return self.get_key_value('theme')

	def set_theme(self, theme):
		"""
		The method to set the value to theme

		Parameters:
			theme (Theme) : An instance of Theme
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.theme import Theme
		except Exception:
			from .theme import Theme

		if theme is not None and not isinstance(theme, Theme):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: theme EXPECTED TYPE: Theme', None, None)
		
		self.add_key_value('theme', theme)

	def get_ntc_notification_type(self):
		"""
		The method to get the ntc_notification_type

		Returns:
			list: An instance of list
		"""

		return self.get_key_value('ntc_notification_type')

	def set_ntc_notification_type(self, ntc_notification_type):
		"""
		The method to set the value to ntc_notification_type

		Parameters:
			ntc_notification_type (list) : An instance of list
		"""

		if ntc_notification_type is not None and not isinstance(ntc_notification_type, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ntc_notification_type EXPECTED TYPE: list', None, None)
		
		self.add_key_value('ntc_notification_type', ntc_notification_type)

	def get_ntc_enabled(self):
		"""
		The method to get the ntc_enabled

		Returns:
			bool: A bool representing the ntc_enabled
		"""

		return self.get_key_value('ntc_enabled')

	def set_ntc_enabled(self, ntc_enabled):
		"""
		The method to set the value to ntc_enabled

		Parameters:
			ntc_enabled (bool) : A bool representing the ntc_enabled
		"""

		if ntc_enabled is not None and not isinstance(ntc_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ntc_enabled EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('ntc_enabled', ntc_enabled)

	def get_rtl_enabled(self):
		"""
		The method to get the rtl_enabled

		Returns:
			bool: A bool representing the rtl_enabled
		"""

		return self.get_key_value('rtl_enabled')

	def set_rtl_enabled(self, rtl_enabled):
		"""
		The method to set the value to rtl_enabled

		Parameters:
			rtl_enabled (bool) : A bool representing the rtl_enabled
		"""

		if rtl_enabled is not None and not isinstance(rtl_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rtl_enabled EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('rtl_enabled', rtl_enabled)

	def get_telephony_enabled(self):
		"""
		The method to get the telephony_enabled

		Returns:
			bool: A bool representing the telephony_enabled
		"""

		return self.get_key_value('telephony_enabled')

	def set_telephony_enabled(self, telephony_enabled):
		"""
		The method to set the value to telephony_enabled

		Parameters:
			telephony_enabled (bool) : A bool representing the telephony_enabled
		"""

		if telephony_enabled is not None and not isinstance(telephony_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: telephony_enabled EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('telephony_enabled', telephony_enabled)

	def get_sort_order_preference(self):
		"""
		The method to get the sort_order_preference

		Returns:
			string: A string representing the sort_order_preference
		"""

		return self.get_key_value('sort_order_preference')

	def set_sort_order_preference(self, sort_order_preference):
		"""
		The method to set the value to sort_order_preference

		Parameters:
			sort_order_preference (string) : A string representing the sort_order_preference
		"""

		if sort_order_preference is not None and not isinstance(sort_order_preference, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_order_preference EXPECTED TYPE: str', None, None)
		
		self.add_key_value('sort_order_preference', sort_order_preference)

	def get_created_by_17(self):
		"""
		The method to get the created_by_17

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.get_key_value('Created_By')

	def set_created_by_17(self, created_by_17):
		"""
		The method to set the value to created_by_17

		Parameters:
			created_by_17 (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.minified_user import MinifiedUser
		except Exception:
			from .minified_user import MinifiedUser

		if created_by_17 is not None and not isinstance(created_by_17, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by_17 EXPECTED TYPE: MinifiedUser', None, None)
		
		self.add_key_value('Created_By', created_by_17)

	def get_created_time_9(self):
		"""
		The method to get the created_time_9

		Returns:
			datetime: An instance of datetime
		"""

		return self.get_key_value('Created_Time')

	def set_created_time_9(self, created_time_9):
		"""
		The method to set the value to created_time_9

		Parameters:
			created_time_9 (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time_9 is not None and not isinstance(created_time_9, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time_9 EXPECTED TYPE: datetime', None, None)
		
		self.add_key_value('Created_Time', created_time_9)

	def get_tag(self):
		"""
		The method to get the tag

		Returns:
			list: An instance of list
		"""

		return self.get_key_value('Tag')

	def set_tag(self, tag):
		"""
		The method to set the value to tag

		Parameters:
			tag (list) : An instance of list
		"""

		if tag is not None and not isinstance(tag, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tag EXPECTED TYPE: list', None, None)
		
		self.add_key_value('Tag', tag)

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.get_key_value('name')

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('name', name)
