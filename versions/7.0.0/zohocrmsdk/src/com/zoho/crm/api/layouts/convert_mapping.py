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
		self.__invoices = None
		self.__salesorders = None
		self.__key_modified = dict()

	def get_contacts(self):
		"""
		The method to get the contacts

		Returns:
			MinifiedLayout: An instance of MinifiedLayout
		"""

		return self.__contacts

	def set_contacts(self, contacts):
		"""
		The method to set the value to contacts

		Parameters:
			contacts (MinifiedLayout) : An instance of MinifiedLayout
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.minified_layout import MinifiedLayout
		except Exception:
			from .minified_layout import MinifiedLayout

		if contacts is not None and not isinstance(contacts, MinifiedLayout):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contacts EXPECTED TYPE: MinifiedLayout', None, None)
		
		self.__contacts = contacts
		self.__key_modified['Contacts'] = 1

	def get_deals(self):
		"""
		The method to get the deals

		Returns:
			DealLayoutMapping: An instance of DealLayoutMapping
		"""

		return self.__deals

	def set_deals(self, deals):
		"""
		The method to set the value to deals

		Parameters:
			deals (DealLayoutMapping) : An instance of DealLayoutMapping
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.deal_layout_mapping import DealLayoutMapping
		except Exception:
			from .deal_layout_mapping import DealLayoutMapping

		if deals is not None and not isinstance(deals, DealLayoutMapping):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deals EXPECTED TYPE: DealLayoutMapping', None, None)
		
		self.__deals = deals
		self.__key_modified['Deals'] = 1

	def get_accounts(self):
		"""
		The method to get the accounts

		Returns:
			MinifiedLayout: An instance of MinifiedLayout
		"""

		return self.__accounts

	def set_accounts(self, accounts):
		"""
		The method to set the value to accounts

		Parameters:
			accounts (MinifiedLayout) : An instance of MinifiedLayout
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.minified_layout import MinifiedLayout
		except Exception:
			from .minified_layout import MinifiedLayout

		if accounts is not None and not isinstance(accounts, MinifiedLayout):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: accounts EXPECTED TYPE: MinifiedLayout', None, None)
		
		self.__accounts = accounts
		self.__key_modified['Accounts'] = 1

	def get_invoices(self):
		"""
		The method to get the invoices

		Returns:
			MinifiedLayout: An instance of MinifiedLayout
		"""

		return self.__invoices

	def set_invoices(self, invoices):
		"""
		The method to set the value to invoices

		Parameters:
			invoices (MinifiedLayout) : An instance of MinifiedLayout
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.minified_layout import MinifiedLayout
		except Exception:
			from .minified_layout import MinifiedLayout

		if invoices is not None and not isinstance(invoices, MinifiedLayout):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: invoices EXPECTED TYPE: MinifiedLayout', None, None)
		
		self.__invoices = invoices
		self.__key_modified['Invoices'] = 1

	def get_salesorders(self):
		"""
		The method to get the salesorders

		Returns:
			MinifiedLayout: An instance of MinifiedLayout
		"""

		return self.__salesorders

	def set_salesorders(self, salesorders):
		"""
		The method to set the value to salesorders

		Parameters:
			salesorders (MinifiedLayout) : An instance of MinifiedLayout
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.minified_layout import MinifiedLayout
		except Exception:
			from .minified_layout import MinifiedLayout

		if salesorders is not None and not isinstance(salesorders, MinifiedLayout):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: salesorders EXPECTED TYPE: MinifiedLayout', None, None)
		
		self.__salesorders = salesorders
		self.__key_modified['SalesOrders'] = 1

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
