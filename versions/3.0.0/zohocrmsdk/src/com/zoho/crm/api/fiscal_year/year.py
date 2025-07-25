try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Year(object):
	def __init__(self):
		"""Creates an instance of Year"""

		self.__start_month = None
		self.__display_based_on = None
		self.__id = None
		self.__key_modified = dict()

	def get_start_month(self):
		"""
		The method to get the start_month

		Returns:
			Choice: An instance of Choice
		"""

		return self.__start_month

	def set_start_month(self, start_month):
		"""
		The method to set the value to start_month

		Parameters:
			start_month (Choice) : An instance of Choice
		"""

		if start_month is not None and not isinstance(start_month, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: start_month EXPECTED TYPE: Choice', None, None)
		
		self.__start_month = start_month
		self.__key_modified['start_month'] = 1

	def get_display_based_on(self):
		"""
		The method to get the display_based_on

		Returns:
			Choice: An instance of Choice
		"""

		return self.__display_based_on

	def set_display_based_on(self, display_based_on):
		"""
		The method to set the value to display_based_on

		Parameters:
			display_based_on (Choice) : An instance of Choice
		"""

		if display_based_on is not None and not isinstance(display_based_on, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_based_on EXPECTED TYPE: Choice', None, None)
		
		self.__display_based_on = display_based_on
		self.__key_modified['display_based_on'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

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
