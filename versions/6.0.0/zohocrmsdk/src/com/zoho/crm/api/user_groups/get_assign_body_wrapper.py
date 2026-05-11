try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class GetAssignBodyWrapper(object):
	def __init__(self):
		"""Creates an instance of GetAssignBodyWrapper"""

		self.__get_assigned = None
		self.__key_modified = dict()

	def get_get_assigned(self):
		"""
		The method to get the get_assigned

		Returns:
			Assign: An instance of Assign
		"""

		return self.__get_assigned

	def set_get_assigned(self, get_assigned):
		"""
		The method to set the value to get_assigned

		Parameters:
			get_assigned (Assign) : An instance of Assign
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.assign import Assign
		except Exception:
			from .assign import Assign

		if get_assigned is not None and not isinstance(get_assigned, Assign):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: get_assigned EXPECTED TYPE: Assign', None, None)
		
		self.__get_assigned = get_assigned
		self.__key_modified['get_assigned'] = 1

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
