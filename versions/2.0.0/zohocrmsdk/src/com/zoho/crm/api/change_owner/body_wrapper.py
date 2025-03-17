try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__owner = None
		self.__notify = None
		self.__related_modules = None
		self.__key_modified = dict()

	def get_owner(self):
		"""
		The method to get the owner

		Returns:
			Owner: An instance of Owner
		"""

		return self.__owner

	def set_owner(self, owner):
		"""
		The method to set the value to owner

		Parameters:
			owner (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.change_owner.owner import Owner
		except Exception:
			from .owner import Owner

		if owner is not None and not isinstance(owner, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: owner EXPECTED TYPE: Owner', None, None)
		
		self.__owner = owner
		self.__key_modified['owner'] = 1

	def get_notify(self):
		"""
		The method to get the notify

		Returns:
			bool: A bool representing the notify
		"""

		return self.__notify

	def set_notify(self, notify):
		"""
		The method to set the value to notify

		Parameters:
			notify (bool) : A bool representing the notify
		"""

		if notify is not None and not isinstance(notify, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notify EXPECTED TYPE: bool', None, None)
		
		self.__notify = notify
		self.__key_modified['notify'] = 1

	def get_related_modules(self):
		"""
		The method to get the related_modules

		Returns:
			list: An instance of list
		"""

		return self.__related_modules

	def set_related_modules(self, related_modules):
		"""
		The method to set the value to related_modules

		Parameters:
			related_modules (list) : An instance of list
		"""

		if related_modules is not None and not isinstance(related_modules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_modules EXPECTED TYPE: list', None, None)
		
		self.__related_modules = related_modules
		self.__key_modified['related_modules'] = 1

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
