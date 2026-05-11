try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Theme(object):
	def __init__(self):
		"""Creates an instance of Theme"""

		self.__normal_tab = None
		self.__selected_tab = None
		self.__new_background = None
		self.__background = None
		self.__screen = None
		self.__type = None
		self.__key_modified = dict()

	def get_normal_tab(self):
		"""
		The method to get the normal_tab

		Returns:
			Tab: An instance of Tab
		"""

		return self.__normal_tab

	def set_normal_tab(self, normal_tab):
		"""
		The method to set the value to normal_tab

		Parameters:
			normal_tab (Tab) : An instance of Tab
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.tab import Tab
		except Exception:
			from .tab import Tab

		if normal_tab is not None and not isinstance(normal_tab, Tab):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: normal_tab EXPECTED TYPE: Tab', None, None)
		
		self.__normal_tab = normal_tab
		self.__key_modified['normal_tab'] = 1

	def get_selected_tab(self):
		"""
		The method to get the selected_tab

		Returns:
			Tab: An instance of Tab
		"""

		return self.__selected_tab

	def set_selected_tab(self, selected_tab):
		"""
		The method to set the value to selected_tab

		Parameters:
			selected_tab (Tab) : An instance of Tab
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users.tab import Tab
		except Exception:
			from .tab import Tab

		if selected_tab is not None and not isinstance(selected_tab, Tab):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: selected_tab EXPECTED TYPE: Tab', None, None)
		
		self.__selected_tab = selected_tab
		self.__key_modified['selected_tab'] = 1

	def get_new_background(self):
		"""
		The method to get the new_background

		Returns:
			string: A string representing the new_background
		"""

		return self.__new_background

	def set_new_background(self, new_background):
		"""
		The method to set the value to new_background

		Parameters:
			new_background (string) : A string representing the new_background
		"""

		if new_background is not None and not isinstance(new_background, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: new_background EXPECTED TYPE: str', None, None)
		
		self.__new_background = new_background
		self.__key_modified['new_background'] = 1

	def get_background(self):
		"""
		The method to get the background

		Returns:
			Choice: An instance of Choice
		"""

		return self.__background

	def set_background(self, background):
		"""
		The method to set the value to background

		Parameters:
			background (Choice) : An instance of Choice
		"""

		if background is not None and not isinstance(background, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: background EXPECTED TYPE: Choice', None, None)
		
		self.__background = background
		self.__key_modified['background'] = 1

	def get_screen(self):
		"""
		The method to get the screen

		Returns:
			Choice: An instance of Choice
		"""

		return self.__screen

	def set_screen(self, screen):
		"""
		The method to set the value to screen

		Parameters:
			screen (Choice) : An instance of Choice
		"""

		if screen is not None and not isinstance(screen, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: screen EXPECTED TYPE: Choice', None, None)
		
		self.__screen = screen
		self.__key_modified['screen'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

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
