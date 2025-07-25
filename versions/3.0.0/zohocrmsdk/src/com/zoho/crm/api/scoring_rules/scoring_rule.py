try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ScoringRule(object):
	def __init__(self):
		"""Creates an instance of ScoringRule"""

		self.__name = None
		self.__description = None
		self.__id = None
		self.__layout = None
		self.__created_time = None
		self.__modified_time = None
		self.__module = None
		self.__modified_by = None
		self.__active = None
		self.__created_by = None
		self.__field_rules = None
		self.__signal_rules = None
		self.__key_modified = dict()

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

	def get_layout(self):
		"""
		The method to get the layout

		Returns:
			Layout: An instance of Layout
		"""

		return self.__layout

	def set_layout(self, layout):
		"""
		The method to set the value to layout

		Parameters:
			layout (Layout) : An instance of Layout
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.scoring_rules.layout import Layout
		except Exception:
			from .layout import Layout

		if layout is not None and not isinstance(layout, Layout):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout EXPECTED TYPE: Layout', None, None)
		
		self.__layout = layout
		self.__key_modified['layout'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			string: A string representing the created_time
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (string) : A string representing the created_time
		"""

		if created_time is not None and not isinstance(created_time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: str', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			string: A string representing the modified_time
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (string) : A string representing the modified_time
		"""

		if modified_time is not None and not isinstance(modified_time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: str', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Modules: An instance of Modules
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Modules) : An instance of Modules
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import Modules
		except Exception:
			from ..modules import Modules

		if module is not None and not isinstance(module, Modules):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Modules', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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

	def get_field_rules(self):
		"""
		The method to get the field_rules

		Returns:
			list: An instance of list
		"""

		return self.__field_rules

	def set_field_rules(self, field_rules):
		"""
		The method to set the value to field_rules

		Parameters:
			field_rules (list) : An instance of list
		"""

		if field_rules is not None and not isinstance(field_rules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_rules EXPECTED TYPE: list', None, None)
		
		self.__field_rules = field_rules
		self.__key_modified['field_rules'] = 1

	def get_signal_rules(self):
		"""
		The method to get the signal_rules

		Returns:
			list: An instance of list
		"""

		return self.__signal_rules

	def set_signal_rules(self, signal_rules):
		"""
		The method to set the value to signal_rules

		Parameters:
			signal_rules (list) : An instance of list
		"""

		if signal_rules is not None and not isinstance(signal_rules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: signal_rules EXPECTED TYPE: list', None, None)
		
		self.__signal_rules = signal_rules
		self.__key_modified['signal_rules'] = 1

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
