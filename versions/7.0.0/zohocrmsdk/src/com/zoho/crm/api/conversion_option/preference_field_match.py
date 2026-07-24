try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class PreferenceFieldMatch(object):
	def __init__(self):
		"""Creates an instance of PreferenceFieldMatch"""

		self.__field = None
		self.__matched_lead_value = None
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
			from zohocrmsdk.src.com.zoho.crm.api.conversion_option.field import Field
		except Exception:
			from .field import Field

		if field is not None and not isinstance(field, Field):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field EXPECTED TYPE: Field', None, None)
		
		self.__field = field
		self.__key_modified['field'] = 1

	def get_matched_lead_value(self):
		"""
		The method to get the matched_lead_value

		Returns:
			string: A string representing the matched_lead_value
		"""

		return self.__matched_lead_value

	def set_matched_lead_value(self, matched_lead_value):
		"""
		The method to set the value to matched_lead_value

		Parameters:
			matched_lead_value (string) : A string representing the matched_lead_value
		"""

		if matched_lead_value is not None and not isinstance(matched_lead_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: matched_lead_value EXPECTED TYPE: str', None, None)
		
		self.__matched_lead_value = matched_lead_value
		self.__key_modified['matched_lead_value'] = 1

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
