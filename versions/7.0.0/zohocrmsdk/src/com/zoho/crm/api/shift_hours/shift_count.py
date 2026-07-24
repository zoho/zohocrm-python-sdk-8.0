try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ShiftCount(object):
	def __init__(self):
		"""Creates an instance of ShiftCount"""

		self.__total_shift_with_user = None
		self.__total_shift = None
		self.__key_modified = dict()

	def get_total_shift_with_user(self):
		"""
		The method to get the total_shift_with_user

		Returns:
			int: An int representing the total_shift_with_user
		"""

		return self.__total_shift_with_user

	def set_total_shift_with_user(self, total_shift_with_user):
		"""
		The method to set the value to total_shift_with_user

		Parameters:
			total_shift_with_user (int) : An int representing the total_shift_with_user
		"""

		if total_shift_with_user is not None and not isinstance(total_shift_with_user, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: total_shift_with_user EXPECTED TYPE: int', None, None)
		
		self.__total_shift_with_user = total_shift_with_user
		self.__key_modified['total_shift_with_user'] = 1

	def get_total_shift(self):
		"""
		The method to get the total_shift

		Returns:
			int: An int representing the total_shift
		"""

		return self.__total_shift

	def set_total_shift(self, total_shift):
		"""
		The method to set the value to total_shift

		Parameters:
			total_shift (int) : An int representing the total_shift
		"""

		if total_shift is not None and not isinstance(total_shift, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: total_shift EXPECTED TYPE: int', None, None)
		
		self.__total_shift = total_shift
		self.__key_modified['total_shift'] = 1

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
