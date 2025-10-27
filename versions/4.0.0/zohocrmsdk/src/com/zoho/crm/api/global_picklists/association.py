try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Association(object):
	def __init__(self):
		"""Creates an instance of Association"""

		self.__field = None
		self.__module = None
		self.__layouts = None
		self.__key_modified = dict()

	def get_field(self):
		"""
		The method to get the field

		Returns:
			Field: An instance of Field
		"""

		return self.__field

	def set_field(self, field):
		"""
		The method to set the value to field

		Parameters:
			field (Field) : An instance of Field
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.global_picklists.field import Field
		except Exception:
			from .field import Field

		if field is not None and not isinstance(field, Field):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field EXPECTED TYPE: Field', None, None)
		
		self.__field = field
		self.__key_modified['field'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.global_picklists.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_layouts(self):
		"""
		The method to get the layouts

		Returns:
			list: An instance of list
		"""

		return self.__layouts

	def set_layouts(self, layouts):
		"""
		The method to set the value to layouts

		Parameters:
			layouts (list) : An instance of list
		"""

		if layouts is not None and not isinstance(layouts, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layouts EXPECTED TYPE: list', None, None)
		
		self.__layouts = layouts
		self.__key_modified['layouts'] = 1

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
