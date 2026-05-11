try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Experience(object):
	def __init__(self):
		"""Creates an instance of Experience"""

		self.__end_date = None
		self.__company_name = None
		self.__title = None
		self.__start_date = None
		self.__primary = None
		self.__key_modified = dict()

	def get_end_date(self):
		"""
		The method to get the end_date

		Returns:
			string: A string representing the end_date
		"""

		return self.__end_date

	def set_end_date(self, end_date):
		"""
		The method to set the value to end_date

		Parameters:
			end_date (string) : A string representing the end_date
		"""

		if end_date is not None and not isinstance(end_date, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: end_date EXPECTED TYPE: str', None, None)
		
		self.__end_date = end_date
		self.__key_modified['end_date'] = 1

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

	def get_title(self):
		"""
		The method to get the title

		Returns:
			string: A string representing the title
		"""

		return self.__title

	def set_title(self, title):
		"""
		The method to set the value to title

		Parameters:
			title (string) : A string representing the title
		"""

		if title is not None and not isinstance(title, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: title EXPECTED TYPE: str', None, None)
		
		self.__title = title
		self.__key_modified['title'] = 1

	def get_start_date(self):
		"""
		The method to get the start_date

		Returns:
			string: A string representing the start_date
		"""

		return self.__start_date

	def set_start_date(self, start_date):
		"""
		The method to set the value to start_date

		Parameters:
			start_date (string) : A string representing the start_date
		"""

		if start_date is not None and not isinstance(start_date, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: start_date EXPECTED TYPE: str', None, None)
		
		self.__start_date = start_date
		self.__key_modified['start_date'] = 1

	def get_primary(self):
		"""
		The method to get the primary

		Returns:
			bool: A bool representing the primary
		"""

		return self.__primary

	def set_primary(self, primary):
		"""
		The method to set the value to primary

		Parameters:
			primary (bool) : A bool representing the primary
		"""

		if primary is not None and not isinstance(primary, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: primary EXPECTED TYPE: bool', None, None)
		
		self.__primary = primary
		self.__key_modified['primary'] = 1

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
