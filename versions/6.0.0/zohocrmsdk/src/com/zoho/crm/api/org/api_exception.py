try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
	from zohocrmsdk.src.com.zoho.crm.api.org.action_response import ActionResponse
	from zohocrmsdk.src.com.zoho.crm.api.org.response_handler import ResponseHandler
	from zohocrmsdk.src.com.zoho.crm.api.org.action_handler import ActionHandler
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants
	from .action_response import ActionResponse
	from .response_handler import ResponseHandler
	from .action_handler import ActionHandler


class APIException(ActionResponse, ResponseHandler, ActionHandler):
	def __init__(self):
		"""Creates an instance of APIException"""
		super().__init__()

		self.__status = None
		self.__code = None
		self.__message = None
		self.__details = None
		self.__key_modified = dict()
		self.__api_name = None
		self.__json_path = None
		self.__features = None

	def get_status(self):
		"""
		The method to get the status

		Returns:
			Choice: An instance of Choice
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (Choice) : An instance of Choice
		"""

		if status is not None and not isinstance(status, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: Choice', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def get_code(self):
		"""
		The method to get the code

		Returns:
			Choice: An instance of Choice
		"""

		return self.__code

	def set_code(self, code):
		"""
		The method to set the value to code

		Parameters:
			code (Choice) : An instance of Choice
		"""

		if code is not None and not isinstance(code, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: code EXPECTED TYPE: Choice', None, None)
		
		self.__code = code
		self.__key_modified['code'] = 1

	def get_message(self):
		"""
		The method to get the message

		Returns:
			Choice: An instance of Choice
		"""

		return self.__message

	def set_message(self, message):
		"""
		The method to set the value to message

		Parameters:
			message (Choice) : An instance of Choice
		"""

		if message is not None and not isinstance(message, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message EXPECTED TYPE: Choice', None, None)
		
		self.__message = message
		self.__key_modified['message'] = 1

	def get_details(self):
		"""
		The method to get the details

		Returns:
			dict: An instance of dict
		"""

		return self.__details

	def set_details(self, details):
		"""
		The method to set the value to details

		Parameters:
			details (dict) : An instance of dict
		"""

		if details is not None and not isinstance(details, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: details EXPECTED TYPE: dict', None, None)
		
		self.__details = details
		self.__key_modified['details'] = 1

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

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_json_path(self):
		"""
		The method to get the json_path

		Returns:
			string: A string representing the json_path
		"""

		return self.__json_path

	def set_json_path(self, json_path):
		"""
		The method to set the value to json_path

		Parameters:
			json_path (string) : A string representing the json_path
		"""

		if json_path is not None and not isinstance(json_path, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: json_path EXPECTED TYPE: str', None, None)
		
		self.__json_path = json_path
		self.__key_modified['json_path'] = 1

	def get_features(self):
		"""
		The method to get the features

		Returns:
			list: An instance of list
		"""

		return self.__features

	def set_features(self, features):
		"""
		The method to set the value to features

		Parameters:
			features (list) : An instance of list
		"""

		if features is not None and not isinstance(features, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: features EXPECTED TYPE: list', None, None)
		
		self.__features = features
		self.__key_modified['features'] = 1
