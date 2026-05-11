try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class RecordLock(object):
	def __init__(self):
		"""Creates an instance of RecordLock"""

		self.__created_time = None
		self.__locked_for = None
		self.__excluded_fields = None
		self.__created_by = None
		self.__feature_type = None
		self.__locking_rules = None
		self.__restricted_actions = None
		self.__lock_for_portal_users = None
		self.__modified_time = None
		self.__restricted_communications = None
		self.__system_defined = None
		self.__modified_by = None
		self.__id = None
		self.__lock_type = None
		self.__restricted_custom_buttons = None
		self.__lock_excluded_profiles = None
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

	def get_locked_for(self):
		"""
		The method to get the locked_for

		Returns:
			string: A string representing the locked_for
		"""

		return self.__locked_for

	def set_locked_for(self, locked_for):
		"""
		The method to set the value to locked_for

		Parameters:
			locked_for (string) : A string representing the locked_for
		"""

		if locked_for is not None and not isinstance(locked_for, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locked_for EXPECTED TYPE: str', None, None)
		
		self.__locked_for = locked_for
		self.__key_modified['locked_for'] = 1

	def get_excluded_fields(self):
		"""
		The method to get the excluded_fields

		Returns:
			list: An instance of list
		"""

		return self.__excluded_fields

	def set_excluded_fields(self, excluded_fields):
		"""
		The method to set the value to excluded_fields

		Parameters:
			excluded_fields (list) : An instance of list
		"""

		if excluded_fields is not None and not isinstance(excluded_fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: excluded_fields EXPECTED TYPE: list', None, None)
		
		self.__excluded_fields = excluded_fields
		self.__key_modified['excluded_fields'] = 1

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

	def get_feature_type(self):
		"""
		The method to get the feature_type

		Returns:
			string: A string representing the feature_type
		"""

		return self.__feature_type

	def set_feature_type(self, feature_type):
		"""
		The method to set the value to feature_type

		Parameters:
			feature_type (string) : A string representing the feature_type
		"""

		if feature_type is not None and not isinstance(feature_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: feature_type EXPECTED TYPE: str', None, None)
		
		self.__feature_type = feature_type
		self.__key_modified['feature_type'] = 1

	def get_locking_rules(self):
		"""
		The method to get the locking_rules

		Returns:
			list: An instance of list
		"""

		return self.__locking_rules

	def set_locking_rules(self, locking_rules):
		"""
		The method to set the value to locking_rules

		Parameters:
			locking_rules (list) : An instance of list
		"""

		if locking_rules is not None and not isinstance(locking_rules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locking_rules EXPECTED TYPE: list', None, None)
		
		self.__locking_rules = locking_rules
		self.__key_modified['locking_rules'] = 1

	def get_restricted_actions(self):
		"""
		The method to get the restricted_actions

		Returns:
			list: An instance of list
		"""

		return self.__restricted_actions

	def set_restricted_actions(self, restricted_actions):
		"""
		The method to set the value to restricted_actions

		Parameters:
			restricted_actions (list) : An instance of list
		"""

		if restricted_actions is not None and not isinstance(restricted_actions, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restricted_actions EXPECTED TYPE: list', None, None)
		
		self.__restricted_actions = restricted_actions
		self.__key_modified['restricted_actions'] = 1

	def get_lock_for_portal_users(self):
		"""
		The method to get the lock_for_portal_users

		Returns:
			bool: A bool representing the lock_for_portal_users
		"""

		return self.__lock_for_portal_users

	def set_lock_for_portal_users(self, lock_for_portal_users):
		"""
		The method to set the value to lock_for_portal_users

		Parameters:
			lock_for_portal_users (bool) : A bool representing the lock_for_portal_users
		"""

		if lock_for_portal_users is not None and not isinstance(lock_for_portal_users, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lock_for_portal_users EXPECTED TYPE: bool', None, None)
		
		self.__lock_for_portal_users = lock_for_portal_users
		self.__key_modified['lock_for_portal_users'] = 1

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

	def get_restricted_communications(self):
		"""
		The method to get the restricted_communications

		Returns:
			list: An instance of list
		"""

		return self.__restricted_communications

	def set_restricted_communications(self, restricted_communications):
		"""
		The method to set the value to restricted_communications

		Parameters:
			restricted_communications (list) : An instance of list
		"""

		if restricted_communications is not None and not isinstance(restricted_communications, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restricted_communications EXPECTED TYPE: list', None, None)
		
		self.__restricted_communications = restricted_communications
		self.__key_modified['restricted_communications'] = 1

	def get_system_defined(self):
		"""
		The method to get the system_defined

		Returns:
			bool: A bool representing the system_defined
		"""

		return self.__system_defined

	def set_system_defined(self, system_defined):
		"""
		The method to set the value to system_defined

		Parameters:
			system_defined (bool) : A bool representing the system_defined
		"""

		if system_defined is not None and not isinstance(system_defined, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: system_defined EXPECTED TYPE: bool', None, None)
		
		self.__system_defined = system_defined
		self.__key_modified['system_defined'] = 1

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

	def get_lock_type(self):
		"""
		The method to get the lock_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__lock_type

	def set_lock_type(self, lock_type):
		"""
		The method to set the value to lock_type

		Parameters:
			lock_type (Choice) : An instance of Choice
		"""

		if lock_type is not None and not isinstance(lock_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lock_type EXPECTED TYPE: Choice', None, None)
		
		self.__lock_type = lock_type
		self.__key_modified['lock_type'] = 1

	def get_restricted_custom_buttons(self):
		"""
		The method to get the restricted_custom_buttons

		Returns:
			list: An instance of list
		"""

		return self.__restricted_custom_buttons

	def set_restricted_custom_buttons(self, restricted_custom_buttons):
		"""
		The method to set the value to restricted_custom_buttons

		Parameters:
			restricted_custom_buttons (list) : An instance of list
		"""

		if restricted_custom_buttons is not None and not isinstance(restricted_custom_buttons, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restricted_custom_buttons EXPECTED TYPE: list', None, None)
		
		self.__restricted_custom_buttons = restricted_custom_buttons
		self.__key_modified['restricted_custom_buttons'] = 1

	def get_lock_excluded_profiles(self):
		"""
		The method to get the lock_excluded_profiles

		Returns:
			list: An instance of list
		"""

		return self.__lock_excluded_profiles

	def set_lock_excluded_profiles(self, lock_excluded_profiles):
		"""
		The method to set the value to lock_excluded_profiles

		Parameters:
			lock_excluded_profiles (list) : An instance of list
		"""

		if lock_excluded_profiles is not None and not isinstance(lock_excluded_profiles, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lock_excluded_profiles EXPECTED TYPE: list', None, None)
		
		self.__lock_excluded_profiles = lock_excluded_profiles
		self.__key_modified['lock_excluded_profiles'] = 1

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
