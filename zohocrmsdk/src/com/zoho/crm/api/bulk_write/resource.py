try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Resource(object):
	def __init__(self):
		"""Creates an instance of Resource"""

		self.__status = None
		self.__type = None
		self.__module = None
		self.__code = None
		self.__file_id = None
		self.__file_names = None
		self.__ignore_empty = None
		self.__find_by = None
		self.__field_mappings = None
		self.__file = None
		self.__key_modified = dict()

	def get_status(self):
		"""
		The method to get the status

		Returns:
			Choice: An instance of Choice
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (Choice) : An instance of Choice
		"""

		if status is not None and not isinstance(status, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: Choice', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

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

	def get_module(self):
		"""
		The method to get the module

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
		except Exception:
			from ..modules import MinifiedModule

		if module is not None and not isinstance(module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_code(self):
		"""
		The method to get the code

		Returns:
			string: A string representing the code
		"""

		return self.__code

	def set_code(self, code):
		"""
		The method to set the value to code

		Parameters:
			code (string) : A string representing the code
		"""

		if code is not None and not isinstance(code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: code EXPECTED TYPE: str', None, None)
		
		self.__code = code
		self.__key_modified['code'] = 1

	def get_file_id(self):
		"""
		The method to get the file_id

		Returns:
			string: A string representing the file_id
		"""

		return self.__file_id

	def set_file_id(self, file_id):
		"""
		The method to set the value to file_id

		Parameters:
			file_id (string) : A string representing the file_id
		"""

		if file_id is not None and not isinstance(file_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_id EXPECTED TYPE: str', None, None)
		
		self.__file_id = file_id
		self.__key_modified['file_id'] = 1

	def get_file_names(self):
		"""
		The method to get the file_names

		Returns:
			list: An instance of list
		"""

		return self.__file_names

	def set_file_names(self, file_names):
		"""
		The method to set the value to file_names

		Parameters:
			file_names (list) : An instance of list
		"""

		if file_names is not None and not isinstance(file_names, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_names EXPECTED TYPE: list', None, None)
		
		self.__file_names = file_names
		self.__key_modified['file_names'] = 1

	def get_ignore_empty(self):
		"""
		The method to get the ignore_empty

		Returns:
			bool: A bool representing the ignore_empty
		"""

		return self.__ignore_empty

	def set_ignore_empty(self, ignore_empty):
		"""
		The method to set the value to ignore_empty

		Parameters:
			ignore_empty (bool) : A bool representing the ignore_empty
		"""

		if ignore_empty is not None and not isinstance(ignore_empty, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ignore_empty EXPECTED TYPE: bool', None, None)
		
		self.__ignore_empty = ignore_empty
		self.__key_modified['ignore_empty'] = 1

	def get_find_by(self):
		"""
		The method to get the find_by

		Returns:
			string: A string representing the find_by
		"""

		return self.__find_by

	def set_find_by(self, find_by):
		"""
		The method to set the value to find_by

		Parameters:
			find_by (string) : A string representing the find_by
		"""

		if find_by is not None and not isinstance(find_by, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: find_by EXPECTED TYPE: str', None, None)
		
		self.__find_by = find_by
		self.__key_modified['find_by'] = 1

	def get_field_mappings(self):
		"""
		The method to get the field_mappings

		Returns:
			list: An instance of list
		"""

		return self.__field_mappings

	def set_field_mappings(self, field_mappings):
		"""
		The method to set the value to field_mappings

		Parameters:
			field_mappings (list) : An instance of list
		"""

		if field_mappings is not None and not isinstance(field_mappings, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_mappings EXPECTED TYPE: list', None, None)
		
		self.__field_mappings = field_mappings
		self.__key_modified['field_mappings'] = 1

	def get_file(self):
		"""
		The method to get the file

		Returns:
			File: An instance of File
		"""

		return self.__file

	def set_file(self, file):
		"""
		The method to set the value to file

		Parameters:
			file (File) : An instance of File
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.file import File
		except Exception:
			from .file import File

		if file is not None and not isinstance(file, File):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file EXPECTED TYPE: File', None, None)
		
		self.__file = file
		self.__key_modified['file'] = 1

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
