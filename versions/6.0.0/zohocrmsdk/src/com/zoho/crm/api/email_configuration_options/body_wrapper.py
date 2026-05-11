try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__configuration_options = None
		self.__key_modified = dict()

	def get_configuration_options(self):
		"""
		The method to get the configuration_options

		Returns:
			list: An instance of list
		"""

		return self.__configuration_options

	def set_configuration_options(self, configuration_options):
		"""
		The method to set the value to configuration_options

		Parameters:
			configuration_options (list) : An instance of list
		"""

		if configuration_options is not None and not isinstance(configuration_options, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: configuration_options EXPECTED TYPE: list', None, None)
		
		self.__configuration_options = configuration_options
		self.__key_modified['configuration_options'] = 1

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
