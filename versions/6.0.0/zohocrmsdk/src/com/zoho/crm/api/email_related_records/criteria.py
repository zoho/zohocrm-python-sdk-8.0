try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Criteria(object):
	def __init__(self):
		"""Creates an instance of Criteria"""

		self.__comparator = None
		self.__field = None
		self.__value = None
		self.__key_modified = dict()

	def get_comparator(self):
		"""
		The method to get the comparator

		Returns:
			Choice: An instance of Choice
		"""

		return self.__comparator

	def set_comparator(self, comparator):
		"""
		The method to set the value to comparator

		Parameters:
			comparator (Choice) : An instance of Choice
		"""

		if comparator is not None and not isinstance(comparator, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: comparator EXPECTED TYPE: Choice', None, None)
		
		self.__comparator = comparator
		self.__key_modified['comparator'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.email_related_records.field import Field
		except Exception:
			from .field import Field

		if field is not None and not isinstance(field, Field):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field EXPECTED TYPE: Field', None, None)
		
		self.__field = field
		self.__key_modified['field'] = 1

	def get_value(self):
		"""
		The method to get the value

		Returns:
			string: A string representing the value
		"""

		return self.__value

	def set_value(self, value):
		"""
		The method to set the value to value

		Parameters:
			value (string) : A string representing the value
		"""

		if value is not None and not isinstance(value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: value EXPECTED TYPE: str', None, None)
		
		self.__value = value
		self.__key_modified['value'] = 1

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
