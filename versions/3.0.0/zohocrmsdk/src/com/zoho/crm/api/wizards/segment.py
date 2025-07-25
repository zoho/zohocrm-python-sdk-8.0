try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Segment(object):
	def __init__(self):
		"""Creates an instance of Segment"""

		self.__sequence_number = None
		self.__display_label = None
		self.__column_count = None
		self.__id = None
		self.__type = None
		self.__fields = None
		self.__buttons = None
		self.__elements = None
		self.__key_modified = dict()

	def get_sequence_number(self):
		"""
		The method to get the sequence_number

		Returns:
			int: An int representing the sequence_number
		"""

		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		"""
		The method to set the value to sequence_number

		Parameters:
			sequence_number (int) : An int representing the sequence_number
		"""

		if sequence_number is not None and not isinstance(sequence_number, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sequence_number EXPECTED TYPE: int', None, None)
		
		self.__sequence_number = sequence_number
		self.__key_modified['sequence_number'] = 1

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

	def get_column_count(self):
		"""
		The method to get the column_count

		Returns:
			int: An int representing the column_count
		"""

		return self.__column_count

	def set_column_count(self, column_count):
		"""
		The method to set the value to column_count

		Parameters:
			column_count (int) : An int representing the column_count
		"""

		if column_count is not None and not isinstance(column_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: column_count EXPECTED TYPE: int', None, None)
		
		self.__column_count = column_count
		self.__key_modified['column_count'] = 1

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

	def get_fields(self):
		"""
		The method to get the fields

		Returns:
			list: An instance of list
		"""

		return self.__fields

	def set_fields(self, fields):
		"""
		The method to set the value to fields

		Parameters:
			fields (list) : An instance of list
		"""

		if fields is not None and not isinstance(fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: list', None, None)
		
		self.__fields = fields
		self.__key_modified['fields'] = 1

	def get_buttons(self):
		"""
		The method to get the buttons

		Returns:
			list: An instance of list
		"""

		return self.__buttons

	def set_buttons(self, buttons):
		"""
		The method to set the value to buttons

		Parameters:
			buttons (list) : An instance of list
		"""

		if buttons is not None and not isinstance(buttons, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: buttons EXPECTED TYPE: list', None, None)
		
		self.__buttons = buttons
		self.__key_modified['buttons'] = 1

	def get_elements(self):
		"""
		The method to get the elements

		Returns:
			list: An instance of list
		"""

		return self.__elements

	def set_elements(self, elements):
		"""
		The method to set the value to elements

		Parameters:
			elements (list) : An instance of list
		"""

		if elements is not None and not isinstance(elements, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: elements EXPECTED TYPE: list', None, None)
		
		self.__elements = elements
		self.__key_modified['elements'] = 1

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
