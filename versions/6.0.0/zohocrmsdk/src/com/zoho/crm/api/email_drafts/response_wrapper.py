try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ResponseWrapper(object):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""

		self.__email_drafts = None
		self.__key_modified = dict()

	def get_email_drafts(self):
		"""
		The method to get the email_drafts

		Returns:
			list: An instance of list
		"""

		return self.__email_drafts

	def set_email_drafts(self, email_drafts):
		"""
		The method to set the value to email_drafts

		Parameters:
			email_drafts (list) : An instance of list
		"""

		if email_drafts is not None and not isinstance(email_drafts, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_drafts EXPECTED TYPE: list', None, None)
		
		self.__email_drafts = email_drafts
		self.__key_modified['__email_drafts'] = 1

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
