try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FieldMapping(object):
	def __init__(self):
		"""Creates an instance of FieldMapping"""

		self.__api_name = None
		self.__index = None
		self.__format = None
		self.__find_by = None
		self.__default_value = None
		self.__module = None
		self.__parent_column_index = None
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

	def get_index(self):
		"""
		The method to get the index

		Returns:
			int: An int representing the index
		"""

		return self.__index

	def set_index(self, index):
		"""
		The method to set the value to index

		Parameters:
			index (int) : An int representing the index
		"""

		if index is not None and not isinstance(index, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: index EXPECTED TYPE: int', None, None)
		
		self.__index = index
		self.__key_modified['index'] = 1

	def get_format(self):
		"""
		The method to get the format

		Returns:
			string: A string representing the format
		"""

		return self.__format

	def set_format(self, format):
		"""
		The method to set the value to format

		Parameters:
			format (string) : A string representing the format
		"""

		if format is not None and not isinstance(format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: format EXPECTED TYPE: str', None, None)
		
		self.__format = format
		self.__key_modified['format'] = 1

	def get_find_by(self):
		"""
		The method to get the find_by

		Returns:
			string: A string representing the find_by
		"""

		return self.__find_by

	def set_find_by(self, find_by):
		"""
		The method to set the value to find_by

		Parameters:
			find_by (string) : A string representing the find_by
		"""

		if find_by is not None and not isinstance(find_by, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: find_by EXPECTED TYPE: str', None, None)
		
		self.__find_by = find_by
		self.__key_modified['find_by'] = 1

	def get_default_value(self):
		"""
		The method to get the default_value

		Returns:
			DefaultValue: An instance of DefaultValue
		"""

		return self.__default_value

	def set_default_value(self, default_value):
		"""
		The method to set the value to default_value

		Parameters:
			default_value (DefaultValue) : An instance of DefaultValue
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.default_value import DefaultValue
		except Exception:
			from .default_value import DefaultValue

		if default_value is not None and not isinstance(default_value, DefaultValue):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_value EXPECTED TYPE: DefaultValue', None, None)
		
		self.__default_value = default_value
		self.__key_modified['default_value'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			string: A string representing the module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (string) : A string representing the module
		"""

		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_parent_column_index(self):
		"""
		The method to get the parent_column_index

		Returns:
			int: An int representing the parent_column_index
		"""

		return self.__parent_column_index

	def set_parent_column_index(self, parent_column_index):
		"""
		The method to set the value to parent_column_index

		Parameters:
			parent_column_index (int) : An int representing the parent_column_index
		"""

		if parent_column_index is not None and not isinstance(parent_column_index, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_column_index EXPECTED TYPE: int', None, None)
		
		self.__parent_column_index = parent_column_index
		self.__key_modified['parent_column_index'] = 1

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
