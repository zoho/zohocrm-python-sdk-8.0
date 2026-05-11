try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.share_records.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__share = None
		self.__shareable_user = None
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

	def get_shareable_user(self):
		"""
		The method to get the shareable_user

		Returns:
			list: An instance of list
		"""

		return self.__shareable_user

	def set_shareable_user(self, shareable_user):
		"""
		The method to set the value to shareable_user

		Parameters:
			shareable_user (list) : An instance of list
		"""

		if shareable_user is not None and not isinstance(shareable_user, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shareable_user EXPECTED TYPE: list', None, None)
		
		self.__shareable_user = shareable_user
		self.__key_modified['shareable_user'] = 1

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
