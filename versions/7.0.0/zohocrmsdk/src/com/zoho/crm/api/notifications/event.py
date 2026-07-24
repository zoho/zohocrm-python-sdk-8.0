try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Event(object):
	def __init__(self):
		"""Creates an instance of Event"""

		self.__resource_name = None
		self.__channel_expiry = None
		self.__resource_id = None
		self.__resource_uri = None
		self.__channel_id = None
		self.__notification_condition = None
		self.__key_modified = dict()

	def get_resource_name(self):
		"""
		The method to get the resource_name

		Returns:
			string: A string representing the resource_name
		"""

		return self.__resource_name

	def set_resource_name(self, resource_name):
		"""
		The method to set the value to resource_name

		Parameters:
			resource_name (string) : A string representing the resource_name
		"""

		if resource_name is not None and not isinstance(resource_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: resource_name EXPECTED TYPE: str', None, None)
		
		self.__resource_name = resource_name
		self.__key_modified['resource_name'] = 1

	def get_channel_expiry(self):
		"""
		The method to get the channel_expiry

		Returns:
			datetime: An instance of datetime
		"""

		return self.__channel_expiry

	def set_channel_expiry(self, channel_expiry):
		"""
		The method to set the value to channel_expiry

		Parameters:
			channel_expiry (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if channel_expiry is not None and not isinstance(channel_expiry, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: channel_expiry EXPECTED TYPE: datetime', None, None)
		
		self.__channel_expiry = channel_expiry
		self.__key_modified['channel_expiry'] = 1

	def get_resource_id(self):
		"""
		The method to get the resource_id

		Returns:
			int: An int representing the resource_id
		"""

		return self.__resource_id

	def set_resource_id(self, resource_id):
		"""
		The method to set the value to resource_id

		Parameters:
			resource_id (int) : An int representing the resource_id
		"""

		if resource_id is not None and not isinstance(resource_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: resource_id EXPECTED TYPE: int', None, None)
		
		self.__resource_id = resource_id
		self.__key_modified['resource_id'] = 1

	def get_resource_uri(self):
		"""
		The method to get the resource_uri

		Returns:
			string: A string representing the resource_uri
		"""

		return self.__resource_uri

	def set_resource_uri(self, resource_uri):
		"""
		The method to set the value to resource_uri

		Parameters:
			resource_uri (string) : A string representing the resource_uri
		"""

		if resource_uri is not None and not isinstance(resource_uri, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: resource_uri EXPECTED TYPE: str', None, None)
		
		self.__resource_uri = resource_uri
		self.__key_modified['resource_uri'] = 1

	def get_channel_id(self):
		"""
		The method to get the channel_id

		Returns:
			string: A string representing the channel_id
		"""

		return self.__channel_id

	def set_channel_id(self, channel_id):
		"""
		The method to set the value to channel_id

		Parameters:
			channel_id (string) : A string representing the channel_id
		"""

		if channel_id is not None and not isinstance(channel_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: channel_id EXPECTED TYPE: str', None, None)
		
		self.__channel_id = channel_id
		self.__key_modified['channel_id'] = 1

	def get_notification_condition(self):
		"""
		The method to get the notification_condition

		Returns:
			list: An instance of list
		"""

		return self.__notification_condition

	def set_notification_condition(self, notification_condition):
		"""
		The method to set the value to notification_condition

		Parameters:
			notification_condition (list) : An instance of list
		"""

		if notification_condition is not None and not isinstance(notification_condition, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notification_condition EXPECTED TYPE: list', None, None)
		
		self.__notification_condition = notification_condition
		self.__key_modified['notification_condition'] = 1

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
