try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ErrorDetails(object):
	def __init__(self):
		"""Creates an instance of ErrorDetails"""

		self.__api_name = None
		self.__json_path = None
		self.__range = None
		self.__supported_values = None
		self.__key_modified = dict()

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_json_path(self):
		"""
		The method to get the json_path

		Returns:
			string: A string representing the json_path
		"""

		return self.__json_path

	def set_json_path(self, json_path):
		"""
		The method to set the value to json_path

		Parameters:
			json_path (string) : A string representing the json_path
		"""

		if json_path is not None and not isinstance(json_path, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: json_path EXPECTED TYPE: str', None, None)
		
		self.__json_path = json_path
		self.__key_modified['json_path'] = 1

	def get_range(self):
		"""
		The method to get the range

		Returns:
			RangeStructure: An instance of RangeStructure
		"""

		return self.__range

	def set_range(self, range):
		"""
		The method to set the value to range

		Parameters:
			range (RangeStructure) : An instance of RangeStructure
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_configuration_options.range_structure import RangeStructure
		except Exception:
			from .range_structure import RangeStructure

		if range is not None and not isinstance(range, RangeStructure):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: range EXPECTED TYPE: RangeStructure', None, None)
		
		self.__range = range
		self.__key_modified['range'] = 1

	def get_supported_values(self):
		"""
		The method to get the supported_values

		Returns:
			list: An instance of list
		"""

		return self.__supported_values

	def set_supported_values(self, supported_values):
		"""
		The method to set the value to supported_values

		Parameters:
			supported_values (list) : An instance of list
		"""

		if supported_values is not None and not isinstance(supported_values, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: supported_values EXPECTED TYPE: list', None, None)
		
		self.__supported_values = supported_values
		self.__key_modified['supported_values'] = 1

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
