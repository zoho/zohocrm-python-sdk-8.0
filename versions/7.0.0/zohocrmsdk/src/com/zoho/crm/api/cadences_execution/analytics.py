try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Analytics(object):
	def __init__(self):
		"""Creates an instance of Analytics"""

		self.__analytics = None
		self.__parent_follow_up = None
		self.__action = None
		self.__id = None
		self.__key_modified = dict()

	def get_analytics(self):
		"""
		The method to get the analytics

		Returns:
			dict: An instance of dict
		"""

		return self.__analytics

	def set_analytics(self, analytics):
		"""
		The method to set the value to analytics

		Parameters:
			analytics (dict) : An instance of dict
		"""

		if analytics is not None and not isinstance(analytics, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: analytics EXPECTED TYPE: dict', None, None)
		
		self.__analytics = analytics
		self.__key_modified['analytics'] = 1

	def get_parent_follow_up(self):
		"""
		The method to get the parent_follow_up

		Returns:
			ParentFollowUp: An instance of ParentFollowUp
		"""

		return self.__parent_follow_up

	def set_parent_follow_up(self, parent_follow_up):
		"""
		The method to set the value to parent_follow_up

		Parameters:
			parent_follow_up (ParentFollowUp) : An instance of ParentFollowUp
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences_execution.parent_follow_up import ParentFollowUp
		except Exception:
			from .parent_follow_up import ParentFollowUp

		if parent_follow_up is not None and not isinstance(parent_follow_up, ParentFollowUp):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_follow_up EXPECTED TYPE: ParentFollowUp', None, None)
		
		self.__parent_follow_up = parent_follow_up
		self.__key_modified['parent_follow_up'] = 1

	def get_action(self):
		"""
		The method to get the action

		Returns:
			Action: An instance of Action
		"""

		return self.__action

	def set_action(self, action):
		"""
		The method to set the value to action

		Parameters:
			action (Action) : An instance of Action
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences_execution.action import Action
		except Exception:
			from .action import Action

		if action is not None and not isinstance(action, Action):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action EXPECTED TYPE: Action', None, None)
		
		self.__action = action
		self.__key_modified['action'] = 1

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
