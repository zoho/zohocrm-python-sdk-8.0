try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class PathFinder(object):
	def __init__(self):
		"""Creates an instance of PathFinder"""

		self.__process_entry = None
		self.__process_exit = None
		self.__state = None
		self.__key_modified = dict()

	def get_process_entry(self):
		"""
		The method to get the process_entry

		Returns:
			bool: A bool representing the process_entry
		"""

		return self.__process_entry

	def set_process_entry(self, process_entry):
		"""
		The method to set the value to process_entry

		Parameters:
			process_entry (bool) : A bool representing the process_entry
		"""

		if process_entry is not None and not isinstance(process_entry, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: process_entry EXPECTED TYPE: bool', None, None)
		
		self.__process_entry = process_entry
		self.__key_modified['process_entry'] = 1

	def get_process_exit(self):
		"""
		The method to get the process_exit

		Returns:
			bool: A bool representing the process_exit
		"""

		return self.__process_exit

	def set_process_exit(self, process_exit):
		"""
		The method to set the value to process_exit

		Parameters:
			process_exit (bool) : A bool representing the process_exit
		"""

		if process_exit is not None and not isinstance(process_exit, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: process_exit EXPECTED TYPE: bool', None, None)
		
		self.__process_exit = process_exit
		self.__key_modified['process_exit'] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			State: An instance of State
		"""

		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (State) : An instance of State
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.state import State
		except Exception:
			from .state import State

		if state is not None and not isinstance(state, State):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: State', None, None)
		
		self.__state = state
		self.__key_modified['state'] = 1

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
