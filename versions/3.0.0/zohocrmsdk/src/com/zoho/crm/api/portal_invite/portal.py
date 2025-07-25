try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Portal(object):
	def __init__(self):
		"""Creates an instance of Portal"""

		self.__id = None
		self.__user_type_id = None
		self.__type = None
		self.__language = None
		self.__key_modified = dict()

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_user_type_id(self):
		"""
		The method to get the user_type_id

		Returns:
			int: An int representing the user_type_id
		"""

		return self.__user_type_id

	def set_user_type_id(self, user_type_id):
		"""
		The method to set the value to user_type_id

		Parameters:
			user_type_id (int) : An int representing the user_type_id
		"""

		if user_type_id is not None and not isinstance(user_type_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_type_id EXPECTED TYPE: int', None, None)
		
		self.__user_type_id = user_type_id
		self.__key_modified['user_type_id'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (Choice) : An instance of Choice
		"""

		if type is not None and not isinstance(type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: Choice', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_language(self):
		"""
		The method to get the language

		Returns:
			Choice: An instance of Choice
		"""

		return self.__language

	def set_language(self, language):
		"""
		The method to set the value to language

		Parameters:
			language (Choice) : An instance of Choice
		"""

		if language is not None and not isinstance(language, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: language EXPECTED TYPE: Choice', None, None)
		
		self.__language = language
		self.__key_modified['language'] = 1

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
