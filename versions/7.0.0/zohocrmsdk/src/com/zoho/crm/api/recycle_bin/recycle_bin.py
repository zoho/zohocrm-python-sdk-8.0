try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class RecycleBin(object):
	def __init__(self):
		"""Creates an instance of RecycleBin"""

		self.__display_name = None
		self.__deleted_time = None
		self.__owner = None
		self.__module = None
		self.__deleted_by = None
		self.__id = None
		self.__key_modified = dict()

	def get_display_name(self):
		"""
		The method to get the display_name

		Returns:
			string: A string representing the display_name
		"""

		return self.__display_name

	def set_display_name(self, display_name):
		"""
		The method to set the value to display_name

		Parameters:
			display_name (string) : A string representing the display_name
		"""

		if display_name is not None and not isinstance(display_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_name EXPECTED TYPE: str', None, None)
		
		self.__display_name = display_name
		self.__key_modified['display_name'] = 1

	def get_deleted_time(self):
		"""
		The method to get the deleted_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__deleted_time

	def set_deleted_time(self, deleted_time):
		"""
		The method to set the value to deleted_time

		Parameters:
			deleted_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if deleted_time is not None and not isinstance(deleted_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deleted_time EXPECTED TYPE: datetime', None, None)
		
		self.__deleted_time = deleted_time
		self.__key_modified['deleted_time'] = 1

	def get_owner(self):
		"""
		The method to get the owner

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__owner

	def set_owner(self, owner):
		"""
		The method to set the value to owner

		Parameters:
			owner (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if owner is not None and not isinstance(owner, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: owner EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__owner = owner
		self.__key_modified['owner'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
		except Exception:
			from ..modules import MinifiedModule

		if module is not None and not isinstance(module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_deleted_by(self):
		"""
		The method to get the deleted_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__deleted_by

	def set_deleted_by(self, deleted_by):
		"""
		The method to set the value to deleted_by

		Parameters:
			deleted_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if deleted_by is not None and not isinstance(deleted_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deleted_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__deleted_by = deleted_by
		self.__key_modified['deleted_by'] = 1

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
