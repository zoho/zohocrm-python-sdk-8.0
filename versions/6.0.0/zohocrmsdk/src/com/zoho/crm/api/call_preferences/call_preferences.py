try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class CallPreferences(object):
	def __init__(self):
		"""Creates an instance of CallPreferences"""

		self.__show_from_number = None
		self.__show_to_number = None
		self.__key_modified = dict()

	def get_show_from_number(self):
		"""
		The method to get the show_from_number

		Returns:
			bool: A bool representing the show_from_number
		"""

		return self.__show_from_number

	def set_show_from_number(self, show_from_number):
		"""
		The method to set the value to show_from_number

		Parameters:
			show_from_number (bool) : A bool representing the show_from_number
		"""

		if show_from_number is not None and not isinstance(show_from_number, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_from_number EXPECTED TYPE: bool', None, None)
		
		self.__show_from_number = show_from_number
		self.__key_modified['show_from_number'] = 1

	def get_show_to_number(self):
		"""
		The method to get the show_to_number

		Returns:
			bool: A bool representing the show_to_number
		"""

		return self.__show_to_number

	def set_show_to_number(self, show_to_number):
		"""
		The method to set the value to show_to_number

		Parameters:
			show_to_number (bool) : A bool representing the show_to_number
		"""

		if show_to_number is not None and not isinstance(show_to_number, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_to_number EXPECTED TYPE: bool', None, None)
		
		self.__show_to_number = show_to_number
		self.__key_modified['show_to_number'] = 1

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
