try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class DoubleOptinDetails(object):
	def __init__(self):
		"""Creates an instance of DoubleOptinDetails"""

		self.__email_template = None
		self.__confirm_page_content = None
		self.__key_modified = dict()

	def get_email_template(self):
		"""
		The method to get the email_template

		Returns:
			DoubleOptinEmailTemplate: An instance of DoubleOptinEmailTemplate
		"""

		return self.__email_template

	def set_email_template(self, email_template):
		"""
		The method to set the value to email_template

		Parameters:
			email_template (DoubleOptinEmailTemplate) : An instance of DoubleOptinEmailTemplate
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.double_optin_email_template import DoubleOptinEmailTemplate
		except Exception:
			from .double_optin_email_template import DoubleOptinEmailTemplate

		if email_template is not None and not isinstance(email_template, DoubleOptinEmailTemplate):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_template EXPECTED TYPE: DoubleOptinEmailTemplate', None, None)
		
		self.__email_template = email_template
		self.__key_modified['email_template'] = 1

	def get_confirm_page_content(self):
		"""
		The method to get the confirm_page_content

		Returns:
			string: A string representing the confirm_page_content
		"""

		return self.__confirm_page_content

	def set_confirm_page_content(self, confirm_page_content):
		"""
		The method to set the value to confirm_page_content

		Parameters:
			confirm_page_content (string) : A string representing the confirm_page_content
		"""

		if confirm_page_content is not None and not isinstance(confirm_page_content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: confirm_page_content EXPECTED TYPE: str', None, None)
		
		self.__confirm_page_content = confirm_page_content
		self.__key_modified['confirm_page_content'] = 1

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
