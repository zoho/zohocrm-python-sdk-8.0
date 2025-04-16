try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class UsersUnavailability(object):
	def __init__(self):
		"""Creates an instance of UsersUnavailability"""

		self.__service = None
		self.__title = None
		self.__all_day = None
		self.__tp_calendar_id = None
		self.__tp_event_id = None
		self.__comments = None
		self.__from_1 = None
		self.__id = None
		self.__to = None
		self.__user = None
		self.__key_modified = dict()

	def get_service(self):
		"""
		The method to get the service

		Returns:
			string: A string representing the service
		"""

		return self.__service

	def set_service(self, service):
		"""
		The method to set the value to service

		Parameters:
			service (string) : A string representing the service
		"""

		if service is not None and not isinstance(service, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: service EXPECTED TYPE: str', None, None)
		
		self.__service = service
		self.__key_modified['service'] = 1

	def get_title(self):
		"""
		The method to get the title

		Returns:
			string: A string representing the title
		"""

		return self.__title

	def set_title(self, title):
		"""
		The method to set the value to title

		Parameters:
			title (string) : A string representing the title
		"""

		if title is not None and not isinstance(title, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: title EXPECTED TYPE: str', None, None)
		
		self.__title = title
		self.__key_modified['title'] = 1

	def get_all_day(self):
		"""
		The method to get the all_day

		Returns:
			bool: A bool representing the all_day
		"""

		return self.__all_day

	def set_all_day(self, all_day):
		"""
		The method to set the value to all_day

		Parameters:
			all_day (bool) : A bool representing the all_day
		"""

		if all_day is not None and not isinstance(all_day, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: all_day EXPECTED TYPE: bool', None, None)
		
		self.__all_day = all_day
		self.__key_modified['all_day'] = 1

	def get_tp_calendar_id(self):
		"""
		The method to get the tp_calendar_id

		Returns:
			string: A string representing the tp_calendar_id
		"""

		return self.__tp_calendar_id

	def set_tp_calendar_id(self, tp_calendar_id):
		"""
		The method to set the value to tp_calendar_id

		Parameters:
			tp_calendar_id (string) : A string representing the tp_calendar_id
		"""

		if tp_calendar_id is not None and not isinstance(tp_calendar_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tp_calendar_id EXPECTED TYPE: str', None, None)
		
		self.__tp_calendar_id = tp_calendar_id
		self.__key_modified['tp_calendar_id'] = 1

	def get_tp_event_id(self):
		"""
		The method to get the tp_event_id

		Returns:
			string: A string representing the tp_event_id
		"""

		return self.__tp_event_id

	def set_tp_event_id(self, tp_event_id):
		"""
		The method to set the value to tp_event_id

		Parameters:
			tp_event_id (string) : A string representing the tp_event_id
		"""

		if tp_event_id is not None and not isinstance(tp_event_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tp_event_id EXPECTED TYPE: str', None, None)
		
		self.__tp_event_id = tp_event_id
		self.__key_modified['tp_event_id'] = 1

	def get_comments(self):
		"""
		The method to get the comments

		Returns:
			string: A string representing the comments
		"""

		return self.__comments

	def set_comments(self, comments):
		"""
		The method to set the value to comments

		Parameters:
			comments (string) : A string representing the comments
		"""

		if comments is not None and not isinstance(comments, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: comments EXPECTED TYPE: str', None, None)
		
		self.__comments = comments
		self.__key_modified['comments'] = 1

	def get_from(self):
		"""
		The method to get the from

		Returns:
			datetime: An instance of datetime
		"""

		return self.__from_1

	def set_from(self, from_1):
		"""
		The method to set the value to from

		Parameters:
			from_1 (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if from_1 is not None and not isinstance(from_1, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_1 EXPECTED TYPE: datetime', None, None)
		
		self.__from_1 = from_1
		self.__key_modified['from'] = 1

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

	def get_to(self):
		"""
		The method to get the to

		Returns:
			datetime: An instance of datetime
		"""

		return self.__to

	def set_to(self, to):
		"""
		The method to set the value to to

		Parameters:
			to (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if to is not None and not isinstance(to, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: to EXPECTED TYPE: datetime', None, None)
		
		self.__to = to
		self.__key_modified['to'] = 1

	def get_user(self):
		"""
		The method to get the user

		Returns:
			User: An instance of User
		"""

		return self.__user

	def set_user(self, user):
		"""
		The method to set the value to user

		Parameters:
			user (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users_unavailability.user import User
		except Exception:
			from .user import User

		if user is not None and not isinstance(user, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user EXPECTED TYPE: User', None, None)
		
		self.__user = user
		self.__key_modified['user'] = 1

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
