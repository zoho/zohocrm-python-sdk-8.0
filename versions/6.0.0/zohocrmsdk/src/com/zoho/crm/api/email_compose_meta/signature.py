try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Signature(object):
	def __init__(self):
		"""Creates an instance of Signature"""

		self.__mode = None
		self.__sign = None
		self.__key_modified = dict()

	def get_mode(self):
		"""
		The method to get the mode

		Returns:
			int: An int representing the mode
		"""

		return self.__mode

	def set_mode(self, mode):
		"""
		The method to set the value to mode

		Parameters:
			mode (int) : An int representing the mode
		"""

		if mode is not None and not isinstance(mode, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mode EXPECTED TYPE: int', None, None)
		
		self.__mode = mode
		self.__key_modified['mode'] = 1

	def get_sign(self):
		"""
		The method to get the sign

		Returns:
			string: A string representing the sign
		"""

		return self.__sign

	def set_sign(self, sign):
		"""
		The method to set the value to sign

		Parameters:
			sign (string) : A string representing the sign
		"""

		if sign is not None and not isinstance(sign, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sign EXPECTED TYPE: str', None, None)
		
		self.__sign = sign
		self.__key_modified['sign'] = 1

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
