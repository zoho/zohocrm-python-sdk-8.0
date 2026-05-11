try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class GetRelatedRecordCount(object):
	def __init__(self):
		"""Creates an instance of GetRelatedRecordCount"""

		self.__related_list = None
		self.__key_modified = dict()

	def get_related_list(self):
		"""
		The method to get the related_list

		Returns:
			RelatedList: An instance of RelatedList
		"""

		return self.__related_list

	def set_related_list(self, related_list):
		"""
		The method to set the value to related_list

		Parameters:
			related_list (RelatedList) : An instance of RelatedList
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.get_related_records_count.related_list import RelatedList
		except Exception:
			from .related_list import RelatedList

		if related_list is not None and not isinstance(related_list, RelatedList):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_list EXPECTED TYPE: RelatedList', None, None)
		
		self.__related_list = related_list
		self.__key_modified['related_list'] = 1

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
