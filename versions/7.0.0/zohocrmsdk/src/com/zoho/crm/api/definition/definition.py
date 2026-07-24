try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Definition(object):
	def __init__(self):
		"""Creates an instance of Definition"""

		self.__root_element_name = None
		self.__extradetails = None
		self.__properties = None
		self.__key_modified = dict()

	def get_root_element_name(self):
		"""
		The method to get the root_element_name

		Returns:
			string: A string representing the root_element_name
		"""

		return self.__root_element_name

	def set_root_element_name(self, root_element_name):
		"""
		The method to set the value to root_element_name

		Parameters:
			root_element_name (string) : A string representing the root_element_name
		"""

		if root_element_name is not None and not isinstance(root_element_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: root_element_name EXPECTED TYPE: str', None, None)
		
		self.__root_element_name = root_element_name
		self.__key_modified['root_element_name'] = 1

	def get_extradetails(self):
		"""
		The method to get the extradetails

		Returns:
			dict: An instance of dict
		"""

		return self.__extradetails

	def set_extradetails(self, extradetails):
		"""
		The method to set the value to extradetails

		Parameters:
			extradetails (dict) : An instance of dict
		"""

		if extradetails is not None and not isinstance(extradetails, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: extradetails EXPECTED TYPE: dict', None, None)
		
		self.__extradetails = extradetails
		self.__key_modified['extraDetails'] = 1

	def get_properties(self):
		"""
		The method to get the properties

		Returns:
			list: An instance of list
		"""

		return self.__properties

	def set_properties(self, properties):
		"""
		The method to set the value to properties

		Parameters:
			properties (list) : An instance of list
		"""

		if properties is not None and not isinstance(properties, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: properties EXPECTED TYPE: list', None, None)
		
		self.__properties = properties
		self.__key_modified['properties'] = 1

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
