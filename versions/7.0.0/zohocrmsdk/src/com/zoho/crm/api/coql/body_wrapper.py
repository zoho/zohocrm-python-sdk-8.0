try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__select_query = None
		self.__key_modified = dict()

	def get_select_query(self):
		"""
		The method to get the select_query

		Returns:
			string: A string representing the select_query
		"""

		return self.__select_query

	def set_select_query(self, select_query):
		"""
		The method to set the value to select_query

		Parameters:
			select_query (string) : A string representing the select_query
		"""

		if select_query is not None and not isinstance(select_query, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: select_query EXPECTED TYPE: str', None, None)
		
		self.__select_query = select_query
		self.__key_modified['select_query'] = 1

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
