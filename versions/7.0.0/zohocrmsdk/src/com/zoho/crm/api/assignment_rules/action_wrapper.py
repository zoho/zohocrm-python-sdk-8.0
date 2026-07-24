try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ActionWrapper(object):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""

		self.__assignment_rules = None
		self.__key_modified = dict()

	def get_assignment_rules(self):
		"""
		The method to get the assignment_rules

		Returns:
			list: An instance of list
		"""

		return self.__assignment_rules

	def set_assignment_rules(self, assignment_rules):
		"""
		The method to set the value to assignment_rules

		Parameters:
			assignment_rules (list) : An instance of list
		"""

		if assignment_rules is not None and not isinstance(assignment_rules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: assignment_rules EXPECTED TYPE: list', None, None)
		
		self.__assignment_rules = assignment_rules
		self.__key_modified['assignment_rules'] = 1

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
