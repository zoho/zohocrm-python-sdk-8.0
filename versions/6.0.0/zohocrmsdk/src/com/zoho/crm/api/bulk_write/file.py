try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class File(object):
	def __init__(self):
		"""Creates an instance of File"""

		self.__status = None
		self.__name = None
		self.__added_count = None
		self.__skipped_count = None
		self.__updated_count = None
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
		self.__key_modified['status'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_added_count(self):
		"""
		The method to get the added_count

		Returns:
			int: An int representing the added_count
		"""

		return self.__added_count

	def set_added_count(self, added_count):
		"""
		The method to set the value to added_count

		Parameters:
			added_count (int) : An int representing the added_count
		"""

		if added_count is not None and not isinstance(added_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: added_count EXPECTED TYPE: int', None, None)
		
		self.__added_count = added_count
		self.__key_modified['added_count'] = 1

	def get_skipped_count(self):
		"""
		The method to get the skipped_count

		Returns:
			int: An int representing the skipped_count
		"""

		return self.__skipped_count

	def set_skipped_count(self, skipped_count):
		"""
		The method to set the value to skipped_count

		Parameters:
			skipped_count (int) : An int representing the skipped_count
		"""

		if skipped_count is not None and not isinstance(skipped_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: skipped_count EXPECTED TYPE: int', None, None)
		
		self.__skipped_count = skipped_count
		self.__key_modified['skipped_count'] = 1

	def get_updated_count(self):
		"""
		The method to get the updated_count

		Returns:
			int: An int representing the updated_count
		"""

		return self.__updated_count

	def set_updated_count(self, updated_count):
		"""
		The method to set the value to updated_count

		Parameters:
			updated_count (int) : An int representing the updated_count
		"""

		if updated_count is not None and not isinstance(updated_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: updated_count EXPECTED TYPE: int', None, None)
		
		self.__updated_count = updated_count
		self.__key_modified['updated_count'] = 1

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
		self.__key_modified['total_count'] = 1

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
