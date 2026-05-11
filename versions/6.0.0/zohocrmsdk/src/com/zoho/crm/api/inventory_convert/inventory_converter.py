try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class InventoryConverter(object):
	def __init__(self):
		"""Creates an instance of InventoryConverter"""

		self.__convert_to = None
		self.__key_modified = dict()

	def get_convert_to(self):
		"""
		The method to get the convert_to

		Returns:
			list: An instance of list
		"""

		return self.__convert_to

	def set_convert_to(self, convert_to):
		"""
		The method to set the value to convert_to

		Parameters:
			convert_to (list) : An instance of list
		"""

		if convert_to is not None and not isinstance(convert_to, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: convert_to EXPECTED TYPE: list', None, None)
		
		self.__convert_to = convert_to
		self.__key_modified['convert_to'] = 1

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
