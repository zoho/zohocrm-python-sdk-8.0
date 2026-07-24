try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class UserType(object):
	def __init__(self):
		"""Creates an instance of UserType"""

		self.__personality_module = None
		self.__created_time = None
		self.__modified_time = None
		self.__modified_by = None
		self.__created_by = None
		self.__name = None
		self.__active = None
		self.__default = None
		self.__no_of_users = None
		self.__id = None
		self.__modules = None
		self.__key_modified = dict()

	def get_personality_module(self):
		"""
		The method to get the personality_module

		Returns:
			PersonalityModule: An instance of PersonalityModule
		"""

		return self.__personality_module

	def set_personality_module(self, personality_module):
		"""
		The method to set the value to personality_module

		Parameters:
			personality_module (PersonalityModule) : An instance of PersonalityModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.portal_user_type.personality_module import PersonalityModule
		except Exception:
			from .personality_module import PersonalityModule

		if personality_module is not None and not isinstance(personality_module, PersonalityModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: personality_module EXPECTED TYPE: PersonalityModule', None, None)
		
		self.__personality_module = personality_module
		self.__key_modified['personality_module'] = 1

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

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			Owner: An instance of Owner
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.portal_user_type.owner import Owner
		except Exception:
			from .owner import Owner

		if modified_by is not None and not isinstance(modified_by, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: Owner', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			Owner: An instance of Owner
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.portal_user_type.owner import Owner
		except Exception:
			from .owner import Owner

		if created_by is not None and not isinstance(created_by, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: Owner', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

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

	def get_default(self):
		"""
		The method to get the default

		Returns:
			bool: A bool representing the default
		"""

		return self.__default

	def set_default(self, default):
		"""
		The method to set the value to default

		Parameters:
			default (bool) : A bool representing the default
		"""

		if default is not None and not isinstance(default, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default EXPECTED TYPE: bool', None, None)
		
		self.__default = default
		self.__key_modified['default'] = 1

	def get_no_of_users(self):
		"""
		The method to get the no_of_users

		Returns:
			int: An int representing the no_of_users
		"""

		return self.__no_of_users

	def set_no_of_users(self, no_of_users):
		"""
		The method to set the value to no_of_users

		Parameters:
			no_of_users (int) : An int representing the no_of_users
		"""

		if no_of_users is not None and not isinstance(no_of_users, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: no_of_users EXPECTED TYPE: int', None, None)
		
		self.__no_of_users = no_of_users
		self.__key_modified['no_of_users'] = 1

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

	def get_modules(self):
		"""
		The method to get the modules

		Returns:
			list: An instance of list
		"""

		return self.__modules

	def set_modules(self, modules):
		"""
		The method to set the value to modules

		Parameters:
			modules (list) : An instance of list
		"""

		if modules is not None and not isinstance(modules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modules EXPECTED TYPE: list', None, None)
		
		self.__modules = modules
		self.__key_modified['modules'] = 1

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
