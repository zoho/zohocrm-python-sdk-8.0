try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AssociationResponse(object):
	def __init__(self):
		"""Creates an instance of AssociationResponse"""

		self.__type = None
		self.__resource = None
		self.__detail = None
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
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.resource import Resource
		except Exception:
			from .resource import Resource

		if resource is not None and not isinstance(resource, Resource):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: resource EXPECTED TYPE: Resource', None, None)
		
		self.__resource = resource
		self.__key_modified['resource'] = 1

	def get_detail(self):
		"""
		The method to get the detail

		Returns:
			AssociationModule: An instance of AssociationModule
		"""

		return self.__detail

	def set_detail(self, detail):
		"""
		The method to set the value to detail

		Parameters:
			detail (AssociationModule) : An instance of AssociationModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.association_module import AssociationModule
		except Exception:
			from .association_module import AssociationModule

		if detail is not None and not isinstance(detail, AssociationModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: detail EXPECTED TYPE: AssociationModule', None, None)
		
		self.__detail = detail
		self.__key_modified['detail'] = 1

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
