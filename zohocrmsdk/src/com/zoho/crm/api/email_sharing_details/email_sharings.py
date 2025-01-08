try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class EmailSharings(object):
	def __init__(self):
		"""Creates an instance of EmailSharings"""

		self.__share_from_users = None
		self.__available_types = None
		self.__key_modified = dict()

	def get_share_from_users(self):
		"""
		The method to get the share_from_users

		Returns:
			list: An instance of list
		"""

		return self.__share_from_users

	def set_share_from_users(self, share_from_users):
		"""
		The method to set the value to share_from_users

		Parameters:
			share_from_users (list) : An instance of list
		"""

		if share_from_users is not None and not isinstance(share_from_users, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: share_from_users EXPECTED TYPE: list', None, None)
		
		self.__share_from_users = share_from_users
		self.__key_modified['share_from_users'] = 1

	def get_available_types(self):
		"""
		The method to get the available_types

		Returns:
			list: An instance of list
		"""

		return self.__available_types

	def set_available_types(self, available_types):
		"""
		The method to set the value to available_types

		Parameters:
			available_types (list) : An instance of list
		"""

		if available_types is not None and not isinstance(available_types, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: available_types EXPECTED TYPE: list', None, None)
		
		self.__available_types = available_types
		self.__key_modified['available_types'] = 1

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
