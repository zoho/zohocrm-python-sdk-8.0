try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Query(object):
	def __init__(self):
		"""Creates an instance of Query"""

		self.__module = None
		self.__cvid = None
		self.__fields = None
		self.__page = None
		self.__criteria = None
		self.__file_type = None
		self.__page_token = None
		self.__key_modified = dict()

	def get_module(self):
		"""
		The method to get the module

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
		except Exception:
			from ..modules import MinifiedModule

		if module is not None and not isinstance(module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_cvid(self):
		"""
		The method to get the cvid

		Returns:
			int: An int representing the cvid
		"""

		return self.__cvid

	def set_cvid(self, cvid):
		"""
		The method to set the value to cvid

		Parameters:
			cvid (int) : An int representing the cvid
		"""

		if cvid is not None and not isinstance(cvid, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cvid EXPECTED TYPE: int', None, None)
		
		self.__cvid = cvid
		self.__key_modified['cvid'] = 1

	def get_fields(self):
		"""
		The method to get the fields

		Returns:
			list: An instance of list
		"""

		return self.__fields

	def set_fields(self, fields):
		"""
		The method to set the value to fields

		Parameters:
			fields (list) : An instance of list
		"""

		if fields is not None and not isinstance(fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: list', None, None)
		
		self.__fields = fields
		self.__key_modified['fields'] = 1

	def get_page(self):
		"""
		The method to get the page

		Returns:
			int: An int representing the page
		"""

		return self.__page

	def set_page(self, page):
		"""
		The method to set the value to page

		Parameters:
			page (int) : An int representing the page
		"""

		if page is not None and not isinstance(page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: page EXPECTED TYPE: int', None, None)
		
		self.__page = page
		self.__key_modified['page'] = 1

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_read.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

	def get_file_type(self):
		"""
		The method to get the file_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__file_type

	def set_file_type(self, file_type):
		"""
		The method to set the value to file_type

		Parameters:
			file_type (Choice) : An instance of Choice
		"""

		if file_type is not None and not isinstance(file_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_type EXPECTED TYPE: Choice', None, None)
		
		self.__file_type = file_type
		self.__key_modified['file_type'] = 1

	def get_page_token(self):
		"""
		The method to get the page_token

		Returns:
			string: A string representing the page_token
		"""

		return self.__page_token

	def set_page_token(self, page_token):
		"""
		The method to set the value to page_token

		Parameters:
			page_token (string) : A string representing the page_token
		"""

		if page_token is not None and not isinstance(page_token, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: page_token EXPECTED TYPE: str', None, None)
		
		self.__page_token = page_token
		self.__key_modified['page_token'] = 1

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
