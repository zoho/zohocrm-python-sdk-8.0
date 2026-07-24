try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class EntityScores(object):
	def __init__(self):
		"""Creates an instance of EntityScores"""

		self.__entity = None
		self.__positive_score = None
		self.__touch_point_score = None
		self.__score = None
		self.__negative_score = None
		self.__touch_point_negative_score = None
		self.__scoring_rule = None
		self.__field_states = None
		self.__id = None
		self.__zia_visions = None
		self.__touch_point_positive_score = None
		self.__key_modified = dict()

	def get_entity(self):
		"""
		The method to get the entity

		Returns:
			Entity: An instance of Entity
		"""

		return self.__entity

	def set_entity(self, entity):
		"""
		The method to set the value to entity

		Parameters:
			entity (Entity) : An instance of Entity
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.entity_scores.entity import Entity
		except Exception:
			from .entity import Entity

		if entity is not None and not isinstance(entity, Entity):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: entity EXPECTED TYPE: Entity', None, None)
		
		self.__entity = entity
		self.__key_modified['Entity'] = 1

	def get_positive_score(self):
		"""
		The method to get the positive_score

		Returns:
			int: An int representing the positive_score
		"""

		return self.__positive_score

	def set_positive_score(self, positive_score):
		"""
		The method to set the value to positive_score

		Parameters:
			positive_score (int) : An int representing the positive_score
		"""

		if positive_score is not None and not isinstance(positive_score, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: positive_score EXPECTED TYPE: int', None, None)
		
		self.__positive_score = positive_score
		self.__key_modified['Positive_Score'] = 1

	def get_touch_point_score(self):
		"""
		The method to get the touch_point_score

		Returns:
			int: An int representing the touch_point_score
		"""

		return self.__touch_point_score

	def set_touch_point_score(self, touch_point_score):
		"""
		The method to set the value to touch_point_score

		Parameters:
			touch_point_score (int) : An int representing the touch_point_score
		"""

		if touch_point_score is not None and not isinstance(touch_point_score, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: touch_point_score EXPECTED TYPE: int', None, None)
		
		self.__touch_point_score = touch_point_score
		self.__key_modified['Touch_Point_Score'] = 1

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
		self.__key_modified['Score'] = 1

	def get_negative_score(self):
		"""
		The method to get the negative_score

		Returns:
			int: An int representing the negative_score
		"""

		return self.__negative_score

	def set_negative_score(self, negative_score):
		"""
		The method to set the value to negative_score

		Parameters:
			negative_score (int) : An int representing the negative_score
		"""

		if negative_score is not None and not isinstance(negative_score, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: negative_score EXPECTED TYPE: int', None, None)
		
		self.__negative_score = negative_score
		self.__key_modified['Negative_Score'] = 1

	def get_touch_point_negative_score(self):
		"""
		The method to get the touch_point_negative_score

		Returns:
			int: An int representing the touch_point_negative_score
		"""

		return self.__touch_point_negative_score

	def set_touch_point_negative_score(self, touch_point_negative_score):
		"""
		The method to set the value to touch_point_negative_score

		Parameters:
			touch_point_negative_score (int) : An int representing the touch_point_negative_score
		"""

		if touch_point_negative_score is not None and not isinstance(touch_point_negative_score, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: touch_point_negative_score EXPECTED TYPE: int', None, None)
		
		self.__touch_point_negative_score = touch_point_negative_score
		self.__key_modified['Touch_Point_Negative_Score'] = 1

	def get_scoring_rule(self):
		"""
		The method to get the scoring_rule

		Returns:
			ScoringRule: An instance of ScoringRule
		"""

		return self.__scoring_rule

	def set_scoring_rule(self, scoring_rule):
		"""
		The method to set the value to scoring_rule

		Parameters:
			scoring_rule (ScoringRule) : An instance of ScoringRule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.entity_scores.scoring_rule import ScoringRule
		except Exception:
			from .scoring_rule import ScoringRule

		if scoring_rule is not None and not isinstance(scoring_rule, ScoringRule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: scoring_rule EXPECTED TYPE: ScoringRule', None, None)
		
		self.__scoring_rule = scoring_rule
		self.__key_modified['Scoring_Rule'] = 1

	def get_field_states(self):
		"""
		The method to get the field_states

		Returns:
			list: An instance of list
		"""

		return self.__field_states

	def set_field_states(self, field_states):
		"""
		The method to set the value to field_states

		Parameters:
			field_states (list) : An instance of list
		"""

		if field_states is not None and not isinstance(field_states, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_states EXPECTED TYPE: list', None, None)
		
		self.__field_states = field_states
		self.__key_modified['$field_states'] = 1

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

	def get_zia_visions(self):
		"""
		The method to get the zia_visions

		Returns:
			bool: A bool representing the zia_visions
		"""

		return self.__zia_visions

	def set_zia_visions(self, zia_visions):
		"""
		The method to set the value to zia_visions

		Parameters:
			zia_visions (bool) : A bool representing the zia_visions
		"""

		if zia_visions is not None and not isinstance(zia_visions, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zia_visions EXPECTED TYPE: bool', None, None)
		
		self.__zia_visions = zia_visions
		self.__key_modified['$zia_visions'] = 1

	def get_touch_point_positive_score(self):
		"""
		The method to get the touch_point_positive_score

		Returns:
			int: An int representing the touch_point_positive_score
		"""

		return self.__touch_point_positive_score

	def set_touch_point_positive_score(self, touch_point_positive_score):
		"""
		The method to set the value to touch_point_positive_score

		Parameters:
			touch_point_positive_score (int) : An int representing the touch_point_positive_score
		"""

		if touch_point_positive_score is not None and not isinstance(touch_point_positive_score, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: touch_point_positive_score EXPECTED TYPE: int', None, None)
		
		self.__touch_point_positive_score = touch_point_positive_score
		self.__key_modified['Touch_Point_Positive_Score'] = 1

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
