try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Unique(object):
	def __init__(self):
		"""Creates an instance of Unique"""

		self.__casesensitive = None
		self.__disable = None
		self.__key_modified = dict()

	def get_casesensitive(self):
		"""
		The method to get the casesensitive

		Returns:
			string: A string representing the casesensitive
		"""

		return self.__casesensitive

	def set_casesensitive(self, casesensitive):
		"""
		The method to set the value to casesensitive

		Parameters:
			casesensitive (string) : A string representing the casesensitive
		"""

		if casesensitive is not None and not isinstance(casesensitive, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: casesensitive EXPECTED TYPE: str', None, None)
		
		self.__casesensitive = casesensitive
		self.__key_modified['casesensitive'] = 1

	def get_disable(self):
		"""
		The method to get the disable

		Returns:
			Object: A Object representing the disable
		"""

		return self.__disable

	def set_disable(self, disable):
		"""
		The method to set the value to disable

		Parameters:
			disable (Object) : A Object representing the disable
		"""

		self.__disable = disable
		self.__key_modified['_disable'] = 1

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
