try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class History(object):
	def __init__(self):
		"""Creates an instance of History"""

		self.__id = None
		self.__log_time = None
		self.__action = None
		self.__repeat_type = None
		self.__count = None
		self.__file_name = None
		self.__state = None
		self.__done_by = None
		self.__key_modified = dict()

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

	def get_log_time(self):
		"""
		The method to get the log_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__log_time

	def set_log_time(self, log_time):
		"""
		The method to set the value to log_time

		Parameters:
			log_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if log_time is not None and not isinstance(log_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: log_time EXPECTED TYPE: datetime', None, None)
		
		self.__log_time = log_time
		self.__key_modified['log_time'] = 1

	def get_action(self):
		"""
		The method to get the action

		Returns:
			string: A string representing the action
		"""

		return self.__action

	def set_action(self, action):
		"""
		The method to set the value to action

		Parameters:
			action (string) : A string representing the action
		"""

		if action is not None and not isinstance(action, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action EXPECTED TYPE: str', None, None)
		
		self.__action = action
		self.__key_modified['action'] = 1

	def get_repeat_type(self):
		"""
		The method to get the repeat_type

		Returns:
			string: A string representing the repeat_type
		"""

		return self.__repeat_type

	def set_repeat_type(self, repeat_type):
		"""
		The method to set the value to repeat_type

		Parameters:
			repeat_type (string) : A string representing the repeat_type
		"""

		if repeat_type is not None and not isinstance(repeat_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: repeat_type EXPECTED TYPE: str', None, None)
		
		self.__repeat_type = repeat_type
		self.__key_modified['repeat_type'] = 1

	def get_count(self):
		"""
		The method to get the count

		Returns:
			int: An int representing the count
		"""

		return self.__count

	def set_count(self, count):
		"""
		The method to set the value to count

		Parameters:
			count (int) : An int representing the count
		"""

		if count is not None and not isinstance(count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: count EXPECTED TYPE: int', None, None)
		
		self.__count = count
		self.__key_modified['count'] = 1

	def get_file_name(self):
		"""
		The method to get the file_name

		Returns:
			string: A string representing the file_name
		"""

		return self.__file_name

	def set_file_name(self, file_name):
		"""
		The method to set the value to file_name

		Parameters:
			file_name (string) : A string representing the file_name
		"""

		if file_name is not None and not isinstance(file_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_name EXPECTED TYPE: str', None, None)
		
		self.__file_name = file_name
		self.__key_modified['file_name'] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string representing the state
		"""

		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string representing the state
		"""

		if state is not None and not isinstance(state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: str', None, None)
		
		self.__state = state
		self.__key_modified['state'] = 1

	def get_done_by(self):
		"""
		The method to get the done_by

		Returns:
			Requester: An instance of Requester
		"""

		return self.__done_by

	def set_done_by(self, done_by):
		"""
		The method to set the value to done_by

		Parameters:
			done_by (Requester) : An instance of Requester
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.backup.requester import Requester
		except Exception:
			from .requester import Requester

		if done_by is not None and not isinstance(done_by, Requester):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: done_by EXPECTED TYPE: Requester', None, None)
		
		self.__done_by = done_by
		self.__key_modified['done_by'] = 1

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
