try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.user_type_users.status_action_handler import StatusActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .status_action_handler import StatusActionHandler


class StatusActionWrapper(StatusActionHandler):
	def __init__(self):
		"""Creates an instance of StatusActionWrapper"""
		super().__init__()

		self.__change_status = None
		self.__key_modified = dict()

	def get_change_status(self):
		"""
		The method to get the change_status

		Returns:
			list: An instance of list
		"""

		return self.__change_status

	def set_change_status(self, change_status):
		"""
		The method to set the value to change_status

		Parameters:
			change_status (list) : An instance of list
		"""

		if change_status is not None and not isinstance(change_status, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: change_status EXPECTED TYPE: list', None, None)
		
		self.__change_status = change_status
		self.__key_modified['change_status'] = 1

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
