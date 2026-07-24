try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FiltersBody(object):
	def __init__(self):
		"""Creates an instance of FiltersBody"""

		self.__filters = None
		self.__key_modified = dict()

	def get_filters(self):
		"""
		The method to get the filters

		Returns:
			list: An instance of list
		"""

		return self.__filters

	def set_filters(self, filters):
		"""
		The method to set the value to filters

		Parameters:
			filters (list) : An instance of list
		"""

		if filters is not None and not isinstance(filters, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: filters EXPECTED TYPE: list', None, None)
		
		self.__filters = filters
		self.__key_modified['filters'] = 1

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
