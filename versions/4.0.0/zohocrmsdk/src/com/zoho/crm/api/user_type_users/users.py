try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Users(object):
	def __init__(self):
		"""Creates an instance of Users"""

		self.__personality_id = None
		self.__confirm = None
		self.__status_reason__s = None
		self.__invited_time = None
		self.__module = None
		self.__name = None
		self.__active = None
		self.__email = None
		self.__key_modified = dict()

	def get_personality_id(self):
		"""
		The method to get the personality_id

		Returns:
			int: An int representing the personality_id
		"""

		return self.__personality_id

	def set_personality_id(self, personality_id):
		"""
		The method to set the value to personality_id

		Parameters:
			personality_id (int) : An int representing the personality_id
		"""

		if personality_id is not None and not isinstance(personality_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: personality_id EXPECTED TYPE: int', None, None)
		
		self.__personality_id = personality_id
		self.__key_modified['personality_id'] = 1

	def get_confirm(self):
		"""
		The method to get the confirm

		Returns:
			bool: A bool representing the confirm
		"""

		return self.__confirm

	def set_confirm(self, confirm):
		"""
		The method to set the value to confirm

		Parameters:
			confirm (bool) : A bool representing the confirm
		"""

		if confirm is not None and not isinstance(confirm, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: confirm EXPECTED TYPE: bool', None, None)
		
		self.__confirm = confirm
		self.__key_modified['confirm'] = 1

	def get_status_reason__s(self):
		"""
		The method to get the status_reason__s

		Returns:
			string: A string representing the status_reason__s
		"""

		return self.__status_reason__s

	def set_status_reason__s(self, status_reason__s):
		"""
		The method to set the value to status_reason__s

		Parameters:
			status_reason__s (string) : A string representing the status_reason__s
		"""

		if status_reason__s is not None and not isinstance(status_reason__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status_reason__s EXPECTED TYPE: str', None, None)
		
		self.__status_reason__s = status_reason__s
		self.__key_modified['status_reason__s'] = 1

	def get_invited_time(self):
		"""
		The method to get the invited_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__invited_time

	def set_invited_time(self, invited_time):
		"""
		The method to set the value to invited_time

		Parameters:
			invited_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if invited_time is not None and not isinstance(invited_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: invited_time EXPECTED TYPE: datetime', None, None)
		
		self.__invited_time = invited_time
		self.__key_modified['invited_time'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			string: A string representing the module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (string) : A string representing the module
		"""

		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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

	def get_active(self):
		"""
		The method to get the active

		Returns:
			bool: A bool representing the active
		"""

		return self.__active

	def set_active(self, active):
		"""
		The method to set the value to active

		Parameters:
			active (bool) : A bool representing the active
		"""

		if active is not None and not isinstance(active, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: active EXPECTED TYPE: bool', None, None)
		
		self.__active = active
		self.__key_modified['active'] = 1

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
