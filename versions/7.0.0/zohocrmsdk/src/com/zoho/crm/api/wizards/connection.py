try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Connection(object):
	def __init__(self):
		"""Creates an instance of Connection"""

		self.__source_button = None
		self.__target_screen = None
		self.__id = None
		self.__key_modified = dict()

	def get_source_button(self):
		"""
		The method to get the source_button

		Returns:
			Button: An instance of Button
		"""

		return self.__source_button

	def set_source_button(self, source_button):
		"""
		The method to set the value to source_button

		Parameters:
			source_button (Button) : An instance of Button
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.wizards.button import Button
		except Exception:
			from .button import Button

		if source_button is not None and not isinstance(source_button, Button):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: source_button EXPECTED TYPE: Button', None, None)
		
		self.__source_button = source_button
		self.__key_modified['source_button'] = 1

	def get_target_screen(self):
		"""
		The method to get the target_screen

		Returns:
			Screen: An instance of Screen
		"""

		return self.__target_screen

	def set_target_screen(self, target_screen):
		"""
		The method to set the value to target_screen

		Parameters:
			target_screen (Screen) : An instance of Screen
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.wizards.screen import Screen
		except Exception:
			from .screen import Screen

		if target_screen is not None and not isinstance(target_screen, Screen):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: target_screen EXPECTED TYPE: Screen', None, None)
		
		self.__target_screen = target_screen
		self.__key_modified['target_screen'] = 1

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
