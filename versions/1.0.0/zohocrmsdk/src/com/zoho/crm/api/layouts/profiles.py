try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Profiles(object):
	def __init__(self):
		"""Creates an instance of Profiles"""

		self.__default = None
		self.__name = None
		self.__id = None
		self.__default_view = None
		self.__default_assignment_view = None
		self.__key_modified = dict()

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
			from zohocrmsdk.src.com.zoho.crm.api.layouts.default_view import DefaultView
		except Exception:
			from .default_view import DefaultView

		if default_view is not None and not isinstance(default_view, DefaultView):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_view EXPECTED TYPE: DefaultView', None, None)
		
		self.__default_view = default_view
		self.__key_modified['_default_view'] = 1

	def get_default_assignment_view(self):
		"""
		The method to get the default_assignment_view

		Returns:
			DefaultAssignmentView: An instance of DefaultAssignmentView
		"""

		return self.__default_assignment_view

	def set_default_assignment_view(self, default_assignment_view):
		"""
		The method to set the value to default_assignment_view

		Parameters:
			default_assignment_view (DefaultAssignmentView) : An instance of DefaultAssignmentView
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.default_assignment_view import DefaultAssignmentView
		except Exception:
			from .default_assignment_view import DefaultAssignmentView

		if default_assignment_view is not None and not isinstance(default_assignment_view, DefaultAssignmentView):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_assignment_view EXPECTED TYPE: DefaultAssignmentView', None, None)
		
		self.__default_assignment_view = default_assignment_view
		self.__key_modified['_default_assignment_view'] = 1

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
