try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class ShiftHoliday(object):
	def __init__(self):
		"""Creates an instance of ShiftHoliday"""

		self.__name = None
		self.__date = None
		self.__type = None
		self.__shift_hour = None
		self.__key_modified = dict()

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

	def get_date(self):
		"""
		The method to get the date

		Returns:
			date: An instance of date
		"""

		return self.__date

	def set_date(self, date):
		"""
		The method to set the value to date

		Parameters:
			date (date) : An instance of date
		"""

		from datetime import date as date1

		if date is not None and not isinstance(date, date1):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: date EXPECTED TYPE: date1', None, None)
		
		self.__date = date
		self.__key_modified['date'] = 1

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

	def get_shift_hour(self):
		"""
		The method to get the shift_hour

		Returns:
			ShiftHour: An instance of ShiftHour
		"""

		return self.__shift_hour

	def set_shift_hour(self, shift_hour):
		"""
		The method to set the value to shift_hour

		Parameters:
			shift_hour (ShiftHour) : An instance of ShiftHour
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.shift_hour import ShiftHour
		except Exception:
			from .shift_hour import ShiftHour

		if shift_hour is not None and not isinstance(shift_hour, ShiftHour):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shift_hour EXPECTED TYPE: ShiftHour', None, None)
		
		self.__shift_hour = shift_hour
		self.__key_modified['shift_hour'] = 1

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
