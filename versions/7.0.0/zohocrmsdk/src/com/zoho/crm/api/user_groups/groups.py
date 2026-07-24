try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Groups(object):
	def __init__(self):
		"""Creates an instance of Groups"""

		self.__created_by = None
		self.__modified_by = None
		self.__modified_time = None
		self.__created_time = None
		self.__description = None
		self.__id = None
		self.__name = None
		self.__sources_count = None
		self.__sources = None
		self.__key_modified = dict()

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			Owner: An instance of Owner
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.owner import Owner
		except Exception:
			from .owner import Owner

		if created_by is not None and not isinstance(created_by, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: Owner', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			Owner: An instance of Owner
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.owner import Owner
		except Exception:
			from .owner import Owner

		if modified_by is not None and not isinstance(modified_by, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: Owner', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

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

	def get_sources_count(self):
		"""
		The method to get the sources_count

		Returns:
			SourcesCount: An instance of SourcesCount
		"""

		return self.__sources_count

	def set_sources_count(self, sources_count):
		"""
		The method to set the value to sources_count

		Parameters:
			sources_count (SourcesCount) : An instance of SourcesCount
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.sources_count import SourcesCount
		except Exception:
			from .sources_count import SourcesCount

		if sources_count is not None and not isinstance(sources_count, SourcesCount):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sources_count EXPECTED TYPE: SourcesCount', None, None)
		
		self.__sources_count = sources_count
		self.__key_modified['sources_count'] = 1

	def get_sources(self):
		"""
		The method to get the sources

		Returns:
			list: An instance of list
		"""

		return self.__sources

	def set_sources(self, sources):
		"""
		The method to set the value to sources

		Parameters:
			sources (list) : An instance of list
		"""

		if sources is not None and not isinstance(sources, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sources EXPECTED TYPE: list', None, None)
		
		self.__sources = sources
		self.__key_modified['sources'] = 1

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
