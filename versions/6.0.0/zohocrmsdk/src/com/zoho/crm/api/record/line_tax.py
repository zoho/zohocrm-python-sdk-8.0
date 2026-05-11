try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class LineTax(object):
	def __init__(self):
		"""Creates an instance of LineTax"""

		self.__percentage = None
		self.__name = None
		self.__id = None
		self.__value = None
		self.__display_name = None
		self.__key_modified = dict()

	def get_percentage(self):
		"""
		The method to get the percentage

		Returns:
			float: A float representing the percentage
		"""

		return self.__percentage

	def set_percentage(self, percentage):
		"""
		The method to set the value to percentage

		Parameters:
			percentage (float) : A float representing the percentage
		"""

		if percentage is not None and not isinstance(percentage, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: percentage EXPECTED TYPE: float', None, None)
		
		self.__percentage = percentage
		self.__key_modified['percentage'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

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

	def get_value(self):
		"""
		The method to get the value

		Returns:
			float: A float representing the value
		"""

		return self.__value

	def set_value(self, value):
		"""
		The method to set the value to value

		Parameters:
			value (float) : A float representing the value
		"""

		if value is not None and not isinstance(value, float):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: value EXPECTED TYPE: float', None, None)
		
		self.__value = value
		self.__key_modified['value'] = 1

	def get_display_name(self):
		"""
		The method to get the display_name

		Returns:
			string: A string representing the display_name
		"""

		return self.__display_name

	def set_display_name(self, display_name):
		"""
		The method to set the value to display_name

		Parameters:
			display_name (string) : A string representing the display_name
		"""

		if display_name is not None and not isinstance(display_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_name EXPECTED TYPE: str', None, None)
		
		self.__display_name = display_name
		self.__key_modified['display_name'] = 1

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
