try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.record.count_handler import CountHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .count_handler import CountHandler


class CountWrapper(CountHandler):
	def __init__(self):
		"""Creates an instance of CountWrapper"""
		super().__init__()

		self.__count = None
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
