try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class RemindAt(object):
	def __init__(self):
		"""Creates an instance of RemindAt"""

		self.__alarm = None
		self.__key_modified = dict()

	def get_alarm(self):
		"""
		The method to get the alarm

		Returns:
			string: A string representing the alarm
		"""

		return self.__alarm

	def set_alarm(self, alarm):
		"""
		The method to set the value to alarm

		Parameters:
			alarm (string) : A string representing the alarm
		"""

		if alarm is not None and not isinstance(alarm, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: alarm EXPECTED TYPE: str', None, None)
		
		self.__alarm = alarm
		self.__key_modified['ALARM'] = 1

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
