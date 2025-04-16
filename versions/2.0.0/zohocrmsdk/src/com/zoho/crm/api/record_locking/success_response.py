try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
	from zohocrmsdk.src.com.zoho.crm.api.record_locking.action_response import ActionResponse
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants
	from .action_response import ActionResponse


class SuccessResponse(ActionResponse):
	def __init__(self):
		"""Creates an instance of SuccessResponse"""
		super().__init__()

		self.__status = None
		self.__code = None
		self.__duplicate_field = None
		self.__action = None
		self.__message = None
		self.__details = None
		self.__key_modified = dict()

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

	def get_duplicate_field(self):
		"""
		The method to get the duplicate_field

		Returns:
			string: A string representing the duplicate_field
		"""

		return self.__duplicate_field

	def set_duplicate_field(self, duplicate_field):
		"""
		The method to set the value to duplicate_field

		Parameters:
			duplicate_field (string) : A string representing the duplicate_field
		"""

		if duplicate_field is not None and not isinstance(duplicate_field, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: duplicate_field EXPECTED TYPE: str', None, None)
		
		self.__duplicate_field = duplicate_field
		self.__key_modified['duplicate_field'] = 1

	def get_action(self):
		"""
		The method to get the action

		Returns:
			Choice: An instance of Choice
		"""

		return self.__action

	def set_action(self, action):
		"""
		The method to set the value to action

		Parameters:
			action (Choice) : An instance of Choice
		"""

		if action is not None and not isinstance(action, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action EXPECTED TYPE: Choice', None, None)
		
		self.__action = action
		self.__key_modified['action'] = 1

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
