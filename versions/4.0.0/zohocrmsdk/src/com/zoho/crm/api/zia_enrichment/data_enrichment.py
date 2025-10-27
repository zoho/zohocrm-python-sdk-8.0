try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class DataEnrichment(object):
	def __init__(self):
		"""Creates an instance of DataEnrichment"""

		self.__module = None
		self.__type = None
		self.__output_data_field_mapping = None
		self.__input_data_field_mapping = None
		self.__id = None
		self.__status = None
		self.__created_time = None
		self.__created_by = None
		self.__modified_time = None
		self.__modified_by = None
		self.__key_modified = dict()

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Module: An instance of Module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Module) : An instance of Module
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_enrichment.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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

	def get_output_data_field_mapping(self):
		"""
		The method to get the output_data_field_mapping

		Returns:
			list: An instance of list
		"""

		return self.__output_data_field_mapping

	def set_output_data_field_mapping(self, output_data_field_mapping):
		"""
		The method to set the value to output_data_field_mapping

		Parameters:
			output_data_field_mapping (list) : An instance of list
		"""

		if output_data_field_mapping is not None and not isinstance(output_data_field_mapping, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: output_data_field_mapping EXPECTED TYPE: list', None, None)
		
		self.__output_data_field_mapping = output_data_field_mapping
		self.__key_modified['output_data_field_mapping'] = 1

	def get_input_data_field_mapping(self):
		"""
		The method to get the input_data_field_mapping

		Returns:
			list: An instance of list
		"""

		return self.__input_data_field_mapping

	def set_input_data_field_mapping(self, input_data_field_mapping):
		"""
		The method to set the value to input_data_field_mapping

		Parameters:
			input_data_field_mapping (list) : An instance of list
		"""

		if input_data_field_mapping is not None and not isinstance(input_data_field_mapping, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: input_data_field_mapping EXPECTED TYPE: list', None, None)
		
		self.__input_data_field_mapping = input_data_field_mapping
		self.__key_modified['input_data_field_mapping'] = 1

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

	def get_status(self):
		"""
		The method to get the status

		Returns:
			bool: A bool representing the status
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (bool) : A bool representing the status
		"""

		if status is not None and not isinstance(status, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: bool', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			User: An instance of User
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_enrichment.user import User
		except Exception:
			from .user import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			User: An instance of User
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_enrichment.user import User
		except Exception:
			from .user import User

		if modified_by is not None and not isinstance(modified_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: User', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

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
