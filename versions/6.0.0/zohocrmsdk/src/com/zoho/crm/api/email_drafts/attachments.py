try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Attachments(object):
	def __init__(self):
		"""Creates an instance of Attachments"""

		self.__service_name = None
		self.__file_size = None
		self.__id = None
		self.__file_name = None
		self.__key_modified = dict()

	def get_service_name(self):
		"""
		The method to get the service_name

		Returns:
			string: A string representing the service_name
		"""

		return self.__service_name

	def set_service_name(self, service_name):
		"""
		The method to set the value to service_name

		Parameters:
			service_name (string) : A string representing the service_name
		"""

		if service_name is not None and not isinstance(service_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: service_name EXPECTED TYPE: str', None, None)
		
		self.__service_name = service_name
		self.__key_modified['service_name'] = 1

	def get_file_size(self):
		"""
		The method to get the file_size

		Returns:
			string: A string representing the file_size
		"""

		return self.__file_size

	def set_file_size(self, file_size):
		"""
		The method to set the value to file_size

		Parameters:
			file_size (string) : A string representing the file_size
		"""

		if file_size is not None and not isinstance(file_size, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_size EXPECTED TYPE: str', None, None)
		
		self.__file_size = file_size
		self.__key_modified['file_size'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string representing the id
		"""

		if id is not None and not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

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
