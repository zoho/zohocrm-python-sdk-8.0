try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Formula(object):
	def __init__(self):
		"""Creates an instance of Formula"""

		self.__return_type = None
		self.__expression = None
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
			int: An int representing the expression
		"""

		return self.__expression

	def set_expression(self, expression):
		"""
		The method to set the value to expression

		Parameters:
			expression (int) : An int representing the expression
		"""

		if expression is not None and not isinstance(expression, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: expression EXPECTED TYPE: int', None, None)
		
		self.__expression = expression
		self.__key_modified['expression'] = 1

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
