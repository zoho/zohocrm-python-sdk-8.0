try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ChartData(object):
	def __init__(self):
		"""Creates an instance of ChartData"""

		self.__nodes = None
		self.__connections = None
		self.__color_palette = None
		self.__canvas_width = None
		self.__canvas_height = None
		self.__key_modified = dict()

	def get_nodes(self):
		"""
		The method to get the nodes

		Returns:
			list: An instance of list
		"""

		return self.__nodes

	def set_nodes(self, nodes):
		"""
		The method to set the value to nodes

		Parameters:
			nodes (list) : An instance of list
		"""

		if nodes is not None and not isinstance(nodes, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: nodes EXPECTED TYPE: list', None, None)
		
		self.__nodes = nodes
		self.__key_modified['nodes'] = 1

	def get_connections(self):
		"""
		The method to get the connections

		Returns:
			list: An instance of list
		"""

		return self.__connections

	def set_connections(self, connections):
		"""
		The method to set the value to connections

		Parameters:
			connections (list) : An instance of list
		"""

		if connections is not None and not isinstance(connections, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: connections EXPECTED TYPE: list', None, None)
		
		self.__connections = connections
		self.__key_modified['connections'] = 1

	def get_color_palette(self):
		"""
		The method to get the color_palette

		Returns:
			ButtonBackground: An instance of ButtonBackground
		"""

		return self.__color_palette

	def set_color_palette(self, color_palette):
		"""
		The method to set the value to color_palette

		Parameters:
			color_palette (ButtonBackground) : An instance of ButtonBackground
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.wizards.button_background import ButtonBackground
		except Exception:
			from .button_background import ButtonBackground

		if color_palette is not None and not isinstance(color_palette, ButtonBackground):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: color_palette EXPECTED TYPE: ButtonBackground', None, None)
		
		self.__color_palette = color_palette
		self.__key_modified['color_palette'] = 1

	def get_canvas_width(self):
		"""
		The method to get the canvas_width

		Returns:
			int: An int representing the canvas_width
		"""

		return self.__canvas_width

	def set_canvas_width(self, canvas_width):
		"""
		The method to set the value to canvas_width

		Parameters:
			canvas_width (int) : An int representing the canvas_width
		"""

		if canvas_width is not None and not isinstance(canvas_width, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: canvas_width EXPECTED TYPE: int', None, None)
		
		self.__canvas_width = canvas_width
		self.__key_modified['canvas_width'] = 1

	def get_canvas_height(self):
		"""
		The method to get the canvas_height

		Returns:
			int: An int representing the canvas_height
		"""

		return self.__canvas_height

	def set_canvas_height(self, canvas_height):
		"""
		The method to set the value to canvas_height

		Parameters:
			canvas_height (int) : An int representing the canvas_height
		"""

		if canvas_height is not None and not isinstance(canvas_height, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: canvas_height EXPECTED TYPE: int', None, None)
		
		self.__canvas_height = canvas_height
		self.__key_modified['canvas_height'] = 1

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
