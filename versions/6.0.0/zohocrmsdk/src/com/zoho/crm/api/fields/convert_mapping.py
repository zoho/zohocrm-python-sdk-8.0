try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ConvertMapping(object):
	def __init__(self):
		"""Creates an instance of ConvertMapping"""

		self.__contacts = None
		self.__deals = None
		self.__accounts = None
		self.__key_modified = dict()

	def get_contacts(self):
		"""
		The method to get the contacts

		Returns:
			string: A string representing the contacts
		"""

		return self.__contacts

	def set_contacts(self, contacts):
		"""
		The method to set the value to contacts

		Parameters:
			contacts (string) : A string representing the contacts
		"""

		if contacts is not None and not isinstance(contacts, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contacts EXPECTED TYPE: str', None, None)
		
		self.__contacts = contacts
		self.__key_modified['Contacts'] = 1

	def get_deals(self):
		"""
		The method to get the deals

		Returns:
			string: A string representing the deals
		"""

		return self.__deals

	def set_deals(self, deals):
		"""
		The method to set the value to deals

		Parameters:
			deals (string) : A string representing the deals
		"""

		if deals is not None and not isinstance(deals, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deals EXPECTED TYPE: str', None, None)
		
		self.__deals = deals
		self.__key_modified['Deals'] = 1

	def get_accounts(self):
		"""
		The method to get the accounts

		Returns:
			string: A string representing the accounts
		"""

		return self.__accounts

	def set_accounts(self, accounts):
		"""
		The method to set the value to accounts

		Parameters:
			accounts (string) : A string representing the accounts
		"""

		if accounts is not None and not isinstance(accounts, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: accounts EXPECTED TYPE: str', None, None)
		
		self.__accounts = accounts
		self.__key_modified['Accounts'] = 1

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
