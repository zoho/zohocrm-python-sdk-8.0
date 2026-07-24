try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class DealField(object):
	def __init__(self):
		"""Creates an instance of DealField"""

		self.__api_name = None
		self.__field_label = None
		self.__id = None
		self.__required = None
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

	def get_field_label(self):
		"""
		The method to get the field_label

		Returns:
			string: A string representing the field_label
		"""

		return self.__field_label

	def set_field_label(self, field_label):
		"""
		The method to set the value to field_label

		Parameters:
			field_label (string) : A string representing the field_label
		"""

		if field_label is not None and not isinstance(field_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_label EXPECTED TYPE: str', None, None)
		
		self.__field_label = field_label
		self.__key_modified['field_label'] = 1

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

	def get_required(self):
		"""
		The method to get the required

		Returns:
			bool: A bool representing the required
		"""

		return self.__required

	def set_required(self, required):
		"""
		The method to set the value to required

		Parameters:
			required (bool) : A bool representing the required
		"""

		if required is not None and not isinstance(required, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: required EXPECTED TYPE: bool', None, None)
		
		self.__required = required
		self.__key_modified['required'] = 1

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
