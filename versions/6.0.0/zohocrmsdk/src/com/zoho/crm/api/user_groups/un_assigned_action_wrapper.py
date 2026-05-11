try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class UnAssignedActionWrapper(object):
	def __init__(self):
		"""Creates an instance of UnAssignedActionWrapper"""

		self.__get_unassigned = None
		self.__key_modified = dict()

	def get_get_unassigned(self):
		"""
		The method to get the get_unassigned

		Returns:
			UnAssignedActionResponse: An instance of UnAssignedActionResponse
		"""

		return self.__get_unassigned

	def set_get_unassigned(self, get_unassigned):
		"""
		The method to set the value to get_unassigned

		Parameters:
			get_unassigned (UnAssignedActionResponse) : An instance of UnAssignedActionResponse
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.un_assigned_action_response import UnAssignedActionResponse
		except Exception:
			from .un_assigned_action_response import UnAssignedActionResponse

		if get_unassigned is not None and not isinstance(get_unassigned, UnAssignedActionResponse):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: get_unassigned EXPECTED TYPE: UnAssignedActionResponse', None, None)
		
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
