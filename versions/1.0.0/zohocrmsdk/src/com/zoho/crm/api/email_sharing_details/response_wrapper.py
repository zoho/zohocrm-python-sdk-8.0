try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.email_sharing_details.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__emails_sharing_details = None
		self.__key_modified = dict()

	def get_emails_sharing_details(self):
		"""
		The method to get the emails_sharing_details

		Returns:
			list: An instance of list
		"""

		return self.__emails_sharing_details

	def set_emails_sharing_details(self, emails_sharing_details):
		"""
		The method to set the value to emails_sharing_details

		Parameters:
			emails_sharing_details (list) : An instance of list
		"""

		if emails_sharing_details is not None and not isinstance(emails_sharing_details, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: emails_sharing_details EXPECTED TYPE: list', None, None)
		
		self.__emails_sharing_details = emails_sharing_details
		self.__key_modified['__emails_sharing_details'] = 1

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
