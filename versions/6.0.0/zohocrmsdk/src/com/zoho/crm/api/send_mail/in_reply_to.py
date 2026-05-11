try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class InReplyTo(object):
	def __init__(self):
		"""Creates an instance of InReplyTo"""

		self.__message_id = None
		self.__owner = None
		self.__key_modified = dict()

	def get_message_id(self):
		"""
		The method to get the message_id

		Returns:
			string: A string representing the message_id
		"""

		return self.__message_id

	def set_message_id(self, message_id):
		"""
		The method to set the value to message_id

		Parameters:
			message_id (string) : A string representing the message_id
		"""

		if message_id is not None and not isinstance(message_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message_id EXPECTED TYPE: str', None, None)
		
		self.__message_id = message_id
		self.__key_modified['message_id'] = 1

	def get_owner(self):
		"""
		The method to get the owner

		Returns:
			Owner: An instance of Owner
		"""

		return self.__owner

	def set_owner(self, owner):
		"""
		The method to set the value to owner

		Parameters:
			owner (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.send_mail.owner import Owner
		except Exception:
			from .owner import Owner

		if owner is not None and not isinstance(owner, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: owner EXPECTED TYPE: Owner', None, None)
		
		self.__owner = owner
		self.__key_modified['owner'] = 1

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
