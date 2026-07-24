try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class LinkingDetails(object):
	def __init__(self):
		"""Creates an instance of LinkingDetails"""

		self.__module = None
		self.__lookup_field = None
		self.__connected_lookup_field = None
		self.__key_modified = dict()

	def get_module(self):
		"""
		The method to get the module

		Returns:
			LinkingModule: An instance of LinkingModule
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (LinkingModule) : An instance of LinkingModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.linking_module import LinkingModule
		except Exception:
			from .linking_module import LinkingModule

		if module is not None and not isinstance(module, LinkingModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: LinkingModule', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_lookup_field(self):
		"""
		The method to get the lookup_field

		Returns:
			LookupField: An instance of LookupField
		"""

		return self.__lookup_field

	def set_lookup_field(self, lookup_field):
		"""
		The method to set the value to lookup_field

		Parameters:
			lookup_field (LookupField) : An instance of LookupField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.lookup_field import LookupField
		except Exception:
			from .lookup_field import LookupField

		if lookup_field is not None and not isinstance(lookup_field, LookupField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lookup_field EXPECTED TYPE: LookupField', None, None)
		
		self.__lookup_field = lookup_field
		self.__key_modified['lookup_field'] = 1

	def get_connected_lookup_field(self):
		"""
		The method to get the connected_lookup_field

		Returns:
			LookupField: An instance of LookupField
		"""

		return self.__connected_lookup_field

	def set_connected_lookup_field(self, connected_lookup_field):
		"""
		The method to set the value to connected_lookup_field

		Parameters:
			connected_lookup_field (LookupField) : An instance of LookupField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.lookup_field import LookupField
		except Exception:
			from .lookup_field import LookupField

		if connected_lookup_field is not None and not isinstance(connected_lookup_field, LookupField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: connected_lookup_field EXPECTED TYPE: LookupField', None, None)
		
		self.__connected_lookup_field = connected_lookup_field
		self.__key_modified['connected_lookup_field'] = 1

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
