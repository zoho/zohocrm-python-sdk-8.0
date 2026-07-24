try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Sections(object):
	def __init__(self):
		"""Creates an instance of Sections"""

		self.__display_label = None
		self.__sequence_number = None
		self.__actions_allowed = None
		self.__issubformsection = None
		self.__tab_traversal = None
		self.__api_name = None
		self.__column_count = None
		self.__name = None
		self.__generated_type = None
		self.__id = None
		self.__type = None
		self.__fields = None
		self.__properties = None
		self.__delete = None
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

	def get_actions_allowed(self):
		"""
		The method to get the actions_allowed

		Returns:
			ActionsAllowed: An instance of ActionsAllowed
		"""

		return self.__actions_allowed

	def set_actions_allowed(self, actions_allowed):
		"""
		The method to set the value to actions_allowed

		Parameters:
			actions_allowed (ActionsAllowed) : An instance of ActionsAllowed
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.actions_allowed import ActionsAllowed
		except Exception:
			from .actions_allowed import ActionsAllowed

		if actions_allowed is not None and not isinstance(actions_allowed, ActionsAllowed):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actions_allowed EXPECTED TYPE: ActionsAllowed', None, None)
		
		self.__actions_allowed = actions_allowed
		self.__key_modified['actions_allowed'] = 1

	def get_issubformsection(self):
		"""
		The method to get the issubformsection

		Returns:
			bool: A bool representing the issubformsection
		"""

		return self.__issubformsection

	def set_issubformsection(self, issubformsection):
		"""
		The method to set the value to issubformsection

		Parameters:
			issubformsection (bool) : A bool representing the issubformsection
		"""

		if issubformsection is not None and not isinstance(issubformsection, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: issubformsection EXPECTED TYPE: bool', None, None)
		
		self.__issubformsection = issubformsection
		self.__key_modified['isSubformSection'] = 1

	def get_tab_traversal(self):
		"""
		The method to get the tab_traversal

		Returns:
			string: A string representing the tab_traversal
		"""

		return self.__tab_traversal

	def set_tab_traversal(self, tab_traversal):
		"""
		The method to set the value to tab_traversal

		Parameters:
			tab_traversal (string) : A string representing the tab_traversal
		"""

		if tab_traversal is not None and not isinstance(tab_traversal, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tab_traversal EXPECTED TYPE: str', None, None)
		
		self.__tab_traversal = tab_traversal
		self.__key_modified['tab_traversal'] = 1

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

	def get_generated_type(self):
		"""
		The method to get the generated_type

		Returns:
			string: A string representing the generated_type
		"""

		return self.__generated_type

	def set_generated_type(self, generated_type):
		"""
		The method to set the value to generated_type

		Parameters:
			generated_type (string) : A string representing the generated_type
		"""

		if generated_type is not None and not isinstance(generated_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: generated_type EXPECTED TYPE: str', None, None)
		
		self.__generated_type = generated_type
		self.__key_modified['generated_type'] = 1

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

	def get_properties(self):
		"""
		The method to get the properties

		Returns:
			Properties: An instance of Properties
		"""

		return self.__properties

	def set_properties(self, properties):
		"""
		The method to set the value to properties

		Parameters:
			properties (Properties) : An instance of Properties
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.properties import Properties
		except Exception:
			from .properties import Properties

		if properties is not None and not isinstance(properties, Properties):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: properties EXPECTED TYPE: Properties', None, None)
		
		self.__properties = properties
		self.__key_modified['properties'] = 1

	def get_delete(self):
		"""
		The method to get the delete

		Returns:
			Delete1: An instance of Delete1
		"""

		return self.__delete

	def set_delete(self, delete):
		"""
		The method to set the value to delete

		Parameters:
			delete (Delete1) : An instance of Delete1
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.delete1 import Delete1
		except Exception:
			from .delete1 import Delete1

		if delete is not None and not isinstance(delete, Delete1):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delete EXPECTED TYPE: Delete1', None, None)
		
		self.__delete = delete
		self.__key_modified['_delete'] = 1

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
