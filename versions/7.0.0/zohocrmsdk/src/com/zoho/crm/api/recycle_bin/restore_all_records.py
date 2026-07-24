try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class RestoreAllRecords(object):
	def __init__(self):
		"""Creates an instance of RestoreAllRecords"""

		self.__restore_all_records = None
		self.__key_modified = dict()

	def get_restore_all_records(self):
		"""
		The method to get the restore_all_records

		Returns:
			Choice: An instance of Choice
		"""

		return self.__restore_all_records

	def set_restore_all_records(self, restore_all_records):
		"""
		The method to set the value to restore_all_records

		Parameters:
			restore_all_records (Choice) : An instance of Choice
		"""

		if restore_all_records is not None and not isinstance(restore_all_records, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: restore_all_records EXPECTED TYPE: Choice', None, None)
		
		self.__restore_all_records = restore_all_records
		self.__key_modified['restore_all_records'] = 1

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
