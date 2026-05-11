try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.shift_hours.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__shift_hours = None
		self.__shift_count = None
		self.__key_modified = dict()

	def get_shift_hours(self):
		"""
		The method to get the shift_hours

		Returns:
			list: An instance of list
		"""

		return self.__shift_hours

	def set_shift_hours(self, shift_hours):
		"""
		The method to set the value to shift_hours

		Parameters:
			shift_hours (list) : An instance of list
		"""

		if shift_hours is not None and not isinstance(shift_hours, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shift_hours EXPECTED TYPE: list', None, None)
		
		self.__shift_hours = shift_hours
		self.__key_modified['shift_hours'] = 1

	def get_shift_count(self):
		"""
		The method to get the shift_count

		Returns:
			ShiftCount: An instance of ShiftCount
		"""

		return self.__shift_count

	def set_shift_count(self, shift_count):
		"""
		The method to set the value to shift_count

		Parameters:
			shift_count (ShiftCount) : An instance of ShiftCount
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.shift_count import ShiftCount
		except Exception:
			from .shift_count import ShiftCount

		if shift_count is not None and not isinstance(shift_count, ShiftCount):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shift_count EXPECTED TYPE: ShiftCount', None, None)
		
		self.__shift_count = shift_count
		self.__key_modified['shift_count'] = 1

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
