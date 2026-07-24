try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class HipaaCompliance(object):
	def __init__(self):
		"""Creates an instance of HipaaCompliance"""

		self.__restricted_in_export = None
		self.__restricted = None
		self.__key_modified = dict()

	def get_restricted_in_export(self):
		"""
		The method to get the restricted_in_export

		Returns:
			bool: A bool representing the restricted_in_export
		"""

		return self.__restricted_in_export

	def set_restricted_in_export(self, restricted_in_export):
		"""
		The method to set the value to restricted_in_export

		Parameters:
			restricted_in_export (bool) : A bool representing the restricted_in_export
		"""

		if restricted_in_export is not None and not isinstance(restricted_in_export, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restricted_in_export EXPECTED TYPE: bool', None, None)
		
		self.__restricted_in_export = restricted_in_export
		self.__key_modified['restricted_in_export'] = 1

	def get_restricted(self):
		"""
		The method to get the restricted

		Returns:
			bool: A bool representing the restricted
		"""

		return self.__restricted

	def set_restricted(self, restricted):
		"""
		The method to set the value to restricted

		Parameters:
			restricted (bool) : A bool representing the restricted
		"""

		if restricted is not None and not isinstance(restricted, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restricted EXPECTED TYPE: bool', None, None)
		
		self.__restricted = restricted
		self.__key_modified['restricted'] = 1

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
