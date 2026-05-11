try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class MassUpdateBodyWrapper(object):
	def __init__(self):
		"""Creates an instance of MassUpdateBodyWrapper"""

		self.__data = None
		self.__cvid = None
		self.__ids = None
		self.__territory = None
		self.__over_write = None
		self.__criteria = None
		self.__key_modified = dict()

	def get_data(self):
		"""
		The method to get the data

		Returns:
			list: An instance of list
		"""

		return self.__data

	def set_data(self, data):
		"""
		The method to set the value to data

		Parameters:
			data (list) : An instance of list
		"""

		if data is not None and not isinstance(data, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data EXPECTED TYPE: list', None, None)
		
		self.__data = data
		self.__key_modified['data'] = 1

	def get_cvid(self):
		"""
		The method to get the cvid

		Returns:
			string: A string representing the cvid
		"""

		return self.__cvid

	def set_cvid(self, cvid):
		"""
		The method to set the value to cvid

		Parameters:
			cvid (string) : A string representing the cvid
		"""

		if cvid is not None and not isinstance(cvid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cvid EXPECTED TYPE: str', None, None)
		
		self.__cvid = cvid
		self.__key_modified['cvid'] = 1

	def get_ids(self):
		"""
		The method to get the ids

		Returns:
			list: An instance of list
		"""

		return self.__ids

	def set_ids(self, ids):
		"""
		The method to set the value to ids

		Parameters:
			ids (list) : An instance of list
		"""

		if ids is not None and not isinstance(ids, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ids EXPECTED TYPE: list', None, None)
		
		self.__ids = ids
		self.__key_modified['ids'] = 1

	def get_territory(self):
		"""
		The method to get the territory

		Returns:
			MassUpdateTerritory: An instance of MassUpdateTerritory
		"""

		return self.__territory

	def set_territory(self, territory):
		"""
		The method to set the value to territory

		Parameters:
			territory (MassUpdateTerritory) : An instance of MassUpdateTerritory
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.mass_update_territory import MassUpdateTerritory
		except Exception:
			from .mass_update_territory import MassUpdateTerritory

		if territory is not None and not isinstance(territory, MassUpdateTerritory):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: MassUpdateTerritory', None, None)
		
		self.__territory = territory
		self.__key_modified['territory'] = 1

	def get_over_write(self):
		"""
		The method to get the over_write

		Returns:
			bool: A bool representing the over_write
		"""

		return self.__over_write

	def set_over_write(self, over_write):
		"""
		The method to set the value to over_write

		Parameters:
			over_write (bool) : A bool representing the over_write
		"""

		if over_write is not None and not isinstance(over_write, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: over_write EXPECTED TYPE: bool', None, None)
		
		self.__over_write = over_write
		self.__key_modified['over_write'] = 1

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			list: An instance of list
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (list) : An instance of list
		"""

		if criteria is not None and not isinstance(criteria, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: list', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

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
