try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class DataSharing(object):
	def __init__(self):
		"""Creates an instance of DataSharing"""

		self.__share_type = None
		self.__public_in_portals = None
		self.__module = None
		self.__rule_computation_running = None
		self.__key_modified = dict()

	def get_share_type(self):
		"""
		The method to get the share_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__share_type

	def set_share_type(self, share_type):
		"""
		The method to set the value to share_type

		Parameters:
			share_type (Choice) : An instance of Choice
		"""

		if share_type is not None and not isinstance(share_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: share_type EXPECTED TYPE: Choice', None, None)
		
		self.__share_type = share_type
		self.__key_modified['share_type'] = 1

	def get_public_in_portals(self):
		"""
		The method to get the public_in_portals

		Returns:
			bool: A bool representing the public_in_portals
		"""

		return self.__public_in_portals

	def set_public_in_portals(self, public_in_portals):
		"""
		The method to set the value to public_in_portals

		Parameters:
			public_in_portals (bool) : A bool representing the public_in_portals
		"""

		if public_in_portals is not None and not isinstance(public_in_portals, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: public_in_portals EXPECTED TYPE: bool', None, None)
		
		self.__public_in_portals = public_in_portals
		self.__key_modified['public_in_portals'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.data_sharing.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_rule_computation_running(self):
		"""
		The method to get the rule_computation_running

		Returns:
			bool: A bool representing the rule_computation_running
		"""

		return self.__rule_computation_running

	def set_rule_computation_running(self, rule_computation_running):
		"""
		The method to set the value to rule_computation_running

		Parameters:
			rule_computation_running (bool) : A bool representing the rule_computation_running
		"""

		if rule_computation_running is not None and not isinstance(rule_computation_running, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rule_computation_running EXPECTED TYPE: bool', None, None)
		
		self.__rule_computation_running = rule_computation_running
		self.__key_modified['rule_computation_running'] = 1

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
