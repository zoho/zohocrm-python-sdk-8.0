try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class OperationType(object):
	def __init__(self):
		"""Creates an instance of OperationType"""

		self.__web_update = None
		self.__api_create = None
		self.__web_create = None
		self.__api_update = None
		self.__key_modified = dict()

	def get_web_update(self):
		"""
		The method to get the web_update

		Returns:
			bool: A bool representing the web_update
		"""

		return self.__web_update

	def set_web_update(self, web_update):
		"""
		The method to set the value to web_update

		Parameters:
			web_update (bool) : A bool representing the web_update
		"""

		if web_update is not None and not isinstance(web_update, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: web_update EXPECTED TYPE: bool', None, None)
		
		self.__web_update = web_update
		self.__key_modified['web_update'] = 1

	def get_api_create(self):
		"""
		The method to get the api_create

		Returns:
			bool: A bool representing the api_create
		"""

		return self.__api_create

	def set_api_create(self, api_create):
		"""
		The method to set the value to api_create

		Parameters:
			api_create (bool) : A bool representing the api_create
		"""

		if api_create is not None and not isinstance(api_create, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_create EXPECTED TYPE: bool', None, None)
		
		self.__api_create = api_create
		self.__key_modified['api_create'] = 1

	def get_web_create(self):
		"""
		The method to get the web_create

		Returns:
			bool: A bool representing the web_create
		"""

		return self.__web_create

	def set_web_create(self, web_create):
		"""
		The method to set the value to web_create

		Parameters:
			web_create (bool) : A bool representing the web_create
		"""

		if web_create is not None and not isinstance(web_create, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: web_create EXPECTED TYPE: bool', None, None)
		
		self.__web_create = web_create
		self.__key_modified['web_create'] = 1

	def get_api_update(self):
		"""
		The method to get the api_update

		Returns:
			bool: A bool representing the api_update
		"""

		return self.__api_update

	def set_api_update(self, api_update):
		"""
		The method to set the value to api_update

		Parameters:
			api_update (bool) : A bool representing the api_update
		"""

		if api_update is not None and not isinstance(api_update, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_update EXPECTED TYPE: bool', None, None)
		
		self.__api_update = api_update
		self.__key_modified['api_update'] = 1

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
