try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Wrapper(object):
	def __init__(self):
		"""Creates an instance of Wrapper"""

		self.__related_lists = None
		self.__key_modified = dict()

	def get_related_lists(self):
		"""
		The method to get the related_lists

		Returns:
			list: An instance of list
		"""

		return self.__related_lists

	def set_related_lists(self, related_lists):
		"""
		The method to set the value to related_lists

		Parameters:
			related_lists (list) : An instance of list
		"""

		if related_lists is not None and not isinstance(related_lists, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_lists EXPECTED TYPE: list', None, None)
		
		self.__related_lists = related_lists
		self.__key_modified['related_lists'] = 1

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
