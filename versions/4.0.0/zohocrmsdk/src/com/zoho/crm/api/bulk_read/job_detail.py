try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class JobDetail(object):
	def __init__(self):
		"""Creates an instance of JobDetail"""

		self.__id = None
		self.__operation = None
		self.__state = None
		self.__query = None
		self.__created_by = None
		self.__created_time = None
		self.__result = None
		self.__file_type = None
		self.__key_modified = dict()

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string representing the id
		"""

		if id is not None and not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_operation(self):
		"""
		The method to get the operation

		Returns:
			string: A string representing the operation
		"""

		return self.__operation

	def set_operation(self, operation):
		"""
		The method to set the value to operation

		Parameters:
			operation (string) : A string representing the operation
		"""

		if operation is not None and not isinstance(operation, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: operation EXPECTED TYPE: str', None, None)
		
		self.__operation = operation
		self.__key_modified['operation'] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			Choice: An instance of Choice
		"""

		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (Choice) : An instance of Choice
		"""

		if state is not None and not isinstance(state, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: Choice', None, None)
		
		self.__state = state
		self.__key_modified['state'] = 1

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

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if created_by is not None and not isinstance(created_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_result(self):
		"""
		The method to get the result

		Returns:
			Result: An instance of Result
		"""

		return self.__result

	def set_result(self, result):
		"""
		The method to set the value to result

		Parameters:
			result (Result) : An instance of Result
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_read.result import Result
		except Exception:
			from .result import Result

		if result is not None and not isinstance(result, Result):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: result EXPECTED TYPE: Result', None, None)
		
		self.__result = result
		self.__key_modified['result'] = 1

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
