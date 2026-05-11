try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Summary(object):
	def __init__(self):
		"""Creates an instance of Summary"""

		self.__task_follow_up_count = None
		self.__call_follow_up_count = None
		self.__email_follow_up_count = None
		self.__key_modified = dict()

	def get_task_follow_up_count(self):
		"""
		The method to get the task_follow_up_count

		Returns:
			int: An int representing the task_follow_up_count
		"""

		return self.__task_follow_up_count

	def set_task_follow_up_count(self, task_follow_up_count):
		"""
		The method to set the value to task_follow_up_count

		Parameters:
			task_follow_up_count (int) : An int representing the task_follow_up_count
		"""

		if task_follow_up_count is not None and not isinstance(task_follow_up_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: task_follow_up_count EXPECTED TYPE: int', None, None)
		
		self.__task_follow_up_count = task_follow_up_count
		self.__key_modified['task_follow_up_count'] = 1

	def get_call_follow_up_count(self):
		"""
		The method to get the call_follow_up_count

		Returns:
			int: An int representing the call_follow_up_count
		"""

		return self.__call_follow_up_count

	def set_call_follow_up_count(self, call_follow_up_count):
		"""
		The method to set the value to call_follow_up_count

		Parameters:
			call_follow_up_count (int) : An int representing the call_follow_up_count
		"""

		if call_follow_up_count is not None and not isinstance(call_follow_up_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: call_follow_up_count EXPECTED TYPE: int', None, None)
		
		self.__call_follow_up_count = call_follow_up_count
		self.__key_modified['call_follow_up_count'] = 1

	def get_email_follow_up_count(self):
		"""
		The method to get the email_follow_up_count

		Returns:
			int: An int representing the email_follow_up_count
		"""

		return self.__email_follow_up_count

	def set_email_follow_up_count(self, email_follow_up_count):
		"""
		The method to set the value to email_follow_up_count

		Parameters:
			email_follow_up_count (int) : An int representing the email_follow_up_count
		"""

		if email_follow_up_count is not None and not isinstance(email_follow_up_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_follow_up_count EXPECTED TYPE: int', None, None)
		
		self.__email_follow_up_count = email_follow_up_count
		self.__key_modified['email_follow_up_count'] = 1

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
