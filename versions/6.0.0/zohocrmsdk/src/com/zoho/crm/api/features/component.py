try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Component(object):
	def __init__(self):
		"""Creates an instance of Component"""

		self.__api_name = None
		self.__module_supported = None
		self.__details = None
		self.__feature_label = None
		self.__key_modified = dict()

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_module_supported(self):
		"""
		The method to get the module_supported

		Returns:
			bool: A bool representing the module_supported
		"""

		return self.__module_supported

	def set_module_supported(self, module_supported):
		"""
		The method to set the value to module_supported

		Parameters:
			module_supported (bool) : A bool representing the module_supported
		"""

		if module_supported is not None and not isinstance(module_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_supported EXPECTED TYPE: bool', None, None)
		
		self.__module_supported = module_supported
		self.__key_modified['module_supported'] = 1

	def get_details(self):
		"""
		The method to get the details

		Returns:
			Detail: An instance of Detail
		"""

		return self.__details

	def set_details(self, details):
		"""
		The method to set the value to details

		Parameters:
			details (Detail) : An instance of Detail
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.features.detail import Detail
		except Exception:
			from .detail import Detail

		if details is not None and not isinstance(details, Detail):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: details EXPECTED TYPE: Detail', None, None)
		
		self.__details = details
		self.__key_modified['details'] = 1

	def get_feature_label(self):
		"""
		The method to get the feature_label

		Returns:
			string: A string representing the feature_label
		"""

		return self.__feature_label

	def set_feature_label(self, feature_label):
		"""
		The method to set the value to feature_label

		Parameters:
			feature_label (string) : A string representing the feature_label
		"""

		if feature_label is not None and not isinstance(feature_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: feature_label EXPECTED TYPE: str', None, None)
		
		self.__feature_label = feature_label
		self.__key_modified['feature_label'] = 1

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
