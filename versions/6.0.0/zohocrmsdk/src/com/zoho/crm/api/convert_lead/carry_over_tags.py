try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class CarryOverTags(object):
	def __init__(self):
		"""Creates an instance of CarryOverTags"""

		self.__contacts = None
		self.__accounts = None
		self.__deals = None
		self.__key_modified = dict()

	def get_contacts(self):
		"""
		The method to get the contacts

		Returns:
			list: An instance of list
		"""

		return self.__contacts

	def set_contacts(self, contacts):
		"""
		The method to set the value to contacts

		Parameters:
			contacts (list) : An instance of list
		"""

		if contacts is not None and not isinstance(contacts, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contacts EXPECTED TYPE: list', None, None)
		
		self.__contacts = contacts
		self.__key_modified['Contacts'] = 1

	def get_accounts(self):
		"""
		The method to get the accounts

		Returns:
			list: An instance of list
		"""

		return self.__accounts

	def set_accounts(self, accounts):
		"""
		The method to set the value to accounts

		Parameters:
			accounts (list) : An instance of list
		"""

		if accounts is not None and not isinstance(accounts, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: accounts EXPECTED TYPE: list', None, None)
		
		self.__accounts = accounts
		self.__key_modified['Accounts'] = 1

	def get_deals(self):
		"""
		The method to get the deals

		Returns:
			list: An instance of list
		"""

		return self.__deals

	def set_deals(self, deals):
		"""
		The method to set the value to deals

		Parameters:
			deals (list) : An instance of list
		"""

		if deals is not None and not isinstance(deals, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deals EXPECTED TYPE: list', None, None)
		
		self.__deals = deals
		self.__key_modified['Deals'] = 1

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
