try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Wizard(object):
	def __init__(self):
		"""Creates an instance of Wizard"""

		self.__created_time = None
		self.__modified_time = None
		self.__module = None
		self.__name = None
		self.__modified_by = None
		self.__profiles = None
		self.__active = None
		self.__containers = None
		self.__id = None
		self.__created_by = None
		self.__portal_user_types = None
		self.__exempted_portal_user_types = None
		self.__parent_wizard = None
		self.__draft = None
		self.__key_modified = dict()

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

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Modules: An instance of Modules
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Modules) : An instance of Modules
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import Modules
		except Exception:
			from ..modules import Modules

		if module is not None and not isinstance(module, Modules):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Modules', None, None)
		
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

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if modified_by is not None and not isinstance(modified_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

	def get_profiles(self):
		"""
		The method to get the profiles

		Returns:
			list: An instance of list
		"""

		return self.__profiles

	def set_profiles(self, profiles):
		"""
		The method to set the value to profiles

		Parameters:
			profiles (list) : An instance of list
		"""

		if profiles is not None and not isinstance(profiles, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: profiles EXPECTED TYPE: list', None, None)
		
		self.__profiles = profiles
		self.__key_modified['profiles'] = 1

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

	def get_containers(self):
		"""
		The method to get the containers

		Returns:
			list: An instance of list
		"""

		return self.__containers

	def set_containers(self, containers):
		"""
		The method to set the value to containers

		Parameters:
			containers (list) : An instance of list
		"""

		if containers is not None and not isinstance(containers, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: containers EXPECTED TYPE: list', None, None)
		
		self.__containers = containers
		self.__key_modified['containers'] = 1

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

	def get_portal_user_types(self):
		"""
		The method to get the portal_user_types

		Returns:
			list: An instance of list
		"""

		return self.__portal_user_types

	def set_portal_user_types(self, portal_user_types):
		"""
		The method to set the value to portal_user_types

		Parameters:
			portal_user_types (list) : An instance of list
		"""

		if portal_user_types is not None and not isinstance(portal_user_types, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: portal_user_types EXPECTED TYPE: list', None, None)
		
		self.__portal_user_types = portal_user_types
		self.__key_modified['portal_user_types'] = 1

	def get_exempted_portal_user_types(self):
		"""
		The method to get the exempted_portal_user_types

		Returns:
			list: An instance of list
		"""

		return self.__exempted_portal_user_types

	def set_exempted_portal_user_types(self, exempted_portal_user_types):
		"""
		The method to set the value to exempted_portal_user_types

		Parameters:
			exempted_portal_user_types (list) : An instance of list
		"""

		if exempted_portal_user_types is not None and not isinstance(exempted_portal_user_types, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exempted_portal_user_types EXPECTED TYPE: list', None, None)
		
		self.__exempted_portal_user_types = exempted_portal_user_types
		self.__key_modified['exempted_portal_user_types'] = 1

	def get_parent_wizard(self):
		"""
		The method to get the parent_wizard

		Returns:
			Wizard: An instance of Wizard
		"""

		return self.__parent_wizard

	def set_parent_wizard(self, parent_wizard):
		"""
		The method to set the value to parent_wizard

		Parameters:
			parent_wizard (Wizard) : An instance of Wizard
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.wizards.wizard import Wizard
		except Exception:
			from .wizard import Wizard

		if parent_wizard is not None and not isinstance(parent_wizard, Wizard):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_wizard EXPECTED TYPE: Wizard', None, None)
		
		self.__parent_wizard = parent_wizard
		self.__key_modified['parent_wizard'] = 1

	def get_draft(self):
		"""
		The method to get the draft

		Returns:
			bool: A bool representing the draft
		"""

		return self.__draft

	def set_draft(self, draft):
		"""
		The method to set the value to draft

		Parameters:
			draft (bool) : A bool representing the draft
		"""

		if draft is not None and not isinstance(draft, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: draft EXPECTED TYPE: bool', None, None)
		
		self.__draft = draft
		self.__key_modified['draft'] = 1

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
