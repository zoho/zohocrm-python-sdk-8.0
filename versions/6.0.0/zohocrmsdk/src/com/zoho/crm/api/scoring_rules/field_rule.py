try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FieldRule(object):
	def __init__(self):
		"""Creates an instance of FieldRule"""

		self.__score = None
		self.__criteria = None
		self.__id = None
		self.__key_modified = dict()

	def get_score(self):
		"""
		The method to get the score

		Returns:
			int: An int representing the score
		"""

		return self.__score

	def set_score(self, score):
		"""
		The method to set the value to score

		Parameters:
			score (int) : An int representing the score
		"""

		if score is not None and not isinstance(score, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: score EXPECTED TYPE: int', None, None)
		
		self.__score = score
		self.__key_modified['score'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.scoring_rules.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

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
