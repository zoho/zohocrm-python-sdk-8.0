try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Detail(object):
	def __init__(self):
		"""Creates an instance of Detail"""

		self.__available_count = None
		self.__limits = None
		self.__used_count = None
		self.__key_modified = dict()

	def get_available_count(self):
		"""
		The method to get the available_count

		Returns:
			Limit: An instance of Limit
		"""

		return self.__available_count

	def set_available_count(self, available_count):
		"""
		The method to set the value to available_count

		Parameters:
			available_count (Limit) : An instance of Limit
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.features.limit import Limit
		except Exception:
			from .limit import Limit

		if available_count is not None and not isinstance(available_count, Limit):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: available_count EXPECTED TYPE: Limit', None, None)
		
		self.__available_count = available_count
		self.__key_modified['available_count'] = 1

	def get_limits(self):
		"""
		The method to get the limits

		Returns:
			Limit: An instance of Limit
		"""

		return self.__limits

	def set_limits(self, limits):
		"""
		The method to set the value to limits

		Parameters:
			limits (Limit) : An instance of Limit
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.features.limit import Limit
		except Exception:
			from .limit import Limit

		if limits is not None and not isinstance(limits, Limit):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: limits EXPECTED TYPE: Limit', None, None)
		
		self.__limits = limits
		self.__key_modified['limits'] = 1

	def get_used_count(self):
		"""
		The method to get the used_count

		Returns:
			Limit: An instance of Limit
		"""

		return self.__used_count

	def set_used_count(self, used_count):
		"""
		The method to set the value to used_count

		Parameters:
			used_count (Limit) : An instance of Limit
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.features.limit import Limit
		except Exception:
			from .limit import Limit

		if used_count is not None and not isinstance(used_count, Limit):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: used_count EXPECTED TYPE: Limit', None, None)
		
		self.__used_count = used_count
		self.__key_modified['used_count'] = 1

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
