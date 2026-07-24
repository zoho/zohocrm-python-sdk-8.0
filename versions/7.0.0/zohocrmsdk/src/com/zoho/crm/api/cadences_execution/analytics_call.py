try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AnalyticsCall(object):
	def __init__(self):
		"""Creates an instance of AnalyticsCall"""

		self.__created_calls_count = None
		self.__cancelled_calls_count = None
		self.__failed_calls_count = None
		self.__completed_calls_count = None
		self.__scheduled_calls_count = None
		self.__calls_count = None
		self.__overdue_calls_count = None
		self.__missed_calls_count = None
		self.__key_modified = dict()

	def get_created_calls_count(self):
		"""
		The method to get the created_calls_count

		Returns:
			int: An int representing the created_calls_count
		"""

		return self.__created_calls_count

	def set_created_calls_count(self, created_calls_count):
		"""
		The method to set the value to created_calls_count

		Parameters:
			created_calls_count (int) : An int representing the created_calls_count
		"""

		if created_calls_count is not None and not isinstance(created_calls_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_calls_count EXPECTED TYPE: int', None, None)
		
		self.__created_calls_count = created_calls_count
		self.__key_modified['created_calls_count'] = 1

	def get_cancelled_calls_count(self):
		"""
		The method to get the cancelled_calls_count

		Returns:
			int: An int representing the cancelled_calls_count
		"""

		return self.__cancelled_calls_count

	def set_cancelled_calls_count(self, cancelled_calls_count):
		"""
		The method to set the value to cancelled_calls_count

		Parameters:
			cancelled_calls_count (int) : An int representing the cancelled_calls_count
		"""

		if cancelled_calls_count is not None and not isinstance(cancelled_calls_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cancelled_calls_count EXPECTED TYPE: int', None, None)
		
		self.__cancelled_calls_count = cancelled_calls_count
		self.__key_modified['cancelled_calls_count'] = 1

	def get_failed_calls_count(self):
		"""
		The method to get the failed_calls_count

		Returns:
			int: An int representing the failed_calls_count
		"""

		return self.__failed_calls_count

	def set_failed_calls_count(self, failed_calls_count):
		"""
		The method to set the value to failed_calls_count

		Parameters:
			failed_calls_count (int) : An int representing the failed_calls_count
		"""

		if failed_calls_count is not None and not isinstance(failed_calls_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: failed_calls_count EXPECTED TYPE: int', None, None)
		
		self.__failed_calls_count = failed_calls_count
		self.__key_modified['failed_calls_count'] = 1

	def get_completed_calls_count(self):
		"""
		The method to get the completed_calls_count

		Returns:
			int: An int representing the completed_calls_count
		"""

		return self.__completed_calls_count

	def set_completed_calls_count(self, completed_calls_count):
		"""
		The method to set the value to completed_calls_count

		Parameters:
			completed_calls_count (int) : An int representing the completed_calls_count
		"""

		if completed_calls_count is not None and not isinstance(completed_calls_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: completed_calls_count EXPECTED TYPE: int', None, None)
		
		self.__completed_calls_count = completed_calls_count
		self.__key_modified['completed_calls_count'] = 1

	def get_scheduled_calls_count(self):
		"""
		The method to get the scheduled_calls_count

		Returns:
			int: An int representing the scheduled_calls_count
		"""

		return self.__scheduled_calls_count

	def set_scheduled_calls_count(self, scheduled_calls_count):
		"""
		The method to set the value to scheduled_calls_count

		Parameters:
			scheduled_calls_count (int) : An int representing the scheduled_calls_count
		"""

		if scheduled_calls_count is not None and not isinstance(scheduled_calls_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: scheduled_calls_count EXPECTED TYPE: int', None, None)
		
		self.__scheduled_calls_count = scheduled_calls_count
		self.__key_modified['scheduled_calls_count'] = 1

	def get_calls_count(self):
		"""
		The method to get the calls_count

		Returns:
			int: An int representing the calls_count
		"""

		return self.__calls_count

	def set_calls_count(self, calls_count):
		"""
		The method to set the value to calls_count

		Parameters:
			calls_count (int) : An int representing the calls_count
		"""

		if calls_count is not None and not isinstance(calls_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: calls_count EXPECTED TYPE: int', None, None)
		
		self.__calls_count = calls_count
		self.__key_modified['calls_count'] = 1

	def get_overdue_calls_count(self):
		"""
		The method to get the overdue_calls_count

		Returns:
			int: An int representing the overdue_calls_count
		"""

		return self.__overdue_calls_count

	def set_overdue_calls_count(self, overdue_calls_count):
		"""
		The method to set the value to overdue_calls_count

		Parameters:
			overdue_calls_count (int) : An int representing the overdue_calls_count
		"""

		if overdue_calls_count is not None and not isinstance(overdue_calls_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: overdue_calls_count EXPECTED TYPE: int', None, None)
		
		self.__overdue_calls_count = overdue_calls_count
		self.__key_modified['overdue_calls_count'] = 1

	def get_missed_calls_count(self):
		"""
		The method to get the missed_calls_count

		Returns:
			int: An int representing the missed_calls_count
		"""

		return self.__missed_calls_count

	def set_missed_calls_count(self, missed_calls_count):
		"""
		The method to set the value to missed_calls_count

		Parameters:
			missed_calls_count (int) : An int representing the missed_calls_count
		"""

		if missed_calls_count is not None and not isinstance(missed_calls_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: missed_calls_count EXPECTED TYPE: int', None, None)
		
		self.__missed_calls_count = missed_calls_count
		self.__key_modified['missed_calls_count'] = 1

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
