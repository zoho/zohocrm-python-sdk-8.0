try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class OrgTax(object):
	def __init__(self):
		"""Creates an instance of OrgTax"""

		self.__taxes = None
		self.__preference = None
		self.__key_modified = dict()

	def get_taxes(self):
		"""
		The method to get the taxes

		Returns:
			list: An instance of list
		"""

		return self.__taxes

	def set_taxes(self, taxes):
		"""
		The method to set the value to taxes

		Parameters:
			taxes (list) : An instance of list
		"""

		if taxes is not None and not isinstance(taxes, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: taxes EXPECTED TYPE: list', None, None)
		
		self.__taxes = taxes
		self.__key_modified['taxes'] = 1

	def get_preference(self):
		"""
		The method to get the preference

		Returns:
			Preference: An instance of Preference
		"""

		return self.__preference

	def set_preference(self, preference):
		"""
		The method to set the value to preference

		Parameters:
			preference (Preference) : An instance of Preference
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.taxes.preference import Preference
		except Exception:
			from .preference import Preference

		if preference is not None and not isinstance(preference, Preference):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: preference EXPECTED TYPE: Preference', None, None)
		
		self.__preference = preference
		self.__key_modified['preference'] = 1

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
