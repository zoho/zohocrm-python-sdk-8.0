try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class RulesSummary(object):
	def __init__(self):
		"""Creates an instance of RulesSummary"""

		self.__module = None
		self.__rule_computation_status = None
		self.__rule_count = None
		self.__key_modified = dict()

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Module: An instance of Module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Module) : An instance of Module
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_rule_computation_status(self):
		"""
		The method to get the rule_computation_status

		Returns:
			bool: A bool representing the rule_computation_status
		"""

		return self.__rule_computation_status

	def set_rule_computation_status(self, rule_computation_status):
		"""
		The method to set the value to rule_computation_status

		Parameters:
			rule_computation_status (bool) : A bool representing the rule_computation_status
		"""

		if rule_computation_status is not None and not isinstance(rule_computation_status, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rule_computation_status EXPECTED TYPE: bool', None, None)
		
		self.__rule_computation_status = rule_computation_status
		self.__key_modified['rule_computation_status'] = 1

	def get_rule_count(self):
		"""
		The method to get the rule_count

		Returns:
			int: An int representing the rule_count
		"""

		return self.__rule_count

	def set_rule_count(self, rule_count):
		"""
		The method to set the value to rule_count

		Parameters:
			rule_count (int) : An int representing the rule_count
		"""

		if rule_count is not None and not isinstance(rule_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rule_count EXPECTED TYPE: int', None, None)
		
		self.__rule_count = rule_count
		self.__key_modified['rule_count'] = 1

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
