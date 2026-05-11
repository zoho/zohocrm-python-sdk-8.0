try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ProcessInfo(object):
	def __init__(self):
		"""Creates an instance of ProcessInfo"""

		self.__field_id = None
		self.__is_continuous = None
		self.__api_name = None
		self.__continuous = None
		self.__field_label = None
		self.__name = None
		self.__column_name = None
		self.__field_value = None
		self.__id = None
		self.__field_name = None
		self.__escalation = None
		self.__current_picklist = None
		self.__key_modified = dict()

	def get_field_id(self):
		"""
		The method to get the field_id

		Returns:
			int: An int representing the field_id
		"""

		return self.__field_id

	def set_field_id(self, field_id):
		"""
		The method to set the value to field_id

		Parameters:
			field_id (int) : An int representing the field_id
		"""

		if field_id is not None and not isinstance(field_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_id EXPECTED TYPE: int', None, None)
		
		self.__field_id = field_id
		self.__key_modified['field_id'] = 1

	def get_is_continuous(self):
		"""
		The method to get the is_continuous

		Returns:
			bool: A bool representing the is_continuous
		"""

		return self.__is_continuous

	def set_is_continuous(self, is_continuous):
		"""
		The method to set the value to is_continuous

		Parameters:
			is_continuous (bool) : A bool representing the is_continuous
		"""

		if is_continuous is not None and not isinstance(is_continuous, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: is_continuous EXPECTED TYPE: bool', None, None)
		
		self.__is_continuous = is_continuous
		self.__key_modified['is_continuous'] = 1

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

	def get_continuous(self):
		"""
		The method to get the continuous

		Returns:
			bool: A bool representing the continuous
		"""

		return self.__continuous

	def set_continuous(self, continuous):
		"""
		The method to set the value to continuous

		Parameters:
			continuous (bool) : A bool representing the continuous
		"""

		if continuous is not None and not isinstance(continuous, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: continuous EXPECTED TYPE: bool', None, None)
		
		self.__continuous = continuous
		self.__key_modified['continuous'] = 1

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

	def get_column_name(self):
		"""
		The method to get the column_name

		Returns:
			string: A string representing the column_name
		"""

		return self.__column_name

	def set_column_name(self, column_name):
		"""
		The method to set the value to column_name

		Parameters:
			column_name (string) : A string representing the column_name
		"""

		if column_name is not None and not isinstance(column_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: column_name EXPECTED TYPE: str', None, None)
		
		self.__column_name = column_name
		self.__key_modified['column_name'] = 1

	def get_field_value(self):
		"""
		The method to get the field_value

		Returns:
			string: A string representing the field_value
		"""

		return self.__field_value

	def set_field_value(self, field_value):
		"""
		The method to set the value to field_value

		Parameters:
			field_value (string) : A string representing the field_value
		"""

		if field_value is not None and not isinstance(field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_value EXPECTED TYPE: str', None, None)
		
		self.__field_value = field_value
		self.__key_modified['field_value'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string representing the id
		"""

		if id is not None and not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_field_name(self):
		"""
		The method to get the field_name

		Returns:
			string: A string representing the field_name
		"""

		return self.__field_name

	def set_field_name(self, field_name):
		"""
		The method to set the value to field_name

		Parameters:
			field_name (string) : A string representing the field_name
		"""

		if field_name is not None and not isinstance(field_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_name EXPECTED TYPE: str', None, None)
		
		self.__field_name = field_name
		self.__key_modified['field_name'] = 1

	def get_escalation(self):
		"""
		The method to get the escalation

		Returns:
			Escalation: An instance of Escalation
		"""

		return self.__escalation

	def set_escalation(self, escalation):
		"""
		The method to set the value to escalation

		Parameters:
			escalation (Escalation) : An instance of Escalation
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.escalation import Escalation
		except Exception:
			from .escalation import Escalation

		if escalation is not None and not isinstance(escalation, Escalation):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: escalation EXPECTED TYPE: Escalation', None, None)
		
		self.__escalation = escalation
		self.__key_modified['escalation'] = 1

	def get_current_picklist(self):
		"""
		The method to get the current_picklist

		Returns:
			CurrentPicklist: An instance of CurrentPicklist
		"""

		return self.__current_picklist

	def set_current_picklist(self, current_picklist):
		"""
		The method to set the value to current_picklist

		Parameters:
			current_picklist (CurrentPicklist) : An instance of CurrentPicklist
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.current_picklist import CurrentPicklist
		except Exception:
			from .current_picklist import CurrentPicklist

		if current_picklist is not None and not isinstance(current_picklist, CurrentPicklist):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: current_picklist EXPECTED TYPE: CurrentPicklist', None, None)
		
		self.__current_picklist = current_picklist
		self.__key_modified['current_picklist'] = 1

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
