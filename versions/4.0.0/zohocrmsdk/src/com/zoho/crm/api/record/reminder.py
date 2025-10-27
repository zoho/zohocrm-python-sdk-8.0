try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Reminder(object):
	def __init__(self):
		"""Creates an instance of Reminder"""

		self.__period = None
		self.__unit = None
		self.__time = None
		self.__key_modified = dict()

	def get_period(self):
		"""
		The method to get the period

		Returns:
			string: A string representing the period
		"""

		return self.__period

	def set_period(self, period):
		"""
		The method to set the value to period

		Parameters:
			period (string) : A string representing the period
		"""

		if period is not None and not isinstance(period, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: period EXPECTED TYPE: str', None, None)
		
		self.__period = period
		self.__key_modified['period'] = 1

	def get_unit(self):
		"""
		The method to get the unit

		Returns:
			int: An int representing the unit
		"""

		return self.__unit

	def set_unit(self, unit):
		"""
		The method to set the value to unit

		Parameters:
			unit (int) : An int representing the unit
		"""

		if unit is not None and not isinstance(unit, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: unit EXPECTED TYPE: int', None, None)
		
		self.__unit = unit
		self.__key_modified['unit'] = 1

	def get_time(self):
		"""
		The method to get the time

		Returns:
			string: A string representing the time
		"""

		return self.__time

	def set_time(self, time):
		"""
		The method to set the value to time

		Parameters:
			time (string) : A string representing the time
		"""

		if time is not None and not isinstance(time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: time EXPECTED TYPE: str', None, None)
		
		self.__time = time
		self.__key_modified['time'] = 1

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
