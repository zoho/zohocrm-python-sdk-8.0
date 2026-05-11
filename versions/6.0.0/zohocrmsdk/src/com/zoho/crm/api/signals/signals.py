try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Signals(object):
	def __init__(self):
		"""Creates an instance of Signals"""

		self.__display_label = None
		self.__namespace = None
		self.__chat_enabled = None
		self.__enabled = None
		self.__id = None
		self.__feature_availability = None
		self.__extension = None
		self.__key_modified = dict()

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

	def get_namespace(self):
		"""
		The method to get the namespace

		Returns:
			string: A string representing the namespace
		"""

		return self.__namespace

	def set_namespace(self, namespace):
		"""
		The method to set the value to namespace

		Parameters:
			namespace (string) : A string representing the namespace
		"""

		if namespace is not None and not isinstance(namespace, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: namespace EXPECTED TYPE: str', None, None)
		
		self.__namespace = namespace
		self.__key_modified['namespace'] = 1

	def get_chat_enabled(self):
		"""
		The method to get the chat_enabled

		Returns:
			bool: A bool representing the chat_enabled
		"""

		return self.__chat_enabled

	def set_chat_enabled(self, chat_enabled):
		"""
		The method to set the value to chat_enabled

		Parameters:
			chat_enabled (bool) : A bool representing the chat_enabled
		"""

		if chat_enabled is not None and not isinstance(chat_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: chat_enabled EXPECTED TYPE: bool', None, None)
		
		self.__chat_enabled = chat_enabled
		self.__key_modified['chat_enabled'] = 1

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

	def get_feature_availability(self):
		"""
		The method to get the feature_availability

		Returns:
			FeatureAvailability: An instance of FeatureAvailability
		"""

		return self.__feature_availability

	def set_feature_availability(self, feature_availability):
		"""
		The method to set the value to feature_availability

		Parameters:
			feature_availability (FeatureAvailability) : An instance of FeatureAvailability
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.signals.feature_availability import FeatureAvailability
		except Exception:
			from .feature_availability import FeatureAvailability

		if feature_availability is not None and not isinstance(feature_availability, FeatureAvailability):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: feature_availability EXPECTED TYPE: FeatureAvailability', None, None)
		
		self.__feature_availability = feature_availability
		self.__key_modified['feature_availability'] = 1

	def get_extension(self):
		"""
		The method to get the extension

		Returns:
			Extension: An instance of Extension
		"""

		return self.__extension

	def set_extension(self, extension):
		"""
		The method to set the value to extension

		Parameters:
			extension (Extension) : An instance of Extension
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.signals.extension import Extension
		except Exception:
			from .extension import Extension

		if extension is not None and not isinstance(extension, Extension):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: extension EXPECTED TYPE: Extension', None, None)
		
		self.__extension = extension
		self.__key_modified['extension'] = 1

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
