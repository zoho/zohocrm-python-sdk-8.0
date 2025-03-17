try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class SharingProperties(object):
	def __init__(self):
		"""Creates an instance of SharingProperties"""

		self.__scheduler_status = None
		self.__share_preference_enabled = None
		self.__share_permission = None
		self.__key_modified = dict()

	def get_scheduler_status(self):
		"""
		The method to get the scheduler_status

		Returns:
			string: A string representing the scheduler_status
		"""

		return self.__scheduler_status

	def set_scheduler_status(self, scheduler_status):
		"""
		The method to set the value to scheduler_status

		Parameters:
			scheduler_status (string) : A string representing the scheduler_status
		"""

		if scheduler_status is not None and not isinstance(scheduler_status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: scheduler_status EXPECTED TYPE: str', None, None)
		
		self.__scheduler_status = scheduler_status
		self.__key_modified['scheduler_status'] = 1

	def get_share_preference_enabled(self):
		"""
		The method to get the share_preference_enabled

		Returns:
			bool: A bool representing the share_preference_enabled
		"""

		return self.__share_preference_enabled

	def set_share_preference_enabled(self, share_preference_enabled):
		"""
		The method to set the value to share_preference_enabled

		Parameters:
			share_preference_enabled (bool) : A bool representing the share_preference_enabled
		"""

		if share_preference_enabled is not None and not isinstance(share_preference_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: share_preference_enabled EXPECTED TYPE: bool', None, None)
		
		self.__share_preference_enabled = share_preference_enabled
		self.__key_modified['share_preference_enabled'] = 1

	def get_share_permission(self):
		"""
		The method to get the share_permission

		Returns:
			Choice: An instance of Choice
		"""

		return self.__share_permission

	def set_share_permission(self, share_permission):
		"""
		The method to set the value to share_permission

		Parameters:
			share_permission (Choice) : An instance of Choice
		"""

		if share_permission is not None and not isinstance(share_permission, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: share_permission EXPECTED TYPE: Choice', None, None)
		
		self.__share_permission = share_permission
		self.__key_modified['share_permission'] = 1

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
