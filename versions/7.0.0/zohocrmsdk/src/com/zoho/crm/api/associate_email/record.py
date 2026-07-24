try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Record(object):
	def __init__(self):
		"""Creates an instance of Record"""

		self.__module = None
		self.__id = None
		self.__linked_record = None
		self.__key_modified = dict()

	def get_module(self):
		"""
		The method to get the module

		Returns:
			ModuleMap: An instance of ModuleMap
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (ModuleMap) : An instance of ModuleMap
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.associate_email.module_map import ModuleMap
		except Exception:
			from .module_map import ModuleMap

		if module is not None and not isinstance(module, ModuleMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: ModuleMap', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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

	def get_linked_record(self):
		"""
		The method to get the linked_record

		Returns:
			LinkedRecord: An instance of LinkedRecord
		"""

		return self.__linked_record

	def set_linked_record(self, linked_record):
		"""
		The method to set the value to linked_record

		Parameters:
			linked_record (LinkedRecord) : An instance of LinkedRecord
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.associate_email.linked_record import LinkedRecord
		except Exception:
			from .linked_record import LinkedRecord

		if linked_record is not None and not isinstance(linked_record, LinkedRecord):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: linked_record EXPECTED TYPE: LinkedRecord', None, None)
		
		self.__linked_record = linked_record
		self.__key_modified['linked_record'] = 1

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
