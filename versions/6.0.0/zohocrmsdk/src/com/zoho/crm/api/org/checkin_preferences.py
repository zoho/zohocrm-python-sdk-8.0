try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class CheckinPreferences(object):
	def __init__(self):
		"""Creates an instance of CheckinPreferences"""

		self.__restricted_event_types = None
		self.__key_modified = dict()

	def get_restricted_event_types(self):
		"""
		The method to get the restricted_event_types

		Returns:
			string: A string representing the restricted_event_types
		"""

		return self.__restricted_event_types

	def set_restricted_event_types(self, restricted_event_types):
		"""
		The method to set the value to restricted_event_types

		Parameters:
			restricted_event_types (string) : A string representing the restricted_event_types
		"""

		if restricted_event_types is not None and not isinstance(restricted_event_types, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restricted_event_types EXPECTED TYPE: str', None, None)
		
		self.__restricted_event_types = restricted_event_types
		self.__key_modified['restricted_event_types'] = 1

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
