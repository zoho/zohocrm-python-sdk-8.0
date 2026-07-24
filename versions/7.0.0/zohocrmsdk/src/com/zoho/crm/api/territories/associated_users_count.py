try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AssociatedUsersCount(object):
	def __init__(self):
		"""Creates an instance of AssociatedUsersCount"""

		self.__count = None
		self.__territory = None
		self.__key_modified = dict()

	def get_count(self):
		"""
		The method to get the count

		Returns:
			string: A string representing the count
		"""

		return self.__count

	def set_count(self, count):
		"""
		The method to set the value to count

		Parameters:
			count (string) : A string representing the count
		"""

		if count is not None and not isinstance(count, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: count EXPECTED TYPE: str', None, None)
		
		self.__count = count
		self.__key_modified['count'] = 1

	def get_territory(self):
		"""
		The method to get the territory

		Returns:
			MinifiedTerritory: An instance of MinifiedTerritory
		"""

		return self.__territory

	def set_territory(self, territory):
		"""
		The method to set the value to territory

		Parameters:
			territory (MinifiedTerritory) : An instance of MinifiedTerritory
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.territories.minified_territory import MinifiedTerritory
		except Exception:
			from .minified_territory import MinifiedTerritory

		if territory is not None and not isinstance(territory, MinifiedTerritory):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: MinifiedTerritory', None, None)
		
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
