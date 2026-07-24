try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Portals(object):
	def __init__(self):
		"""Creates an instance of Portals"""

		self.__created_time = None
		self.__modified_time = None
		self.__modified_by = None
		self.__created_by = None
		self.__zaid = None
		self.__name = None
		self.__active = None
		self.__key_modified = dict()

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
			from zohocrmsdk.src.com.zoho.crm.api.portals.owner import Owner
		except Exception:
			from .owner import Owner

		if modified_by is not None and not isinstance(modified_by, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: Owner', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.portals.owner import Owner
		except Exception:
			from .owner import Owner

		if created_by is not None and not isinstance(created_by, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: Owner', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_zaid(self):
		"""
		The method to get the zaid

		Returns:
			string: A string representing the zaid
		"""

		return self.__zaid

	def set_zaid(self, zaid):
		"""
		The method to set the value to zaid

		Parameters:
			zaid (string) : A string representing the zaid
		"""

		if zaid is not None and not isinstance(zaid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zaid EXPECTED TYPE: str', None, None)
		
		self.__zaid = zaid
		self.__key_modified['zaid'] = 1

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

	def get_active(self):
		"""
		The method to get the active

		Returns:
			bool: A bool representing the active
		"""

		return self.__active

	def set_active(self, active):
		"""
		The method to set the value to active

		Parameters:
			active (bool) : A bool representing the active
		"""

		if active is not None and not isinstance(active, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: active EXPECTED TYPE: bool', None, None)
		
		self.__active = active
		self.__key_modified['active'] = 1

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
