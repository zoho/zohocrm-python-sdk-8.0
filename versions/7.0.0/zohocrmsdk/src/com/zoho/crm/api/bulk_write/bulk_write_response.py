try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.bulk_write.response_wrapper import ResponseWrapper
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_wrapper import ResponseWrapper


class BulkWriteResponse(ResponseWrapper):
	def __init__(self):
		"""Creates an instance of BulkWriteResponse"""
		super().__init__()

		self.__status = None
		self.__character_encoding = None
		self.__resource = None
		self.__id = None
		self.__result = None
		self.__created_by = None
		self.__operation = None
		self.__created_time = None
		self.__callback = None
		self.__key_modified = dict()

	def get_status(self):
		"""
		The method to get the status

		Returns:
			string: A string representing the status
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (string) : A string representing the status
		"""

		if status is not None and not isinstance(status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: str', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def get_character_encoding(self):
		"""
		The method to get the character_encoding

		Returns:
			string: A string representing the character_encoding
		"""

		return self.__character_encoding

	def set_character_encoding(self, character_encoding):
		"""
		The method to set the value to character_encoding

		Parameters:
			character_encoding (string) : A string representing the character_encoding
		"""

		if character_encoding is not None and not isinstance(character_encoding, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: character_encoding EXPECTED TYPE: str', None, None)
		
		self.__character_encoding = character_encoding
		self.__key_modified['character_encoding'] = 1

	def get_resource(self):
		"""
		The method to get the resource

		Returns:
			list: An instance of list
		"""

		return self.__resource

	def set_resource(self, resource):
		"""
		The method to set the value to resource

		Parameters:
			resource (list) : An instance of list
		"""

		if resource is not None and not isinstance(resource, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: resource EXPECTED TYPE: list', None, None)
		
		self.__resource = resource
		self.__key_modified['resource'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.result import Result
		except Exception:
			from .result import Result

		if result is not None and not isinstance(result, Result):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: result EXPECTED TYPE: Result', None, None)
		
		self.__result = result
		self.__key_modified['result'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.call_back import CallBack
		except Exception:
			from .call_back import CallBack

		if callback is not None and not isinstance(callback, CallBack):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: callback EXPECTED TYPE: CallBack', None, None)
		
		self.__callback = callback
		self.__key_modified['callback'] = 1

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
