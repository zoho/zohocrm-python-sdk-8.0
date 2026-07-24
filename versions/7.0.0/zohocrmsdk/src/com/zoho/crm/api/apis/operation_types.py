try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class OperationTypes(object):
	def __init__(self):
		"""Creates an instance of OperationTypes"""

		self.__method = None
		self.__oauth_scope = None
		self.__max_credits = None
		self.__min_credits = None
		self.__key_modified = dict()

	def get_method(self):
		"""
		The method to get the method

		Returns:
			string: A string representing the method
		"""

		return self.__method

	def set_method(self, method):
		"""
		The method to set the value to method

		Parameters:
			method (string) : A string representing the method
		"""

		if method is not None and not isinstance(method, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: method EXPECTED TYPE: str', None, None)
		
		self.__method = method
		self.__key_modified['method'] = 1

	def get_oauth_scope(self):
		"""
		The method to get the oauth_scope

		Returns:
			string: A string representing the oauth_scope
		"""

		return self.__oauth_scope

	def set_oauth_scope(self, oauth_scope):
		"""
		The method to set the value to oauth_scope

		Parameters:
			oauth_scope (string) : A string representing the oauth_scope
		"""

		if oauth_scope is not None and not isinstance(oauth_scope, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: oauth_scope EXPECTED TYPE: str', None, None)
		
		self.__oauth_scope = oauth_scope
		self.__key_modified['oauth_scope'] = 1

	def get_max_credits(self):
		"""
		The method to get the max_credits

		Returns:
			int: An int representing the max_credits
		"""

		return self.__max_credits

	def set_max_credits(self, max_credits):
		"""
		The method to set the value to max_credits

		Parameters:
			max_credits (int) : An int representing the max_credits
		"""

		if max_credits is not None and not isinstance(max_credits, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: max_credits EXPECTED TYPE: int', None, None)
		
		self.__max_credits = max_credits
		self.__key_modified['max_credits'] = 1

	def get_min_credits(self):
		"""
		The method to get the min_credits

		Returns:
			int: An int representing the min_credits
		"""

		return self.__min_credits

	def set_min_credits(self, min_credits):
		"""
		The method to set the value to min_credits

		Parameters:
			min_credits (int) : An int representing the min_credits
		"""

		if min_credits is not None and not isinstance(min_credits, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: min_credits EXPECTED TYPE: int', None, None)
		
		self.__min_credits = min_credits
		self.__key_modified['min_credits'] = 1

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
