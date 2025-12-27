try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__convert_to = None
		self.__assign_to = None
		self.__related_modules = None
		self.__ids = None
		self.__key_modified = dict()

	def get_convert_to(self):
		"""
		The method to get the convert_to

		Returns:
			list: An instance of list
		"""

		return self.__convert_to

	def set_convert_to(self, convert_to):
		"""
		The method to set the value to convert_to

		Parameters:
			convert_to (list) : An instance of list
		"""

		if convert_to is not None and not isinstance(convert_to, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: convert_to EXPECTED TYPE: list', None, None)
		
		self.__convert_to = convert_to
		self.__key_modified['convert_to'] = 1

	def get_assign_to(self):
		"""
		The method to get the assign_to

		Returns:
			User: An instance of User
		"""

		return self.__assign_to

	def set_assign_to(self, assign_to):
		"""
		The method to set the value to assign_to

		Parameters:
			assign_to (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.inventory_mass_convert.user import User
		except Exception:
			from .user import User

		if assign_to is not None and not isinstance(assign_to, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: assign_to EXPECTED TYPE: User', None, None)
		
		self.__assign_to = assign_to
		self.__key_modified['assign_to'] = 1

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

	def get_ids(self):
		"""
		The method to get the ids

		Returns:
			list: An instance of list
		"""

		return self.__ids

	def set_ids(self, ids):
		"""
		The method to set the value to ids

		Parameters:
			ids (list) : An instance of list
		"""

		if ids is not None and not isinstance(ids, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ids EXPECTED TYPE: list', None, None)
		
		self.__ids = ids
		self.__key_modified['ids'] = 1

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
