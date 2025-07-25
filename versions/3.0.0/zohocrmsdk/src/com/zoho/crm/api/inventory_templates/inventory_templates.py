try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.send_mail import Template
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from ..send_mail import Template


class InventoryTemplates(Template):
	def __init__(self):
		"""Creates an instance of InventoryTemplates"""
		super().__init__()

		self.__created_time = None
		self.__modified_time = None
		self.__last_usage_time = None
		self.__folder = None
		self.__module = None
		self.__created_by = None
		self.__modified_by = None
		self.__name = None
		self.__id = None
		self.__editor_mode = None
		self.__category = None
		self.__favorite = None
		self.__content = None
		self.__active = None
		self.__mail_content = None
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

	def get_last_usage_time(self):
		"""
		The method to get the last_usage_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__last_usage_time

	def set_last_usage_time(self, last_usage_time):
		"""
		The method to set the value to last_usage_time

		Parameters:
			last_usage_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if last_usage_time is not None and not isinstance(last_usage_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_usage_time EXPECTED TYPE: datetime', None, None)
		
		self.__last_usage_time = last_usage_time
		self.__key_modified['last_usage_time'] = 1

	def get_folder(self):
		"""
		The method to get the folder

		Returns:
			Folder: An instance of Folder
		"""

		return self.__folder

	def set_folder(self, folder):
		"""
		The method to set the value to folder

		Parameters:
			folder (Folder) : An instance of Folder
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.inventory_templates.folder import Folder
		except Exception:
			from .folder import Folder

		if folder is not None and not isinstance(folder, Folder):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: folder EXPECTED TYPE: Folder', None, None)
		
		self.__folder = folder
		self.__key_modified['folder'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			ModuleMap: An instance of ModuleMap
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (ModuleMap) : An instance of ModuleMap
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.inventory_templates.module_map import ModuleMap
		except Exception:
			from .module_map import ModuleMap

		if module is not None and not isinstance(module, ModuleMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: ModuleMap', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.inventory_templates.user import User
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
			from zohocrmsdk.src.com.zoho.crm.api.inventory_templates.user import User
		except Exception:
			from .user import User

		if modified_by is not None and not isinstance(modified_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: User', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

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

	def get_editor_mode(self):
		"""
		The method to get the editor_mode

		Returns:
			string: A string representing the editor_mode
		"""

		return self.__editor_mode

	def set_editor_mode(self, editor_mode):
		"""
		The method to set the value to editor_mode

		Parameters:
			editor_mode (string) : A string representing the editor_mode
		"""

		if editor_mode is not None and not isinstance(editor_mode, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editor_mode EXPECTED TYPE: str', None, None)
		
		self.__editor_mode = editor_mode
		self.__key_modified['editor_mode'] = 1

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

	def get_favorite(self):
		"""
		The method to get the favorite

		Returns:
			bool: A bool representing the favorite
		"""

		return self.__favorite

	def set_favorite(self, favorite):
		"""
		The method to set the value to favorite

		Parameters:
			favorite (bool) : A bool representing the favorite
		"""

		if favorite is not None and not isinstance(favorite, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: favorite EXPECTED TYPE: bool', None, None)
		
		self.__favorite = favorite
		self.__key_modified['favorite'] = 1

	def get_content(self):
		"""
		The method to get the content

		Returns:
			string: A string representing the content
		"""

		return self.__content

	def set_content(self, content):
		"""
		The method to set the value to content

		Parameters:
			content (string) : A string representing the content
		"""

		if content is not None and not isinstance(content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: content EXPECTED TYPE: str', None, None)
		
		self.__content = content
		self.__key_modified['content'] = 1

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

	def get_mail_content(self):
		"""
		The method to get the mail_content

		Returns:
			string: A string representing the mail_content
		"""

		return self.__mail_content

	def set_mail_content(self, mail_content):
		"""
		The method to set the value to mail_content

		Parameters:
			mail_content (string) : A string representing the mail_content
		"""

		if mail_content is not None and not isinstance(mail_content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mail_content EXPECTED TYPE: str', None, None)
		
		self.__mail_content = mail_content
		self.__key_modified['mail_content'] = 1

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
