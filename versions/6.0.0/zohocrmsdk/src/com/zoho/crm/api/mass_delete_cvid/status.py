try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Status(object):
	def __init__(self):
		"""Creates an instance of Status"""

		self.__status = None
		self.__failed_count = None
		self.__deleted_count = None
		self.__total_count = None
		self.__key_modified = dict()

	def get_status(self):
		"""
		The method to get the status

		Returns:
			Choice: An instance of Choice
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (Choice) : An instance of Choice
		"""

		if status is not None and not isinstance(status, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: Choice', None, None)
		
		self.__status = status
		self.__key_modified['Status'] = 1

	def get_failed_count(self):
		"""
		The method to get the failed_count

		Returns:
			int: An int representing the failed_count
		"""

		return self.__failed_count

	def set_failed_count(self, failed_count):
		"""
		The method to set the value to failed_count

		Parameters:
			failed_count (int) : An int representing the failed_count
		"""

		if failed_count is not None and not isinstance(failed_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: failed_count EXPECTED TYPE: int', None, None)
		
		self.__failed_count = failed_count
		self.__key_modified['Failed_Count'] = 1

	def get_deleted_count(self):
		"""
		The method to get the deleted_count

		Returns:
			int: An int representing the deleted_count
		"""

		return self.__deleted_count

	def set_deleted_count(self, deleted_count):
		"""
		The method to set the value to deleted_count

		Parameters:
			deleted_count (int) : An int representing the deleted_count
		"""

		if deleted_count is not None and not isinstance(deleted_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deleted_count EXPECTED TYPE: int', None, None)
		
		self.__deleted_count = deleted_count
		self.__key_modified['Deleted_Count'] = 1

	def get_total_count(self):
		"""
		The method to get the total_count

		Returns:
			int: An int representing the total_count
		"""

		return self.__total_count

	def set_total_count(self, total_count):
		"""
		The method to set the value to total_count

		Parameters:
			total_count (int) : An int representing the total_count
		"""

		if total_count is not None and not isinstance(total_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: total_count EXPECTED TYPE: int', None, None)
		
		self.__total_count = total_count
		self.__key_modified['Total_Count'] = 1

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
