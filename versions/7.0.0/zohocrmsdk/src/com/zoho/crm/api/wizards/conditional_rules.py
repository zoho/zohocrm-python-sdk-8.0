try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class ConditionalRules(object):
	def __init__(self):
		"""Creates an instance of ConditionalRules"""

		self.__query_id = None
		self.__execute_on = None
		self.__criteria = None
		self.__actions = None
		self.__key_modified = dict()

	def get_query_id(self):
		"""
		The method to get the query_id

		Returns:
			int: An int representing the query_id
		"""

		return self.__query_id

	def set_query_id(self, query_id):
		"""
		The method to set the value to query_id

		Parameters:
			query_id (int) : An int representing the query_id
		"""

		if query_id is not None and not isinstance(query_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: query_id EXPECTED TYPE: int', None, None)
		
		self.__query_id = query_id
		self.__key_modified['query_id'] = 1

	def get_execute_on(self):
		"""
		The method to get the execute_on

		Returns:
			Choice: An instance of Choice
		"""

		return self.__execute_on

	def set_execute_on(self, execute_on):
		"""
		The method to set the value to execute_on

		Parameters:
			execute_on (Choice) : An instance of Choice
		"""

		if execute_on is not None and not isinstance(execute_on, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: execute_on EXPECTED TYPE: Choice', None, None)
		
		self.__execute_on = execute_on
		self.__key_modified['execute_on'] = 1

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.wizards.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

	def get_actions(self):
		"""
		The method to get the actions

		Returns:
			list: An instance of list
		"""

		return self.__actions

	def set_actions(self, actions):
		"""
		The method to set the value to actions

		Parameters:
			actions (list) : An instance of list
		"""

		if actions is not None and not isinstance(actions, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actions EXPECTED TYPE: list', None, None)
		
		self.__actions = actions
		self.__key_modified['actions'] = 1

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
