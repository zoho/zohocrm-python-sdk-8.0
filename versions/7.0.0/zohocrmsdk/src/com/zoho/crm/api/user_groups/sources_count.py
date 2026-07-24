try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class SourcesCount(object):
	def __init__(self):
		"""Creates an instance of SourcesCount"""

		self.__territories = None
		self.__roles = None
		self.__groups = None
		self.__users = None
		self.__key_modified = dict()

	def get_territories(self):
		"""
		The method to get the territories

		Returns:
			int: An int representing the territories
		"""

		return self.__territories

	def set_territories(self, territories):
		"""
		The method to set the value to territories

		Parameters:
			territories (int) : An int representing the territories
		"""

		if territories is not None and not isinstance(territories, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territories EXPECTED TYPE: int', None, None)
		
		self.__territories = territories
		self.__key_modified['territories'] = 1

	def get_roles(self):
		"""
		The method to get the roles

		Returns:
			int: An int representing the roles
		"""

		return self.__roles

	def set_roles(self, roles):
		"""
		The method to set the value to roles

		Parameters:
			roles (int) : An int representing the roles
		"""

		if roles is not None and not isinstance(roles, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: roles EXPECTED TYPE: int', None, None)
		
		self.__roles = roles
		self.__key_modified['roles'] = 1

	def get_groups(self):
		"""
		The method to get the groups

		Returns:
			int: An int representing the groups
		"""

		return self.__groups

	def set_groups(self, groups):
		"""
		The method to set the value to groups

		Parameters:
			groups (int) : An int representing the groups
		"""

		if groups is not None and not isinstance(groups, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: groups EXPECTED TYPE: int', None, None)
		
		self.__groups = groups
		self.__key_modified['groups'] = 1

	def get_users(self):
		"""
		The method to get the users

		Returns:
			Users: An instance of Users
		"""

		return self.__users

	def set_users(self, users):
		"""
		The method to set the value to users

		Parameters:
			users (Users) : An instance of Users
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.users import Users
		except Exception:
			from .users import Users

		if users is not None and not isinstance(users, Users):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: users EXPECTED TYPE: Users', None, None)
		
		self.__users = users
		self.__key_modified['users'] = 1

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
