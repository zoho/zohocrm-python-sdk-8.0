try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class TPipeline(object):
	def __init__(self):
		"""Creates an instance of TPipeline"""

		self.__from_1 = None
		self.__to = None
		self.__key_modified = dict()

	def get_from(self):
		"""
		The method to get the from

		Returns:
			int: An int representing the from_1
		"""

		return self.__from_1

	def set_from(self, from_1):
		"""
		The method to set the value to from

		Parameters:
			from_1 (int) : An int representing the from_1
		"""

		if from_1 is not None and not isinstance(from_1, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_1 EXPECTED TYPE: int', None, None)
		
		self.__from_1 = from_1
		self.__key_modified['from'] = 1

	def get_to(self):
		"""
		The method to get the to

		Returns:
			int: An int representing the to
		"""

		return self.__to

	def set_to(self, to):
		"""
		The method to set the value to to

		Parameters:
			to (int) : An int representing the to
		"""

		if to is not None and not isinstance(to, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: to EXPECTED TYPE: int', None, None)
		
		self.__to = to
		self.__key_modified['to'] = 1

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
