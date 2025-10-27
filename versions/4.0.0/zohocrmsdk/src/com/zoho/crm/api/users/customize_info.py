try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class CustomizeInfo(object):
	def __init__(self):
		"""Creates an instance of CustomizeInfo"""

		self.__notes_desc = None
		self.__show_right_panel = None
		self.__bc_view = None
		self.__unpin_recent_item = None
		self.__show_home = None
		self.__show_detail_view = None
		self.__key_modified = dict()

	def get_notes_desc(self):
		"""
		The method to get the notes_desc

		Returns:
			Object: A Object representing the notes_desc
		"""

		return self.__notes_desc

	def set_notes_desc(self, notes_desc):
		"""
		The method to set the value to notes_desc

		Parameters:
			notes_desc (Object) : A Object representing the notes_desc
		"""

		self.__notes_desc = notes_desc
		self.__key_modified['notes_desc'] = 1

	def get_show_right_panel(self):
		"""
		The method to get the show_right_panel

		Returns:
			Object: A Object representing the show_right_panel
		"""

		return self.__show_right_panel

	def set_show_right_panel(self, show_right_panel):
		"""
		The method to set the value to show_right_panel

		Parameters:
			show_right_panel (Object) : A Object representing the show_right_panel
		"""

		self.__show_right_panel = show_right_panel
		self.__key_modified['show_right_panel'] = 1

	def get_bc_view(self):
		"""
		The method to get the bc_view

		Returns:
			Object: A Object representing the bc_view
		"""

		return self.__bc_view

	def set_bc_view(self, bc_view):
		"""
		The method to set the value to bc_view

		Parameters:
			bc_view (Object) : A Object representing the bc_view
		"""

		self.__bc_view = bc_view
		self.__key_modified['bc_view'] = 1

	def get_unpin_recent_item(self):
		"""
		The method to get the unpin_recent_item

		Returns:
			Object: A Object representing the unpin_recent_item
		"""

		return self.__unpin_recent_item

	def set_unpin_recent_item(self, unpin_recent_item):
		"""
		The method to set the value to unpin_recent_item

		Parameters:
			unpin_recent_item (Object) : A Object representing the unpin_recent_item
		"""

		self.__unpin_recent_item = unpin_recent_item
		self.__key_modified['unpin_recent_item'] = 1

	def get_show_home(self):
		"""
		The method to get the show_home

		Returns:
			bool: A bool representing the show_home
		"""

		return self.__show_home

	def set_show_home(self, show_home):
		"""
		The method to set the value to show_home

		Parameters:
			show_home (bool) : A bool representing the show_home
		"""

		if show_home is not None and not isinstance(show_home, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_home EXPECTED TYPE: bool', None, None)
		
		self.__show_home = show_home
		self.__key_modified['show_home'] = 1

	def get_show_detail_view(self):
		"""
		The method to get the show_detail_view

		Returns:
			bool: A bool representing the show_detail_view
		"""

		return self.__show_detail_view

	def set_show_detail_view(self, show_detail_view):
		"""
		The method to set the value to show_detail_view

		Parameters:
			show_detail_view (bool) : A bool representing the show_detail_view
		"""

		if show_detail_view is not None and not isinstance(show_detail_view, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_detail_view EXPECTED TYPE: bool', None, None)
		
		self.__show_detail_view = show_detail_view
		self.__key_modified['show_detail_view'] = 1

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
