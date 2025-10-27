try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
	from zohocrmsdk.src.com.zoho.crm.api.notifications.event import Event
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants
	from .event import Event


class Notification(Event):
	def __init__(self):
		"""Creates an instance of Notification"""
		super().__init__()

		self.__channel_id = None
		self.__notify_url = None
		self.__events = None
		self.__token = None
		self.__fields = None
		self.__notify_on_related_action = None
		self.__return_affected_field_values = None
		self.__delete_events = None
		self.__resource_name = None
		self.__channel_expiry = None
		self.__resource_id = None
		self.__resource_uri = None
		self.__notification_condition = None
		self.__key_modified = dict()

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

	def get_notify_url(self):
		"""
		The method to get the notify_url

		Returns:
			string: A string representing the notify_url
		"""

		return self.__notify_url

	def set_notify_url(self, notify_url):
		"""
		The method to set the value to notify_url

		Parameters:
			notify_url (string) : A string representing the notify_url
		"""

		if notify_url is not None and not isinstance(notify_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notify_url EXPECTED TYPE: str', None, None)
		
		self.__notify_url = notify_url
		self.__key_modified['notify_url'] = 1

	def get_events(self):
		"""
		The method to get the events

		Returns:
			list: An instance of list
		"""

		return self.__events

	def set_events(self, events):
		"""
		The method to set the value to events

		Parameters:
			events (list) : An instance of list
		"""

		if events is not None and not isinstance(events, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: events EXPECTED TYPE: list', None, None)
		
		self.__events = events
		self.__key_modified['events'] = 1

	def get_token(self):
		"""
		The method to get the token

		Returns:
			string: A string representing the token
		"""

		return self.__token

	def set_token(self, token):
		"""
		The method to set the value to token

		Parameters:
			token (string) : A string representing the token
		"""

		if token is not None and not isinstance(token, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: token EXPECTED TYPE: str', None, None)
		
		self.__token = token
		self.__key_modified['token'] = 1

	def get_fields(self):
		"""
		The method to get the fields

		Returns:
			dict: An instance of dict
		"""

		return self.__fields

	def set_fields(self, fields):
		"""
		The method to set the value to fields

		Parameters:
			fields (dict) : An instance of dict
		"""

		if fields is not None and not isinstance(fields, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: dict', None, None)
		
		self.__fields = fields
		self.__key_modified['fields'] = 1

	def get_notify_on_related_action(self):
		"""
		The method to get the notify_on_related_action

		Returns:
			bool: A bool representing the notify_on_related_action
		"""

		return self.__notify_on_related_action

	def set_notify_on_related_action(self, notify_on_related_action):
		"""
		The method to set the value to notify_on_related_action

		Parameters:
			notify_on_related_action (bool) : A bool representing the notify_on_related_action
		"""

		if notify_on_related_action is not None and not isinstance(notify_on_related_action, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notify_on_related_action EXPECTED TYPE: bool', None, None)
		
		self.__notify_on_related_action = notify_on_related_action
		self.__key_modified['notify_on_related_action'] = 1

	def get_return_affected_field_values(self):
		"""
		The method to get the return_affected_field_values

		Returns:
			bool: A bool representing the return_affected_field_values
		"""

		return self.__return_affected_field_values

	def set_return_affected_field_values(self, return_affected_field_values):
		"""
		The method to set the value to return_affected_field_values

		Parameters:
			return_affected_field_values (bool) : A bool representing the return_affected_field_values
		"""

		if return_affected_field_values is not None and not isinstance(return_affected_field_values, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: return_affected_field_values EXPECTED TYPE: bool', None, None)
		
		self.__return_affected_field_values = return_affected_field_values
		self.__key_modified['return_affected_field_values'] = 1

	def get_delete_events(self):
		"""
		The method to get the delete_events

		Returns:
			Choice: An instance of Choice
		"""

		return self.__delete_events

	def set_delete_events(self, delete_events):
		"""
		The method to set the value to delete_events

		Parameters:
			delete_events (Choice) : An instance of Choice
		"""

		if delete_events is not None and not isinstance(delete_events, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delete_events EXPECTED TYPE: Choice', None, None)
		
		self.__delete_events = delete_events
		self.__key_modified['_delete_events'] = 1

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
