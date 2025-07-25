try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.mass_delete_tags.status_response_handler import StatusResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .status_response_handler import StatusResponseHandler


class StatusResponseWrapper(StatusResponseHandler):
	def __init__(self):
		"""Creates an instance of StatusResponseWrapper"""
		super().__init__()

		self.__mass_delete = None
		self.__key_modified = dict()

	def get_mass_delete(self):
		"""
		The method to get the mass_delete

		Returns:
			list: An instance of list
		"""

		return self.__mass_delete

	def set_mass_delete(self, mass_delete):
		"""
		The method to set the value to mass_delete

		Parameters:
			mass_delete (list) : An instance of list
		"""

		if mass_delete is not None and not isinstance(mass_delete, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mass_delete EXPECTED TYPE: list', None, None)
		
		self.__mass_delete = mass_delete
		self.__key_modified['mass_delete'] = 1

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
