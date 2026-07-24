try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Limit(object):
	def __init__(self):
		"""Creates an instance of Limit"""

		self.__total = None
		self.__edition_limit = None
		self.__key_modified = dict()

	def get_total(self):
		"""
		The method to get the total

		Returns:
			int: An int representing the total
		"""

		return self.__total

	def set_total(self, total):
		"""
		The method to set the value to total

		Parameters:
			total (int) : An int representing the total
		"""

		if total is not None and not isinstance(total, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: total EXPECTED TYPE: int', None, None)
		
		self.__total = total
		self.__key_modified['total'] = 1

	def get_edition_limit(self):
		"""
		The method to get the edition_limit

		Returns:
			int: An int representing the edition_limit
		"""

		return self.__edition_limit

	def set_edition_limit(self, edition_limit):
		"""
		The method to set the value to edition_limit

		Parameters:
			edition_limit (int) : An int representing the edition_limit
		"""

		if edition_limit is not None and not isinstance(edition_limit, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: edition_limit EXPECTED TYPE: int', None, None)
		
		self.__edition_limit = edition_limit
		self.__key_modified['edition_limit'] = 1

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
