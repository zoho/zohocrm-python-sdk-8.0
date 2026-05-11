try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ReplacePicklistValues(object):
	def __init__(self):
		"""Creates an instance of ReplacePicklistValues"""

		self.__new_value = None
		self.__old_value = None
		self.__key_modified = dict()

	def get_new_value(self):
		"""
		The method to get the new_value

		Returns:
			ReplacePicklistValue: An instance of ReplacePicklistValue
		"""

		return self.__new_value

	def set_new_value(self, new_value):
		"""
		The method to set the value to new_value

		Parameters:
			new_value (ReplacePicklistValue) : An instance of ReplacePicklistValue
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.global_picklists.replace_picklist_value import ReplacePicklistValue
		except Exception:
			from .replace_picklist_value import ReplacePicklistValue

		if new_value is not None and not isinstance(new_value, ReplacePicklistValue):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: new_value EXPECTED TYPE: ReplacePicklistValue', None, None)
		
		self.__new_value = new_value
		self.__key_modified['new_value'] = 1

	def get_old_value(self):
		"""
		The method to get the old_value

		Returns:
			ReplacePicklistValue: An instance of ReplacePicklistValue
		"""

		return self.__old_value

	def set_old_value(self, old_value):
		"""
		The method to set the value to old_value

		Parameters:
			old_value (ReplacePicklistValue) : An instance of ReplacePicklistValue
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.global_picklists.replace_picklist_value import ReplacePicklistValue
		except Exception:
			from .replace_picklist_value import ReplacePicklistValue

		if old_value is not None and not isinstance(old_value, ReplacePicklistValue):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: old_value EXPECTED TYPE: ReplacePicklistValue', None, None)
		
		self.__old_value = old_value
		self.__key_modified['old_value'] = 1

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
