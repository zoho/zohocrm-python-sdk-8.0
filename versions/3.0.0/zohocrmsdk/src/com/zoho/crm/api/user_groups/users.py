try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Users(object):
	def __init__(self):
		"""Creates an instance of Users"""

		self.__inactive = None
		self.__deleted = None
		self.__active = None
		self.__key_modified = dict()

	def get_inactive(self):
		"""
		The method to get the inactive

		Returns:
			int: An int representing the inactive
		"""

		return self.__inactive

	def set_inactive(self, inactive):
		"""
		The method to set the value to inactive

		Parameters:
			inactive (int) : An int representing the inactive
		"""

		if inactive is not None and not isinstance(inactive, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: inactive EXPECTED TYPE: int', None, None)
		
		self.__inactive = inactive
		self.__key_modified['inactive'] = 1

	def get_deleted(self):
		"""
		The method to get the deleted

		Returns:
			int: An int representing the deleted
		"""

		return self.__deleted

	def set_deleted(self, deleted):
		"""
		The method to set the value to deleted

		Parameters:
			deleted (int) : An int representing the deleted
		"""

		if deleted is not None and not isinstance(deleted, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deleted EXPECTED TYPE: int', None, None)
		
		self.__deleted = deleted
		self.__key_modified['deleted'] = 1

	def get_active(self):
		"""
		The method to get the active

		Returns:
			int: An int representing the active
		"""

		return self.__active

	def set_active(self, active):
		"""
		The method to set the value to active

		Parameters:
			active (int) : An int representing the active
		"""

		if active is not None and not isinstance(active, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: active EXPECTED TYPE: int', None, None)
		
		self.__active = active
		self.__key_modified['active'] = 1

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
