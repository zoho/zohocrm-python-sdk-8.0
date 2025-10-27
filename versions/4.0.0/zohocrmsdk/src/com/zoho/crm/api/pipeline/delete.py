try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Delete(object):
	def __init__(self):
		"""Creates an instance of Delete"""

		self.__permanent = None
		self.__key_modified = dict()

	def get_permanent(self):
		"""
		The method to get the permanent

		Returns:
			bool: A bool representing the permanent
		"""

		return self.__permanent

	def set_permanent(self, permanent):
		"""
		The method to set the value to permanent

		Parameters:
			permanent (bool) : A bool representing the permanent
		"""

		if permanent is not None and not isinstance(permanent, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permanent EXPECTED TYPE: bool', None, None)
		
		self.__permanent = permanent
		self.__key_modified['permanent'] = 1

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
