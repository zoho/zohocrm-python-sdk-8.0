try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Action(object):
	def __init__(self):
		"""Creates an instance of Action"""

		self.__type = None
		self.__open_in = None
		self.__display_name = None
		self.__url = None
		self.__key_modified = dict()

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

	def get_open_in(self):
		"""
		The method to get the open_in

		Returns:
			string: A string representing the open_in
		"""

		return self.__open_in

	def set_open_in(self, open_in):
		"""
		The method to set the value to open_in

		Parameters:
			open_in (string) : A string representing the open_in
		"""

		if open_in is not None and not isinstance(open_in, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: open_in EXPECTED TYPE: str', None, None)
		
		self.__open_in = open_in
		self.__key_modified['open_in'] = 1

	def get_display_name(self):
		"""
		The method to get the display_name

		Returns:
			string: A string representing the display_name
		"""

		return self.__display_name

	def set_display_name(self, display_name):
		"""
		The method to set the value to display_name

		Parameters:
			display_name (string) : A string representing the display_name
		"""

		if display_name is not None and not isinstance(display_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_name EXPECTED TYPE: str', None, None)
		
		self.__display_name = display_name
		self.__key_modified['display_name'] = 1

	def get_url(self):
		"""
		The method to get the url

		Returns:
			string: A string representing the url
		"""

		return self.__url

	def set_url(self, url):
		"""
		The method to set the value to url

		Parameters:
			url (string) : A string representing the url
		"""

		if url is not None and not isinstance(url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: url EXPECTED TYPE: str', None, None)
		
		self.__url = url
		self.__key_modified['url'] = 1

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
