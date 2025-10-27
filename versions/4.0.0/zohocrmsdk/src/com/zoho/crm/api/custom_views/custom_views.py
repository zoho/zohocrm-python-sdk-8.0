try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class CustomViews(object):
	def __init__(self):
		"""Creates an instance of CustomViews"""

		self.__display_value = None
		self.__system_name = None
		self.__category = None
		self.__created_time = None
		self.__modified_time = None
		self.__last_accessed_time = None
		self.__name = None
		self.__created_by = None
		self.__modified_by = None
		self.__module = None
		self.__criteria = None
		self.__default = None
		self.__system_defined = None
		self.__locked = None
		self.__favorite = None
		self.__offline = None
		self.__access_type = None
		self.__shared_to = None
		self.__fields = None
		self.__sort_by = None
		self.__sort_order = None
		self.__id = None
		self.__key_modified = dict()

	def get_display_value(self):
		"""
		The method to get the display_value

		Returns:
			string: A string representing the display_value
		"""

		return self.__display_value

	def set_display_value(self, display_value):
		"""
		The method to set the value to display_value

		Parameters:
			display_value (string) : A string representing the display_value
		"""

		if display_value is not None and not isinstance(display_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_value EXPECTED TYPE: str', None, None)
		
		self.__display_value = display_value
		self.__key_modified['display_value'] = 1

	def get_system_name(self):
		"""
		The method to get the system_name

		Returns:
			string: A string representing the system_name
		"""

		return self.__system_name

	def set_system_name(self, system_name):
		"""
		The method to set the value to system_name

		Parameters:
			system_name (string) : A string representing the system_name
		"""

		if system_name is not None and not isinstance(system_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: system_name EXPECTED TYPE: str', None, None)
		
		self.__system_name = system_name
		self.__key_modified['system_name'] = 1

	def get_category(self):
		"""
		The method to get the category

		Returns:
			string: A string representing the category
		"""

		return self.__category

	def set_category(self, category):
		"""
		The method to set the value to category

		Parameters:
			category (string) : A string representing the category
		"""

		if category is not None and not isinstance(category, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: str', None, None)
		
		self.__category = category
		self.__key_modified['category'] = 1

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

	def get_last_accessed_time(self):
		"""
		The method to get the last_accessed_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__last_accessed_time

	def set_last_accessed_time(self, last_accessed_time):
		"""
		The method to set the value to last_accessed_time

		Parameters:
			last_accessed_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if last_accessed_time is not None and not isinstance(last_accessed_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_accessed_time EXPECTED TYPE: datetime', None, None)
		
		self.__last_accessed_time = last_accessed_time
		self.__key_modified['last_accessed_time'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.custom_views.owner import Owner
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
			from zohocrmsdk.src.com.zoho.crm.api.custom_views.owner import Owner
		except Exception:
			from .owner import Owner

		if modified_by is not None and not isinstance(modified_by, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: Owner', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Owner: An instance of Owner
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.custom_views.owner import Owner
		except Exception:
			from .owner import Owner

		if module is not None and not isinstance(module, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Owner', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.custom_views.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

	def get_default(self):
		"""
		The method to get the default

		Returns:
			bool: A bool representing the default
		"""

		return self.__default

	def set_default(self, default):
		"""
		The method to set the value to default

		Parameters:
			default (bool) : A bool representing the default
		"""

		if default is not None and not isinstance(default, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default EXPECTED TYPE: bool', None, None)
		
		self.__default = default
		self.__key_modified['default'] = 1

	def get_system_defined(self):
		"""
		The method to get the system_defined

		Returns:
			bool: A bool representing the system_defined
		"""

		return self.__system_defined

	def set_system_defined(self, system_defined):
		"""
		The method to set the value to system_defined

		Parameters:
			system_defined (bool) : A bool representing the system_defined
		"""

		if system_defined is not None and not isinstance(system_defined, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: system_defined EXPECTED TYPE: bool', None, None)
		
		self.__system_defined = system_defined
		self.__key_modified['system_defined'] = 1

	def get_locked(self):
		"""
		The method to get the locked

		Returns:
			bool: A bool representing the locked
		"""

		return self.__locked

	def set_locked(self, locked):
		"""
		The method to set the value to locked

		Parameters:
			locked (bool) : A bool representing the locked
		"""

		if locked is not None and not isinstance(locked, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locked EXPECTED TYPE: bool', None, None)
		
		self.__locked = locked
		self.__key_modified['locked'] = 1

	def get_favorite(self):
		"""
		The method to get the favorite

		Returns:
			int: An int representing the favorite
		"""

		return self.__favorite

	def set_favorite(self, favorite):
		"""
		The method to set the value to favorite

		Parameters:
			favorite (int) : An int representing the favorite
		"""

		if favorite is not None and not isinstance(favorite, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: favorite EXPECTED TYPE: int', None, None)
		
		self.__favorite = favorite
		self.__key_modified['favorite'] = 1

	def get_offline(self):
		"""
		The method to get the offline

		Returns:
			bool: A bool representing the offline
		"""

		return self.__offline

	def set_offline(self, offline):
		"""
		The method to set the value to offline

		Parameters:
			offline (bool) : A bool representing the offline
		"""

		if offline is not None and not isinstance(offline, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: offline EXPECTED TYPE: bool', None, None)
		
		self.__offline = offline
		self.__key_modified['offline'] = 1

	def get_access_type(self):
		"""
		The method to get the access_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__access_type

	def set_access_type(self, access_type):
		"""
		The method to set the value to access_type

		Parameters:
			access_type (Choice) : An instance of Choice
		"""

		if access_type is not None and not isinstance(access_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: access_type EXPECTED TYPE: Choice', None, None)
		
		self.__access_type = access_type
		self.__key_modified['access_type'] = 1

	def get_shared_to(self):
		"""
		The method to get the shared_to

		Returns:
			list: An instance of list
		"""

		return self.__shared_to

	def set_shared_to(self, shared_to):
		"""
		The method to set the value to shared_to

		Parameters:
			shared_to (list) : An instance of list
		"""

		if shared_to is not None and not isinstance(shared_to, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shared_to EXPECTED TYPE: list', None, None)
		
		self.__shared_to = shared_to
		self.__key_modified['shared_to'] = 1

	def get_fields(self):
		"""
		The method to get the fields

		Returns:
			list: An instance of list
		"""

		return self.__fields

	def set_fields(self, fields):
		"""
		The method to set the value to fields

		Parameters:
			fields (list) : An instance of list
		"""

		if fields is not None and not isinstance(fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: list', None, None)
		
		self.__fields = fields
		self.__key_modified['fields'] = 1

	def get_sort_by(self):
		"""
		The method to get the sort_by

		Returns:
			SortBy: An instance of SortBy
		"""

		return self.__sort_by

	def set_sort_by(self, sort_by):
		"""
		The method to set the value to sort_by

		Parameters:
			sort_by (SortBy) : An instance of SortBy
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.custom_views.sort_by import SortBy
		except Exception:
			from .sort_by import SortBy

		if sort_by is not None and not isinstance(sort_by, SortBy):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_by EXPECTED TYPE: SortBy', None, None)
		
		self.__sort_by = sort_by
		self.__key_modified['sort_by'] = 1

	def get_sort_order(self):
		"""
		The method to get the sort_order

		Returns:
			Choice: An instance of Choice
		"""

		return self.__sort_order

	def set_sort_order(self, sort_order):
		"""
		The method to set the value to sort_order

		Parameters:
			sort_order (Choice) : An instance of Choice
		"""

		if sort_order is not None and not isinstance(sort_order, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sort_order EXPECTED TYPE: Choice', None, None)
		
		self.__sort_order = sort_order
		self.__key_modified['sort_order'] = 1

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
