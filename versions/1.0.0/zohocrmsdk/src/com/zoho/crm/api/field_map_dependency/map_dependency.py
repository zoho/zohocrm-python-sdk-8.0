try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class MapDependency(object):
	def __init__(self):
		"""Creates an instance of MapDependency"""

		self.__parent = None
		self.__child = None
		self.__pick_list_values = None
		self.__internal = None
		self.__active = None
		self.__id = None
		self.__source = None
		self.__category = None
		self.__sub_module = None
		self.__key_modified = dict()

	def get_parent(self):
		"""
		The method to get the parent

		Returns:
			Parent: An instance of Parent
		"""

		return self.__parent

	def set_parent(self, parent):
		"""
		The method to set the value to parent

		Parameters:
			parent (Parent) : An instance of Parent
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.parent import Parent
		except Exception:
			from .parent import Parent

		if parent is not None and not isinstance(parent, Parent):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent EXPECTED TYPE: Parent', None, None)
		
		self.__parent = parent
		self.__key_modified['parent'] = 1

	def get_child(self):
		"""
		The method to get the child

		Returns:
			Child: An instance of Child
		"""

		return self.__child

	def set_child(self, child):
		"""
		The method to set the value to child

		Parameters:
			child (Child) : An instance of Child
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.child import Child
		except Exception:
			from .child import Child

		if child is not None and not isinstance(child, Child):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: child EXPECTED TYPE: Child', None, None)
		
		self.__child = child
		self.__key_modified['child'] = 1

	def get_pick_list_values(self):
		"""
		The method to get the pick_list_values

		Returns:
			list: An instance of list
		"""

		return self.__pick_list_values

	def set_pick_list_values(self, pick_list_values):
		"""
		The method to set the value to pick_list_values

		Parameters:
			pick_list_values (list) : An instance of list
		"""

		if pick_list_values is not None and not isinstance(pick_list_values, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pick_list_values EXPECTED TYPE: list', None, None)
		
		self.__pick_list_values = pick_list_values
		self.__key_modified['pick_list_values'] = 1

	def get_internal(self):
		"""
		The method to get the internal

		Returns:
			bool: A bool representing the internal
		"""

		return self.__internal

	def set_internal(self, internal):
		"""
		The method to set the value to internal

		Parameters:
			internal (bool) : A bool representing the internal
		"""

		if internal is not None and not isinstance(internal, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: internal EXPECTED TYPE: bool', None, None)
		
		self.__internal = internal
		self.__key_modified['internal'] = 1

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

	def get_source(self):
		"""
		The method to get the source

		Returns:
			int: An int representing the source
		"""

		return self.__source

	def set_source(self, source):
		"""
		The method to set the value to source

		Parameters:
			source (int) : An int representing the source
		"""

		if source is not None and not isinstance(source, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: source EXPECTED TYPE: int', None, None)
		
		self.__source = source
		self.__key_modified['source'] = 1

	def get_category(self):
		"""
		The method to get the category

		Returns:
			int: An int representing the category
		"""

		return self.__category

	def set_category(self, category):
		"""
		The method to set the value to category

		Parameters:
			category (int) : An int representing the category
		"""

		if category is not None and not isinstance(category, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: int', None, None)
		
		self.__category = category
		self.__key_modified['category'] = 1

	def get_sub_module(self):
		"""
		The method to get the sub_module

		Returns:
			SubModule: An instance of SubModule
		"""

		return self.__sub_module

	def set_sub_module(self, sub_module):
		"""
		The method to set the value to sub_module

		Parameters:
			sub_module (SubModule) : An instance of SubModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.sub_module import SubModule
		except Exception:
			from .sub_module import SubModule

		if sub_module is not None and not isinstance(sub_module, SubModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sub_module EXPECTED TYPE: SubModule', None, None)
		
		self.__sub_module = sub_module
		self.__key_modified['sub_module'] = 1

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
