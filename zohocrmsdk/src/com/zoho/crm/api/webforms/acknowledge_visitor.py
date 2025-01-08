try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AcknowledgeVisitor(object):
	def __init__(self):
		"""Creates an instance of AcknowledgeVisitor"""

		self.__auto_response_rule = None
		self.__template_id = None
		self.__key_modified = dict()

	def get_auto_response_rule(self):
		"""
		The method to get the auto_response_rule

		Returns:
			AutoResponseRule: An instance of AutoResponseRule
		"""

		return self.__auto_response_rule

	def set_auto_response_rule(self, auto_response_rule):
		"""
		The method to set the value to auto_response_rule

		Parameters:
			auto_response_rule (AutoResponseRule) : An instance of AutoResponseRule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.auto_response_rule import AutoResponseRule
		except Exception:
			from .auto_response_rule import AutoResponseRule

		if auto_response_rule is not None and not isinstance(auto_response_rule, AutoResponseRule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: auto_response_rule EXPECTED TYPE: AutoResponseRule', None, None)
		
		self.__auto_response_rule = auto_response_rule
		self.__key_modified['auto_response_rule'] = 1

	def get_template_id(self):
		"""
		The method to get the template_id

		Returns:
			int: An int representing the template_id
		"""

		return self.__template_id

	def set_template_id(self, template_id):
		"""
		The method to set the value to template_id

		Parameters:
			template_id (int) : An int representing the template_id
		"""

		if template_id is not None and not isinstance(template_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: template_id EXPECTED TYPE: int', None, None)
		
		self.__template_id = template_id
		self.__key_modified['template_id'] = 1

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
