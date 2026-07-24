try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class DeletedAssociatedTerritories(object):
	def __init__(self):
		"""Creates an instance of DeletedAssociatedTerritories"""

		self.__name = None
		self.__id = None
		self.__deleted_time = None
		self.__deleted_by = None
		self.__key_modified = dict()

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

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string representing the id
		"""

		if id is not None and not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_deleted_time(self):
		"""
		The method to get the deleted_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__deleted_time

	def set_deleted_time(self, deleted_time):
		"""
		The method to set the value to deleted_time

		Parameters:
			deleted_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if deleted_time is not None and not isinstance(deleted_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deleted_time EXPECTED TYPE: datetime', None, None)
		
		self.__deleted_time = deleted_time
		self.__key_modified['deleted_time'] = 1

	def get_deleted_by(self):
		"""
		The method to get the deleted_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__deleted_by

	def set_deleted_by(self, deleted_by):
		"""
		The method to set the value to deleted_by

		Parameters:
			deleted_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if deleted_by is not None and not isinstance(deleted_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deleted_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__deleted_by = deleted_by
		self.__key_modified['deleted_by'] = 1

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
