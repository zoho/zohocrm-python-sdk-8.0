try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class BusinessHours(object):
	def __init__(self):
		"""Creates an instance of BusinessHours"""

		self.__week_starts_on = None
		self.__type = None
		self.__id = None
		self.__business_days = None
		self.__same_as_everyday = None
		self.__daily_timing = None
		self.__custom_timing = None
		self.__key_modified = dict()

	def get_week_starts_on(self):
		"""
		The method to get the week_starts_on

		Returns:
			Choice: An instance of Choice
		"""

		return self.__week_starts_on

	def set_week_starts_on(self, week_starts_on):
		"""
		The method to set the value to week_starts_on

		Parameters:
			week_starts_on (Choice) : An instance of Choice
		"""

		if week_starts_on is not None and not isinstance(week_starts_on, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: week_starts_on EXPECTED TYPE: Choice', None, None)
		
		self.__week_starts_on = week_starts_on
		self.__key_modified['week_starts_on'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (Choice) : An instance of Choice
		"""

		if type is not None and not isinstance(type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: Choice', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

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

	def get_business_days(self):
		"""
		The method to get the business_days

		Returns:
			list: An instance of list
		"""

		return self.__business_days

	def set_business_days(self, business_days):
		"""
		The method to set the value to business_days

		Parameters:
			business_days (list) : An instance of list
		"""

		if business_days is not None and not isinstance(business_days, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: business_days EXPECTED TYPE: list', None, None)
		
		self.__business_days = business_days
		self.__key_modified['business_days'] = 1

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
