try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.call_preferences.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .action_handler import ActionHandler


class ActionWrapper(ActionHandler):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""
		super().__init__()

		self.__call_preferences = None
		self.__key_modified = dict()

	def get_call_preferences(self):
		"""
		The method to get the call_preferences

		Returns:
			ActionResponse: An instance of ActionResponse
		"""

		return self.__call_preferences

	def set_call_preferences(self, call_preferences):
		"""
		The method to set the value to call_preferences

		Parameters:
			call_preferences (ActionResponse) : An instance of ActionResponse
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.call_preferences.action_response import ActionResponse
		except Exception:
			from .action_response import ActionResponse

		if call_preferences is not None and not isinstance(call_preferences, ActionResponse):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: call_preferences EXPECTED TYPE: ActionResponse', None, None)
		
		self.__call_preferences = call_preferences
		self.__key_modified['call_preferences'] = 1

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
