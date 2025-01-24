try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ActionsAllowed(object):
	def __init__(self):
		"""Creates an instance of ActionsAllowed"""

		self.__edit = None
		self.__rename = None
		self.__clone = None
		self.__downgrade = None
		self.__delete = None
		self.__deactivate = None
		self.__set_layout_permissions = None
		self.__add_field = None
		self.__change_tab_traversal = None
		self.__reorder = None
		self.__remove_field = None
		self.__change_column_count = None
		self.__key_modified = dict()

	def get_edit(self):
		"""
		The method to get the edit

		Returns:
			bool: A bool representing the edit
		"""

		return self.__edit

	def set_edit(self, edit):
		"""
		The method to set the value to edit

		Parameters:
			edit (bool) : A bool representing the edit
		"""

		if edit is not None and not isinstance(edit, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: edit EXPECTED TYPE: bool', None, None)
		
		self.__edit = edit
		self.__key_modified['edit'] = 1

	def get_rename(self):
		"""
		The method to get the rename

		Returns:
			bool: A bool representing the rename
		"""

		return self.__rename

	def set_rename(self, rename):
		"""
		The method to set the value to rename

		Parameters:
			rename (bool) : A bool representing the rename
		"""

		if rename is not None and not isinstance(rename, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rename EXPECTED TYPE: bool', None, None)
		
		self.__rename = rename
		self.__key_modified['rename'] = 1

	def get_clone(self):
		"""
		The method to get the clone

		Returns:
			bool: A bool representing the clone
		"""

		return self.__clone

	def set_clone(self, clone):
		"""
		The method to set the value to clone

		Parameters:
			clone (bool) : A bool representing the clone
		"""

		if clone is not None and not isinstance(clone, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: clone EXPECTED TYPE: bool', None, None)
		
		self.__clone = clone
		self.__key_modified['clone'] = 1

	def get_downgrade(self):
		"""
		The method to get the downgrade

		Returns:
			bool: A bool representing the downgrade
		"""

		return self.__downgrade

	def set_downgrade(self, downgrade):
		"""
		The method to set the value to downgrade

		Parameters:
			downgrade (bool) : A bool representing the downgrade
		"""

		if downgrade is not None and not isinstance(downgrade, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: downgrade EXPECTED TYPE: bool', None, None)
		
		self.__downgrade = downgrade
		self.__key_modified['downgrade'] = 1

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
		self.__key_modified['delete'] = 1

	def get_deactivate(self):
		"""
		The method to get the deactivate

		Returns:
			bool: A bool representing the deactivate
		"""

		return self.__deactivate

	def set_deactivate(self, deactivate):
		"""
		The method to set the value to deactivate

		Parameters:
			deactivate (bool) : A bool representing the deactivate
		"""

		if deactivate is not None and not isinstance(deactivate, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deactivate EXPECTED TYPE: bool', None, None)
		
		self.__deactivate = deactivate
		self.__key_modified['deactivate'] = 1

	def get_set_layout_permissions(self):
		"""
		The method to get the set_layout_permissions

		Returns:
			bool: A bool representing the set_layout_permissions
		"""

		return self.__set_layout_permissions

	def set_set_layout_permissions(self, set_layout_permissions):
		"""
		The method to set the value to set_layout_permissions

		Parameters:
			set_layout_permissions (bool) : A bool representing the set_layout_permissions
		"""

		if set_layout_permissions is not None and not isinstance(set_layout_permissions, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: set_layout_permissions EXPECTED TYPE: bool', None, None)
		
		self.__set_layout_permissions = set_layout_permissions
		self.__key_modified['set_layout_permissions'] = 1

	def get_add_field(self):
		"""
		The method to get the add_field

		Returns:
			bool: A bool representing the add_field
		"""

		return self.__add_field

	def set_add_field(self, add_field):
		"""
		The method to set the value to add_field

		Parameters:
			add_field (bool) : A bool representing the add_field
		"""

		if add_field is not None and not isinstance(add_field, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: add_field EXPECTED TYPE: bool', None, None)
		
		self.__add_field = add_field
		self.__key_modified['add_field'] = 1

	def get_change_tab_traversal(self):
		"""
		The method to get the change_tab_traversal

		Returns:
			bool: A bool representing the change_tab_traversal
		"""

		return self.__change_tab_traversal

	def set_change_tab_traversal(self, change_tab_traversal):
		"""
		The method to set the value to change_tab_traversal

		Parameters:
			change_tab_traversal (bool) : A bool representing the change_tab_traversal
		"""

		if change_tab_traversal is not None and not isinstance(change_tab_traversal, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: change_tab_traversal EXPECTED TYPE: bool', None, None)
		
		self.__change_tab_traversal = change_tab_traversal
		self.__key_modified['change_tab_traversal'] = 1

	def get_reorder(self):
		"""
		The method to get the reorder

		Returns:
			bool: A bool representing the reorder
		"""

		return self.__reorder

	def set_reorder(self, reorder):
		"""
		The method to set the value to reorder

		Parameters:
			reorder (bool) : A bool representing the reorder
		"""

		if reorder is not None and not isinstance(reorder, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reorder EXPECTED TYPE: bool', None, None)
		
		self.__reorder = reorder
		self.__key_modified['reorder'] = 1

	def get_remove_field(self):
		"""
		The method to get the remove_field

		Returns:
			bool: A bool representing the remove_field
		"""

		return self.__remove_field

	def set_remove_field(self, remove_field):
		"""
		The method to set the value to remove_field

		Parameters:
			remove_field (bool) : A bool representing the remove_field
		"""

		if remove_field is not None and not isinstance(remove_field, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: remove_field EXPECTED TYPE: bool', None, None)
		
		self.__remove_field = remove_field
		self.__key_modified['remove_field'] = 1

	def get_change_column_count(self):
		"""
		The method to get the change_column_count

		Returns:
			bool: A bool representing the change_column_count
		"""

		return self.__change_column_count

	def set_change_column_count(self, change_column_count):
		"""
		The method to set the value to change_column_count

		Parameters:
			change_column_count (bool) : A bool representing the change_column_count
		"""

		if change_column_count is not None and not isinstance(change_column_count, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: change_column_count EXPECTED TYPE: bool', None, None)
		
		self.__change_column_count = change_column_count
		self.__key_modified['change_column_count'] = 1

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
