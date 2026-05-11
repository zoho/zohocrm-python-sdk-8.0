try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Note(object):
	def __init__(self):
		"""Creates an instance of Note"""

		self.__modified_time = None
		self.__attachments = None
		self.__owner = None
		self.__created_time = None
		self.__parent_id = None
		self.__editable = None
		self.__is_shared_to_client = None
		self.__sharing_permission = None
		self.__modified_by = None
		self.__size = None
		self.__state = None
		self.__voice_note = None
		self.__id = None
		self.__created_by = None
		self.__note_title = None
		self.__note_content = None
		self.__key_modified = dict()

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
		self.__key_modified['Modified_Time'] = 1

	def get_attachments(self):
		"""
		The method to get the attachments

		Returns:
			list: An instance of list
		"""

		return self.__attachments

	def set_attachments(self, attachments):
		"""
		The method to set the value to attachments

		Parameters:
			attachments (list) : An instance of list
		"""

		if attachments is not None and not isinstance(attachments, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachments EXPECTED TYPE: list', None, None)
		
		self.__attachments = attachments
		self.__key_modified['$attachments'] = 1

	def get_owner(self):
		"""
		The method to get the owner

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__owner

	def set_owner(self, owner):
		"""
		The method to set the value to owner

		Parameters:
			owner (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if owner is not None and not isinstance(owner, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: owner EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__owner = owner
		self.__key_modified['Owner'] = 1

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
		self.__key_modified['Created_Time'] = 1

	def get_parent_id(self):
		"""
		The method to get the parent_id

		Returns:
			ParentId: An instance of ParentId
		"""

		return self.__parent_id

	def set_parent_id(self, parent_id):
		"""
		The method to set the value to parent_id

		Parameters:
			parent_id (ParentId) : An instance of ParentId
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.notes.parent_id import ParentId
		except Exception:
			from .parent_id import ParentId

		if parent_id is not None and not isinstance(parent_id, ParentId):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_id EXPECTED TYPE: ParentId', None, None)
		
		self.__parent_id = parent_id
		self.__key_modified['Parent_Id'] = 1

	def get_editable(self):
		"""
		The method to get the editable

		Returns:
			bool: A bool representing the editable
		"""

		return self.__editable

	def set_editable(self, editable):
		"""
		The method to set the value to editable

		Parameters:
			editable (bool) : A bool representing the editable
		"""

		if editable is not None and not isinstance(editable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editable EXPECTED TYPE: bool', None, None)
		
		self.__editable = editable
		self.__key_modified['$editable'] = 1

	def get_is_shared_to_client(self):
		"""
		The method to get the is_shared_to_client

		Returns:
			bool: A bool representing the is_shared_to_client
		"""

		return self.__is_shared_to_client

	def set_is_shared_to_client(self, is_shared_to_client):
		"""
		The method to set the value to is_shared_to_client

		Parameters:
			is_shared_to_client (bool) : A bool representing the is_shared_to_client
		"""

		if is_shared_to_client is not None and not isinstance(is_shared_to_client, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: is_shared_to_client EXPECTED TYPE: bool', None, None)
		
		self.__is_shared_to_client = is_shared_to_client
		self.__key_modified['$is_shared_to_client'] = 1

	def get_sharing_permission(self):
		"""
		The method to get the sharing_permission

		Returns:
			string: A string representing the sharing_permission
		"""

		return self.__sharing_permission

	def set_sharing_permission(self, sharing_permission):
		"""
		The method to set the value to sharing_permission

		Parameters:
			sharing_permission (string) : A string representing the sharing_permission
		"""

		if sharing_permission is not None and not isinstance(sharing_permission, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sharing_permission EXPECTED TYPE: str', None, None)
		
		self.__sharing_permission = sharing_permission
		self.__key_modified['$sharing_permission'] = 1

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
		self.__key_modified['Modified_By'] = 1

	def get_size(self):
		"""
		The method to get the size

		Returns:
			string: A string representing the size
		"""

		return self.__size

	def set_size(self, size):
		"""
		The method to set the value to size

		Parameters:
			size (string) : A string representing the size
		"""

		if size is not None and not isinstance(size, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: size EXPECTED TYPE: str', None, None)
		
		self.__size = size
		self.__key_modified['$size'] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string representing the state
		"""

		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string representing the state
		"""

		if state is not None and not isinstance(state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: str', None, None)
		
		self.__state = state
		self.__key_modified['$state'] = 1

	def get_voice_note(self):
		"""
		The method to get the voice_note

		Returns:
			bool: A bool representing the voice_note
		"""

		return self.__voice_note

	def set_voice_note(self, voice_note):
		"""
		The method to set the value to voice_note

		Parameters:
			voice_note (bool) : A bool representing the voice_note
		"""

		if voice_note is not None and not isinstance(voice_note, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: voice_note EXPECTED TYPE: bool', None, None)
		
		self.__voice_note = voice_note
		self.__key_modified['$voice_note'] = 1

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
		self.__key_modified['Created_By'] = 1

	def get_note_title(self):
		"""
		The method to get the note_title

		Returns:
			string: A string representing the note_title
		"""

		return self.__note_title

	def set_note_title(self, note_title):
		"""
		The method to set the value to note_title

		Parameters:
			note_title (string) : A string representing the note_title
		"""

		if note_title is not None and not isinstance(note_title, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: note_title EXPECTED TYPE: str', None, None)
		
		self.__note_title = note_title
		self.__key_modified['Note_Title'] = 1

	def get_note_content(self):
		"""
		The method to get the note_content

		Returns:
			string: A string representing the note_content
		"""

		return self.__note_content

	def set_note_content(self, note_content):
		"""
		The method to set the value to note_content

		Parameters:
			note_content (string) : A string representing the note_content
		"""

		if note_content is not None and not isinstance(note_content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: note_content EXPECTED TYPE: str', None, None)
		
		self.__note_content = note_content
		self.__key_modified['Note_Content'] = 1

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
