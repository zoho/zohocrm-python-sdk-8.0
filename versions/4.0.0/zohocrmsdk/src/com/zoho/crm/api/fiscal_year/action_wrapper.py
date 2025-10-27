try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.fiscal_year.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .action_handler import ActionHandler


class ActionWrapper(ActionHandler):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""
		super().__init__()

		self.__fiscal_year = None
		self.__key_modified = dict()

	def get_fiscal_year(self):
		"""
		The method to get the fiscal_year

		Returns:
			ActionResponse: An instance of ActionResponse
		"""

		return self.__fiscal_year

	def set_fiscal_year(self, fiscal_year):
		"""
		The method to set the value to fiscal_year

		Parameters:
			fiscal_year (ActionResponse) : An instance of ActionResponse
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fiscal_year.action_response import ActionResponse
		except Exception:
			from .action_response import ActionResponse

		if fiscal_year is not None and not isinstance(fiscal_year, ActionResponse):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fiscal_year EXPECTED TYPE: ActionResponse', None, None)
		
		self.__fiscal_year = fiscal_year
		self.__key_modified['fiscal_year'] = 1

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
