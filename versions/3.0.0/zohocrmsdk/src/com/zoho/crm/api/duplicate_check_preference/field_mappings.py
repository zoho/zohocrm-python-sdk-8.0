try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FieldMappings(object):
	def __init__(self):
		"""Creates an instance of FieldMappings"""

		self.__current_field = None
		self.__mapped_field = None
		self.__key_modified = dict()

	def get_current_field(self):
		"""
		The method to get the current_field

		Returns:
			CurrentField: An instance of CurrentField
		"""

		return self.__current_field

	def set_current_field(self, current_field):
		"""
		The method to set the value to current_field

		Parameters:
			current_field (CurrentField) : An instance of CurrentField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.current_field import CurrentField
		except Exception:
			from .current_field import CurrentField

		if current_field is not None and not isinstance(current_field, CurrentField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: current_field EXPECTED TYPE: CurrentField', None, None)
		
		self.__current_field = current_field
		self.__key_modified['current_field'] = 1

	def get_mapped_field(self):
		"""
		The method to get the mapped_field

		Returns:
			MappedField: An instance of MappedField
		"""

		return self.__mapped_field

	def set_mapped_field(self, mapped_field):
		"""
		The method to set the value to mapped_field

		Parameters:
			mapped_field (MappedField) : An instance of MappedField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.duplicate_check_preference.mapped_field import MappedField
		except Exception:
			from .mapped_field import MappedField

		if mapped_field is not None and not isinstance(mapped_field, MappedField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mapped_field EXPECTED TYPE: MappedField', None, None)
		
		self.__mapped_field = mapped_field
		self.__key_modified['mapped_field'] = 1

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
