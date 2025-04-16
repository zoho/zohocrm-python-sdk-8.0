try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Config(object):
	def __init__(self):
		"""Creates an instance of Config"""

		self.__tpt = None
		self.__section = None
		self.__zoho_integ = None
		self.__key_modified = dict()

	def get_tpt(self):
		"""
		The method to get the tpt

		Returns:
			list: An instance of list
		"""

		return self.__tpt

	def set_tpt(self, tpt):
		"""
		The method to set the value to tpt

		Parameters:
			tpt (list) : An instance of list
		"""

		if tpt is not None and not isinstance(tpt, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tpt EXPECTED TYPE: list', None, None)
		
		self.__tpt = tpt
		self.__key_modified['tpt'] = 1

	def get_section(self):
		"""
		The method to get the section

		Returns:
			list: An instance of list
		"""

		return self.__section

	def set_section(self, section):
		"""
		The method to set the value to section

		Parameters:
			section (list) : An instance of list
		"""

		if section is not None and not isinstance(section, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: section EXPECTED TYPE: list', None, None)
		
		self.__section = section
		self.__key_modified['section'] = 1

	def get_zoho_integ(self):
		"""
		The method to get the zoho_integ

		Returns:
			list: An instance of list
		"""

		return self.__zoho_integ

	def set_zoho_integ(self, zoho_integ):
		"""
		The method to set the value to zoho_integ

		Parameters:
			zoho_integ (list) : An instance of list
		"""

		if zoho_integ is not None and not isinstance(zoho_integ, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zoho_integ EXPECTED TYPE: list', None, None)
		
		self.__zoho_integ = zoho_integ
		self.__key_modified['zoho_integ'] = 1

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
