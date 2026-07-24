try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class MinifiedProperty1(object):
	def __init__(self):
		"""Creates an instance of MinifiedProperty1"""

		self.__read_only = None
		self.__api_name = None
		self.__data_type = None
		self.__length = None
		self.__required = None
		self.__key_modified = dict()

	def get_read_only(self):
		"""
		The method to get the read_only

		Returns:
			bool: A bool representing the read_only
		"""

		return self.__read_only

	def set_read_only(self, read_only):
		"""
		The method to set the value to read_only

		Parameters:
			read_only (bool) : A bool representing the read_only
		"""

		if read_only is not None and not isinstance(read_only, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: read_only EXPECTED TYPE: bool', None, None)
		
		self.__read_only = read_only
		self.__key_modified['read_only'] = 1

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_data_type(self):
		"""
		The method to get the data_type

		Returns:
			string: A string representing the data_type
		"""

		return self.__data_type

	def set_data_type(self, data_type):
		"""
		The method to set the value to data_type

		Parameters:
			data_type (string) : A string representing the data_type
		"""

		if data_type is not None and not isinstance(data_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_type EXPECTED TYPE: str', None, None)
		
		self.__data_type = data_type
		self.__key_modified['data_type'] = 1

	def get_length(self):
		"""
		The method to get the length

		Returns:
			int: An int representing the length
		"""

		return self.__length

	def set_length(self, length):
		"""
		The method to set the value to length

		Parameters:
			length (int) : An int representing the length
		"""

		if length is not None and not isinstance(length, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: length EXPECTED TYPE: int', None, None)
		
		self.__length = length
		self.__key_modified['length'] = 1

	def get_required(self):
		"""
		The method to get the required

		Returns:
			bool: A bool representing the required
		"""

		return self.__required

	def set_required(self, required):
		"""
		The method to set the value to required

		Parameters:
			required (bool) : A bool representing the required
		"""

		if required is not None and not isinstance(required, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: required EXPECTED TYPE: bool', None, None)
		
		self.__required = required
		self.__key_modified['required'] = 1

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
