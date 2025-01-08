try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ResponseWrapper(object):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""

		self.__definition = None
		self.__key_modified = dict()

	def get_definition(self):
		"""
		The method to get the definition

		Returns:
			Definition: An instance of Definition
		"""

		return self.__definition

	def set_definition(self, definition):
		"""
		The method to set the value to definition

		Parameters:
			definition (Definition) : An instance of Definition
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.definition.definition import Definition
		except Exception:
			from .definition import Definition

		if definition is not None and not isinstance(definition, Definition):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: definition EXPECTED TYPE: Definition', None, None)
		
		self.__definition = definition
		self.__key_modified['definition'] = 1

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
