try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ResponseWrapper(object):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""

		self.__allowed_field_mappings = None
		self.__key_modified = dict()

	def get_allowed_field_mappings(self):
		"""
		The method to get the allowed_field_mappings

		Returns:
			AllowedFieldMap: An instance of AllowedFieldMap
		"""

		return self.__allowed_field_mappings

	def set_allowed_field_mappings(self, allowed_field_mappings):
		"""
		The method to set the value to allowed_field_mappings

		Parameters:
			allowed_field_mappings (AllowedFieldMap) : An instance of AllowedFieldMap
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_allowed_field_mappings.allowed_field_map import AllowedFieldMap
		except Exception:
			from .allowed_field_map import AllowedFieldMap

		if allowed_field_mappings is not None and not isinstance(allowed_field_mappings, AllowedFieldMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: allowed_field_mappings EXPECTED TYPE: AllowedFieldMap', None, None)
		
		self.__allowed_field_mappings = allowed_field_mappings
		self.__key_modified['allowed_field_mappings'] = 1

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
