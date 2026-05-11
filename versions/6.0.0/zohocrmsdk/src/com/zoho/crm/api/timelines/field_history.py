try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FieldHistory(object):
	def __init__(self):
		"""Creates an instance of FieldHistory"""

		self.__data_type = None
		self.__enable_colour_code = None
		self.__pick_list_values = None
		self.__field_label = None
		self.__api_name = None
		self.__id = None
		self.__value = None
		self.__key_modified = dict()

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

	def get_enable_colour_code(self):
		"""
		The method to get the enable_colour_code

		Returns:
			bool: A bool representing the enable_colour_code
		"""

		return self.__enable_colour_code

	def set_enable_colour_code(self, enable_colour_code):
		"""
		The method to set the value to enable_colour_code

		Parameters:
			enable_colour_code (bool) : A bool representing the enable_colour_code
		"""

		if enable_colour_code is not None and not isinstance(enable_colour_code, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enable_colour_code EXPECTED TYPE: bool', None, None)
		
		self.__enable_colour_code = enable_colour_code
		self.__key_modified['enable_colour_code'] = 1

	def get_pick_list_values(self):
		"""
		The method to get the pick_list_values

		Returns:
			list: An instance of list
		"""

		return self.__pick_list_values

	def set_pick_list_values(self, pick_list_values):
		"""
		The method to set the value to pick_list_values

		Parameters:
			pick_list_values (list) : An instance of list
		"""

		if pick_list_values is not None and not isinstance(pick_list_values, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pick_list_values EXPECTED TYPE: list', None, None)
		
		self.__pick_list_values = pick_list_values
		self.__key_modified['pick_list_values'] = 1

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

	def get_value(self):
		"""
		The method to get the value

		Returns:
			FieldHistoryValue: An instance of FieldHistoryValue
		"""

		return self.__value

	def set_value(self, value):
		"""
		The method to set the value to value

		Parameters:
			value (FieldHistoryValue) : An instance of FieldHistoryValue
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.field_history_value import FieldHistoryValue
		except Exception:
			from .field_history_value import FieldHistoryValue

		if value is not None and not isinstance(value, FieldHistoryValue):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: value EXPECTED TYPE: FieldHistoryValue', None, None)
		
		self.__value = value
		self.__key_modified['_value'] = 1

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
