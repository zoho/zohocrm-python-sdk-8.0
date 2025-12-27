try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Expression(object):
	def __init__(self):
		"""Creates an instance of Expression"""

		self.__function_parameters = None
		self.__criteria = None
		self.__function = None
		self.__key_modified = dict()

	def get_function_parameters(self):
		"""
		The method to get the function_parameters

		Returns:
			list: An instance of list
		"""

		return self.__function_parameters

	def set_function_parameters(self, function_parameters):
		"""
		The method to set the value to function_parameters

		Parameters:
			function_parameters (list) : An instance of list
		"""

		if function_parameters is not None and not isinstance(function_parameters, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: function_parameters EXPECTED TYPE: list', None, None)
		
		self.__function_parameters = function_parameters
		self.__key_modified['function_parameters'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.fields.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

	def get_function(self):
		"""
		The method to get the function

		Returns:
			string: A string representing the function
		"""

		return self.__function

	def set_function(self, function):
		"""
		The method to set the value to function

		Parameters:
			function (string) : A string representing the function
		"""

		if function is not None and not isinstance(function, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: function EXPECTED TYPE: str', None, None)
		
		self.__function = function
		self.__key_modified['function'] = 1

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
