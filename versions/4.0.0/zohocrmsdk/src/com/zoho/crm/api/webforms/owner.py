try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Owner(object):
	def __init__(self):
		"""Creates an instance of Owner"""

		self.__name = None
		self.__id = None
		self.__system_mail = None
		self.__email_template = None
		self.__key_modified = dict()

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

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

	def get_system_mail(self):
		"""
		The method to get the system_mail

		Returns:
			bool: A bool representing the system_mail
		"""

		return self.__system_mail

	def set_system_mail(self, system_mail):
		"""
		The method to set the value to system_mail

		Parameters:
			system_mail (bool) : A bool representing the system_mail
		"""

		if system_mail is not None and not isinstance(system_mail, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: system_mail EXPECTED TYPE: bool', None, None)
		
		self.__system_mail = system_mail
		self.__key_modified['system_mail'] = 1

	def get_email_template(self):
		"""
		The method to get the email_template

		Returns:
			dict: An instance of dict
		"""

		return self.__email_template

	def set_email_template(self, email_template):
		"""
		The method to set the value to email_template

		Parameters:
			email_template (dict) : An instance of dict
		"""

		if email_template is not None and not isinstance(email_template, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_template EXPECTED TYPE: dict', None, None)
		
		self.__email_template = email_template
		self.__key_modified['email_template'] = 1

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
