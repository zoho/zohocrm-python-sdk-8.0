try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.share_records.delete_action_handler import DeleteActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .delete_action_handler import DeleteActionHandler


class DeleteActionWrapper(DeleteActionHandler):
	def __init__(self):
		"""Creates an instance of DeleteActionWrapper"""
		super().__init__()

		self.__share = None
		self.__key_modified = dict()

	def get_share(self):
		"""
		The method to get the share

		Returns:
			DeleteActionResponse: An instance of DeleteActionResponse
		"""

		return self.__share

	def set_share(self, share):
		"""
		The method to set the value to share

		Parameters:
			share (DeleteActionResponse) : An instance of DeleteActionResponse
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.share_records.delete_action_response import DeleteActionResponse
		except Exception:
			from .delete_action_response import DeleteActionResponse

		if share is not None and not isinstance(share, DeleteActionResponse):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: share EXPECTED TYPE: DeleteActionResponse', None, None)
		
		self.__share = share
		self.__key_modified['share'] = 1

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
