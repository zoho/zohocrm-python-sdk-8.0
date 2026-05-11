try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Translation(object):
	def __init__(self):
		"""Creates an instance of Translation"""

		self.__public_views = None
		self.__other_users_views = None
		self.__shared_with_me = None
		self.__created_by_me = None
		self.__key_modified = dict()

	def get_public_views(self):
		"""
		The method to get the public_views

		Returns:
			string: A string representing the public_views
		"""

		return self.__public_views

	def set_public_views(self, public_views):
		"""
		The method to set the value to public_views

		Parameters:
			public_views (string) : A string representing the public_views
		"""

		if public_views is not None and not isinstance(public_views, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: public_views EXPECTED TYPE: str', None, None)
		
		self.__public_views = public_views
		self.__key_modified['public_views'] = 1

	def get_other_users_views(self):
		"""
		The method to get the other_users_views

		Returns:
			string: A string representing the other_users_views
		"""

		return self.__other_users_views

	def set_other_users_views(self, other_users_views):
		"""
		The method to set the value to other_users_views

		Parameters:
			other_users_views (string) : A string representing the other_users_views
		"""

		if other_users_views is not None and not isinstance(other_users_views, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: other_users_views EXPECTED TYPE: str', None, None)
		
		self.__other_users_views = other_users_views
		self.__key_modified['other_users_views'] = 1

	def get_shared_with_me(self):
		"""
		The method to get the shared_with_me

		Returns:
			string: A string representing the shared_with_me
		"""

		return self.__shared_with_me

	def set_shared_with_me(self, shared_with_me):
		"""
		The method to set the value to shared_with_me

		Parameters:
			shared_with_me (string) : A string representing the shared_with_me
		"""

		if shared_with_me is not None and not isinstance(shared_with_me, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_with_me EXPECTED TYPE: str', None, None)
		
		self.__shared_with_me = shared_with_me
		self.__key_modified['shared_with_me'] = 1

	def get_created_by_me(self):
		"""
		The method to get the created_by_me

		Returns:
			string: A string representing the created_by_me
		"""

		return self.__created_by_me

	def set_created_by_me(self, created_by_me):
		"""
		The method to set the value to created_by_me

		Parameters:
			created_by_me (string) : A string representing the created_by_me
		"""

		if created_by_me is not None and not isinstance(created_by_me, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by_me EXPECTED TYPE: str', None, None)
		
		self.__created_by_me = created_by_me
		self.__key_modified['created_by_me'] = 1

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
