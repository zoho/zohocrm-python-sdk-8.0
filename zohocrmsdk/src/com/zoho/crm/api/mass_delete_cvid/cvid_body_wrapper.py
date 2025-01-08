try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class CvidBodyWrapper(object):
	def __init__(self):
		"""Creates an instance of CvidBodyWrapper"""

		self.__cvid = None
		self.__territory = None
		self.__key_modified = dict()

	def get_cvid(self):
		"""
		The method to get the cvid

		Returns:
			int: An int representing the cvid
		"""

		return self.__cvid

	def set_cvid(self, cvid):
		"""
		The method to set the value to cvid

		Parameters:
			cvid (int) : An int representing the cvid
		"""

		if cvid is not None and not isinstance(cvid, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cvid EXPECTED TYPE: int', None, None)
		
		self.__cvid = cvid
		self.__key_modified['cvid'] = 1

	def get_territory(self):
		"""
		The method to get the territory

		Returns:
			Territory: An instance of Territory
		"""

		return self.__territory

	def set_territory(self, territory):
		"""
		The method to set the value to territory

		Parameters:
			territory (Territory) : An instance of Territory
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mass_delete_cvid.territory import Territory
		except Exception:
			from .territory import Territory

		if territory is not None and not isinstance(territory, Territory):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: Territory', None, None)
		
		self.__territory = territory
		self.__key_modified['territory'] = 1

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
