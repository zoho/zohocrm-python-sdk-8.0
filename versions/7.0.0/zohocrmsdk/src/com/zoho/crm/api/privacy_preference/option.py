try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Option(object):
	def __init__(self):
		"""Creates an instance of Option"""

		self.__name = None
		self.__tooltip = None
		self.__type = None
		self.__suboptions = None
		self.__key_modified = dict()

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

	def get_tooltip(self):
		"""
		The method to get the tooltip

		Returns:
			string: A string representing the tooltip
		"""

		return self.__tooltip

	def set_tooltip(self, tooltip):
		"""
		The method to set the value to tooltip

		Parameters:
			tooltip (string) : A string representing the tooltip
		"""

		if tooltip is not None and not isinstance(tooltip, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tooltip EXPECTED TYPE: str', None, None)
		
		self.__tooltip = tooltip
		self.__key_modified['tooltip'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_suboptions(self):
		"""
		The method to get the suboptions

		Returns:
			list: An instance of list
		"""

		return self.__suboptions

	def set_suboptions(self, suboptions):
		"""
		The method to set the value to suboptions

		Parameters:
			suboptions (list) : An instance of list
		"""

		if suboptions is not None and not isinstance(suboptions, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: suboptions EXPECTED TYPE: list', None, None)
		
		self.__suboptions = suboptions
		self.__key_modified['suboptions'] = 1

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
