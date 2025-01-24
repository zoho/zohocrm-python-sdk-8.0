try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Info(object):
	def __init__(self):
		"""Creates an instance of Info"""

		self.__count = None
		self.__next_index = None
		self.__prev_index = None
		self.__per_page = None
		self.__more_records = None
		self.__key_modified = dict()

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

	def get_next_index(self):
		"""
		The method to get the next_index

		Returns:
			string: A string representing the next_index
		"""

		return self.__next_index

	def set_next_index(self, next_index):
		"""
		The method to set the value to next_index

		Parameters:
			next_index (string) : A string representing the next_index
		"""

		if next_index is not None and not isinstance(next_index, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: next_index EXPECTED TYPE: str', None, None)
		
		self.__next_index = next_index
		self.__key_modified['next_index'] = 1

	def get_prev_index(self):
		"""
		The method to get the prev_index

		Returns:
			string: A string representing the prev_index
		"""

		return self.__prev_index

	def set_prev_index(self, prev_index):
		"""
		The method to set the value to prev_index

		Parameters:
			prev_index (string) : A string representing the prev_index
		"""

		if prev_index is not None and not isinstance(prev_index, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: prev_index EXPECTED TYPE: str', None, None)
		
		self.__prev_index = prev_index
		self.__key_modified['prev_index'] = 1

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
