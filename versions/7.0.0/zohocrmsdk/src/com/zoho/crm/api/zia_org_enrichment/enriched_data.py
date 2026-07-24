try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class EnrichedData(object):
	def __init__(self):
		"""Creates an instance of EnrichedData"""

		self.__org_status = None
		self.__description = None
		self.__ceo = None
		self.__secondary_email = None
		self.__revenue = None
		self.__years_in_industry = None
		self.__other_contacts = None
		self.__techno_graphic_data = None
		self.__logo = None
		self.__secondary_contact = None
		self.__id = None
		self.__other_emails = None
		self.__sign_in = None
		self.__website = None
		self.__address = None
		self.__sign_up = None
		self.__org_type = None
		self.__head_quarters = None
		self.__no_of_employees = None
		self.__territory_list = None
		self.__founding_year = None
		self.__industries = None
		self.__name = None
		self.__primary_email = None
		self.__business_model = None
		self.__primary_contact = None
		self.__social_media = None
		self.__key_modified = dict()

	def get_org_status(self):
		"""
		The method to get the org_status

		Returns:
			string: A string representing the org_status
		"""

		return self.__org_status

	def set_org_status(self, org_status):
		"""
		The method to set the value to org_status

		Parameters:
			org_status (string) : A string representing the org_status
		"""

		if org_status is not None and not isinstance(org_status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: org_status EXPECTED TYPE: str', None, None)
		
		self.__org_status = org_status
		self.__key_modified['org_status'] = 1

	def get_description(self):
		"""
		The method to get the description

		Returns:
			list: An instance of list
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (list) : An instance of list
		"""

		if description is not None and not isinstance(description, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: list', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

	def get_ceo(self):
		"""
		The method to get the ceo

		Returns:
			string: A string representing the ceo
		"""

		return self.__ceo

	def set_ceo(self, ceo):
		"""
		The method to set the value to ceo

		Parameters:
			ceo (string) : A string representing the ceo
		"""

		if ceo is not None and not isinstance(ceo, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ceo EXPECTED TYPE: str', None, None)
		
		self.__ceo = ceo
		self.__key_modified['ceo'] = 1

	def get_secondary_email(self):
		"""
		The method to get the secondary_email

		Returns:
			string: A string representing the secondary_email
		"""

		return self.__secondary_email

	def set_secondary_email(self, secondary_email):
		"""
		The method to set the value to secondary_email

		Parameters:
			secondary_email (string) : A string representing the secondary_email
		"""

		if secondary_email is not None and not isinstance(secondary_email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: secondary_email EXPECTED TYPE: str', None, None)
		
		self.__secondary_email = secondary_email
		self.__key_modified['secondary_email'] = 1

	def get_revenue(self):
		"""
		The method to get the revenue

		Returns:
			string: A string representing the revenue
		"""

		return self.__revenue

	def set_revenue(self, revenue):
		"""
		The method to set the value to revenue

		Parameters:
			revenue (string) : A string representing the revenue
		"""

		if revenue is not None and not isinstance(revenue, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: revenue EXPECTED TYPE: str', None, None)
		
		self.__revenue = revenue
		self.__key_modified['revenue'] = 1

	def get_years_in_industry(self):
		"""
		The method to get the years_in_industry

		Returns:
			string: A string representing the years_in_industry
		"""

		return self.__years_in_industry

	def set_years_in_industry(self, years_in_industry):
		"""
		The method to set the value to years_in_industry

		Parameters:
			years_in_industry (string) : A string representing the years_in_industry
		"""

		if years_in_industry is not None and not isinstance(years_in_industry, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: years_in_industry EXPECTED TYPE: str', None, None)
		
		self.__years_in_industry = years_in_industry
		self.__key_modified['years_in_industry'] = 1

	def get_other_contacts(self):
		"""
		The method to get the other_contacts

		Returns:
			list: An instance of list
		"""

		return self.__other_contacts

	def set_other_contacts(self, other_contacts):
		"""
		The method to set the value to other_contacts

		Parameters:
			other_contacts (list) : An instance of list
		"""

		if other_contacts is not None and not isinstance(other_contacts, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: other_contacts EXPECTED TYPE: list', None, None)
		
		self.__other_contacts = other_contacts
		self.__key_modified['other_contacts'] = 1

	def get_techno_graphic_data(self):
		"""
		The method to get the techno_graphic_data

		Returns:
			string: A string representing the techno_graphic_data
		"""

		return self.__techno_graphic_data

	def set_techno_graphic_data(self, techno_graphic_data):
		"""
		The method to set the value to techno_graphic_data

		Parameters:
			techno_graphic_data (string) : A string representing the techno_graphic_data
		"""

		if techno_graphic_data is not None and not isinstance(techno_graphic_data, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: techno_graphic_data EXPECTED TYPE: str', None, None)
		
		self.__techno_graphic_data = techno_graphic_data
		self.__key_modified['techno_graphic_data'] = 1

	def get_logo(self):
		"""
		The method to get the logo

		Returns:
			string: A string representing the logo
		"""

		return self.__logo

	def set_logo(self, logo):
		"""
		The method to set the value to logo

		Parameters:
			logo (string) : A string representing the logo
		"""

		if logo is not None and not isinstance(logo, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: logo EXPECTED TYPE: str', None, None)
		
		self.__logo = logo
		self.__key_modified['logo'] = 1

	def get_secondary_contact(self):
		"""
		The method to get the secondary_contact

		Returns:
			string: A string representing the secondary_contact
		"""

		return self.__secondary_contact

	def set_secondary_contact(self, secondary_contact):
		"""
		The method to set the value to secondary_contact

		Parameters:
			secondary_contact (string) : A string representing the secondary_contact
		"""

		if secondary_contact is not None and not isinstance(secondary_contact, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: secondary_contact EXPECTED TYPE: str', None, None)
		
		self.__secondary_contact = secondary_contact
		self.__key_modified['secondary_contact'] = 1

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

	def get_other_emails(self):
		"""
		The method to get the other_emails

		Returns:
			list: An instance of list
		"""

		return self.__other_emails

	def set_other_emails(self, other_emails):
		"""
		The method to set the value to other_emails

		Parameters:
			other_emails (list) : An instance of list
		"""

		if other_emails is not None and not isinstance(other_emails, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: other_emails EXPECTED TYPE: list', None, None)
		
		self.__other_emails = other_emails
		self.__key_modified['other_emails'] = 1

	def get_sign_in(self):
		"""
		The method to get the sign_in

		Returns:
			string: A string representing the sign_in
		"""

		return self.__sign_in

	def set_sign_in(self, sign_in):
		"""
		The method to set the value to sign_in

		Parameters:
			sign_in (string) : A string representing the sign_in
		"""

		if sign_in is not None and not isinstance(sign_in, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sign_in EXPECTED TYPE: str', None, None)
		
		self.__sign_in = sign_in
		self.__key_modified['sign_in'] = 1

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

	def get_address(self):
		"""
		The method to get the address

		Returns:
			list: An instance of list
		"""

		return self.__address

	def set_address(self, address):
		"""
		The method to set the value to address

		Parameters:
			address (list) : An instance of list
		"""

		if address is not None and not isinstance(address, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: address EXPECTED TYPE: list', None, None)
		
		self.__address = address
		self.__key_modified['address'] = 1

	def get_sign_up(self):
		"""
		The method to get the sign_up

		Returns:
			string: A string representing the sign_up
		"""

		return self.__sign_up

	def set_sign_up(self, sign_up):
		"""
		The method to set the value to sign_up

		Parameters:
			sign_up (string) : A string representing the sign_up
		"""

		if sign_up is not None and not isinstance(sign_up, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sign_up EXPECTED TYPE: str', None, None)
		
		self.__sign_up = sign_up
		self.__key_modified['sign_up'] = 1

	def get_org_type(self):
		"""
		The method to get the org_type

		Returns:
			string: A string representing the org_type
		"""

		return self.__org_type

	def set_org_type(self, org_type):
		"""
		The method to set the value to org_type

		Parameters:
			org_type (string) : A string representing the org_type
		"""

		if org_type is not None and not isinstance(org_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: org_type EXPECTED TYPE: str', None, None)
		
		self.__org_type = org_type
		self.__key_modified['org_type'] = 1

	def get_head_quarters(self):
		"""
		The method to get the head_quarters

		Returns:
			list: An instance of list
		"""

		return self.__head_quarters

	def set_head_quarters(self, head_quarters):
		"""
		The method to set the value to head_quarters

		Parameters:
			head_quarters (list) : An instance of list
		"""

		if head_quarters is not None and not isinstance(head_quarters, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: head_quarters EXPECTED TYPE: list', None, None)
		
		self.__head_quarters = head_quarters
		self.__key_modified['head_quarters'] = 1

	def get_no_of_employees(self):
		"""
		The method to get the no_of_employees

		Returns:
			string: A string representing the no_of_employees
		"""

		return self.__no_of_employees

	def set_no_of_employees(self, no_of_employees):
		"""
		The method to set the value to no_of_employees

		Parameters:
			no_of_employees (string) : A string representing the no_of_employees
		"""

		if no_of_employees is not None and not isinstance(no_of_employees, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: no_of_employees EXPECTED TYPE: str', None, None)
		
		self.__no_of_employees = no_of_employees
		self.__key_modified['no_of_employees'] = 1

	def get_territory_list(self):
		"""
		The method to get the territory_list

		Returns:
			list: An instance of list
		"""

		return self.__territory_list

	def set_territory_list(self, territory_list):
		"""
		The method to set the value to territory_list

		Parameters:
			territory_list (list) : An instance of list
		"""

		if territory_list is not None and not isinstance(territory_list, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory_list EXPECTED TYPE: list', None, None)
		
		self.__territory_list = territory_list
		self.__key_modified['territory_list'] = 1

	def get_founding_year(self):
		"""
		The method to get the founding_year

		Returns:
			string: A string representing the founding_year
		"""

		return self.__founding_year

	def set_founding_year(self, founding_year):
		"""
		The method to set the value to founding_year

		Parameters:
			founding_year (string) : A string representing the founding_year
		"""

		if founding_year is not None and not isinstance(founding_year, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: founding_year EXPECTED TYPE: str', None, None)
		
		self.__founding_year = founding_year
		self.__key_modified['founding_year'] = 1

	def get_industries(self):
		"""
		The method to get the industries

		Returns:
			list: An instance of list
		"""

		return self.__industries

	def set_industries(self, industries):
		"""
		The method to set the value to industries

		Parameters:
			industries (list) : An instance of list
		"""

		if industries is not None and not isinstance(industries, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: industries EXPECTED TYPE: list', None, None)
		
		self.__industries = industries
		self.__key_modified['industries'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

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

	def get_business_model(self):
		"""
		The method to get the business_model

		Returns:
			list: An instance of list
		"""

		return self.__business_model

	def set_business_model(self, business_model):
		"""
		The method to set the value to business_model

		Parameters:
			business_model (list) : An instance of list
		"""

		if business_model is not None and not isinstance(business_model, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: business_model EXPECTED TYPE: list', None, None)
		
		self.__business_model = business_model
		self.__key_modified['business_model'] = 1

	def get_primary_contact(self):
		"""
		The method to get the primary_contact

		Returns:
			string: A string representing the primary_contact
		"""

		return self.__primary_contact

	def set_primary_contact(self, primary_contact):
		"""
		The method to set the value to primary_contact

		Parameters:
			primary_contact (string) : A string representing the primary_contact
		"""

		if primary_contact is not None and not isinstance(primary_contact, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: primary_contact EXPECTED TYPE: str', None, None)
		
		self.__primary_contact = primary_contact
		self.__key_modified['primary_contact'] = 1

	def get_social_media(self):
		"""
		The method to get the social_media

		Returns:
			list: An instance of list
		"""

		return self.__social_media

	def set_social_media(self, social_media):
		"""
		The method to set the value to social_media

		Parameters:
			social_media (list) : An instance of list
		"""

		if social_media is not None and not isinstance(social_media, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: social_media EXPECTED TYPE: list', None, None)
		
		self.__social_media = social_media
		self.__key_modified['social_media'] = 1

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
