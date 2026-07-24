try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Transition(object):
	def __init__(self):
		"""Creates an instance of Transition"""

		self.__type = None
		self.__execution_time = None
		self.__sequence = None
		self.__next_transitions = None
		self.__parent_transition = None
		self.__percent_partial_save = None
		self.__data = None
		self.__next_field_value = None
		self.__text_color_code = None
		self.__name = None
		self.__criteria_matched = None
		self.__id = None
		self.__fields = None
		self.__color_code = None
		self.__criteria_message = None
		self.__key_modified = dict()

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

	def get_execution_time(self):
		"""
		The method to get the execution_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__execution_time

	def set_execution_time(self, execution_time):
		"""
		The method to set the value to execution_time

		Parameters:
			execution_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if execution_time is not None and not isinstance(execution_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: execution_time EXPECTED TYPE: datetime', None, None)
		
		self.__execution_time = execution_time
		self.__key_modified['execution_time'] = 1

	def get_sequence(self):
		"""
		The method to get the sequence

		Returns:
			int: An int representing the sequence
		"""

		return self.__sequence

	def set_sequence(self, sequence):
		"""
		The method to set the value to sequence

		Parameters:
			sequence (int) : An int representing the sequence
		"""

		if sequence is not None and not isinstance(sequence, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sequence EXPECTED TYPE: int', None, None)
		
		self.__sequence = sequence
		self.__key_modified['sequence'] = 1

	def get_next_transitions(self):
		"""
		The method to get the next_transitions

		Returns:
			list: An instance of list
		"""

		return self.__next_transitions

	def set_next_transitions(self, next_transitions):
		"""
		The method to set the value to next_transitions

		Parameters:
			next_transitions (list) : An instance of list
		"""

		if next_transitions is not None and not isinstance(next_transitions, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: next_transitions EXPECTED TYPE: list', None, None)
		
		self.__next_transitions = next_transitions
		self.__key_modified['next_transitions'] = 1

	def get_parent_transition(self):
		"""
		The method to get the parent_transition

		Returns:
			Transition: An instance of Transition
		"""

		return self.__parent_transition

	def set_parent_transition(self, parent_transition):
		"""
		The method to set the value to parent_transition

		Parameters:
			parent_transition (Transition) : An instance of Transition
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.transition import Transition
		except Exception:
			from .transition import Transition

		if parent_transition is not None and not isinstance(parent_transition, Transition):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_transition EXPECTED TYPE: Transition', None, None)
		
		self.__parent_transition = parent_transition
		self.__key_modified['parent_transition'] = 1

	def get_percent_partial_save(self):
		"""
		The method to get the percent_partial_save

		Returns:
			float: A float representing the percent_partial_save
		"""

		return self.__percent_partial_save

	def set_percent_partial_save(self, percent_partial_save):
		"""
		The method to set the value to percent_partial_save

		Parameters:
			percent_partial_save (float) : A float representing the percent_partial_save
		"""

		if percent_partial_save is not None and not isinstance(percent_partial_save, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: percent_partial_save EXPECTED TYPE: float', None, None)
		
		self.__percent_partial_save = percent_partial_save
		self.__key_modified['percent_partial_save'] = 1

	def get_data(self):
		"""
		The method to get the data

		Returns:
			Record: An instance of Record
		"""

		return self.__data

	def set_data(self, data):
		"""
		The method to set the value to data

		Parameters:
			data (Record) : An instance of Record
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record import Record
		except Exception:
			from ..record import Record

		if data is not None and not isinstance(data, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data EXPECTED TYPE: Record', None, None)
		
		self.__data = data
		self.__key_modified['data'] = 1

	def get_next_field_value(self):
		"""
		The method to get the next_field_value

		Returns:
			string: A string representing the next_field_value
		"""

		return self.__next_field_value

	def set_next_field_value(self, next_field_value):
		"""
		The method to set the value to next_field_value

		Parameters:
			next_field_value (string) : A string representing the next_field_value
		"""

		if next_field_value is not None and not isinstance(next_field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: next_field_value EXPECTED TYPE: str', None, None)
		
		self.__next_field_value = next_field_value
		self.__key_modified['next_field_value'] = 1

	def get_text_color_code(self):
		"""
		The method to get the text_color_code

		Returns:
			string: A string representing the text_color_code
		"""

		return self.__text_color_code

	def set_text_color_code(self, text_color_code):
		"""
		The method to set the value to text_color_code

		Parameters:
			text_color_code (string) : A string representing the text_color_code
		"""

		if text_color_code is not None and not isinstance(text_color_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: text_color_code EXPECTED TYPE: str', None, None)
		
		self.__text_color_code = text_color_code
		self.__key_modified['text_color_code'] = 1

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

	def get_criteria_matched(self):
		"""
		The method to get the criteria_matched

		Returns:
			bool: A bool representing the criteria_matched
		"""

		return self.__criteria_matched

	def set_criteria_matched(self, criteria_matched):
		"""
		The method to set the value to criteria_matched

		Parameters:
			criteria_matched (bool) : A bool representing the criteria_matched
		"""

		if criteria_matched is not None and not isinstance(criteria_matched, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria_matched EXPECTED TYPE: bool', None, None)
		
		self.__criteria_matched = criteria_matched
		self.__key_modified['criteria_matched'] = 1

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

	def get_color_code(self):
		"""
		The method to get the color_code

		Returns:
			string: A string representing the color_code
		"""

		return self.__color_code

	def set_color_code(self, color_code):
		"""
		The method to set the value to color_code

		Parameters:
			color_code (string) : A string representing the color_code
		"""

		if color_code is not None and not isinstance(color_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: color_code EXPECTED TYPE: str', None, None)
		
		self.__color_code = color_code
		self.__key_modified['color_code'] = 1

	def get_criteria_message(self):
		"""
		The method to get the criteria_message

		Returns:
			string: A string representing the criteria_message
		"""

		return self.__criteria_message

	def set_criteria_message(self, criteria_message):
		"""
		The method to set the value to criteria_message

		Parameters:
			criteria_message (string) : A string representing the criteria_message
		"""

		if criteria_message is not None and not isinstance(criteria_message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria_message EXPECTED TYPE: str', None, None)
		
		self.__criteria_message = criteria_message
		self.__key_modified['criteria_message'] = 1

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
