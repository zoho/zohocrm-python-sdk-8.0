try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ButtonBackground(object):
	def __init__(self):
		"""Creates an instance of ButtonBackground"""

		self.__button_background = None
		self.__key_modified = dict()

	def get_button_background(self):
		"""
		The method to get the button_background

		Returns:
			list: An instance of list
		"""

		return self.__button_background

	def set_button_background(self, button_background):
		"""
		The method to set the value to button_background

		Parameters:
			button_background (list) : An instance of list
		"""

		if button_background is not None and not isinstance(button_background, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: button_background EXPECTED TYPE: list', None, None)
		
		self.__button_background = button_background
		self.__key_modified['button_background'] = 1

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
