try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class UnsubscribeLinks(object):
	def __init__(self):
		"""Creates an instance of UnsubscribeLinks"""

		self.__id = None
		self.__name = None
		self.__page_type = None
		self.__custom_location_url = None
		self.__standard_page_message = None
		self.__submission_action_type = None
		self.__submission_message = None
		self.__submission_redirect_url = None
		self.__location_url_type = None
		self.__action_on_unsubscribe = None
		self.__created_by = None
		self.__modified_by = None
		self.__modified_time = None
		self.__created_time = None
		self.__landing_url = None
		self.__key_modified = dict()

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

	def get_page_type(self):
		"""
		The method to get the page_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__page_type

	def set_page_type(self, page_type):
		"""
		The method to set the value to page_type

		Parameters:
			page_type (Choice) : An instance of Choice
		"""

		if page_type is not None and not isinstance(page_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: page_type EXPECTED TYPE: Choice', None, None)
		
		self.__page_type = page_type
		self.__key_modified['page_type'] = 1

	def get_custom_location_url(self):
		"""
		The method to get the custom_location_url

		Returns:
			string: A string representing the custom_location_url
		"""

		return self.__custom_location_url

	def set_custom_location_url(self, custom_location_url):
		"""
		The method to set the value to custom_location_url

		Parameters:
			custom_location_url (string) : A string representing the custom_location_url
		"""

		if custom_location_url is not None and not isinstance(custom_location_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: custom_location_url EXPECTED TYPE: str', None, None)
		
		self.__custom_location_url = custom_location_url
		self.__key_modified['custom_location_url'] = 1

	def get_standard_page_message(self):
		"""
		The method to get the standard_page_message

		Returns:
			string: A string representing the standard_page_message
		"""

		return self.__standard_page_message

	def set_standard_page_message(self, standard_page_message):
		"""
		The method to set the value to standard_page_message

		Parameters:
			standard_page_message (string) : A string representing the standard_page_message
		"""

		if standard_page_message is not None and not isinstance(standard_page_message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: standard_page_message EXPECTED TYPE: str', None, None)
		
		self.__standard_page_message = standard_page_message
		self.__key_modified['standard_page_message'] = 1

	def get_submission_action_type(self):
		"""
		The method to get the submission_action_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__submission_action_type

	def set_submission_action_type(self, submission_action_type):
		"""
		The method to set the value to submission_action_type

		Parameters:
			submission_action_type (Choice) : An instance of Choice
		"""

		if submission_action_type is not None and not isinstance(submission_action_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: submission_action_type EXPECTED TYPE: Choice', None, None)
		
		self.__submission_action_type = submission_action_type
		self.__key_modified['submission_action_type'] = 1

	def get_submission_message(self):
		"""
		The method to get the submission_message

		Returns:
			string: A string representing the submission_message
		"""

		return self.__submission_message

	def set_submission_message(self, submission_message):
		"""
		The method to set the value to submission_message

		Parameters:
			submission_message (string) : A string representing the submission_message
		"""

		if submission_message is not None and not isinstance(submission_message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: submission_message EXPECTED TYPE: str', None, None)
		
		self.__submission_message = submission_message
		self.__key_modified['submission_message'] = 1

	def get_submission_redirect_url(self):
		"""
		The method to get the submission_redirect_url

		Returns:
			string: A string representing the submission_redirect_url
		"""

		return self.__submission_redirect_url

	def set_submission_redirect_url(self, submission_redirect_url):
		"""
		The method to set the value to submission_redirect_url

		Parameters:
			submission_redirect_url (string) : A string representing the submission_redirect_url
		"""

		if submission_redirect_url is not None and not isinstance(submission_redirect_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: submission_redirect_url EXPECTED TYPE: str', None, None)
		
		self.__submission_redirect_url = submission_redirect_url
		self.__key_modified['submission_redirect_url'] = 1

	def get_location_url_type(self):
		"""
		The method to get the location_url_type

		Returns:
			string: A string representing the location_url_type
		"""

		return self.__location_url_type

	def set_location_url_type(self, location_url_type):
		"""
		The method to set the value to location_url_type

		Parameters:
			location_url_type (string) : A string representing the location_url_type
		"""

		if location_url_type is not None and not isinstance(location_url_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: location_url_type EXPECTED TYPE: str', None, None)
		
		self.__location_url_type = location_url_type
		self.__key_modified['location_url_type'] = 1

	def get_action_on_unsubscribe(self):
		"""
		The method to get the action_on_unsubscribe

		Returns:
			string: A string representing the action_on_unsubscribe
		"""

		return self.__action_on_unsubscribe

	def set_action_on_unsubscribe(self, action_on_unsubscribe):
		"""
		The method to set the value to action_on_unsubscribe

		Parameters:
			action_on_unsubscribe (string) : A string representing the action_on_unsubscribe
		"""

		if action_on_unsubscribe is not None and not isinstance(action_on_unsubscribe, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action_on_unsubscribe EXPECTED TYPE: str', None, None)
		
		self.__action_on_unsubscribe = action_on_unsubscribe
		self.__key_modified['action_on_unsubscribe'] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			User: An instance of User
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.unsubscribe_links.user import User
		except Exception:
			from .user import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			User: An instance of User
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.unsubscribe_links.user import User
		except Exception:
			from .user import User

		if modified_by is not None and not isinstance(modified_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: User', None, None)
		
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

	def get_landing_url(self):
		"""
		The method to get the landing_url

		Returns:
			string: A string representing the landing_url
		"""

		return self.__landing_url

	def set_landing_url(self, landing_url):
		"""
		The method to set the value to landing_url

		Parameters:
			landing_url (string) : A string representing the landing_url
		"""

		if landing_url is not None and not isinstance(landing_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: landing_url EXPECTED TYPE: str', None, None)
		
		self.__landing_url = landing_url
		self.__key_modified['landing_url'] = 1

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
