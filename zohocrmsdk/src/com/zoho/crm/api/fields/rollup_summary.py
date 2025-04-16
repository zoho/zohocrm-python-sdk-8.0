try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class RollupSummary(object):
	def __init__(self):
		"""Creates an instance of RollupSummary"""

		self.__return_type = None
		self.__expression = None
		self.__based_on_module = None
		self.__related_list = None
		self.__rollup_based_on = None
		self.__key_modified = dict()

	def get_return_type(self):
		"""
		The method to get the return_type

		Returns:
			string: A string representing the return_type
		"""

		return self.__return_type

	def set_return_type(self, return_type):
		"""
		The method to set the value to return_type

		Parameters:
			return_type (string) : A string representing the return_type
		"""

		if return_type is not None and not isinstance(return_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: return_type EXPECTED TYPE: str', None, None)
		
		self.__return_type = return_type
		self.__key_modified['return_type'] = 1

	def get_expression(self):
		"""
		The method to get the expression

		Returns:
			Expression: An instance of Expression
		"""

		return self.__expression

	def set_expression(self, expression):
		"""
		The method to set the value to expression

		Parameters:
			expression (Expression) : An instance of Expression
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.expression import Expression
		except Exception:
			from .expression import Expression

		if expression is not None and not isinstance(expression, Expression):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: expression EXPECTED TYPE: Expression', None, None)
		
		self.__expression = expression
		self.__key_modified['expression'] = 1

	def get_based_on_module(self):
		"""
		The method to get the based_on_module

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__based_on_module

	def set_based_on_module(self, based_on_module):
		"""
		The method to set the value to based_on_module

		Parameters:
			based_on_module (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
		except Exception:
			from ..modules import MinifiedModule

		if based_on_module is not None and not isinstance(based_on_module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: based_on_module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__based_on_module = based_on_module
		self.__key_modified['based_on_module'] = 1

	def get_related_list(self):
		"""
		The method to get the related_list

		Returns:
			RelatedList: An instance of RelatedList
		"""

		return self.__related_list

	def set_related_list(self, related_list):
		"""
		The method to set the value to related_list

		Parameters:
			related_list (RelatedList) : An instance of RelatedList
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_lists import RelatedList
		except Exception:
			from ..related_lists import RelatedList

		if related_list is not None and not isinstance(related_list, RelatedList):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_list EXPECTED TYPE: RelatedList', None, None)
		
		self.__related_list = related_list
		self.__key_modified['related_list'] = 1

	def get_rollup_based_on(self):
		"""
		The method to get the rollup_based_on

		Returns:
			string: A string representing the rollup_based_on
		"""

		return self.__rollup_based_on

	def set_rollup_based_on(self, rollup_based_on):
		"""
		The method to set the value to rollup_based_on

		Parameters:
			rollup_based_on (string) : A string representing the rollup_based_on
		"""

		if rollup_based_on is not None and not isinstance(rollup_based_on, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rollup_based_on EXPECTED TYPE: str', None, None)
		
		self.__rollup_based_on = rollup_based_on
		self.__key_modified['rollup_based_on'] = 1

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
