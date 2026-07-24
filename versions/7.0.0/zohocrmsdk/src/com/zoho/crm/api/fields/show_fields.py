try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ShowFields(object):
	def __init__(self):
		"""Creates an instance of ShowFields"""

		self.__show_data = None
		self.__field = None
		self.__key_modified = dict()

	def get_show_data(self):
		"""
		The method to get the show_data

		Returns:
			bool: A bool representing the show_data
		"""

		return self.__show_data

	def set_show_data(self, show_data):
		"""
		The method to set the value to show_data

		Parameters:
			show_data (bool) : A bool representing the show_data
		"""

		if show_data is not None and not isinstance(show_data, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_data EXPECTED TYPE: bool', None, None)
		
		self.__show_data = show_data
		self.__key_modified['show_data'] = 1

	def get_field(self):
		"""
		The method to get the field

		Returns:
			MinifiedField: An instance of MinifiedField
		"""

		return self.__field

	def set_field(self, field):
		"""
		The method to set the value to field

		Parameters:
			field (MinifiedField) : An instance of MinifiedField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.minified_field import MinifiedField
		except Exception:
			from .minified_field import MinifiedField

		if field is not None and not isinstance(field, MinifiedField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field EXPECTED TYPE: MinifiedField', None, None)
		
		self.__field = field
		self.__key_modified['field'] = 1

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
