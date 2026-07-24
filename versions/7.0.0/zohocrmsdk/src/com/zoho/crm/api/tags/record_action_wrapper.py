try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.tags.record_action_handler import RecordActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .record_action_handler import RecordActionHandler


class RecordActionWrapper(RecordActionHandler):
	def __init__(self):
		"""Creates an instance of RecordActionWrapper"""
		super().__init__()

		self.__data = None
		self.__wf_scheduler = None
		self.__success_count = None
		self.__locked_count = None
		self.__key_modified = dict()

	def get_data(self):
		"""
		The method to get the data

		Returns:
			list: An instance of list
		"""

		return self.__data

	def set_data(self, data):
		"""
		The method to set the value to data

		Parameters:
			data (list) : An instance of list
		"""

		if data is not None and not isinstance(data, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data EXPECTED TYPE: list', None, None)
		
		self.__data = data
		self.__key_modified['data'] = 1

	def get_wf_scheduler(self):
		"""
		The method to get the wf_scheduler

		Returns:
			bool: A bool representing the wf_scheduler
		"""

		return self.__wf_scheduler

	def set_wf_scheduler(self, wf_scheduler):
		"""
		The method to set the value to wf_scheduler

		Parameters:
			wf_scheduler (bool) : A bool representing the wf_scheduler
		"""

		if wf_scheduler is not None and not isinstance(wf_scheduler, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: wf_scheduler EXPECTED TYPE: bool', None, None)
		
		self.__wf_scheduler = wf_scheduler
		self.__key_modified['wf_scheduler'] = 1

	def get_success_count(self):
		"""
		The method to get the success_count

		Returns:
			string: A string representing the success_count
		"""

		return self.__success_count

	def set_success_count(self, success_count):
		"""
		The method to set the value to success_count

		Parameters:
			success_count (string) : A string representing the success_count
		"""

		if success_count is not None and not isinstance(success_count, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: success_count EXPECTED TYPE: str', None, None)
		
		self.__success_count = success_count
		self.__key_modified['success_count'] = 1

	def get_locked_count(self):
		"""
		The method to get the locked_count

		Returns:
			string: A string representing the locked_count
		"""

		return self.__locked_count

	def set_locked_count(self, locked_count):
		"""
		The method to set the value to locked_count

		Parameters:
			locked_count (string) : A string representing the locked_count
		"""

		if locked_count is not None and not isinstance(locked_count, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locked_count EXPECTED TYPE: str', None, None)
		
		self.__locked_count = locked_count
		self.__key_modified['locked_count'] = 1

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
