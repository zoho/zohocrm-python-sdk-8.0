try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Logo(object):
	def __init__(self):
		"""Creates an instance of Logo"""

		self.__image_name = None
		self.__align = None
		self.__size = None
		self.__key_modified = dict()

	def get_image_name(self):
		"""
		The method to get the image_name

		Returns:
			string: A string representing the image_name
		"""

		return self.__image_name

	def set_image_name(self, image_name):
		"""
		The method to set the value to image_name

		Parameters:
			image_name (string) : A string representing the image_name
		"""

		if image_name is not None and not isinstance(image_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: image_name EXPECTED TYPE: str', None, None)
		
		self.__image_name = image_name
		self.__key_modified['image_name'] = 1

	def get_align(self):
		"""
		The method to get the align

		Returns:
			string: A string representing the align
		"""

		return self.__align

	def set_align(self, align):
		"""
		The method to set the value to align

		Parameters:
			align (string) : A string representing the align
		"""

		if align is not None and not isinstance(align, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: align EXPECTED TYPE: str', None, None)
		
		self.__align = align
		self.__key_modified['align'] = 1

	def get_size(self):
		"""
		The method to get the size

		Returns:
			string: A string representing the size
		"""

		return self.__size

	def set_size(self, size):
		"""
		The method to set the value to size

		Parameters:
			size (string) : A string representing the size
		"""

		if size is not None and not isinstance(size, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: size EXPECTED TYPE: str', None, None)
		
		self.__size = size
		self.__key_modified['size'] = 1

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
