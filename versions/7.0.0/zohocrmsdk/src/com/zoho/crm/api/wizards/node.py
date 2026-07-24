try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Node(object):
	def __init__(self):
		"""Creates an instance of Node"""

		self.__pos_y = None
		self.__pos_x = None
		self.__start_node = None
		self.__screen = None
		self.__key_modified = dict()

	def get_pos_y(self):
		"""
		The method to get the pos_y

		Returns:
			int: An int representing the pos_y
		"""

		return self.__pos_y

	def set_pos_y(self, pos_y):
		"""
		The method to set the value to pos_y

		Parameters:
			pos_y (int) : An int representing the pos_y
		"""

		if pos_y is not None and not isinstance(pos_y, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pos_y EXPECTED TYPE: int', None, None)
		
		self.__pos_y = pos_y
		self.__key_modified['pos_y'] = 1

	def get_pos_x(self):
		"""
		The method to get the pos_x

		Returns:
			int: An int representing the pos_x
		"""

		return self.__pos_x

	def set_pos_x(self, pos_x):
		"""
		The method to set the value to pos_x

		Parameters:
			pos_x (int) : An int representing the pos_x
		"""

		if pos_x is not None and not isinstance(pos_x, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pos_x EXPECTED TYPE: int', None, None)
		
		self.__pos_x = pos_x
		self.__key_modified['pos_x'] = 1

	def get_start_node(self):
		"""
		The method to get the start_node

		Returns:
			bool: A bool representing the start_node
		"""

		return self.__start_node

	def set_start_node(self, start_node):
		"""
		The method to set the value to start_node

		Parameters:
			start_node (bool) : A bool representing the start_node
		"""

		if start_node is not None and not isinstance(start_node, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: start_node EXPECTED TYPE: bool', None, None)
		
		self.__start_node = start_node
		self.__key_modified['start_node'] = 1

	def get_screen(self):
		"""
		The method to get the screen

		Returns:
			Screen: An instance of Screen
		"""

		return self.__screen

	def set_screen(self, screen):
		"""
		The method to set the value to screen

		Parameters:
			screen (Screen) : An instance of Screen
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.wizards.screen import Screen
		except Exception:
			from .screen import Screen

		if screen is not None and not isinstance(screen, Screen):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: screen EXPECTED TYPE: Screen', None, None)
		
		self.__screen = screen
		self.__key_modified['screen'] = 1

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
