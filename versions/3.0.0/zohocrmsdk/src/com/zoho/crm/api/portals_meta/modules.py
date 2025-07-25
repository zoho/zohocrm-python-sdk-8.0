try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Modules(object):
	def __init__(self):
		"""Creates an instance of Modules"""

		self.__plural_label = None
		self.__shared_type = None
		self.__api_name = None
		self.__id = None
		self.__filters = None
		self.__layouts = None
		self.__views = None
		self.__key_modified = dict()

	def get_plural_label(self):
		"""
		The method to get the plural_label

		Returns:
			string: A string representing the plural_label
		"""

		return self.__plural_label

	def set_plural_label(self, plural_label):
		"""
		The method to set the value to plural_label

		Parameters:
			plural_label (string) : A string representing the plural_label
		"""

		if plural_label is not None and not isinstance(plural_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: plural_label EXPECTED TYPE: str', None, None)
		
		self.__plural_label = plural_label
		self.__key_modified['plural_label'] = 1

	def get_shared_type(self):
		"""
		The method to get the shared_type

		Returns:
			string: A string representing the shared_type
		"""

		return self.__shared_type

	def set_shared_type(self, shared_type):
		"""
		The method to set the value to shared_type

		Parameters:
			shared_type (string) : A string representing the shared_type
		"""

		if shared_type is not None and not isinstance(shared_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_type EXPECTED TYPE: str', None, None)
		
		self.__shared_type = shared_type
		self.__key_modified['shared_type'] = 1

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

	def get_filters(self):
		"""
		The method to get the filters

		Returns:
			list: An instance of list
		"""

		return self.__filters

	def set_filters(self, filters):
		"""
		The method to set the value to filters

		Parameters:
			filters (list) : An instance of list
		"""

		if filters is not None and not isinstance(filters, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: filters EXPECTED TYPE: list', None, None)
		
		self.__filters = filters
		self.__key_modified['filters'] = 1

	def get_layouts(self):
		"""
		The method to get the layouts

		Returns:
			list: An instance of list
		"""

		return self.__layouts

	def set_layouts(self, layouts):
		"""
		The method to set the value to layouts

		Parameters:
			layouts (list) : An instance of list
		"""

		if layouts is not None and not isinstance(layouts, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layouts EXPECTED TYPE: list', None, None)
		
		self.__layouts = layouts
		self.__key_modified['layouts'] = 1

	def get_views(self):
		"""
		The method to get the views

		Returns:
			list: An instance of list
		"""

		return self.__views

	def set_views(self, views):
		"""
		The method to set the value to views

		Parameters:
			views (list) : An instance of list
		"""

		if views is not None and not isinstance(views, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: views EXPECTED TYPE: list', None, None)
		
		self.__views = views
		self.__key_modified['views'] = 1

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
