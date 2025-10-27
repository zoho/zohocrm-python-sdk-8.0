try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ConflictWrapper(object):
	def __init__(self):
		"""Creates an instance of ConflictWrapper"""

		self.__conflict_id = None
		self.__key_modified = dict()

	def get_conflict_id(self):
		"""
		The method to get the conflict_id

		Returns:
			string: A string representing the conflict_id
		"""

		return self.__conflict_id

	def set_conflict_id(self, conflict_id):
		"""
		The method to set the value to conflict_id

		Parameters:
			conflict_id (string) : A string representing the conflict_id
		"""

		if conflict_id is not None and not isinstance(conflict_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: conflict_id EXPECTED TYPE: str', None, None)
		
		self.__conflict_id = conflict_id
		self.__key_modified['conflict_id'] = 1

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
