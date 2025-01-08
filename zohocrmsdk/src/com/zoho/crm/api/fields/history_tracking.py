try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class HistoryTracking(object):
	def __init__(self):
		"""Creates an instance of HistoryTracking"""

		self.__module = None
		self.__duration_configured_field = None
		self.__key_modified = dict()

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

	def get_duration_configured_field(self):
		"""
		The method to get the duration_configured_field

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__duration_configured_field

	def set_duration_configured_field(self, duration_configured_field):
		"""
		The method to set the value to duration_configured_field

		Parameters:
			duration_configured_field (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
		except Exception:
			from ..modules import MinifiedModule

		if duration_configured_field is not None and not isinstance(duration_configured_field, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: duration_configured_field EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__duration_configured_field = duration_configured_field
		self.__key_modified['duration_configured_field'] = 1

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
