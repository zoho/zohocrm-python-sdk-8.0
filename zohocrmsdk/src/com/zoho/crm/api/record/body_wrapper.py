try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__data = None
		self.__trigger = None
		self.__process = None
		self.__duplicate_check_fields = None
		self.__wf_trigger = None
		self.__lar_id = None
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

	def get_trigger(self):
		"""
		The method to get the trigger

		Returns:
			list: An instance of list
		"""

		return self.__trigger

	def set_trigger(self, trigger):
		"""
		The method to set the value to trigger

		Parameters:
			trigger (list) : An instance of list
		"""

		if trigger is not None and not isinstance(trigger, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: trigger EXPECTED TYPE: list', None, None)
		
		self.__trigger = trigger
		self.__key_modified['trigger'] = 1

	def get_process(self):
		"""
		The method to get the process

		Returns:
			list: An instance of list
		"""

		return self.__process

	def set_process(self, process):
		"""
		The method to set the value to process

		Parameters:
			process (list) : An instance of list
		"""

		if process is not None and not isinstance(process, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: process EXPECTED TYPE: list', None, None)
		
		self.__process = process
		self.__key_modified['process'] = 1

	def get_duplicate_check_fields(self):
		"""
		The method to get the duplicate_check_fields

		Returns:
			list: An instance of list
		"""

		return self.__duplicate_check_fields

	def set_duplicate_check_fields(self, duplicate_check_fields):
		"""
		The method to set the value to duplicate_check_fields

		Parameters:
			duplicate_check_fields (list) : An instance of list
		"""

		if duplicate_check_fields is not None and not isinstance(duplicate_check_fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: duplicate_check_fields EXPECTED TYPE: list', None, None)
		
		self.__duplicate_check_fields = duplicate_check_fields
		self.__key_modified['duplicate_check_fields'] = 1

	def get_wf_trigger(self):
		"""
		The method to get the wf_trigger

		Returns:
			string: A string representing the wf_trigger
		"""

		return self.__wf_trigger

	def set_wf_trigger(self, wf_trigger):
		"""
		The method to set the value to wf_trigger

		Parameters:
			wf_trigger (string) : A string representing the wf_trigger
		"""

		if wf_trigger is not None and not isinstance(wf_trigger, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: wf_trigger EXPECTED TYPE: str', None, None)
		
		self.__wf_trigger = wf_trigger
		self.__key_modified['wf_trigger'] = 1

	def get_lar_id(self):
		"""
		The method to get the lar_id

		Returns:
			string: A string representing the lar_id
		"""

		return self.__lar_id

	def set_lar_id(self, lar_id):
		"""
		The method to set the value to lar_id

		Parameters:
			lar_id (string) : A string representing the lar_id
		"""

		if lar_id is not None and not isinstance(lar_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lar_id EXPECTED TYPE: str', None, None)
		
		self.__lar_id = lar_id
		self.__key_modified['lar_id'] = 1

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
