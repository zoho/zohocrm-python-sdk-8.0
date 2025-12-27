try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.users_unavailability.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .action_handler import ActionHandler


class ActionWrapper(ActionHandler):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""
		super().__init__()

		self.__users_unavailability = None
		self.__key_modified = dict()

	def get_users_unavailability(self):
		"""
		The method to get the users_unavailability

		Returns:
			list: An instance of list
		"""

		return self.__users_unavailability

	def set_users_unavailability(self, users_unavailability):
		"""
		The method to set the value to users_unavailability

		Parameters:
			users_unavailability (list) : An instance of list
		"""

		if users_unavailability is not None and not isinstance(users_unavailability, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: users_unavailability EXPECTED TYPE: list', None, None)
		
		self.__users_unavailability = users_unavailability
		self.__key_modified['users_unavailability'] = 1

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
