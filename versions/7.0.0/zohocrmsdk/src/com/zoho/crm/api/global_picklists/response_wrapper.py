try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.global_picklists.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__global_picklists = None
		self.__key_modified = dict()

	def get_global_picklists(self):
		"""
		The method to get the global_picklists

		Returns:
			list: An instance of list
		"""

		return self.__global_picklists

	def set_global_picklists(self, global_picklists):
		"""
		The method to set the value to global_picklists

		Parameters:
			global_picklists (list) : An instance of list
		"""

		if global_picklists is not None and not isinstance(global_picklists, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: global_picklists EXPECTED TYPE: list', None, None)
		
		self.__global_picklists = global_picklists
		self.__key_modified['global_picklists'] = 1

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
