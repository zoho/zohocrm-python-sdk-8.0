try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.call_preferences.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__call_preferences = None
		self.__key_modified = dict()

	def get_call_preferences(self):
		"""
		The method to get the call_preferences

		Returns:
			CallPreferences: An instance of CallPreferences
		"""

		return self.__call_preferences

	def set_call_preferences(self, call_preferences):
		"""
		The method to set the value to call_preferences

		Parameters:
			call_preferences (CallPreferences) : An instance of CallPreferences
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.call_preferences.call_preferences import CallPreferences
		except Exception:
			from .call_preferences import CallPreferences

		if call_preferences is not None and not isinstance(call_preferences, CallPreferences):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: call_preferences EXPECTED TYPE: CallPreferences', None, None)
		
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
