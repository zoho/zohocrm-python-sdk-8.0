try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__share = None
		self.__notify_on_completion = None
		self.__notify = None
		self.__key_modified = dict()

	def get_share(self):
		"""
		The method to get the share

		Returns:
			list: An instance of list
		"""

		return self.__share

	def set_share(self, share):
		"""
		The method to set the value to share

		Parameters:
			share (list) : An instance of list
		"""

		if share is not None and not isinstance(share, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: share EXPECTED TYPE: list', None, None)
		
		self.__share = share
		self.__key_modified['share'] = 1

	def get_notify_on_completion(self):
		"""
		The method to get the notify_on_completion

		Returns:
			bool: A bool representing the notify_on_completion
		"""

		return self.__notify_on_completion

	def set_notify_on_completion(self, notify_on_completion):
		"""
		The method to set the value to notify_on_completion

		Parameters:
			notify_on_completion (bool) : A bool representing the notify_on_completion
		"""

		if notify_on_completion is not None and not isinstance(notify_on_completion, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notify_on_completion EXPECTED TYPE: bool', None, None)
		
		self.__notify_on_completion = notify_on_completion
		self.__key_modified['notify_on_completion'] = 1

	def get_notify(self):
		"""
		The method to get the notify

		Returns:
			bool: A bool representing the notify
		"""

		return self.__notify

	def set_notify(self, notify):
		"""
		The method to set the value to notify

		Parameters:
			notify (bool) : A bool representing the notify
		"""

		if notify is not None and not isinstance(notify, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notify EXPECTED TYPE: bool', None, None)
		
		self.__notify = notify
		self.__key_modified['notify'] = 1

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
