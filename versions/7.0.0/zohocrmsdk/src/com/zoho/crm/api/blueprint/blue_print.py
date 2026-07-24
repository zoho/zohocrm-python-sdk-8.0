try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BluePrint(object):
	def __init__(self):
		"""Creates an instance of BluePrint"""

		self.__transition_id = None
		self.__data = None
		self.__process_info = None
		self.__transitions = None
		self.__key_modified = dict()

	def get_transition_id(self):
		"""
		The method to get the transition_id

		Returns:
			string: A string representing the transition_id
		"""

		return self.__transition_id

	def set_transition_id(self, transition_id):
		"""
		The method to set the value to transition_id

		Parameters:
			transition_id (string) : A string representing the transition_id
		"""

		if transition_id is not None and not isinstance(transition_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: transition_id EXPECTED TYPE: str', None, None)
		
		self.__transition_id = transition_id
		self.__key_modified['transition_id'] = 1

	def get_data(self):
		"""
		The method to get the data

		Returns:
			Record: An instance of Record
		"""

		return self.__data

	def set_data(self, data):
		"""
		The method to set the value to data

		Parameters:
			data (Record) : An instance of Record
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record import Record
		except Exception:
			from ..record import Record

		if data is not None and not isinstance(data, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data EXPECTED TYPE: Record', None, None)
		
		self.__data = data
		self.__key_modified['data'] = 1

	def get_process_info(self):
		"""
		The method to get the process_info

		Returns:
			ProcessInfo: An instance of ProcessInfo
		"""

		return self.__process_info

	def set_process_info(self, process_info):
		"""
		The method to set the value to process_info

		Parameters:
			process_info (ProcessInfo) : An instance of ProcessInfo
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.process_info import ProcessInfo
		except Exception:
			from .process_info import ProcessInfo

		if process_info is not None and not isinstance(process_info, ProcessInfo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: process_info EXPECTED TYPE: ProcessInfo', None, None)
		
		self.__process_info = process_info
		self.__key_modified['process_info'] = 1

	def get_transitions(self):
		"""
		The method to get the transitions

		Returns:
			list: An instance of list
		"""

		return self.__transitions

	def set_transitions(self, transitions):
		"""
		The method to set the value to transitions

		Parameters:
			transitions (list) : An instance of list
		"""

		if transitions is not None and not isinstance(transitions, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: transitions EXPECTED TYPE: list', None, None)
		
		self.__transitions = transitions
		self.__key_modified['transitions'] = 1

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
