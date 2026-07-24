try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class BreakHoursCustomTiming(object):
	def __init__(self):
		"""Creates an instance of BreakHoursCustomTiming"""

		self.__days = None
		self.__business_timing = None
		self.__key_modified = dict()

	def get_days(self):
		"""
		The method to get the days

		Returns:
			Choice: An instance of Choice
		"""

		return self.__days

	def set_days(self, days):
		"""
		The method to set the value to days

		Parameters:
			days (Choice) : An instance of Choice
		"""

		if days is not None and not isinstance(days, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: days EXPECTED TYPE: Choice', None, None)
		
		self.__days = days
		self.__key_modified['days'] = 1

	def get_business_timing(self):
		"""
		The method to get the business_timing

		Returns:
			list: An instance of list
		"""

		return self.__business_timing

	def set_business_timing(self, business_timing):
		"""
		The method to set the value to business_timing

		Parameters:
			business_timing (list) : An instance of list
		"""

		if business_timing is not None and not isinstance(business_timing, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: business_timing EXPECTED TYPE: list', None, None)
		
		self.__business_timing = business_timing
		self.__key_modified['business_timing'] = 1

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
