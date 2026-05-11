try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class LockRecord(object):
	def __init__(self):
		"""Creates an instance of LockRecord"""

		self.__locked_reason__s = None
		self.__key_modified = dict()

	def get_locked_reason__s(self):
		"""
		The method to get the locked_reason__s

		Returns:
			string: A string representing the locked_reason__s
		"""

		return self.__locked_reason__s

	def set_locked_reason__s(self, locked_reason__s):
		"""
		The method to set the value to locked_reason__s

		Parameters:
			locked_reason__s (string) : A string representing the locked_reason__s
		"""

		if locked_reason__s is not None and not isinstance(locked_reason__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locked_reason__s EXPECTED TYPE: str', None, None)
		
		self.__locked_reason__s = locked_reason__s
		self.__key_modified['Locked_Reason__s'] = 1

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
