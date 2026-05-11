try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FieldHistoryValue(object):
	def __init__(self):
		"""Creates an instance of FieldHistoryValue"""

		self.__new = None
		self.__old = None
		self.__key_modified = dict()

	def get_new(self):
		"""
		The method to get the new

		Returns:
			string: A string representing the new
		"""

		return self.__new

	def set_new(self, new):
		"""
		The method to set the value to new

		Parameters:
			new (string) : A string representing the new
		"""

		if new is not None and not isinstance(new, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: new EXPECTED TYPE: str', None, None)
		
		self.__new = new
		self.__key_modified['new'] = 1

	def get_old(self):
		"""
		The method to get the old

		Returns:
			string: A string representing the old
		"""

		return self.__old

	def set_old(self, old):
		"""
		The method to set the value to old

		Parameters:
			old (string) : A string representing the old
		"""

		if old is not None and not isinstance(old, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: old EXPECTED TYPE: str', None, None)
		
		self.__old = old
		self.__key_modified['old'] = 1

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
