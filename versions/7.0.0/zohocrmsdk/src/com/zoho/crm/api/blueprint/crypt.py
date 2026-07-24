try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Crypt(object):
	def __init__(self):
		"""Creates an instance of Crypt"""

		self.__mode = None
		self.__column = None
		self.__table = None
		self.__status = None
		self.__key_modified = dict()

	def get_mode(self):
		"""
		The method to get the mode

		Returns:
			string: A string representing the mode
		"""

		return self.__mode

	def set_mode(self, mode):
		"""
		The method to set the value to mode

		Parameters:
			mode (string) : A string representing the mode
		"""

		if mode is not None and not isinstance(mode, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mode EXPECTED TYPE: str', None, None)
		
		self.__mode = mode
		self.__key_modified['mode'] = 1

	def get_column(self):
		"""
		The method to get the column

		Returns:
			string: A string representing the column
		"""

		return self.__column

	def set_column(self, column):
		"""
		The method to set the value to column

		Parameters:
			column (string) : A string representing the column
		"""

		if column is not None and not isinstance(column, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: column EXPECTED TYPE: str', None, None)
		
		self.__column = column
		self.__key_modified['column'] = 1

	def get_table(self):
		"""
		The method to get the table

		Returns:
			string: A string representing the table
		"""

		return self.__table

	def set_table(self, table):
		"""
		The method to set the value to table

		Parameters:
			table (string) : A string representing the table
		"""

		if table is not None and not isinstance(table, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: table EXPECTED TYPE: str', None, None)
		
		self.__table = table
		self.__key_modified['table'] = 1

	def get_status(self):
		"""
		The method to get the status

		Returns:
			int: An int representing the status
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (int) : An int representing the status
		"""

		if status is not None and not isinstance(status, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: int', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

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
