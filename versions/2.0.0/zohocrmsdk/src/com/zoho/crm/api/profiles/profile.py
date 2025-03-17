try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Profile(object):
	def __init__(self):
		"""Creates an instance of Profile"""

		self.__default_view = None
		self.__name = None
		self.__description = None
		self.__id = None
		self.__default = None
		self.__delete = None
		self.__permission_type = None
		self.__custom = None
		self.__display_label = None
		self.__type = None
		self.__permissions_details = None
		self.__sections = None
		self.__created_time = None
		self.__modified_time = None
		self.__modified_by = None
		self.__category = None
		self.__created_by = None
		self.__key_modified = dict()

	def get_default_view(self):
		"""
		The method to get the default_view

		Returns:
			DefaultView: An instance of DefaultView
		"""

		return self.__default_view

	def set_default_view(self, default_view):
		"""
		The method to set the value to default_view

		Parameters:
			default_view (DefaultView) : An instance of DefaultView
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.profiles.default_view import DefaultView
		except Exception:
			from .default_view import DefaultView

		if default_view is not None and not isinstance(default_view, DefaultView):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_view EXPECTED TYPE: DefaultView', None, None)
		
		self.__default_view = default_view
		self.__key_modified['_default_view'] = 1

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

	def get_delete(self):
		"""
		The method to get the delete

		Returns:
			bool: A bool representing the delete
		"""

		return self.__delete

	def set_delete(self, delete):
		"""
		The method to set the value to delete

		Parameters:
			delete (bool) : A bool representing the delete
		"""

		if delete is not None and not isinstance(delete, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delete EXPECTED TYPE: bool', None, None)
		
		self.__delete = delete
		self.__key_modified['_delete'] = 1

	def get_permission_type(self):
		"""
		The method to get the permission_type

		Returns:
			string: A string representing the permission_type
		"""

		return self.__permission_type

	def set_permission_type(self, permission_type):
		"""
		The method to set the value to permission_type

		Parameters:
			permission_type (string) : A string representing the permission_type
		"""

		if permission_type is not None and not isinstance(permission_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permission_type EXPECTED TYPE: str', None, None)
		
		self.__permission_type = permission_type
		self.__key_modified['permission_type'] = 1

	def get_custom(self):
		"""
		The method to get the custom

		Returns:
			bool: A bool representing the custom
		"""

		return self.__custom

	def set_custom(self, custom):
		"""
		The method to set the value to custom

		Parameters:
			custom (bool) : A bool representing the custom
		"""

		if custom is not None and not isinstance(custom, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: custom EXPECTED TYPE: bool', None, None)
		
		self.__custom = custom
		self.__key_modified['custom'] = 1

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

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

	def get_permissions_details(self):
		"""
		The method to get the permissions_details

		Returns:
			list: An instance of list
		"""

		return self.__permissions_details

	def set_permissions_details(self, permissions_details):
		"""
		The method to set the value to permissions_details

		Parameters:
			permissions_details (list) : An instance of list
		"""

		if permissions_details is not None and not isinstance(permissions_details, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permissions_details EXPECTED TYPE: list', None, None)
		
		self.__permissions_details = permissions_details
		self.__key_modified['permissions_details'] = 1

	def get_sections(self):
		"""
		The method to get the sections

		Returns:
			list: An instance of list
		"""

		return self.__sections

	def set_sections(self, sections):
		"""
		The method to set the value to sections

		Parameters:
			sections (list) : An instance of list
		"""

		if sections is not None and not isinstance(sections, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sections EXPECTED TYPE: list', None, None)
		
		self.__sections = sections
		self.__key_modified['sections'] = 1

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
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if modified_by is not None and not isinstance(modified_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

	def get_category(self):
		"""
		The method to get the category

		Returns:
			bool: A bool representing the category
		"""

		return self.__category

	def set_category(self, category):
		"""
		The method to set the value to category

		Parameters:
			category (bool) : A bool representing the category
		"""

		if category is not None and not isinstance(category, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: bool', None, None)
		
		self.__category = category
		self.__key_modified['category'] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if created_by is not None and not isinstance(created_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

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
