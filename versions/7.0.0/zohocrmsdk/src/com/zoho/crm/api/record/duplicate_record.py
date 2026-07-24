try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class DuplicateRecord(object):
	def __init__(self):
		"""Creates an instance of DuplicateRecord"""

		self.__owner = None
		self.__module = None
		self.__id = None
		self.__key_modified = dict()

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
		self.__key_modified['Owner'] = 1

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
