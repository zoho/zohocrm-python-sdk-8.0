try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class HipaaCompliance(object):
	def __init__(self):
		"""Creates an instance of HipaaCompliance"""

		self.__enabled = None
		self.__enabled_for_modules = None
		self.__restrict_to_zoho_apps = None
		self.__restrict_data_access_through_api = None
		self.__restrict_data_in_export = None
		self.__restrict_to_third_party_apps = None
		self.__key_modified = dict()

	def get_enabled(self):
		"""
		The method to get the enabled

		Returns:
			bool: A bool representing the enabled
		"""

		return self.__enabled

	def set_enabled(self, enabled):
		"""
		The method to set the value to enabled

		Parameters:
			enabled (bool) : A bool representing the enabled
		"""

		if enabled is not None and not isinstance(enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enabled EXPECTED TYPE: bool', None, None)
		
		self.__enabled = enabled
		self.__key_modified['enabled'] = 1

	def get_enabled_for_modules(self):
		"""
		The method to get the enabled_for_modules

		Returns:
			list: An instance of list
		"""

		return self.__enabled_for_modules

	def set_enabled_for_modules(self, enabled_for_modules):
		"""
		The method to set the value to enabled_for_modules

		Parameters:
			enabled_for_modules (list) : An instance of list
		"""

		if enabled_for_modules is not None and not isinstance(enabled_for_modules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enabled_for_modules EXPECTED TYPE: list', None, None)
		
		self.__enabled_for_modules = enabled_for_modules
		self.__key_modified['enabled_for_modules'] = 1

	def get_restrict_to_zoho_apps(self):
		"""
		The method to get the restrict_to_zoho_apps

		Returns:
			bool: A bool representing the restrict_to_zoho_apps
		"""

		return self.__restrict_to_zoho_apps

	def set_restrict_to_zoho_apps(self, restrict_to_zoho_apps):
		"""
		The method to set the value to restrict_to_zoho_apps

		Parameters:
			restrict_to_zoho_apps (bool) : A bool representing the restrict_to_zoho_apps
		"""

		if restrict_to_zoho_apps is not None and not isinstance(restrict_to_zoho_apps, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_to_zoho_apps EXPECTED TYPE: bool', None, None)
		
		self.__restrict_to_zoho_apps = restrict_to_zoho_apps
		self.__key_modified['restrict_to_zoho_apps'] = 1

	def get_restrict_data_access_through_api(self):
		"""
		The method to get the restrict_data_access_through_api

		Returns:
			bool: A bool representing the restrict_data_access_through_api
		"""

		return self.__restrict_data_access_through_api

	def set_restrict_data_access_through_api(self, restrict_data_access_through_api):
		"""
		The method to set the value to restrict_data_access_through_api

		Parameters:
			restrict_data_access_through_api (bool) : A bool representing the restrict_data_access_through_api
		"""

		if restrict_data_access_through_api is not None and not isinstance(restrict_data_access_through_api, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_data_access_through_api EXPECTED TYPE: bool', None, None)
		
		self.__restrict_data_access_through_api = restrict_data_access_through_api
		self.__key_modified['restrict_data_access_through_api'] = 1

	def get_restrict_data_in_export(self):
		"""
		The method to get the restrict_data_in_export

		Returns:
			bool: A bool representing the restrict_data_in_export
		"""

		return self.__restrict_data_in_export

	def set_restrict_data_in_export(self, restrict_data_in_export):
		"""
		The method to set the value to restrict_data_in_export

		Parameters:
			restrict_data_in_export (bool) : A bool representing the restrict_data_in_export
		"""

		if restrict_data_in_export is not None and not isinstance(restrict_data_in_export, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_data_in_export EXPECTED TYPE: bool', None, None)
		
		self.__restrict_data_in_export = restrict_data_in_export
		self.__key_modified['restrict_data_in_export'] = 1

	def get_restrict_to_third_party_apps(self):
		"""
		The method to get the restrict_to_third_party_apps

		Returns:
			list: An instance of list
		"""

		return self.__restrict_to_third_party_apps

	def set_restrict_to_third_party_apps(self, restrict_to_third_party_apps):
		"""
		The method to set the value to restrict_to_third_party_apps

		Parameters:
			restrict_to_third_party_apps (list) : An instance of list
		"""

		if restrict_to_third_party_apps is not None and not isinstance(restrict_to_third_party_apps, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restrict_to_third_party_apps EXPECTED TYPE: list', None, None)
		
		self.__restrict_to_third_party_apps = restrict_to_third_party_apps
		self.__key_modified['restrict_to_third_party_apps'] = 1

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
