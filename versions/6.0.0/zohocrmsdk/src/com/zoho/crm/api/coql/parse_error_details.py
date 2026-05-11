try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.coql.details_wrapper import DetailsWrapper
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .details_wrapper import DetailsWrapper


class ParseErrorDetails(DetailsWrapper):
	def __init__(self):
		"""Creates an instance of ParseErrorDetails"""
		super().__init__()

		self.__line = None
		self.__column = None
		self.__near = None
		self.__key_modified = dict()

	def get_line(self):
		"""
		The method to get the line

		Returns:
			int: An int representing the line
		"""

		return self.__line

	def set_line(self, line):
		"""
		The method to set the value to line

		Parameters:
			line (int) : An int representing the line
		"""

		if line is not None and not isinstance(line, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: line EXPECTED TYPE: int', None, None)
		
		self.__line = line
		self.__key_modified['line'] = 1

	def get_column(self):
		"""
		The method to get the column

		Returns:
			int: An int representing the column
		"""

		return self.__column

	def set_column(self, column):
		"""
		The method to set the value to column

		Parameters:
			column (int) : An int representing the column
		"""

		if column is not None and not isinstance(column, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: column EXPECTED TYPE: int', None, None)
		
		self.__column = column
		self.__key_modified['column'] = 1

	def get_near(self):
		"""
		The method to get the near

		Returns:
			string: A string representing the near
		"""

		return self.__near

	def set_near(self, near):
		"""
		The method to set the value to near

		Parameters:
			near (string) : A string representing the near
		"""

		if near is not None and not isinstance(near, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: near EXPECTED TYPE: str', None, None)
		
		self.__near = near
		self.__key_modified['near'] = 1

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
