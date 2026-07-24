try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class SupportedAPI(object):
	def __init__(self):
		"""Creates an instance of SupportedAPI"""

		self.__path = None
		self.__operation_types = None
		self.__key_modified = dict()

	def get_path(self):
		"""
		The method to get the path

		Returns:
			string: A string representing the path
		"""

		return self.__path

	def set_path(self, path):
		"""
		The method to set the value to path

		Parameters:
			path (string) : A string representing the path
		"""

		if path is not None and not isinstance(path, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: path EXPECTED TYPE: str', None, None)
		
		self.__path = path
		self.__key_modified['path'] = 1

	def get_operation_types(self):
		"""
		The method to get the operation_types

		Returns:
			list: An instance of list
		"""

		return self.__operation_types

	def set_operation_types(self, operation_types):
		"""
		The method to set the value to operation_types

		Parameters:
			operation_types (list) : An instance of list
		"""

		if operation_types is not None and not isinstance(operation_types, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: operation_types EXPECTED TYPE: list', None, None)
		
		self.__operation_types = operation_types
		self.__key_modified['operation_types'] = 1

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
