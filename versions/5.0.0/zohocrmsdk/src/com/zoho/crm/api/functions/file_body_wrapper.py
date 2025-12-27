try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import StreamWrapper, Constants
except Exception:
	from ..exception import SDKException
	from ..util import StreamWrapper, Constants


class FileBodyWrapper(object):
	def __init__(self):
		"""Creates an instance of FileBodyWrapper"""

		self.__inputfile = None
		self.__key_modified = dict()

	def get_inputfile(self):
		"""
		The method to get the inputfile

		Returns:
			StreamWrapper: An instance of StreamWrapper
		"""

		return self.__inputfile

	def set_inputfile(self, inputfile):
		"""
		The method to set the value to inputfile

		Parameters:
			inputfile (StreamWrapper) : An instance of StreamWrapper
		"""

		if inputfile is not None and not isinstance(inputfile, StreamWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: inputfile EXPECTED TYPE: StreamWrapper', None, None)
		
		self.__inputfile = inputfile
		self.__key_modified['inputFile'] = 1

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
