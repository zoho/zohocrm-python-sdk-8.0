try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class SignMailMergeWrapper(object):
	def __init__(self):
		"""Creates an instance of SignMailMergeWrapper"""

		self.__sign_mail_merge = None
		self.__key_modified = dict()

	def get_sign_mail_merge(self):
		"""
		The method to get the sign_mail_merge

		Returns:
			list: An instance of list
		"""

		return self.__sign_mail_merge

	def set_sign_mail_merge(self, sign_mail_merge):
		"""
		The method to set the value to sign_mail_merge

		Parameters:
			sign_mail_merge (list) : An instance of list
		"""

		if sign_mail_merge is not None and not isinstance(sign_mail_merge, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sign_mail_merge EXPECTED TYPE: list', None, None)
		
		self.__sign_mail_merge = sign_mail_merge
		self.__key_modified['sign_mail_merge'] = 1

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
