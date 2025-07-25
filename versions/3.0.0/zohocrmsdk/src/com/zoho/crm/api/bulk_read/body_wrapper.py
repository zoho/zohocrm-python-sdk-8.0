try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__callback = None
		self.__query = None
		self.__file_type = None
		self.__key_modified = dict()

	def get_callback(self):
		"""
		The method to get the callback

		Returns:
			CallBack: An instance of CallBack
		"""

		return self.__callback

	def set_callback(self, callback):
		"""
		The method to set the value to callback

		Parameters:
			callback (CallBack) : An instance of CallBack
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_read.call_back import CallBack
		except Exception:
			from .call_back import CallBack

		if callback is not None and not isinstance(callback, CallBack):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: callback EXPECTED TYPE: CallBack', None, None)
		
		self.__callback = callback
		self.__key_modified['callback'] = 1

	def get_query(self):
		"""
		The method to get the query

		Returns:
			Query: An instance of Query
		"""

		return self.__query

	def set_query(self, query):
		"""
		The method to set the value to query

		Parameters:
			query (Query) : An instance of Query
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_read.query import Query
		except Exception:
			from .query import Query

		if query is not None and not isinstance(query, Query):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: query EXPECTED TYPE: Query', None, None)
		
		self.__query = query
		self.__key_modified['query'] = 1

	def get_file_type(self):
		"""
		The method to get the file_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__file_type

	def set_file_type(self, file_type):
		"""
		The method to set the value to file_type

		Parameters:
			file_type (Choice) : An instance of Choice
		"""

		if file_type is not None and not isinstance(file_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_type EXPECTED TYPE: Choice', None, None)
		
		self.__file_type = file_type
		self.__key_modified['file_type'] = 1

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
