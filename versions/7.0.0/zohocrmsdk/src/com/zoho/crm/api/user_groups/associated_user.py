try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AssociatedUser(object):
	def __init__(self):
		"""Creates an instance of AssociatedUser"""

		self.__user_group = None
		self.__count = None
		self.__key_modified = dict()

	def get_user_group(self):
		"""
		The method to get the user_group

		Returns:
			UserGroup: An instance of UserGroup
		"""

		return self.__user_group

	def set_user_group(self, user_group):
		"""
		The method to set the value to user_group

		Parameters:
			user_group (UserGroup) : An instance of UserGroup
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.user_group import UserGroup
		except Exception:
			from .user_group import UserGroup

		if user_group is not None and not isinstance(user_group, UserGroup):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_group EXPECTED TYPE: UserGroup', None, None)
		
		self.__user_group = user_group
		self.__key_modified['user_group'] = 1

	def get_count(self):
		"""
		The method to get the count

		Returns:
			int: An int representing the count
		"""

		return self.__count

	def set_count(self, count):
		"""
		The method to set the value to count

		Parameters:
			count (int) : An int representing the count
		"""

		if count is not None and not isinstance(count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: count EXPECTED TYPE: int', None, None)
		
		self.__count = count
		self.__key_modified['count'] = 1

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
