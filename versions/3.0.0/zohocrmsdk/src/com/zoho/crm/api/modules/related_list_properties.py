try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class RelatedListProperties(object):
	def __init__(self):
		"""Creates an instance of RelatedListProperties"""

		self.__sort_by = None
		self.__fields = None
		self.__sort_order = None
		self.__key_modified = dict()

	def get_sort_by(self):
		"""
		The method to get the sort_by

		Returns:
			MinifiedField: An instance of MinifiedField
		"""

		return self.__sort_by

	def set_sort_by(self, sort_by):
		"""
		The method to set the value to sort_by

		Parameters:
			sort_by (MinifiedField) : An instance of MinifiedField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import MinifiedField
		except Exception:
			from ..fields import MinifiedField

		if sort_by is not None and not isinstance(sort_by, MinifiedField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_by EXPECTED TYPE: MinifiedField', None, None)
		
		self.__sort_by = sort_by
		self.__key_modified['sort_by'] = 1

	def get_fields(self):
		"""
		The method to get the fields

		Returns:
			list: An instance of list
		"""

		return self.__fields

	def set_fields(self, fields):
		"""
		The method to set the value to fields

		Parameters:
			fields (list) : An instance of list
		"""

		if fields is not None and not isinstance(fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: list', None, None)
		
		self.__fields = fields
		self.__key_modified['fields'] = 1

	def get_sort_order(self):
		"""
		The method to get the sort_order

		Returns:
			string: A string representing the sort_order
		"""

		return self.__sort_order

	def set_sort_order(self, sort_order):
		"""
		The method to set the value to sort_order

		Parameters:
			sort_order (string) : A string representing the sort_order
		"""

		if sort_order is not None and not isinstance(sort_order, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_order EXPECTED TYPE: str', None, None)
		
		self.__sort_order = sort_order
		self.__key_modified['sort_order'] = 1

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
