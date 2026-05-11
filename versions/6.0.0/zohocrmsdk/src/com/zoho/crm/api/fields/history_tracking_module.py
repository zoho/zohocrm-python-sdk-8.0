try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class HistoryTrackingModule(object):
	def __init__(self):
		"""Creates an instance of HistoryTrackingModule"""

		self.__layout = None
		self.__display_label = None
		self.__api_name = None
		self.__module = None
		self.__id = None
		self.__module_name = None
		self.__key_modified = dict()

	def get_layout(self):
		"""
		The method to get the layout

		Returns:
			Layouts: An instance of Layouts
		"""

		return self.__layout

	def set_layout(self, layout):
		"""
		The method to set the value to layout

		Parameters:
			layout (Layouts) : An instance of Layouts
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts import Layouts
		except Exception:
			from ..layouts import Layouts

		if layout is not None and not isinstance(layout, Layouts):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout EXPECTED TYPE: Layouts', None, None)
		
		self.__layout = layout
		self.__key_modified['layout'] = 1

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

	def get_module(self):
		"""
		The method to get the module

		Returns:
			HistoryTrackingModule: An instance of HistoryTrackingModule
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (HistoryTrackingModule) : An instance of HistoryTrackingModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.history_tracking_module import HistoryTrackingModule
		except Exception:
			from .history_tracking_module import HistoryTrackingModule

		if module is not None and not isinstance(module, HistoryTrackingModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: HistoryTrackingModule', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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

	def get_module_name(self):
		"""
		The method to get the module_name

		Returns:
			string: A string representing the module_name
		"""

		return self.__module_name

	def set_module_name(self, module_name):
		"""
		The method to set the value to module_name

		Parameters:
			module_name (string) : A string representing the module_name
		"""

		if module_name is not None and not isinstance(module_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_name EXPECTED TYPE: str', None, None)
		
		self.__module_name = module_name
		self.__key_modified['module_name'] = 1

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
