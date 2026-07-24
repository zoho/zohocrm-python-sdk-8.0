try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Info(object):
	def __init__(self):
		"""Creates an instance of Info"""

		self.__count = None
		self.__allowed_count = None
		self.__key_modified = dict()

	def get_count(self):
		"""
		The method to get the count

		Returns:
			int: An int representing the count
		"""

		return self.__count

	def set_count(self, count):
		"""
		The method to set the value to count

		Parameters:
			count (int) : An int representing the count
		"""

		if count is not None and not isinstance(count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: count EXPECTED TYPE: int', None, None)
		
		self.__count = count
		self.__key_modified['count'] = 1

	def get_allowed_count(self):
		"""
		The method to get the allowed_count

		Returns:
			int: An int representing the allowed_count
		"""

		return self.__allowed_count

	def set_allowed_count(self, allowed_count):
		"""
		The method to set the value to allowed_count

		Parameters:
			allowed_count (int) : An int representing the allowed_count
		"""

		if allowed_count is not None and not isinstance(allowed_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: allowed_count EXPECTED TYPE: int', None, None)
		
		self.__allowed_count = allowed_count
		self.__key_modified['allowed_count'] = 1

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
