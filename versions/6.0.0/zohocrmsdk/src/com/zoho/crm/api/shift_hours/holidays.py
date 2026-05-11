try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Holidays(object):
	def __init__(self):
		"""Creates an instance of Holidays"""

		self.__date = None
		self.__year = None
		self.__name = None
		self.__id = None
		self.__key_modified = dict()

	def get_date(self):
		"""
		The method to get the date

		Returns:
			date: An instance of date
		"""

		return self.__date

	def set_date(self, date):
		"""
		The method to set the value to date

		Parameters:
			date (date) : An instance of date
		"""

		from datetime import date as date1

		if date is not None and not isinstance(date, date1):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: date EXPECTED TYPE: date1', None, None)
		
		self.__date = date
		self.__key_modified['date'] = 1

	def get_year(self):
		"""
		The method to get the year

		Returns:
			int: An int representing the year
		"""

		return self.__year

	def set_year(self, year):
		"""
		The method to set the value to year

		Parameters:
			year (int) : An int representing the year
		"""

		if year is not None and not isinstance(year, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: year EXPECTED TYPE: int', None, None)
		
		self.__year = year
		self.__key_modified['year'] = 1

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

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

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
