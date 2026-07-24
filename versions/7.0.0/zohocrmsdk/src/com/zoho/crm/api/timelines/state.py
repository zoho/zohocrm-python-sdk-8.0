try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class State(object):
	def __init__(self):
		"""Creates an instance of State"""

		self.__trigger_type = None
		self.__name = None
		self.__is_last_state = None
		self.__id = None
		self.__key_modified = dict()

	def get_trigger_type(self):
		"""
		The method to get the trigger_type

		Returns:
			string: A string representing the trigger_type
		"""

		return self.__trigger_type

	def set_trigger_type(self, trigger_type):
		"""
		The method to set the value to trigger_type

		Parameters:
			trigger_type (string) : A string representing the trigger_type
		"""

		if trigger_type is not None and not isinstance(trigger_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: trigger_type EXPECTED TYPE: str', None, None)
		
		self.__trigger_type = trigger_type
		self.__key_modified['trigger_type'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_is_last_state(self):
		"""
		The method to get the is_last_state

		Returns:
			bool: A bool representing the is_last_state
		"""

		return self.__is_last_state

	def set_is_last_state(self, is_last_state):
		"""
		The method to set the value to is_last_state

		Parameters:
			is_last_state (bool) : A bool representing the is_last_state
		"""

		if is_last_state is not None and not isinstance(is_last_state, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: is_last_state EXPECTED TYPE: bool', None, None)
		
		self.__is_last_state = is_last_state
		self.__key_modified['is_last_state'] = 1

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
