try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Address(object):
	def __init__(self):
		"""Creates an instance of Address"""

		self.__continent = None
		self.__country = None
		self.__name = None
		self.__region = None
		self.__primary = None
		self.__key_modified = dict()

	def get_continent(self):
		"""
		The method to get the continent

		Returns:
			string: A string representing the continent
		"""

		return self.__continent

	def set_continent(self, continent):
		"""
		The method to set the value to continent

		Parameters:
			continent (string) : A string representing the continent
		"""

		if continent is not None and not isinstance(continent, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: continent EXPECTED TYPE: str', None, None)
		
		self.__continent = continent
		self.__key_modified['continent'] = 1

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

	def get_region(self):
		"""
		The method to get the region

		Returns:
			string: A string representing the region
		"""

		return self.__region

	def set_region(self, region):
		"""
		The method to set the value to region

		Parameters:
			region (string) : A string representing the region
		"""

		if region is not None and not isinstance(region, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: region EXPECTED TYPE: str', None, None)
		
		self.__region = region
		self.__key_modified['region'] = 1

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
