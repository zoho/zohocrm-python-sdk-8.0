try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.get_related_records_count.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .action_handler import ActionHandler


class ActionWrapper(ActionHandler):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""
		super().__init__()

		self.__get_related_records_count = None
		self.__key_modified = dict()

	def get_get_related_records_count(self):
		"""
		The method to get the get_related_records_count

		Returns:
			list: An instance of list
		"""

		return self.__get_related_records_count

	def set_get_related_records_count(self, get_related_records_count):
		"""
		The method to set the value to get_related_records_count

		Parameters:
			get_related_records_count (list) : An instance of list
		"""

		if get_related_records_count is not None and not isinstance(get_related_records_count, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: get_related_records_count EXPECTED TYPE: list', None, None)
		
		self.__get_related_records_count = get_related_records_count
		self.__key_modified['get_related_records_count'] = 1

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
