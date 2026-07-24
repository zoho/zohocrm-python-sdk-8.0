try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class FromAddress(object):
	def __init__(self):
		"""Creates an instance of FromAddress"""

		self.__user_name = None
		self.__type = None
		self.__email = None
		self.__id = None
		self.__default = None
		self.__key_modified = dict()

	def get_user_name(self):
		"""
		The method to get the user_name

		Returns:
			string: A string representing the user_name
		"""

		return self.__user_name

	def set_user_name(self, user_name):
		"""
		The method to set the value to user_name

		Parameters:
			user_name (string) : A string representing the user_name
		"""

		if user_name is not None and not isinstance(user_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_name EXPECTED TYPE: str', None, None)
		
		self.__user_name = user_name
		self.__key_modified['user_name'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_email(self):
		"""
		The method to get the email

		Returns:
			string: A string representing the email
		"""

		return self.__email

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (string) : A string representing the email
		"""

		if email is not None and not isinstance(email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: str', None, None)
		
		self.__email = email
		self.__key_modified['email'] = 1

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

	def get_default(self):
		"""
		The method to get the default

		Returns:
			Choice: An instance of Choice
		"""

		return self.__default

	def set_default(self, default):
		"""
		The method to set the value to default

		Parameters:
			default (Choice) : An instance of Choice
		"""

		if default is not None and not isinstance(default, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default EXPECTED TYPE: Choice', None, None)
		
		self.__default = default
		self.__key_modified['default'] = 1

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
