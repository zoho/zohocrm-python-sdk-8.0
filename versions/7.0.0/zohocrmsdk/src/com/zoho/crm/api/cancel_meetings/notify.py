try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Notify(object):
	def __init__(self):
		"""Creates an instance of Notify"""

		self.__send_cancelling_mail = None
		self.__key_modified = dict()

	def get_send_cancelling_mail(self):
		"""
		The method to get the send_cancelling_mail

		Returns:
			bool: A bool representing the send_cancelling_mail
		"""

		return self.__send_cancelling_mail

	def set_send_cancelling_mail(self, send_cancelling_mail):
		"""
		The method to set the value to send_cancelling_mail

		Parameters:
			send_cancelling_mail (bool) : A bool representing the send_cancelling_mail
		"""

		if send_cancelling_mail is not None and not isinstance(send_cancelling_mail, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: send_cancelling_mail EXPECTED TYPE: bool', None, None)
		
		self.__send_cancelling_mail = send_cancelling_mail
		self.__key_modified['send_cancelling_mail'] = 1

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
