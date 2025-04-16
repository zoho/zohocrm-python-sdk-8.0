try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ZiaOrgEnrichment(object):
	def __init__(self):
		"""Creates an instance of ZiaOrgEnrichment"""

		self.__enriched_data = None
		self.__created_time = None
		self.__id = None
		self.__created_by = None
		self.__status = None
		self.__enrich_based_on = None
		self.__key_modified = dict()

	def get_enriched_data(self):
		"""
		The method to get the enriched_data

		Returns:
			EnrichedData: An instance of EnrichedData
		"""

		return self.__enriched_data

	def set_enriched_data(self, enriched_data):
		"""
		The method to set the value to enriched_data

		Parameters:
			enriched_data (EnrichedData) : An instance of EnrichedData
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.enriched_data import EnrichedData
		except Exception:
			from .enriched_data import EnrichedData

		if enriched_data is not None and not isinstance(enriched_data, EnrichedData):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enriched_data EXPECTED TYPE: EnrichedData', None, None)
		
		self.__enriched_data = enriched_data
		self.__key_modified['enriched_data'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			string: A string representing the created_time
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (string) : A string representing the created_time
		"""

		if created_time is not None and not isinstance(created_time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: str', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

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

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			User: An instance of User
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.user import User
		except Exception:
			from .user import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_status(self):
		"""
		The method to get the status

		Returns:
			string: A string representing the status
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (string) : A string representing the status
		"""

		if status is not None and not isinstance(status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: str', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def get_enrich_based_on(self):
		"""
		The method to get the enrich_based_on

		Returns:
			EnrichBasedOn: An instance of EnrichBasedOn
		"""

		return self.__enrich_based_on

	def set_enrich_based_on(self, enrich_based_on):
		"""
		The method to set the value to enrich_based_on

		Parameters:
			enrich_based_on (EnrichBasedOn) : An instance of EnrichBasedOn
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.enrich_based_on import EnrichBasedOn
		except Exception:
			from .enrich_based_on import EnrichBasedOn

		if enrich_based_on is not None and not isinstance(enrich_based_on, EnrichBasedOn):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enrich_based_on EXPECTED TYPE: EnrichBasedOn', None, None)
		
		self.__enrich_based_on = enrich_based_on
		self.__key_modified['enrich_based_on'] = 1

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
