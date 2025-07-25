try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Variable(object):
	def __init__(self):
		"""Creates an instance of Variable"""

		self.__api_name = None
		self.__name = None
		self.__description = None
		self.__source = None
		self.__id = None
		self.__type = None
		self.__variable_group = None
		self.__read_only = None
		self.__value = None
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

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

	def get_source(self):
		"""
		The method to get the source

		Returns:
			string: A string representing the source
		"""

		return self.__source

	def set_source(self, source):
		"""
		The method to set the value to source

		Parameters:
			source (string) : A string representing the source
		"""

		if source is not None and not isinstance(source, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: source EXPECTED TYPE: str', None, None)
		
		self.__source = source
		self.__key_modified['source'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (Choice) : An instance of Choice
		"""

		if type is not None and not isinstance(type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: Choice', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_variable_group(self):
		"""
		The method to get the variable_group

		Returns:
			VariableGroup: An instance of VariableGroup
		"""

		return self.__variable_group

	def set_variable_group(self, variable_group):
		"""
		The method to set the value to variable_group

		Parameters:
			variable_group (VariableGroup) : An instance of VariableGroup
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.variables.variable_group import VariableGroup
		except Exception:
			from .variable_group import VariableGroup

		if variable_group is not None and not isinstance(variable_group, VariableGroup):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: variable_group EXPECTED TYPE: VariableGroup', None, None)
		
		self.__variable_group = variable_group
		self.__key_modified['variable_group'] = 1

	def get_read_only(self):
		"""
		The method to get the read_only

		Returns:
			bool: A bool representing the read_only
		"""

		return self.__read_only

	def set_read_only(self, read_only):
		"""
		The method to set the value to read_only

		Parameters:
			read_only (bool) : A bool representing the read_only
		"""

		if read_only is not None and not isinstance(read_only, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: read_only EXPECTED TYPE: bool', None, None)
		
		self.__read_only = read_only
		self.__key_modified['read_only'] = 1

	def get_value(self):
		"""
		The method to get the value

		Returns:
			Object: A Object representing the value
		"""

		return self.__value

	def set_value(self, value):
		"""
		The method to set the value to value

		Parameters:
			value (Object) : A Object representing the value
		"""

		self.__value = value
		self.__key_modified['value'] = 1

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
