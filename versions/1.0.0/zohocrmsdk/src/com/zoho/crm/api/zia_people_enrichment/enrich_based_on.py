try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class EnrichBasedOn(object):
	def __init__(self):
		"""Creates an instance of EnrichBasedOn"""

		self.__social = None
		self.__name = None
		self.__company = None
		self.__email = None
		self.__key_modified = dict()

	def get_social(self):
		"""
		The method to get the social

		Returns:
			Social: An instance of Social
		"""

		return self.__social

	def set_social(self, social):
		"""
		The method to set the value to social

		Parameters:
			social (Social) : An instance of Social
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.social import Social
		except Exception:
			from .social import Social

		if social is not None and not isinstance(social, Social):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: social EXPECTED TYPE: Social', None, None)
		
		self.__social = social
		self.__key_modified['social'] = 1

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

	def get_company(self):
		"""
		The method to get the company

		Returns:
			Company: An instance of Company
		"""

		return self.__company

	def set_company(self, company):
		"""
		The method to set the value to company

		Parameters:
			company (Company) : An instance of Company
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_people_enrichment.company import Company
		except Exception:
			from .company import Company

		if company is not None and not isinstance(company, Company):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: company EXPECTED TYPE: Company', None, None)
		
		self.__company = company
		self.__key_modified['company'] = 1

	def get_email(self):
		"""
		The method to get the email

		Returns:
			string: A string representing the email
		"""

		return self.__email

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (string) : A string representing the email
		"""

		if email is not None and not isinstance(email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: str', None, None)
		
		self.__email = email
		self.__key_modified['email'] = 1

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
