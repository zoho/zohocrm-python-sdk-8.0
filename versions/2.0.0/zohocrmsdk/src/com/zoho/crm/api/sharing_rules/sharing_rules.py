try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class SharingRules(object):
	def __init__(self):
		"""Creates an instance of SharingRules"""

		self.__id = None
		self.__permission_type = None
		self.__superiors_allowed = None
		self.__name = None
		self.__type = None
		self.__shared_from = None
		self.__shared_to = None
		self.__criteria = None
		self.__module = None
		self.__status = None
		self.__match_limit_exceeded = None
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

	def get_permission_type(self):
		"""
		The method to get the permission_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__permission_type

	def set_permission_type(self, permission_type):
		"""
		The method to set the value to permission_type

		Parameters:
			permission_type (Choice) : An instance of Choice
		"""

		if permission_type is not None and not isinstance(permission_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permission_type EXPECTED TYPE: Choice', None, None)
		
		self.__permission_type = permission_type
		self.__key_modified['permission_type'] = 1

	def get_superiors_allowed(self):
		"""
		The method to get the superiors_allowed

		Returns:
			bool: A bool representing the superiors_allowed
		"""

		return self.__superiors_allowed

	def set_superiors_allowed(self, superiors_allowed):
		"""
		The method to set the value to superiors_allowed

		Parameters:
			superiors_allowed (bool) : A bool representing the superiors_allowed
		"""

		if superiors_allowed is not None and not isinstance(superiors_allowed, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: superiors_allowed EXPECTED TYPE: bool', None, None)
		
		self.__superiors_allowed = superiors_allowed
		self.__key_modified['superiors_allowed'] = 1

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

	def get_shared_from(self):
		"""
		The method to get the shared_from

		Returns:
			Shared: An instance of Shared
		"""

		return self.__shared_from

	def set_shared_from(self, shared_from):
		"""
		The method to set the value to shared_from

		Parameters:
			shared_from (Shared) : An instance of Shared
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.shared import Shared
		except Exception:
			from .shared import Shared

		if shared_from is not None and not isinstance(shared_from, Shared):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_from EXPECTED TYPE: Shared', None, None)
		
		self.__shared_from = shared_from
		self.__key_modified['shared_from'] = 1

	def get_shared_to(self):
		"""
		The method to get the shared_to

		Returns:
			Shared: An instance of Shared
		"""

		return self.__shared_to

	def set_shared_to(self, shared_to):
		"""
		The method to set the value to shared_to

		Parameters:
			shared_to (Shared) : An instance of Shared
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.shared import Shared
		except Exception:
			from .shared import Shared

		if shared_to is not None and not isinstance(shared_to, Shared):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_to EXPECTED TYPE: Shared', None, None)
		
		self.__shared_to = shared_to
		self.__key_modified['shared_to'] = 1

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Module: An instance of Module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Module) : An instance of Module
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_status(self):
		"""
		The method to get the status

		Returns:
			Choice: An instance of Choice
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (Choice) : An instance of Choice
		"""

		if status is not None and not isinstance(status, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: Choice', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def get_match_limit_exceeded(self):
		"""
		The method to get the match_limit_exceeded

		Returns:
			bool: A bool representing the match_limit_exceeded
		"""

		return self.__match_limit_exceeded

	def set_match_limit_exceeded(self, match_limit_exceeded):
		"""
		The method to set the value to match_limit_exceeded

		Parameters:
			match_limit_exceeded (bool) : A bool representing the match_limit_exceeded
		"""

		if match_limit_exceeded is not None and not isinstance(match_limit_exceeded, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: match_limit_exceeded EXPECTED TYPE: bool', None, None)
		
		self.__match_limit_exceeded = match_limit_exceeded
		self.__key_modified['match_limit_exceeded'] = 1

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
