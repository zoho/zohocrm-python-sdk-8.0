try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class SubformProperty(object):
	def __init__(self):
		"""Creates an instance of SubformProperty"""

		self.__pinned_column = None
		self.__key_modified = dict()

	def get_pinned_column(self):
		"""
		The method to get the pinned_column

		Returns:
			bool: A bool representing the pinned_column
		"""

		return self.__pinned_column

	def set_pinned_column(self, pinned_column):
		"""
		The method to set the value to pinned_column

		Parameters:
			pinned_column (bool) : A bool representing the pinned_column
		"""

		if pinned_column is not None and not isinstance(pinned_column, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pinned_column EXPECTED TYPE: bool', None, None)
		
		self.__pinned_column = pinned_column
		self.__key_modified['pinned_column'] = 1

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
