try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class EnrichedData(object):
	def __init__(self):
		"""Creates an instance of EnrichedData"""

		self.__website = None
		self.__email_infos = None
		self.__gender = None
		self.__company_info = None
		self.__last_name = None
		self.__educations = None
		self.__middle_name = None
		self.__skills = None
		self.__other_contacts = None
		self.__address_list_info = None
		self.__primary_address_info = None
		self.__name = None
		self.__secondary_contact = None
		self.__primary_email = None
		self.__designation = None
		self.__id = None
		self.__interests = None
		self.__first_name = None
		self.__primary_contact = None
		self.__social_media = None
		self.__key_modified = dict()

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

	def get_email_infos(self):
		"""
		The method to get the email_infos

		Returns:
			list: An instance of list
		"""

		return self.__email_infos

	def set_email_infos(self, email_infos):
		"""
		The method to set the value to email_infos

		Parameters:
			email_infos (list) : An instance of list
		"""

		if email_infos is not None and not isinstance(email_infos, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_infos EXPECTED TYPE: list', None, None)
		
		self.__email_infos = email_infos
		self.__key_modified['email_infos'] = 1

	def get_gender(self):
		"""
		The method to get the gender

		Returns:
			string: A string representing the gender
		"""

		return self.__gender

	def set_gender(self, gender):
		"""
		The method to set the value to gender

		Parameters:
			gender (string) : A string representing the gender
		"""

		if gender is not None and not isinstance(gender, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: gender EXPECTED TYPE: str', None, None)
		
		self.__gender = gender
		self.__key_modified['gender'] = 1

	def get_company_info(self):
		"""
		The method to get the company_info

		Returns:
			CompanyInfo: An instance of CompanyInfo
		"""

		return self.__company_info

	def set_company_info(self, company_info):
		"""
		The method to set the value to company_info

		Parameters:
			company_info (CompanyInfo) : An instance of CompanyInfo
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.company_info import CompanyInfo
		except Exception:
			from .company_info import CompanyInfo

		if company_info is not None and not isinstance(company_info, CompanyInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: company_info EXPECTED TYPE: CompanyInfo', None, None)
		
		self.__company_info = company_info
		self.__key_modified['company_info'] = 1

	def get_last_name(self):
		"""
		The method to get the last_name

		Returns:
			string: A string representing the last_name
		"""

		return self.__last_name

	def set_last_name(self, last_name):
		"""
		The method to set the value to last_name

		Parameters:
			last_name (string) : A string representing the last_name
		"""

		if last_name is not None and not isinstance(last_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_name EXPECTED TYPE: str', None, None)
		
		self.__last_name = last_name
		self.__key_modified['last_name'] = 1

	def get_educations(self):
		"""
		The method to get the educations

		Returns:
			list: An instance of list
		"""

		return self.__educations

	def set_educations(self, educations):
		"""
		The method to set the value to educations

		Parameters:
			educations (list) : An instance of list
		"""

		if educations is not None and not isinstance(educations, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: educations EXPECTED TYPE: list', None, None)
		
		self.__educations = educations
		self.__key_modified['educations'] = 1

	def get_middle_name(self):
		"""
		The method to get the middle_name

		Returns:
			string: A string representing the middle_name
		"""

		return self.__middle_name

	def set_middle_name(self, middle_name):
		"""
		The method to set the value to middle_name

		Parameters:
			middle_name (string) : A string representing the middle_name
		"""

		if middle_name is not None and not isinstance(middle_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: middle_name EXPECTED TYPE: str', None, None)
		
		self.__middle_name = middle_name
		self.__key_modified['middle_name'] = 1

	def get_skills(self):
		"""
		The method to get the skills

		Returns:
			list: An instance of list
		"""

		return self.__skills

	def set_skills(self, skills):
		"""
		The method to set the value to skills

		Parameters:
			skills (list) : An instance of list
		"""

		if skills is not None and not isinstance(skills, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: skills EXPECTED TYPE: list', None, None)
		
		self.__skills = skills
		self.__key_modified['skills'] = 1

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

	def get_address_list_info(self):
		"""
		The method to get the address_list_info

		Returns:
			list: An instance of list
		"""

		return self.__address_list_info

	def set_address_list_info(self, address_list_info):
		"""
		The method to set the value to address_list_info

		Parameters:
			address_list_info (list) : An instance of list
		"""

		if address_list_info is not None and not isinstance(address_list_info, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: address_list_info EXPECTED TYPE: list', None, None)
		
		self.__address_list_info = address_list_info
		self.__key_modified['address_list_info'] = 1

	def get_primary_address_info(self):
		"""
		The method to get the primary_address_info

		Returns:
			Address: An instance of Address
		"""

		return self.__primary_address_info

	def set_primary_address_info(self, primary_address_info):
		"""
		The method to set the value to primary_address_info

		Parameters:
			primary_address_info (Address) : An instance of Address
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.address import Address
		except Exception:
			from .address import Address

		if primary_address_info is not None and not isinstance(primary_address_info, Address):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: primary_address_info EXPECTED TYPE: Address', None, None)
		
		self.__primary_address_info = primary_address_info
		self.__key_modified['primary_address_info'] = 1

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

	def get_designation(self):
		"""
		The method to get the designation

		Returns:
			string: A string representing the designation
		"""

		return self.__designation

	def set_designation(self, designation):
		"""
		The method to set the value to designation

		Parameters:
			designation (string) : A string representing the designation
		"""

		if designation is not None and not isinstance(designation, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: designation EXPECTED TYPE: str', None, None)
		
		self.__designation = designation
		self.__key_modified['designation'] = 1

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

	def get_interests(self):
		"""
		The method to get the interests

		Returns:
			list: An instance of list
		"""

		return self.__interests

	def set_interests(self, interests):
		"""
		The method to set the value to interests

		Parameters:
			interests (list) : An instance of list
		"""

		if interests is not None and not isinstance(interests, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: interests EXPECTED TYPE: list', None, None)
		
		self.__interests = interests
		self.__key_modified['interests'] = 1

	def get_first_name(self):
		"""
		The method to get the first_name

		Returns:
			string: A string representing the first_name
		"""

		return self.__first_name

	def set_first_name(self, first_name):
		"""
		The method to set the value to first_name

		Parameters:
			first_name (string) : A string representing the first_name
		"""

		if first_name is not None and not isinstance(first_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: first_name EXPECTED TYPE: str', None, None)
		
		self.__first_name = first_name
		self.__key_modified['first_name'] = 1

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
