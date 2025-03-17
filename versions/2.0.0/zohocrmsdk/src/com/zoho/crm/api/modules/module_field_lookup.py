try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.fields import Lookup
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from ..fields import Lookup


class ModuleFieldLookup(Lookup):
	def __init__(self):
		"""Creates an instance of ModuleFieldLookup"""
		super().__init__()

		self.__query_details = None
		self.__module = None
		self.__display_label = None
		self.__api_name = None
		self.__id = None
		self.__revalidate_filter_during_edit = None
		self.__show_fields = None
		self.__key_modified = dict()

	def get_query_details(self):
		"""
		The method to get the query_details

		Returns:
			QueryDetails: An instance of QueryDetails
		"""

		return self.__query_details

	def set_query_details(self, query_details):
		"""
		The method to set the value to query_details

		Parameters:
			query_details (QueryDetails) : An instance of QueryDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import QueryDetails
		except Exception:
			from ..fields import QueryDetails

		if query_details is not None and not isinstance(query_details, QueryDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: query_details EXPECTED TYPE: QueryDetails', None, None)
		
		self.__query_details = query_details
		self.__key_modified['query_details'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.modules.minified_module import MinifiedModule
		except Exception:
			from .minified_module import MinifiedModule

		if module is not None and not isinstance(module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

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

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_revalidate_filter_during_edit(self):
		"""
		The method to get the revalidate_filter_during_edit

		Returns:
			bool: A bool representing the revalidate_filter_during_edit
		"""

		return self.__revalidate_filter_during_edit

	def set_revalidate_filter_during_edit(self, revalidate_filter_during_edit):
		"""
		The method to set the value to revalidate_filter_during_edit

		Parameters:
			revalidate_filter_during_edit (bool) : A bool representing the revalidate_filter_during_edit
		"""

		if revalidate_filter_during_edit is not None and not isinstance(revalidate_filter_during_edit, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: revalidate_filter_during_edit EXPECTED TYPE: bool', None, None)
		
		self.__revalidate_filter_during_edit = revalidate_filter_during_edit
		self.__key_modified['revalidate_filter_during_edit'] = 1

	def get_show_fields(self):
		"""
		The method to get the show_fields

		Returns:
			list: An instance of list
		"""

		return self.__show_fields

	def set_show_fields(self, show_fields):
		"""
		The method to set the value to show_fields

		Parameters:
			show_fields (list) : An instance of list
		"""

		if show_fields is not None and not isinstance(show_fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_fields EXPECTED TYPE: list', None, None)
		
		self.__show_fields = show_fields
		self.__key_modified['show_fields'] = 1

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
