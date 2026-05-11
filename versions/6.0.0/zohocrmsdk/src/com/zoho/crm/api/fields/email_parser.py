try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class EmailParser(object):
	def __init__(self):
		"""Creates an instance of EmailParser"""

		self.__fields_update_supported = None
		self.__record_operations_supported = None
		self.__key_modified = dict()

	def get_fields_update_supported(self):
		"""
		The method to get the fields_update_supported

		Returns:
			bool: A bool representing the fields_update_supported
		"""

		return self.__fields_update_supported

	def set_fields_update_supported(self, fields_update_supported):
		"""
		The method to set the value to fields_update_supported

		Parameters:
			fields_update_supported (bool) : A bool representing the fields_update_supported
		"""

		if fields_update_supported is not None and not isinstance(fields_update_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields_update_supported EXPECTED TYPE: bool', None, None)
		
		self.__fields_update_supported = fields_update_supported
		self.__key_modified['fields_update_supported'] = 1

	def get_record_operations_supported(self):
		"""
		The method to get the record_operations_supported

		Returns:
			bool: A bool representing the record_operations_supported
		"""

		return self.__record_operations_supported

	def set_record_operations_supported(self, record_operations_supported):
		"""
		The method to set the value to record_operations_supported

		Parameters:
			record_operations_supported (bool) : A bool representing the record_operations_supported
		"""

		if record_operations_supported is not None and not isinstance(record_operations_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_operations_supported EXPECTED TYPE: bool', None, None)
		
		self.__record_operations_supported = record_operations_supported
		self.__key_modified['record_operations_supported'] = 1

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
