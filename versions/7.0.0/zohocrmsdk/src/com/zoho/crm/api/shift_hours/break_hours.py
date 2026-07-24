try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BreakHours(object):
	def __init__(self):
		"""Creates an instance of BreakHours"""

		self.__break_days = None
		self.__same_as_everyday = None
		self.__daily_timing = None
		self.__custom_timing = None
		self.__id = None
		self.__key_modified = dict()

	def get_break_days(self):
		"""
		The method to get the break_days

		Returns:
			list: An instance of list
		"""

		return self.__break_days

	def set_break_days(self, break_days):
		"""
		The method to set the value to break_days

		Parameters:
			break_days (list) : An instance of list
		"""

		if break_days is not None and not isinstance(break_days, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: break_days EXPECTED TYPE: list', None, None)
		
		self.__break_days = break_days
		self.__key_modified['break_days'] = 1

	def get_same_as_everyday(self):
		"""
		The method to get the same_as_everyday

		Returns:
			bool: A bool representing the same_as_everyday
		"""

		return self.__same_as_everyday

	def set_same_as_everyday(self, same_as_everyday):
		"""
		The method to set the value to same_as_everyday

		Parameters:
			same_as_everyday (bool) : A bool representing the same_as_everyday
		"""

		if same_as_everyday is not None and not isinstance(same_as_everyday, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: same_as_everyday EXPECTED TYPE: bool', None, None)
		
		self.__same_as_everyday = same_as_everyday
		self.__key_modified['same_as_everyday'] = 1

	def get_daily_timing(self):
		"""
		The method to get the daily_timing

		Returns:
			list: An instance of list
		"""

		return self.__daily_timing

	def set_daily_timing(self, daily_timing):
		"""
		The method to set the value to daily_timing

		Parameters:
			daily_timing (list) : An instance of list
		"""

		if daily_timing is not None and not isinstance(daily_timing, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: daily_timing EXPECTED TYPE: list', None, None)
		
		self.__daily_timing = daily_timing
		self.__key_modified['daily_timing'] = 1

	def get_custom_timing(self):
		"""
		The method to get the custom_timing

		Returns:
			list: An instance of list
		"""

		return self.__custom_timing

	def set_custom_timing(self, custom_timing):
		"""
		The method to set the value to custom_timing

		Parameters:
			custom_timing (list) : An instance of list
		"""

		if custom_timing is not None and not isinstance(custom_timing, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: custom_timing EXPECTED TYPE: list', None, None)
		
		self.__custom_timing = custom_timing
		self.__key_modified['custom_timing'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

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
