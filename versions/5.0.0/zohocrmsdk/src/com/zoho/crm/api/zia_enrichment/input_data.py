try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class InputData(object):
	def __init__(self):
		"""Creates an instance of InputData"""

		self.__enrich_field = None
		self.__crm_field = None
		self.__key_modified = dict()

	def get_enrich_field(self):
		"""
		The method to get the enrich_field

		Returns:
			EnrichField: An instance of EnrichField
		"""

		return self.__enrich_field

	def set_enrich_field(self, enrich_field):
		"""
		The method to set the value to enrich_field

		Parameters:
			enrich_field (EnrichField) : An instance of EnrichField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_enrichment.enrich_field import EnrichField
		except Exception:
			from .enrich_field import EnrichField

		if enrich_field is not None and not isinstance(enrich_field, EnrichField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enrich_field EXPECTED TYPE: EnrichField', None, None)
		
		self.__enrich_field = enrich_field
		self.__key_modified['enrich_field'] = 1

	def get_crm_field(self):
		"""
		The method to get the crm_field

		Returns:
			CrmField: An instance of CrmField
		"""

		return self.__crm_field

	def set_crm_field(self, crm_field):
		"""
		The method to set the value to crm_field

		Parameters:
			crm_field (CrmField) : An instance of CrmField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_enrichment.crm_field import CrmField
		except Exception:
			from .crm_field import CrmField

		if crm_field is not None and not isinstance(crm_field, CrmField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: crm_field EXPECTED TYPE: CrmField', None, None)
		
		self.__crm_field = crm_field
		self.__key_modified['crm_field'] = 1

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
