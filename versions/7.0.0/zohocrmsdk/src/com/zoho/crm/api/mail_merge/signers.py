try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Signers(object):
	def __init__(self):
		"""Creates an instance of Signers"""

		self.__recipient_name = None
		self.__action_type = None
		self.__recipient = None
		self.__key_modified = dict()

	def get_recipient_name(self):
		"""
		The method to get the recipient_name

		Returns:
			string: A string representing the recipient_name
		"""

		return self.__recipient_name

	def set_recipient_name(self, recipient_name):
		"""
		The method to set the value to recipient_name

		Parameters:
			recipient_name (string) : A string representing the recipient_name
		"""

		if recipient_name is not None and not isinstance(recipient_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: recipient_name EXPECTED TYPE: str', None, None)
		
		self.__recipient_name = recipient_name
		self.__key_modified['recipient_name'] = 1

	def get_action_type(self):
		"""
		The method to get the action_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__action_type

	def set_action_type(self, action_type):
		"""
		The method to set the value to action_type

		Parameters:
			action_type (Choice) : An instance of Choice
		"""

		if action_type is not None and not isinstance(action_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action_type EXPECTED TYPE: Choice', None, None)
		
		self.__action_type = action_type
		self.__key_modified['action_type'] = 1

	def get_recipient(self):
		"""
		The method to get the recipient

		Returns:
			Address: An instance of Address
		"""

		return self.__recipient

	def set_recipient(self, recipient):
		"""
		The method to set the value to recipient

		Parameters:
			recipient (Address) : An instance of Address
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.address import Address
		except Exception:
			from .address import Address

		if recipient is not None and not isinstance(recipient, Address):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: recipient EXPECTED TYPE: Address', None, None)
		
		self.__recipient = recipient
		self.__key_modified['recipient'] = 1

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
