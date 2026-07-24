try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class ConfigurationOptions(object):
	def __init__(self):
		"""Creates an instance of ConfigurationOptions"""

		self.__name = None
		self.__values = None
		self.__data_type = None
		self.__properties = None
		self.__key_modified = dict()

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_values(self):
		"""
		The method to get the values

		Returns:
			list: An instance of list
		"""

		return self.__values

	def set_values(self, values):
		"""
		The method to set the value to values

		Parameters:
			values (list) : An instance of list
		"""

		if values is not None and not isinstance(values, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: values EXPECTED TYPE: list', None, None)
		
		self.__values = values
		self.__key_modified['values'] = 1

	def get_data_type(self):
		"""
		The method to get the data_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__data_type

	def set_data_type(self, data_type):
		"""
		The method to set the value to data_type

		Parameters:
			data_type (Choice) : An instance of Choice
		"""

		if data_type is not None and not isinstance(data_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_type EXPECTED TYPE: Choice', None, None)
		
		self.__data_type = data_type
		self.__key_modified['data_type'] = 1

	def get_properties(self):
		"""
		The method to get the properties

		Returns:
			list: An instance of list
		"""

		return self.__properties

	def set_properties(self, properties):
		"""
		The method to set the value to properties

		Parameters:
			properties (list) : An instance of list
		"""

		if properties is not None and not isinstance(properties, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: properties EXPECTED TYPE: list', None, None)
		
		self.__properties = properties
		self.__key_modified['properties'] = 1

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
