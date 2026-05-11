try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.business_hours.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .action_handler import ActionHandler


class ActionWrapper(ActionHandler):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""
		super().__init__()

		self.__business_hours = None
		self.__key_modified = dict()

	def get_business_hours(self):
		"""
		The method to get the business_hours

		Returns:
			ActionResponse: An instance of ActionResponse
		"""

		return self.__business_hours

	def set_business_hours(self, business_hours):
		"""
		The method to set the value to business_hours

		Parameters:
			business_hours (ActionResponse) : An instance of ActionResponse
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.business_hours.action_response import ActionResponse
		except Exception:
			from .action_response import ActionResponse

		if business_hours is not None and not isinstance(business_hours, ActionResponse):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: business_hours EXPECTED TYPE: ActionResponse', None, None)
		
		self.__business_hours = business_hours
		self.__key_modified['business_hours'] = 1

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
