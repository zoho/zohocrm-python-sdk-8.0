try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class ShareRecord(object):
	def __init__(self):
		"""Creates an instance of ShareRecord"""

		self.__shared_with = None
		self.__share_related_records = None
		self.__shared_through = None
		self.__shared_time = None
		self.__permission = None
		self.__shared_by = None
		self.__user = None
		self.__type = None
		self.__key_modified = dict()

	def get_shared_with(self):
		"""
		The method to get the shared_with

		Returns:
			Users: An instance of Users
		"""

		return self.__shared_with

	def set_shared_with(self, shared_with):
		"""
		The method to set the value to shared_with

		Parameters:
			shared_with (Users) : An instance of Users
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import Users
		except Exception:
			from ..users import Users

		if shared_with is not None and not isinstance(shared_with, Users):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_with EXPECTED TYPE: Users', None, None)
		
		self.__shared_with = shared_with
		self.__key_modified['shared_with'] = 1

	def get_share_related_records(self):
		"""
		The method to get the share_related_records

		Returns:
			bool: A bool representing the share_related_records
		"""

		return self.__share_related_records

	def set_share_related_records(self, share_related_records):
		"""
		The method to set the value to share_related_records

		Parameters:
			share_related_records (bool) : A bool representing the share_related_records
		"""

		if share_related_records is not None and not isinstance(share_related_records, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: share_related_records EXPECTED TYPE: bool', None, None)
		
		self.__share_related_records = share_related_records
		self.__key_modified['share_related_records'] = 1

	def get_shared_through(self):
		"""
		The method to get the shared_through

		Returns:
			SharedThrough: An instance of SharedThrough
		"""

		return self.__shared_through

	def set_shared_through(self, shared_through):
		"""
		The method to set the value to shared_through

		Parameters:
			shared_through (SharedThrough) : An instance of SharedThrough
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.share_records.shared_through import SharedThrough
		except Exception:
			from .shared_through import SharedThrough

		if shared_through is not None and not isinstance(shared_through, SharedThrough):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_through EXPECTED TYPE: SharedThrough', None, None)
		
		self.__shared_through = shared_through
		self.__key_modified['shared_through'] = 1

	def get_shared_time(self):
		"""
		The method to get the shared_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__shared_time

	def set_shared_time(self, shared_time):
		"""
		The method to set the value to shared_time

		Parameters:
			shared_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if shared_time is not None and not isinstance(shared_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_time EXPECTED TYPE: datetime', None, None)
		
		self.__shared_time = shared_time
		self.__key_modified['shared_time'] = 1

	def get_permission(self):
		"""
		The method to get the permission

		Returns:
			string: A string representing the permission
		"""

		return self.__permission

	def set_permission(self, permission):
		"""
		The method to set the value to permission

		Parameters:
			permission (string) : A string representing the permission
		"""

		if permission is not None and not isinstance(permission, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permission EXPECTED TYPE: str', None, None)
		
		self.__permission = permission
		self.__key_modified['permission'] = 1

	def get_shared_by(self):
		"""
		The method to get the shared_by

		Returns:
			Users: An instance of Users
		"""

		return self.__shared_by

	def set_shared_by(self, shared_by):
		"""
		The method to set the value to shared_by

		Parameters:
			shared_by (Users) : An instance of Users
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import Users
		except Exception:
			from ..users import Users

		if shared_by is not None and not isinstance(shared_by, Users):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_by EXPECTED TYPE: Users', None, None)
		
		self.__shared_by = shared_by
		self.__key_modified['shared_by'] = 1

	def get_user(self):
		"""
		The method to get the user

		Returns:
			Users: An instance of Users
		"""

		return self.__user

	def set_user(self, user):
		"""
		The method to set the value to user

		Parameters:
			user (Users) : An instance of Users
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import Users
		except Exception:
			from ..users import Users

		if user is not None and not isinstance(user, Users):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user EXPECTED TYPE: Users', None, None)
		
		self.__user = user
		self.__key_modified['user'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (Choice) : An instance of Choice
		"""

		if type is not None and not isinstance(type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: Choice', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

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
