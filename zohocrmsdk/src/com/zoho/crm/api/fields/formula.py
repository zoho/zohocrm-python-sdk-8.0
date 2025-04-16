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
		self.__assume_default = None
		self.__expression = None
		self.__dynamic = None
		self.__stop_compute_conditionally = None
		self.__stop_compute_expression = None
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

	def get_assume_default(self):
		"""
		The method to get the assume_default

		Returns:
			bool: A bool representing the assume_default
		"""

		return self.__assume_default

	def set_assume_default(self, assume_default):
		"""
		The method to set the value to assume_default

		Parameters:
			assume_default (bool) : A bool representing the assume_default
		"""

		if assume_default is not None and not isinstance(assume_default, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: assume_default EXPECTED TYPE: bool', None, None)
		
		self.__assume_default = assume_default
		self.__key_modified['assume_default'] = 1

	def get_expression(self):
		"""
		The method to get the expression

		Returns:
			string: A string representing the expression
		"""

		return self.__expression

	def set_expression(self, expression):
		"""
		The method to set the value to expression

		Parameters:
			expression (string) : A string representing the expression
		"""

		if expression is not None and not isinstance(expression, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: expression EXPECTED TYPE: str', None, None)
		
		self.__expression = expression
		self.__key_modified['expression'] = 1

	def get_dynamic(self):
		"""
		The method to get the dynamic

		Returns:
			bool: A bool representing the dynamic
		"""

		return self.__dynamic

	def set_dynamic(self, dynamic):
		"""
		The method to set the value to dynamic

		Parameters:
			dynamic (bool) : A bool representing the dynamic
		"""

		if dynamic is not None and not isinstance(dynamic, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: dynamic EXPECTED TYPE: bool', None, None)
		
		self.__dynamic = dynamic
		self.__key_modified['dynamic'] = 1

	def get_stop_compute_conditionally(self):
		"""
		The method to get the stop_compute_conditionally

		Returns:
			bool: A bool representing the stop_compute_conditionally
		"""

		return self.__stop_compute_conditionally

	def set_stop_compute_conditionally(self, stop_compute_conditionally):
		"""
		The method to set the value to stop_compute_conditionally

		Parameters:
			stop_compute_conditionally (bool) : A bool representing the stop_compute_conditionally
		"""

		if stop_compute_conditionally is not None and not isinstance(stop_compute_conditionally, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: stop_compute_conditionally EXPECTED TYPE: bool', None, None)
		
		self.__stop_compute_conditionally = stop_compute_conditionally
		self.__key_modified['stop_compute_conditionally'] = 1

	def get_stop_compute_expression(self):
		"""
		The method to get the stop_compute_expression

		Returns:
			string: A string representing the stop_compute_expression
		"""

		return self.__stop_compute_expression

	def set_stop_compute_expression(self, stop_compute_expression):
		"""
		The method to set the value to stop_compute_expression

		Parameters:
			stop_compute_expression (string) : A string representing the stop_compute_expression
		"""

		if stop_compute_expression is not None and not isinstance(stop_compute_expression, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: stop_compute_expression EXPECTED TYPE: str', None, None)
		
		self.__stop_compute_expression = stop_compute_expression
		self.__key_modified['stop_compute_expression'] = 1

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
