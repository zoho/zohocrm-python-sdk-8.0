try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class LayoutRequestWrapper(object):
	def __init__(self):
		"""Creates an instance of LayoutRequestWrapper"""

		self.__layout = None
		self.__key_modified = dict()

	def get_layout(self):
		"""
		The method to get the layout

		Returns:
			Layout: An instance of Layout
		"""

		return self.__layout

	def set_layout(self, layout):
		"""
		The method to set the value to layout

		Parameters:
			layout (Layout) : An instance of Layout
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.scoring_rules.layout import Layout
		except Exception:
			from .layout import Layout

		if layout is not None and not isinstance(layout, Layout):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout EXPECTED TYPE: Layout', None, None)
		
		self.__layout = layout
		self.__key_modified['layout'] = 1

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
