try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.global_picklists.replaced_response_handler import ReplacedResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .replaced_response_handler import ReplacedResponseHandler


class ReplacedResponseWrapper(ReplacedResponseHandler):
	def __init__(self):
		"""Creates an instance of ReplacedResponseWrapper"""
		super().__init__()

		self.__replaced_values = None
		self.__key_modified = dict()

	def get_replaced_values(self):
		"""
		The method to get the replaced_values

		Returns:
			list: An instance of list
		"""

		return self.__replaced_values

	def set_replaced_values(self, replaced_values):
		"""
		The method to set the value to replaced_values

		Parameters:
			replaced_values (list) : An instance of list
		"""

		if replaced_values is not None and not isinstance(replaced_values, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: replaced_values EXPECTED TYPE: list', None, None)
		
		self.__replaced_values = replaced_values
		self.__key_modified['replaced_values'] = 1

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
