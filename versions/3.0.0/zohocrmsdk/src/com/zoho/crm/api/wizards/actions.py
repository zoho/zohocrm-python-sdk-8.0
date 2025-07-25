try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Actions(object):
	def __init__(self):
		"""Creates an instance of Actions"""

		self.__id = None
		self.__type = None
		self.__segment = None
		self.__fields = None
		self.__field = None
		self.__value = None
		self.__exempted_profiles = None
		self.__key_modified = dict()

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

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_segment(self):
		"""
		The method to get the segment

		Returns:
			Segment: An instance of Segment
		"""

		return self.__segment

	def set_segment(self, segment):
		"""
		The method to set the value to segment

		Parameters:
			segment (Segment) : An instance of Segment
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.wizards.segment import Segment
		except Exception:
			from .segment import Segment

		if segment is not None and not isinstance(segment, Segment):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: segment EXPECTED TYPE: Segment', None, None)
		
		self.__segment = segment
		self.__key_modified['segment'] = 1

	def get_fields(self):
		"""
		The method to get the fields

		Returns:
			Fields: An instance of Fields
		"""

		return self.__fields

	def set_fields(self, fields):
		"""
		The method to set the value to fields

		Parameters:
			fields (Fields) : An instance of Fields
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Fields
		except Exception:
			from ..fields import Fields

		if fields is not None and not isinstance(fields, Fields):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: Fields', None, None)
		
		self.__fields = fields
		self.__key_modified['fields'] = 1

	def get_field(self):
		"""
		The method to get the field

		Returns:
			Fields: An instance of Fields
		"""

		return self.__field

	def set_field(self, field):
		"""
		The method to set the value to field

		Parameters:
			field (Fields) : An instance of Fields
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Fields
		except Exception:
			from ..fields import Fields

		if field is not None and not isinstance(field, Fields):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field EXPECTED TYPE: Fields', None, None)
		
		self.__field = field
		self.__key_modified['field'] = 1

	def get_value(self):
		"""
		The method to get the value

		Returns:
			Object: A Object representing the value
		"""

		return self.__value

	def set_value(self, value):
		"""
		The method to set the value to value

		Parameters:
			value (Object) : A Object representing the value
		"""

		self.__value = value
		self.__key_modified['value'] = 1

	def get_exempted_profiles(self):
		"""
		The method to get the exempted_profiles

		Returns:
			list: An instance of list
		"""

		return self.__exempted_profiles

	def set_exempted_profiles(self, exempted_profiles):
		"""
		The method to set the value to exempted_profiles

		Parameters:
			exempted_profiles (list) : An instance of list
		"""

		if exempted_profiles is not None and not isinstance(exempted_profiles, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exempted_profiles EXPECTED TYPE: list', None, None)
		
		self.__exempted_profiles = exempted_profiles
		self.__key_modified['exempted_profiles'] = 1

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
