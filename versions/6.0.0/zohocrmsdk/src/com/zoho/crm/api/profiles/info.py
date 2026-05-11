try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Info(object):
	def __init__(self):
		"""Creates an instance of Info"""

		self.__license_limit = None
		self.__key_modified = dict()

	def get_license_limit(self):
		"""
		The method to get the license_limit

		Returns:
			int: An int representing the license_limit
		"""

		return self.__license_limit

	def set_license_limit(self, license_limit):
		"""
		The method to set the value to license_limit

		Parameters:
			license_limit (int) : An int representing the license_limit
		"""

		if license_limit is not None and not isinstance(license_limit, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: license_limit EXPECTED TYPE: int', None, None)
		
		self.__license_limit = license_limit
		self.__key_modified['license_limit'] = 1

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
