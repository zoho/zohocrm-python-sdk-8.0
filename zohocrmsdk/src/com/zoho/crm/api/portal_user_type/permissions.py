try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Permissions(object):
	def __init__(self):
		"""Creates an instance of Permissions"""

		self.__view = None
		self.__edit = None
		self.__edit_shared_records = None
		self.__create = None
		self.__delete = None
		self.__delete_attachment = None
		self.__create_attachment = None
		self.__key_modified = dict()

	def get_view(self):
		"""
		The method to get the view

		Returns:
			bool: A bool representing the view
		"""

		return self.__view

	def set_view(self, view):
		"""
		The method to set the value to view

		Parameters:
			view (bool) : A bool representing the view
		"""

		if view is not None and not isinstance(view, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: view EXPECTED TYPE: bool', None, None)
		
		self.__view = view
		self.__key_modified['view'] = 1

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

	def get_edit_shared_records(self):
		"""
		The method to get the edit_shared_records

		Returns:
			bool: A bool representing the edit_shared_records
		"""

		return self.__edit_shared_records

	def set_edit_shared_records(self, edit_shared_records):
		"""
		The method to set the value to edit_shared_records

		Parameters:
			edit_shared_records (bool) : A bool representing the edit_shared_records
		"""

		if edit_shared_records is not None and not isinstance(edit_shared_records, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: edit_shared_records EXPECTED TYPE: bool', None, None)
		
		self.__edit_shared_records = edit_shared_records
		self.__key_modified['edit_shared_records'] = 1

	def get_create(self):
		"""
		The method to get the create

		Returns:
			bool: A bool representing the create
		"""

		return self.__create

	def set_create(self, create):
		"""
		The method to set the value to create

		Parameters:
			create (bool) : A bool representing the create
		"""

		if create is not None and not isinstance(create, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: create EXPECTED TYPE: bool', None, None)
		
		self.__create = create
		self.__key_modified['create'] = 1

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

	def get_delete_attachment(self):
		"""
		The method to get the delete_attachment

		Returns:
			bool: A bool representing the delete_attachment
		"""

		return self.__delete_attachment

	def set_delete_attachment(self, delete_attachment):
		"""
		The method to set the value to delete_attachment

		Parameters:
			delete_attachment (bool) : A bool representing the delete_attachment
		"""

		if delete_attachment is not None and not isinstance(delete_attachment, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delete_attachment EXPECTED TYPE: bool', None, None)
		
		self.__delete_attachment = delete_attachment
		self.__key_modified['delete_attachment'] = 1

	def get_create_attachment(self):
		"""
		The method to get the create_attachment

		Returns:
			bool: A bool representing the create_attachment
		"""

		return self.__create_attachment

	def set_create_attachment(self, create_attachment):
		"""
		The method to set the value to create_attachment

		Parameters:
			create_attachment (bool) : A bool representing the create_attachment
		"""

		if create_attachment is not None and not isinstance(create_attachment, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: create_attachment EXPECTED TYPE: bool', None, None)
		
		self.__create_attachment = create_attachment
		self.__key_modified['create_attachment'] = 1

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
