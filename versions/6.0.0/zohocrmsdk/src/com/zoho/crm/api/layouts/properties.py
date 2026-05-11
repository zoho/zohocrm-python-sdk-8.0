try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Properties(object):
	def __init__(self):
		"""Creates an instance of Properties"""

		self.__reorder_rows = None
		self.__maximum_rows = None
		self.__tooltip = None
		self.__key_modified = dict()

	def get_reorder_rows(self):
		"""
		The method to get the reorder_rows

		Returns:
			bool: A bool representing the reorder_rows
		"""

		return self.__reorder_rows

	def set_reorder_rows(self, reorder_rows):
		"""
		The method to set the value to reorder_rows

		Parameters:
			reorder_rows (bool) : A bool representing the reorder_rows
		"""

		if reorder_rows is not None and not isinstance(reorder_rows, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reorder_rows EXPECTED TYPE: bool', None, None)
		
		self.__reorder_rows = reorder_rows
		self.__key_modified['reorder_rows'] = 1

	def get_maximum_rows(self):
		"""
		The method to get the maximum_rows

		Returns:
			int: An int representing the maximum_rows
		"""

		return self.__maximum_rows

	def set_maximum_rows(self, maximum_rows):
		"""
		The method to set the value to maximum_rows

		Parameters:
			maximum_rows (int) : An int representing the maximum_rows
		"""

		if maximum_rows is not None and not isinstance(maximum_rows, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: maximum_rows EXPECTED TYPE: int', None, None)
		
		self.__maximum_rows = maximum_rows
		self.__key_modified['maximum_rows'] = 1

	def get_tooltip(self):
		"""
		The method to get the tooltip

		Returns:
			Tooltip: An instance of Tooltip
		"""

		return self.__tooltip

	def set_tooltip(self, tooltip):
		"""
		The method to set the value to tooltip

		Parameters:
			tooltip (Tooltip) : An instance of Tooltip
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.tooltip import Tooltip
		except Exception:
			from .tooltip import Tooltip

		if tooltip is not None and not isinstance(tooltip, Tooltip):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tooltip EXPECTED TYPE: Tooltip', None, None)
		
		self.__tooltip = tooltip
		self.__key_modified['tooltip'] = 1

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
