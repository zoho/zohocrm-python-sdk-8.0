try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ConvertTo(object):
	def __init__(self):
		"""Creates an instance of ConvertTo"""

		self.__module = None
		self.__carry_over_tags = None
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
			from zohocrmsdk.src.com.zoho.crm.api.inventory_convert.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_carry_over_tags(self):
		"""
		The method to get the carry_over_tags

		Returns:
			bool: A bool representing the carry_over_tags
		"""

		return self.__carry_over_tags

	def set_carry_over_tags(self, carry_over_tags):
		"""
		The method to set the value to carry_over_tags

		Parameters:
			carry_over_tags (bool) : A bool representing the carry_over_tags
		"""

		if carry_over_tags is not None and not isinstance(carry_over_tags, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: carry_over_tags EXPECTED TYPE: bool', None, None)
		
		self.__carry_over_tags = carry_over_tags
		self.__key_modified['carry_over_tags'] = 1

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
