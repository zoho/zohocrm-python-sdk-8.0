try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.email_templates.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__email_templates = None
		self.__info = None
		self.__key_modified = dict()

	def get_email_templates(self):
		"""
		The method to get the email_templates

		Returns:
			list: An instance of list
		"""

		return self.__email_templates

	def set_email_templates(self, email_templates):
		"""
		The method to set the value to email_templates

		Parameters:
			email_templates (list) : An instance of list
		"""

		if email_templates is not None and not isinstance(email_templates, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_templates EXPECTED TYPE: list', None, None)
		
		self.__email_templates = email_templates
		self.__key_modified['email_templates'] = 1

	def get_info(self):
		"""
		The method to get the info

		Returns:
			Info: An instance of Info
		"""

		return self.__info

	def set_info(self, info):
		"""
		The method to set the value to info

		Parameters:
			info (Info) : An instance of Info
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_templates.info import Info
		except Exception:
			from .info import Info

		if info is not None and not isinstance(info, Info):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: info EXPECTED TYPE: Info', None, None)
		
		self.__info = info
		self.__key_modified['info'] = 1

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
