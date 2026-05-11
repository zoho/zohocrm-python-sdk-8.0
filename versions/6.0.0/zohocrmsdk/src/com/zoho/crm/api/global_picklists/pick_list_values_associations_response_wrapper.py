try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.global_picklists.pick_list_values_associations_response_handler import PickListValuesAssociationsResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .pick_list_values_associations_response_handler import PickListValuesAssociationsResponseHandler


class PickListValuesAssociationsResponseWrapper(PickListValuesAssociationsResponseHandler):
	def __init__(self):
		"""Creates an instance of PickListValuesAssociationsResponseWrapper"""
		super().__init__()

		self.__pick_list_values_associations = None
		self.__key_modified = dict()

	def get_pick_list_values_associations(self):
		"""
		The method to get the pick_list_values_associations

		Returns:
			list: An instance of list
		"""

		return self.__pick_list_values_associations

	def set_pick_list_values_associations(self, pick_list_values_associations):
		"""
		The method to set the value to pick_list_values_associations

		Parameters:
			pick_list_values_associations (list) : An instance of list
		"""

		if pick_list_values_associations is not None and not isinstance(pick_list_values_associations, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pick_list_values_associations EXPECTED TYPE: list', None, None)
		
		self.__pick_list_values_associations = pick_list_values_associations
		self.__key_modified['pick_list_values_associations'] = 1

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
