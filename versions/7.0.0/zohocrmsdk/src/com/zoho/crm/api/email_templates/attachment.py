try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Attachment(object):
	def __init__(self):
		"""Creates an instance of Attachment"""

		self.__size = None
		self.__file_name = None
		self.__file_id = None
		self.__id = None
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

	def get_file_name(self):
		"""
		The method to get the file_name

		Returns:
			string: A string representing the file_name
		"""

		return self.__file_name

	def set_file_name(self, file_name):
		"""
		The method to set the value to file_name

		Parameters:
			file_name (string) : A string representing the file_name
		"""

		if file_name is not None and not isinstance(file_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_name EXPECTED TYPE: str', None, None)
		
		self.__file_name = file_name
		self.__key_modified['file_name'] = 1

	def get_file_id(self):
		"""
		The method to get the file_id

		Returns:
			string: A string representing the file_id
		"""

		return self.__file_id

	def set_file_id(self, file_id):
		"""
		The method to set the value to file_id

		Parameters:
			file_id (string) : A string representing the file_id
		"""

		if file_id is not None and not isinstance(file_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_id EXPECTED TYPE: str', None, None)
		
		self.__file_id = file_id
		self.__key_modified['file_id'] = 1

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
