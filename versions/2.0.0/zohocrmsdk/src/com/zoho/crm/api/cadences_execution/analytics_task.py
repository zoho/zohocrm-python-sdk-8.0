try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AnalyticsTask(object):
	def __init__(self):
		"""Creates an instance of AnalyticsTask"""

		self.__open_tasks_count = None
		self.__failed_tasks_count = None
		self.__subject = None
		self.__completed_tasks_count = None
		self.__created_tasks_count = None
		self.__tasks_count = None
		self.__key_modified = dict()

	def get_open_tasks_count(self):
		"""
		The method to get the open_tasks_count

		Returns:
			int: An int representing the open_tasks_count
		"""

		return self.__open_tasks_count

	def set_open_tasks_count(self, open_tasks_count):
		"""
		The method to set the value to open_tasks_count

		Parameters:
			open_tasks_count (int) : An int representing the open_tasks_count
		"""

		if open_tasks_count is not None and not isinstance(open_tasks_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: open_tasks_count EXPECTED TYPE: int', None, None)
		
		self.__open_tasks_count = open_tasks_count
		self.__key_modified['open_tasks_count'] = 1

	def get_failed_tasks_count(self):
		"""
		The method to get the failed_tasks_count

		Returns:
			int: An int representing the failed_tasks_count
		"""

		return self.__failed_tasks_count

	def set_failed_tasks_count(self, failed_tasks_count):
		"""
		The method to set the value to failed_tasks_count

		Parameters:
			failed_tasks_count (int) : An int representing the failed_tasks_count
		"""

		if failed_tasks_count is not None and not isinstance(failed_tasks_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: failed_tasks_count EXPECTED TYPE: int', None, None)
		
		self.__failed_tasks_count = failed_tasks_count
		self.__key_modified['failed_tasks_count'] = 1

	def get_subject(self):
		"""
		The method to get the subject

		Returns:
			string: A string representing the subject
		"""

		return self.__subject

	def set_subject(self, subject):
		"""
		The method to set the value to subject

		Parameters:
			subject (string) : A string representing the subject
		"""

		if subject is not None and not isinstance(subject, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subject EXPECTED TYPE: str', None, None)
		
		self.__subject = subject
		self.__key_modified['subject'] = 1

	def get_completed_tasks_count(self):
		"""
		The method to get the completed_tasks_count

		Returns:
			int: An int representing the completed_tasks_count
		"""

		return self.__completed_tasks_count

	def set_completed_tasks_count(self, completed_tasks_count):
		"""
		The method to set the value to completed_tasks_count

		Parameters:
			completed_tasks_count (int) : An int representing the completed_tasks_count
		"""

		if completed_tasks_count is not None and not isinstance(completed_tasks_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: completed_tasks_count EXPECTED TYPE: int', None, None)
		
		self.__completed_tasks_count = completed_tasks_count
		self.__key_modified['completed_tasks_count'] = 1

	def get_created_tasks_count(self):
		"""
		The method to get the created_tasks_count

		Returns:
			int: An int representing the created_tasks_count
		"""

		return self.__created_tasks_count

	def set_created_tasks_count(self, created_tasks_count):
		"""
		The method to set the value to created_tasks_count

		Parameters:
			created_tasks_count (int) : An int representing the created_tasks_count
		"""

		if created_tasks_count is not None and not isinstance(created_tasks_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_tasks_count EXPECTED TYPE: int', None, None)
		
		self.__created_tasks_count = created_tasks_count
		self.__key_modified['created_tasks_count'] = 1

	def get_tasks_count(self):
		"""
		The method to get the tasks_count

		Returns:
			int: An int representing the tasks_count
		"""

		return self.__tasks_count

	def set_tasks_count(self, tasks_count):
		"""
		The method to set the value to tasks_count

		Parameters:
			tasks_count (int) : An int representing the tasks_count
		"""

		if tasks_count is not None and not isinstance(tasks_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tasks_count EXPECTED TYPE: int', None, None)
		
		self.__tasks_count = tasks_count
		self.__key_modified['tasks_count'] = 1

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
