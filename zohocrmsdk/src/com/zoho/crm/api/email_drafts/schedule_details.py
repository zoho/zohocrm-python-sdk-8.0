try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ScheduleDetails(object):
	def __init__(self):
		"""Creates an instance of ScheduleDetails"""

		self.__time = None
		self.__timezone = None
		self.__source = None
		self.__key_modified = dict()

	def get_time(self):
		"""
		The method to get the time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__time

	def set_time(self, time):
		"""
		The method to set the value to time

		Parameters:
			time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if time is not None and not isinstance(time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: time EXPECTED TYPE: datetime', None, None)
		
		self.__time = time
		self.__key_modified['time'] = 1

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

	def get_source(self):
		"""
		The method to get the source

		Returns:
			string: A string representing the source
		"""

		return self.__source

	def set_source(self, source):
		"""
		The method to set the value to source

		Parameters:
			source (string) : A string representing the source
		"""

		if source is not None and not isinstance(source, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: source EXPECTED TYPE: str', None, None)
		
		self.__source = source
		self.__key_modified['source'] = 1

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
