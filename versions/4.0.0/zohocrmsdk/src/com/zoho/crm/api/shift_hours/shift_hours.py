try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ShiftHours(object):
	def __init__(self):
		"""Creates an instance of ShiftHours"""

		self.__same_as_everyday = None
		self.__shift_days = None
		self.__daily_timing = None
		self.__custom_timing = None
		self.__id = None
		self.__break_hours = None
		self.__users = None
		self.__holidays = None
		self.__users_count = None
		self.__timezone = None
		self.__name = None
		self.__key_modified = dict()

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

	def get_shift_days(self):
		"""
		The method to get the shift_days

		Returns:
			list: An instance of list
		"""

		return self.__shift_days

	def set_shift_days(self, shift_days):
		"""
		The method to set the value to shift_days

		Parameters:
			shift_days (list) : An instance of list
		"""

		if shift_days is not None and not isinstance(shift_days, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shift_days EXPECTED TYPE: list', None, None)
		
		self.__shift_days = shift_days
		self.__key_modified['shift_days'] = 1

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

	def get_break_hours(self):
		"""
		The method to get the break_hours

		Returns:
			list: An instance of list
		"""

		return self.__break_hours

	def set_break_hours(self, break_hours):
		"""
		The method to set the value to break_hours

		Parameters:
			break_hours (list) : An instance of list
		"""

		if break_hours is not None and not isinstance(break_hours, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: break_hours EXPECTED TYPE: list', None, None)
		
		self.__break_hours = break_hours
		self.__key_modified['break_hours'] = 1

	def get_users(self):
		"""
		The method to get the users

		Returns:
			list: An instance of list
		"""

		return self.__users

	def set_users(self, users):
		"""
		The method to set the value to users

		Parameters:
			users (list) : An instance of list
		"""

		if users is not None and not isinstance(users, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: users EXPECTED TYPE: list', None, None)
		
		self.__users = users
		self.__key_modified['users'] = 1

	def get_holidays(self):
		"""
		The method to get the holidays

		Returns:
			list: An instance of list
		"""

		return self.__holidays

	def set_holidays(self, holidays):
		"""
		The method to set the value to holidays

		Parameters:
			holidays (list) : An instance of list
		"""

		if holidays is not None and not isinstance(holidays, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: holidays EXPECTED TYPE: list', None, None)
		
		self.__holidays = holidays
		self.__key_modified['holidays'] = 1

	def get_users_count(self):
		"""
		The method to get the users_count

		Returns:
			int: An int representing the users_count
		"""

		return self.__users_count

	def set_users_count(self, users_count):
		"""
		The method to set the value to users_count

		Parameters:
			users_count (int) : An int representing the users_count
		"""

		if users_count is not None and not isinstance(users_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: users_count EXPECTED TYPE: int', None, None)
		
		self.__users_count = users_count
		self.__key_modified['users_count'] = 1

	def get_timezone(self):
		"""
		The method to get the timezone

		Returns:
			string: An instance of string
		"""

		return self.__timezone

	def set_timezone(self, timezone):
		"""
		The method to set the value to timezone

		Parameters:
			timezone (string) : An instance of string
		"""

		self.__timezone = timezone
		self.__key_modified['timezone'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

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
