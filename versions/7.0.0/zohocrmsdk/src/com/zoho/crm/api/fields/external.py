try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class External(object):
	def __init__(self):
		"""Creates an instance of External"""

		self.__show = None
		self.__type = None
		self.__allow_multiple_config = None
		self.__key_modified = dict()

	def get_show(self):
		"""
		The method to get the show

		Returns:
			bool: A bool representing the show
		"""

		return self.__show

	def set_show(self, show):
		"""
		The method to set the value to show

		Parameters:
			show (bool) : A bool representing the show
		"""

		if show is not None and not isinstance(show, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show EXPECTED TYPE: bool', None, None)
		
		self.__show = show
		self.__key_modified['show'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_allow_multiple_config(self):
		"""
		The method to get the allow_multiple_config

		Returns:
			bool: A bool representing the allow_multiple_config
		"""

		return self.__allow_multiple_config

	def set_allow_multiple_config(self, allow_multiple_config):
		"""
		The method to set the value to allow_multiple_config

		Parameters:
			allow_multiple_config (bool) : A bool representing the allow_multiple_config
		"""

		if allow_multiple_config is not None and not isinstance(allow_multiple_config, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: allow_multiple_config EXPECTED TYPE: bool', None, None)
		
		self.__allow_multiple_config = allow_multiple_config
		self.__key_modified['allow_multiple_config'] = 1

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
