try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Info(object):
	def __init__(self):
		"""Creates an instance of Info"""

		self.__per_page = None
		self.__count = None
		self.__page = None
		self.__more_records = None
		self.__key_modified = dict()

	def get_per_page(self):
		"""
		The method to get the per_page

		Returns:
			int: An int representing the per_page
		"""

		return self.__per_page

	def set_per_page(self, per_page):
		"""
		The method to set the value to per_page

		Parameters:
			per_page (int) : An int representing the per_page
		"""

		if per_page is not None and not isinstance(per_page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: per_page EXPECTED TYPE: int', None, None)
		
		self.__per_page = per_page
		self.__key_modified['per_page'] = 1

	def get_count(self):
		"""
		The method to get the count

		Returns:
			int: An int representing the count
		"""

		return self.__count

	def set_count(self, count):
		"""
		The method to set the value to count

		Parameters:
			count (int) : An int representing the count
		"""

		if count is not None and not isinstance(count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: count EXPECTED TYPE: int', None, None)
		
		self.__count = count
		self.__key_modified['count'] = 1

	def get_page(self):
		"""
		The method to get the page

		Returns:
			int: An int representing the page
		"""

		return self.__page

	def set_page(self, page):
		"""
		The method to set the value to page

		Parameters:
			page (int) : An int representing the page
		"""

		if page is not None and not isinstance(page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: page EXPECTED TYPE: int', None, None)
		
		self.__page = page
		self.__key_modified['page'] = 1

	def get_more_records(self):
		"""
		The method to get the more_records

		Returns:
			bool: A bool representing the more_records
		"""

		return self.__more_records

	def set_more_records(self, more_records):
		"""
		The method to set the value to more_records

		Parameters:
			more_records (bool) : A bool representing the more_records
		"""

		if more_records is not None and not isinstance(more_records, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: more_records EXPECTED TYPE: bool', None, None)
		
		self.__more_records = more_records
		self.__key_modified['more_records'] = 1

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
