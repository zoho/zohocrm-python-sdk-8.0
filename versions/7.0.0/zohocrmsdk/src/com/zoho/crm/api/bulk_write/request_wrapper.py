try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class RequestWrapper(object):
	def __init__(self):
		"""Creates an instance of RequestWrapper"""

		self.__character_encoding = None
		self.__operation = None
		self.__callback = None
		self.__resource = None
		self.__ignore_empty = None
		self.__key_modified = dict()

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

	def get_operation(self):
		"""
		The method to get the operation

		Returns:
			Choice: An instance of Choice
		"""

		return self.__operation

	def set_operation(self, operation):
		"""
		The method to set the value to operation

		Parameters:
			operation (Choice) : An instance of Choice
		"""

		if operation is not None and not isinstance(operation, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: operation EXPECTED TYPE: Choice', None, None)
		
		self.__operation = operation
		self.__key_modified['operation'] = 1

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

	def get_ignore_empty(self):
		"""
		The method to get the ignore_empty

		Returns:
			bool: A bool representing the ignore_empty
		"""

		return self.__ignore_empty

	def set_ignore_empty(self, ignore_empty):
		"""
		The method to set the value to ignore_empty

		Parameters:
			ignore_empty (bool) : A bool representing the ignore_empty
		"""

		if ignore_empty is not None and not isinstance(ignore_empty, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ignore_empty EXPECTED TYPE: bool', None, None)
		
		self.__ignore_empty = ignore_empty
		self.__key_modified['ignore_empty'] = 1

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
