try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ConversionOptions(object):
	def __init__(self):
		"""Creates an instance of ConversionOptions"""

		self.__module_preference = None
		self.__contacts = None
		self.__deals = None
		self.__accounts = None
		self.__preference_field_matched_value = None
		self.__modules_with_multiple_layouts = None
		self.__key_modified = dict()

	def get_module_preference(self):
		"""
		The method to get the module_preference

		Returns:
			Modules: An instance of Modules
		"""

		return self.__module_preference

	def set_module_preference(self, module_preference):
		"""
		The method to set the value to module_preference

		Parameters:
			module_preference (Modules) : An instance of Modules
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import Modules
		except Exception:
			from ..modules import Modules

		if module_preference is not None and not isinstance(module_preference, Modules):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_preference EXPECTED TYPE: Modules', None, None)
		
		self.__module_preference = module_preference
		self.__key_modified['module_preference'] = 1

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

	def get_preference_field_matched_value(self):
		"""
		The method to get the preference_field_matched_value

		Returns:
			PreferenceFieldMatchedValue: An instance of PreferenceFieldMatchedValue
		"""

		return self.__preference_field_matched_value

	def set_preference_field_matched_value(self, preference_field_matched_value):
		"""
		The method to set the value to preference_field_matched_value

		Parameters:
			preference_field_matched_value (PreferenceFieldMatchedValue) : An instance of PreferenceFieldMatchedValue
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.conversion_option.preference_field_matched_value import PreferenceFieldMatchedValue
		except Exception:
			from .preference_field_matched_value import PreferenceFieldMatchedValue

		if preference_field_matched_value is not None and not isinstance(preference_field_matched_value, PreferenceFieldMatchedValue):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: preference_field_matched_value EXPECTED TYPE: PreferenceFieldMatchedValue', None, None)
		
		self.__preference_field_matched_value = preference_field_matched_value
		self.__key_modified['preference_field_matched_value'] = 1

	def get_modules_with_multiple_layouts(self):
		"""
		The method to get the modules_with_multiple_layouts

		Returns:
			list: An instance of list
		"""

		return self.__modules_with_multiple_layouts

	def set_modules_with_multiple_layouts(self, modules_with_multiple_layouts):
		"""
		The method to set the value to modules_with_multiple_layouts

		Parameters:
			modules_with_multiple_layouts (list) : An instance of list
		"""

		if modules_with_multiple_layouts is not None and not isinstance(modules_with_multiple_layouts, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modules_with_multiple_layouts EXPECTED TYPE: list', None, None)
		
		self.__modules_with_multiple_layouts = modules_with_multiple_layouts
		self.__key_modified['modules_with_multiple_layouts'] = 1

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
