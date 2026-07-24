try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class CompanyInfo(object):
	def __init__(self):
		"""Creates an instance of CompanyInfo"""

		self.__name = None
		self.__industries = None
		self.__experiences = None
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

	def get_industries(self):
		"""
		The method to get the industries

		Returns:
			list: An instance of list
		"""

		return self.__industries

	def set_industries(self, industries):
		"""
		The method to set the value to industries

		Parameters:
			industries (list) : An instance of list
		"""

		if industries is not None and not isinstance(industries, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: industries EXPECTED TYPE: list', None, None)
		
		self.__industries = industries
		self.__key_modified['industries'] = 1

	def get_experiences(self):
		"""
		The method to get the experiences

		Returns:
			list: An instance of list
		"""

		return self.__experiences

	def set_experiences(self, experiences):
		"""
		The method to set the value to experiences

		Parameters:
			experiences (list) : An instance of list
		"""

		if experiences is not None and not isinstance(experiences, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: experiences EXPECTED TYPE: list', None, None)
		
		self.__experiences = experiences
		self.__key_modified['experiences'] = 1

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
