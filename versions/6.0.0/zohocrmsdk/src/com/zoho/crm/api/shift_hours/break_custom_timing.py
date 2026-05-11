try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BreakCustomTiming(object):
	def __init__(self):
		"""Creates an instance of BreakCustomTiming"""

		self.__days = None
		self.__break_timing = None
		self.__key_modified = dict()

	def get_days(self):
		"""
		The method to get the days

		Returns:
			string: A string representing the days
		"""

		return self.__days

	def set_days(self, days):
		"""
		The method to set the value to days

		Parameters:
			days (string) : A string representing the days
		"""

		if days is not None and not isinstance(days, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: days EXPECTED TYPE: str', None, None)
		
		self.__days = days
		self.__key_modified['days'] = 1

	def get_break_timing(self):
		"""
		The method to get the break_timing

		Returns:
			list: An instance of list
		"""

		return self.__break_timing

	def set_break_timing(self, break_timing):
		"""
		The method to set the value to break_timing

		Parameters:
			break_timing (list) : An instance of list
		"""

		if break_timing is not None and not isinstance(break_timing, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: break_timing EXPECTED TYPE: list', None, None)
		
		self.__break_timing = break_timing
		self.__key_modified['break_timing'] = 1

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
