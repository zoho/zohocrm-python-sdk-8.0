try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AutomationDetail(object):
	def __init__(self):
		"""Creates an instance of AutomationDetail"""

		self.__type = None
		self.__rule = None
		self.__pathfinder = None
		self.__key_modified = dict()

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_rule(self):
		"""
		The method to get the rule

		Returns:
			NameIdStructure: An instance of NameIdStructure
		"""

		return self.__rule

	def set_rule(self, rule):
		"""
		The method to set the value to rule

		Parameters:
			rule (NameIdStructure) : An instance of NameIdStructure
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.name_id_structure import NameIdStructure
		except Exception:
			from .name_id_structure import NameIdStructure

		if rule is not None and not isinstance(rule, NameIdStructure):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rule EXPECTED TYPE: NameIdStructure', None, None)
		
		self.__rule = rule
		self.__key_modified['rule'] = 1

	def get_pathfinder(self):
		"""
		The method to get the pathfinder

		Returns:
			PathFinder: An instance of PathFinder
		"""

		return self.__pathfinder

	def set_pathfinder(self, pathfinder):
		"""
		The method to set the value to pathfinder

		Parameters:
			pathfinder (PathFinder) : An instance of PathFinder
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.path_finder import PathFinder
		except Exception:
			from .path_finder import PathFinder

		if pathfinder is not None and not isinstance(pathfinder, PathFinder):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pathfinder EXPECTED TYPE: PathFinder', None, None)
		
		self.__pathfinder = pathfinder
		self.__key_modified['pathfinder'] = 1

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
