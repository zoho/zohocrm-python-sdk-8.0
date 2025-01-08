try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.user_groups.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class SourcesCountWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of SourcesCountWrapper"""
		super().__init__()

		self.__sources_count = None
		self.__key_modified = dict()

	def get_sources_count(self):
		"""
		The method to get the sources_count

		Returns:
			list: An instance of list
		"""

		return self.__sources_count

	def set_sources_count(self, sources_count):
		"""
		The method to set the value to sources_count

		Parameters:
			sources_count (list) : An instance of list
		"""

		if sources_count is not None and not isinstance(sources_count, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sources_count EXPECTED TYPE: list', None, None)
		
		self.__sources_count = sources_count
		self.__key_modified['sources_count'] = 1

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
