try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Shared(object):
	def __init__(self):
		"""Creates an instance of Shared"""

		self.__resource = None
		self.__subordinates = None
		self.__type = None
		self.__key_modified = dict()

	def get_resource(self):
		"""
		The method to get the resource

		Returns:
			Resource: An instance of Resource
		"""

		return self.__resource

	def set_resource(self, resource):
		"""
		The method to set the value to resource

		Parameters:
			resource (Resource) : An instance of Resource
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.resource import Resource
		except Exception:
			from .resource import Resource

		if resource is not None and not isinstance(resource, Resource):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: resource EXPECTED TYPE: Resource', None, None)
		
		self.__resource = resource
		self.__key_modified['resource'] = 1

	def get_subordinates(self):
		"""
		The method to get the subordinates

		Returns:
			bool: A bool representing the subordinates
		"""

		return self.__subordinates

	def set_subordinates(self, subordinates):
		"""
		The method to set the value to subordinates

		Parameters:
			subordinates (bool) : A bool representing the subordinates
		"""

		if subordinates is not None and not isinstance(subordinates, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subordinates EXPECTED TYPE: bool', None, None)
		
		self.__subordinates = subordinates
		self.__key_modified['subordinates'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (Choice) : An instance of Choice
		"""

		if type is not None and not isinstance(type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: Choice', None, None)
		
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
