try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.user_groups.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class AssociationWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of AssociationWrapper"""
		super().__init__()

		self.__associations = None
		self.__key_modified = dict()

	def get_associations(self):
		"""
		The method to get the associations

		Returns:
			list: An instance of list
		"""

		return self.__associations

	def set_associations(self, associations):
		"""
		The method to set the value to associations

		Parameters:
			associations (list) : An instance of list
		"""

		if associations is not None and not isinstance(associations, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: associations EXPECTED TYPE: list', None, None)
		
		self.__associations = associations
		self.__key_modified['associations'] = 1

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
