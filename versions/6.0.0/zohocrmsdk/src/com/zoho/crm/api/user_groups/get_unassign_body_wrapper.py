try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class GetUnassignBodyWrapper(object):
	def __init__(self):
		"""Creates an instance of GetUnassignBodyWrapper"""

		self.__get_unassigned = None
		self.__key_modified = dict()

	def get_get_unassigned(self):
		"""
		The method to get the get_unassigned

		Returns:
			Assign: An instance of Assign
		"""

		return self.__get_unassigned

	def set_get_unassigned(self, get_unassigned):
		"""
		The method to set the value to get_unassigned

		Parameters:
			get_unassigned (Assign) : An instance of Assign
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.assign import Assign
		except Exception:
			from .assign import Assign

		if get_unassigned is not None and not isinstance(get_unassigned, Assign):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: get_unassigned EXPECTED TYPE: Assign', None, None)
		
		self.__get_unassigned = get_unassigned
		self.__key_modified['get_unassigned'] = 1

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
