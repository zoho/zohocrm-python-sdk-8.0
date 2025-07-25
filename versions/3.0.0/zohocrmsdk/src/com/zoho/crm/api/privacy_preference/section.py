try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Section(object):
	def __init__(self):
		"""Creates an instance of Section"""

		self.__name = None
		self.__tooltip = None
		self.__show_type = None
		self.__title = None
		self.__options = None
		self.__key_modified = dict()

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_tooltip(self):
		"""
		The method to get the tooltip

		Returns:
			string: A string representing the tooltip
		"""

		return self.__tooltip

	def set_tooltip(self, tooltip):
		"""
		The method to set the value to tooltip

		Parameters:
			tooltip (string) : A string representing the tooltip
		"""

		if tooltip is not None and not isinstance(tooltip, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tooltip EXPECTED TYPE: str', None, None)
		
		self.__tooltip = tooltip
		self.__key_modified['tooltip'] = 1

	def get_show_type(self):
		"""
		The method to get the show_type

		Returns:
			string: A string representing the show_type
		"""

		return self.__show_type

	def set_show_type(self, show_type):
		"""
		The method to set the value to show_type

		Parameters:
			show_type (string) : A string representing the show_type
		"""

		if show_type is not None and not isinstance(show_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_type EXPECTED TYPE: str', None, None)
		
		self.__show_type = show_type
		self.__key_modified['show_type'] = 1

	def get_title(self):
		"""
		The method to get the title

		Returns:
			string: A string representing the title
		"""

		return self.__title

	def set_title(self, title):
		"""
		The method to set the value to title

		Parameters:
			title (string) : A string representing the title
		"""

		if title is not None and not isinstance(title, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: title EXPECTED TYPE: str', None, None)
		
		self.__title = title
		self.__key_modified['title'] = 1

	def get_options(self):
		"""
		The method to get the options

		Returns:
			list: An instance of list
		"""

		return self.__options

	def set_options(self, options):
		"""
		The method to set the value to options

		Parameters:
			options (list) : An instance of list
		"""

		if options is not None and not isinstance(options, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: options EXPECTED TYPE: list', None, None)
		
		self.__options = options
		self.__key_modified['options'] = 1

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
