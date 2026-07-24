try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Multiselectlookup(object):
	def __init__(self):
		"""Creates an instance of Multiselectlookup"""

		self.__linking_details = None
		self.__connected_details = None
		self.__related_list = None
		self.__record_access = None
		self.__key_modified = dict()

	def get_linking_details(self):
		"""
		The method to get the linking_details

		Returns:
			LinkingDetails: An instance of LinkingDetails
		"""

		return self.__linking_details

	def set_linking_details(self, linking_details):
		"""
		The method to set the value to linking_details

		Parameters:
			linking_details (LinkingDetails) : An instance of LinkingDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.linking_details import LinkingDetails
		except Exception:
			from .linking_details import LinkingDetails

		if linking_details is not None and not isinstance(linking_details, LinkingDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: linking_details EXPECTED TYPE: LinkingDetails', None, None)
		
		self.__linking_details = linking_details
		self.__key_modified['linking_details'] = 1

	def get_connected_details(self):
		"""
		The method to get the connected_details

		Returns:
			ConnectedDetails: An instance of ConnectedDetails
		"""

		return self.__connected_details

	def set_connected_details(self, connected_details):
		"""
		The method to set the value to connected_details

		Parameters:
			connected_details (ConnectedDetails) : An instance of ConnectedDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.connected_details import ConnectedDetails
		except Exception:
			from .connected_details import ConnectedDetails

		if connected_details is not None and not isinstance(connected_details, ConnectedDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: connected_details EXPECTED TYPE: ConnectedDetails', None, None)
		
		self.__connected_details = connected_details
		self.__key_modified['connected_details'] = 1

	def get_related_list(self):
		"""
		The method to get the related_list

		Returns:
			LookupRelatedList: An instance of LookupRelatedList
		"""

		return self.__related_list

	def set_related_list(self, related_list):
		"""
		The method to set the value to related_list

		Parameters:
			related_list (LookupRelatedList) : An instance of LookupRelatedList
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.lookup_related_list import LookupRelatedList
		except Exception:
			from .lookup_related_list import LookupRelatedList

		if related_list is not None and not isinstance(related_list, LookupRelatedList):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_list EXPECTED TYPE: LookupRelatedList', None, None)
		
		self.__related_list = related_list
		self.__key_modified['related_list'] = 1

	def get_record_access(self):
		"""
		The method to get the record_access

		Returns:
			bool: A bool representing the record_access
		"""

		return self.__record_access

	def set_record_access(self, record_access):
		"""
		The method to set the value to record_access

		Parameters:
			record_access (bool) : A bool representing the record_access
		"""

		if record_access is not None and not isinstance(record_access, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_access EXPECTED TYPE: bool', None, None)
		
		self.__record_access = record_access
		self.__key_modified['record_access'] = 1

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
