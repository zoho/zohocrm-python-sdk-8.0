try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class TypeConfiguration(object):
	def __init__(self):
		"""Creates an instance of TypeConfiguration"""

		self.__field_mappings = None
		self.__mapped_module = None
		self.__key_modified = dict()

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

	def get_mapped_module(self):
		"""
		The method to get the mapped_module

		Returns:
			MappedModule: An instance of MappedModule
		"""

		return self.__mapped_module

	def set_mapped_module(self, mapped_module):
		"""
		The method to set the value to mapped_module

		Parameters:
			mapped_module (MappedModule) : An instance of MappedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.mapped_module import MappedModule
		except Exception:
			from .mapped_module import MappedModule

		if mapped_module is not None and not isinstance(mapped_module, MappedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mapped_module EXPECTED TYPE: MappedModule', None, None)
		
		self.__mapped_module = mapped_module
		self.__key_modified['mapped_module'] = 1

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
