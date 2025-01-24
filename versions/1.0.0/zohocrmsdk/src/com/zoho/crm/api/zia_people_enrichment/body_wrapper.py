try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__zia_people_enrichment = None
		self.__key_modified = dict()

	def get_zia_people_enrichment(self):
		"""
		The method to get the zia_people_enrichment

		Returns:
			list: An instance of list
		"""

		return self.__zia_people_enrichment

	def set_zia_people_enrichment(self, zia_people_enrichment):
		"""
		The method to set the value to zia_people_enrichment

		Parameters:
			zia_people_enrichment (list) : An instance of list
		"""

		if zia_people_enrichment is not None and not isinstance(zia_people_enrichment, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zia_people_enrichment EXPECTED TYPE: list', None, None)
		
		self.__zia_people_enrichment = zia_people_enrichment
		self.__key_modified['__zia_people_enrichment'] = 1

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
