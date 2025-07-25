try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class PermissionDetail(object):
	def __init__(self):
		"""Creates an instance of PermissionDetail"""

		self.__id = None
		self.__enabled = None
		self.__name = None
		self.__display_label = None
		self.__customizable = None
		self.__parent_permissions = None
		self.__module = None
		self.__key_modified = dict()

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string representing the id
		"""

		if id is not None and not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_enabled(self):
		"""
		The method to get the enabled

		Returns:
			bool: A bool representing the enabled
		"""

		return self.__enabled

	def set_enabled(self, enabled):
		"""
		The method to set the value to enabled

		Parameters:
			enabled (bool) : A bool representing the enabled
		"""

		if enabled is not None and not isinstance(enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enabled EXPECTED TYPE: bool', None, None)
		
		self.__enabled = enabled
		self.__key_modified['enabled'] = 1

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

	def get_customizable(self):
		"""
		The method to get the customizable

		Returns:
			bool: A bool representing the customizable
		"""

		return self.__customizable

	def set_customizable(self, customizable):
		"""
		The method to set the value to customizable

		Parameters:
			customizable (bool) : A bool representing the customizable
		"""

		if customizable is not None and not isinstance(customizable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: customizable EXPECTED TYPE: bool', None, None)
		
		self.__customizable = customizable
		self.__key_modified['customizable'] = 1

	def get_parent_permissions(self):
		"""
		The method to get the parent_permissions

		Returns:
			list: An instance of list
		"""

		return self.__parent_permissions

	def set_parent_permissions(self, parent_permissions):
		"""
		The method to set the value to parent_permissions

		Parameters:
			parent_permissions (list) : An instance of list
		"""

		if parent_permissions is not None and not isinstance(parent_permissions, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_permissions EXPECTED TYPE: list', None, None)
		
		self.__parent_permissions = parent_permissions
		self.__key_modified['parent_permissions'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			string: A string representing the module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (string) : A string representing the module
		"""

		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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
