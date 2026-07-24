try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Screen(object):
	def __init__(self):
		"""Creates an instance of Screen"""

		self.__display_label = None
		self.__api_name = None
		self.__id = None
		self.__reference_id = None
		self.__conditional_rules = None
		self.__segments = None
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

	def get_reference_id(self):
		"""
		The method to get the reference_id

		Returns:
			string: A string representing the reference_id
		"""

		return self.__reference_id

	def set_reference_id(self, reference_id):
		"""
		The method to set the value to reference_id

		Parameters:
			reference_id (string) : A string representing the reference_id
		"""

		if reference_id is not None and not isinstance(reference_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reference_id EXPECTED TYPE: str', None, None)
		
		self.__reference_id = reference_id
		self.__key_modified['reference_id'] = 1

	def get_conditional_rules(self):
		"""
		The method to get the conditional_rules

		Returns:
			list: An instance of list
		"""

		return self.__conditional_rules

	def set_conditional_rules(self, conditional_rules):
		"""
		The method to set the value to conditional_rules

		Parameters:
			conditional_rules (list) : An instance of list
		"""

		if conditional_rules is not None and not isinstance(conditional_rules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: conditional_rules EXPECTED TYPE: list', None, None)
		
		self.__conditional_rules = conditional_rules
		self.__key_modified['conditional_rules'] = 1

	def get_segments(self):
		"""
		The method to get the segments

		Returns:
			list: An instance of list
		"""

		return self.__segments

	def set_segments(self, segments):
		"""
		The method to set the value to segments

		Parameters:
			segments (list) : An instance of list
		"""

		if segments is not None and not isinstance(segments, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: segments EXPECTED TYPE: list', None, None)
		
		self.__segments = segments
		self.__key_modified['segments'] = 1

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
