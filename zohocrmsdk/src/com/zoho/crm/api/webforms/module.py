try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Module(object):
	def __init__(self):
		"""Creates an instance of Module"""

		self.__id = None
		self.__module_name = None
		self.__api_name = None
		self.__display_label = None
		self.__key_modified = dict()

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string representing the id
		"""

		if id is not None and not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_module_name(self):
		"""
		The method to get the module_name

		Returns:
			string: A string representing the module_name
		"""

		return self.__module_name

	def set_module_name(self, module_name):
		"""
		The method to set the value to module_name

		Parameters:
			module_name (string) : A string representing the module_name
		"""

		if module_name is not None and not isinstance(module_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_name EXPECTED TYPE: str', None, None)
		
		self.__module_name = module_name
		self.__key_modified['module_name'] = 1

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

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
