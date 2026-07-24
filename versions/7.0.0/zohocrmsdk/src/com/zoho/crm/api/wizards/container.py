try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Container(object):
	def __init__(self):
		"""Creates an instance of Container"""

		self.__id = None
		self.__layout = None
		self.__chart_data = None
		self.__screens = None
		self.__key_modified = dict()

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

	def get_chart_data(self):
		"""
		The method to get the chart_data

		Returns:
			ChartData: An instance of ChartData
		"""

		return self.__chart_data

	def set_chart_data(self, chart_data):
		"""
		The method to set the value to chart_data

		Parameters:
			chart_data (ChartData) : An instance of ChartData
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.wizards.chart_data import ChartData
		except Exception:
			from .chart_data import ChartData

		if chart_data is not None and not isinstance(chart_data, ChartData):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: chart_data EXPECTED TYPE: ChartData', None, None)
		
		self.__chart_data = chart_data
		self.__key_modified['chart_data'] = 1

	def get_screens(self):
		"""
		The method to get the screens

		Returns:
			list: An instance of list
		"""

		return self.__screens

	def set_screens(self, screens):
		"""
		The method to set the value to screens

		Parameters:
			screens (list) : An instance of list
		"""

		if screens is not None and not isinstance(screens, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: screens EXPECTED TYPE: list', None, None)
		
		self.__screens = screens
		self.__key_modified['screens'] = 1

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
