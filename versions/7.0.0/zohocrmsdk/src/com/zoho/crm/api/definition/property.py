try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Property(object):
	def __init__(self):
		"""Creates an instance of Property"""

		self.__display_label = None
		self.__allowed_values = None
		self.__ui_type = None
		self.__regex = None
		self.__read_only = None
		self.__api_name = None
		self.__field_label = None
		self.__data_type = None
		self.__length = None
		self.__available_in_user_layout = None
		self.__required = None
		self.__properties = None
		self.__key_modified = dict()

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

	def get_allowed_values(self):
		"""
		The method to get the allowed_values

		Returns:
			list: An instance of list
		"""

		return self.__allowed_values

	def set_allowed_values(self, allowed_values):
		"""
		The method to set the value to allowed_values

		Parameters:
			allowed_values (list) : An instance of list
		"""

		if allowed_values is not None and not isinstance(allowed_values, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: allowed_values EXPECTED TYPE: list', None, None)
		
		self.__allowed_values = allowed_values
		self.__key_modified['allowed_values'] = 1

	def get_ui_type(self):
		"""
		The method to get the ui_type

		Returns:
			int: An int representing the ui_type
		"""

		return self.__ui_type

	def set_ui_type(self, ui_type):
		"""
		The method to set the value to ui_type

		Parameters:
			ui_type (int) : An int representing the ui_type
		"""

		if ui_type is not None and not isinstance(ui_type, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ui_type EXPECTED TYPE: int', None, None)
		
		self.__ui_type = ui_type
		self.__key_modified['ui_type'] = 1

	def get_regex(self):
		"""
		The method to get the regex

		Returns:
			string: A string representing the regex
		"""

		return self.__regex

	def set_regex(self, regex):
		"""
		The method to set the value to regex

		Parameters:
			regex (string) : A string representing the regex
		"""

		if regex is not None and not isinstance(regex, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: regex EXPECTED TYPE: str', None, None)
		
		self.__regex = regex
		self.__key_modified['regex'] = 1

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

	def get_field_label(self):
		"""
		The method to get the field_label

		Returns:
			string: A string representing the field_label
		"""

		return self.__field_label

	def set_field_label(self, field_label):
		"""
		The method to set the value to field_label

		Parameters:
			field_label (string) : A string representing the field_label
		"""

		if field_label is not None and not isinstance(field_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_label EXPECTED TYPE: str', None, None)
		
		self.__field_label = field_label
		self.__key_modified['field_label'] = 1

	def get_data_type(self):
		"""
		The method to get the data_type

		Returns:
			string: A string representing the data_type
		"""

		return self.__data_type

	def set_data_type(self, data_type):
		"""
		The method to set the value to data_type

		Parameters:
			data_type (string) : A string representing the data_type
		"""

		if data_type is not None and not isinstance(data_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_type EXPECTED TYPE: str', None, None)
		
		self.__data_type = data_type
		self.__key_modified['data_type'] = 1

	def get_length(self):
		"""
		The method to get the length

		Returns:
			int: An int representing the length
		"""

		return self.__length

	def set_length(self, length):
		"""
		The method to set the value to length

		Parameters:
			length (int) : An int representing the length
		"""

		if length is not None and not isinstance(length, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: length EXPECTED TYPE: int', None, None)
		
		self.__length = length
		self.__key_modified['length'] = 1

	def get_available_in_user_layout(self):
		"""
		The method to get the available_in_user_layout

		Returns:
			bool: A bool representing the available_in_user_layout
		"""

		return self.__available_in_user_layout

	def set_available_in_user_layout(self, available_in_user_layout):
		"""
		The method to set the value to available_in_user_layout

		Parameters:
			available_in_user_layout (bool) : A bool representing the available_in_user_layout
		"""

		if available_in_user_layout is not None and not isinstance(available_in_user_layout, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: available_in_user_layout EXPECTED TYPE: bool', None, None)
		
		self.__available_in_user_layout = available_in_user_layout
		self.__key_modified['available_in_user_layout'] = 1

	def get_required(self):
		"""
		The method to get the required

		Returns:
			bool: A bool representing the required
		"""

		return self.__required

	def set_required(self, required):
		"""
		The method to set the value to required

		Parameters:
			required (bool) : A bool representing the required
		"""

		if required is not None and not isinstance(required, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: required EXPECTED TYPE: bool', None, None)
		
		self.__required = required
		self.__key_modified['required'] = 1

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
