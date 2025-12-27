try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Preference(object):
	def __init__(self):
		"""Creates an instance of Preference"""

		self.__auto_populate_tax = None
		self.__modify_tax_rates = None
		self.__key_modified = dict()

	def get_auto_populate_tax(self):
		"""
		The method to get the auto_populate_tax

		Returns:
			bool: A bool representing the auto_populate_tax
		"""

		return self.__auto_populate_tax

	def set_auto_populate_tax(self, auto_populate_tax):
		"""
		The method to set the value to auto_populate_tax

		Parameters:
			auto_populate_tax (bool) : A bool representing the auto_populate_tax
		"""

		if auto_populate_tax is not None and not isinstance(auto_populate_tax, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: auto_populate_tax EXPECTED TYPE: bool', None, None)
		
		self.__auto_populate_tax = auto_populate_tax
		self.__key_modified['auto_populate_tax'] = 1

	def get_modify_tax_rates(self):
		"""
		The method to get the modify_tax_rates

		Returns:
			bool: A bool representing the modify_tax_rates
		"""

		return self.__modify_tax_rates

	def set_modify_tax_rates(self, modify_tax_rates):
		"""
		The method to set the value to modify_tax_rates

		Parameters:
			modify_tax_rates (bool) : A bool representing the modify_tax_rates
		"""

		if modify_tax_rates is not None and not isinstance(modify_tax_rates, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modify_tax_rates EXPECTED TYPE: bool', None, None)
		
		self.__modify_tax_rates = modify_tax_rates
		self.__key_modified['modify_tax_rates'] = 1

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
