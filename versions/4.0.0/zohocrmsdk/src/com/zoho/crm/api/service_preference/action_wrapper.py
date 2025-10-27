try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.service_preference.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .action_handler import ActionHandler


class ActionWrapper(ActionHandler):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""
		super().__init__()

		self.__service_preferences = None
		self.__key_modified = dict()

	def get_service_preferences(self):
		"""
		The method to get the service_preferences

		Returns:
			ActionResponse: An instance of ActionResponse
		"""

		return self.__service_preferences

	def set_service_preferences(self, service_preferences):
		"""
		The method to set the value to service_preferences

		Parameters:
			service_preferences (ActionResponse) : An instance of ActionResponse
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.service_preference.action_response import ActionResponse
		except Exception:
			from .action_response import ActionResponse

		if service_preferences is not None and not isinstance(service_preferences, ActionResponse):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: service_preferences EXPECTED TYPE: ActionResponse', None, None)
		
		self.__service_preferences = service_preferences
		self.__key_modified['service_preferences'] = 1

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
