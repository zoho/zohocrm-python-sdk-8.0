try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FontAttributes(object):
	def __init__(self):
		"""Creates an instance of FontAttributes"""

		self.__size = None
		self.__color = None
		self.__family = None
		self.__key_modified = dict()

	def get_size(self):
		"""
		The method to get the size

		Returns:
			int: An int representing the size
		"""

		return self.__size

	def set_size(self, size):
		"""
		The method to set the value to size

		Parameters:
			size (int) : An int representing the size
		"""

		if size is not None and not isinstance(size, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: size EXPECTED TYPE: int', None, None)
		
		self.__size = size
		self.__key_modified['size'] = 1

	def get_color(self):
		"""
		The method to get the color

		Returns:
			string: A string representing the color
		"""

		return self.__color

	def set_color(self, color):
		"""
		The method to set the value to color

		Parameters:
			color (string) : A string representing the color
		"""

		if color is not None and not isinstance(color, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: color EXPECTED TYPE: str', None, None)
		
		self.__color = color
		self.__key_modified['color'] = 1

	def get_family(self):
		"""
		The method to get the family

		Returns:
			string: A string representing the family
		"""

		return self.__family

	def set_family(self, family):
		"""
		The method to set the value to family

		Parameters:
			family (string) : A string representing the family
		"""

		if family is not None and not isinstance(family, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: family EXPECTED TYPE: str', None, None)
		
		self.__family = family
		self.__key_modified['family'] = 1

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
