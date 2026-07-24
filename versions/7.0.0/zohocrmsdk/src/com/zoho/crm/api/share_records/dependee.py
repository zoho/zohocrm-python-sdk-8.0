try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Dependee(object):
	def __init__(self):
		"""Creates an instance of Dependee"""

		self.__json_path = None
		self.__api_name = None
		self.__key_modified = dict()

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
