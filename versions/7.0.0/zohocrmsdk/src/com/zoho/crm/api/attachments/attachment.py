try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Attachment(object):
	def __init__(self):
		"""Creates an instance of Attachment"""

		self.__owner = None
		self.__modified_by = None
		self.__created_by = None
		self.__parent_id = None
		self.__sharing_permission = None
		self.__record_status__s = None
		self.__attachment_type = None
		self.__id = None
		self.__modified_time = None
		self.__created_time = None
		self.__file_name = None
		self.__size = None
		self.__editable = None
		self.__file_id = None
		self.__type = None
		self.__se_module = None
		self.__state = None
		self.__link_url = None
		self.__attachment_source__s = None
		self.__file_id__s = None
		self.__field_states = None
		self.__zia_visions = None
		self.__key_modified = dict()

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
			from zohocrmsdk.src.com.zoho.crm.api.attachments.parent_id import ParentId
		except Exception:
			from .parent_id import ParentId

		if parent_id is not None and not isinstance(parent_id, ParentId):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: parent_id EXPECTED TYPE: ParentId', None, None)
		
		self.__parent_id = parent_id
		self.__key_modified['Parent_Id'] = 1

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

	def get_record_status__s(self):
		"""
		The method to get the record_status__s

		Returns:
			string: A string representing the record_status__s
		"""

		return self.__record_status__s

	def set_record_status__s(self, record_status__s):
		"""
		The method to set the value to record_status__s

		Parameters:
			record_status__s (string) : A string representing the record_status__s
		"""

		if record_status__s is not None and not isinstance(record_status__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_status__s EXPECTED TYPE: str', None, None)
		
		self.__record_status__s = record_status__s
		self.__key_modified['Record_Status__s'] = 1

	def get_attachment_type(self):
		"""
		The method to get the attachment_type

		Returns:
			int: An int representing the attachment_type
		"""

		return self.__attachment_type

	def set_attachment_type(self, attachment_type):
		"""
		The method to set the value to attachment_type

		Parameters:
			attachment_type (int) : An int representing the attachment_type
		"""

		if attachment_type is not None and not isinstance(attachment_type, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachment_type EXPECTED TYPE: int', None, None)
		
		self.__attachment_type = attachment_type
		self.__key_modified['$attachment_type'] = 1

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

	def get_file_name(self):
		"""
		The method to get the file_name

		Returns:
			string: A string representing the file_name
		"""

		return self.__file_name

	def set_file_name(self, file_name):
		"""
		The method to set the value to file_name

		Parameters:
			file_name (string) : A string representing the file_name
		"""

		if file_name is not None and not isinstance(file_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_name EXPECTED TYPE: str', None, None)
		
		self.__file_name = file_name
		self.__key_modified['File_Name'] = 1

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
		self.__key_modified['Size'] = 1

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

	def get_file_id(self):
		"""
		The method to get the file_id

		Returns:
			string: A string representing the file_id
		"""

		return self.__file_id

	def set_file_id(self, file_id):
		"""
		The method to set the value to file_id

		Parameters:
			file_id (string) : A string representing the file_id
		"""

		if file_id is not None and not isinstance(file_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_id EXPECTED TYPE: str', None, None)
		
		self.__file_id = file_id
		self.__key_modified['$file_id'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.__type = type
		self.__key_modified['$type'] = 1

	def get_se_module(self):
		"""
		The method to get the se_module

		Returns:
			string: A string representing the se_module
		"""

		return self.__se_module

	def set_se_module(self, se_module):
		"""
		The method to set the value to se_module

		Parameters:
			se_module (string) : A string representing the se_module
		"""

		if se_module is not None and not isinstance(se_module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: se_module EXPECTED TYPE: str', None, None)
		
		self.__se_module = se_module
		self.__key_modified['$se_module'] = 1

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

	def get_link_url(self):
		"""
		The method to get the link_url

		Returns:
			string: A string representing the link_url
		"""

		return self.__link_url

	def set_link_url(self, link_url):
		"""
		The method to set the value to link_url

		Parameters:
			link_url (string) : A string representing the link_url
		"""

		if link_url is not None and not isinstance(link_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: link_url EXPECTED TYPE: str', None, None)
		
		self.__link_url = link_url
		self.__key_modified['$link_url'] = 1

	def get_attachment_source__s(self):
		"""
		The method to get the attachment_source__s

		Returns:
			string: A string representing the attachment_source__s
		"""

		return self.__attachment_source__s

	def set_attachment_source__s(self, attachment_source__s):
		"""
		The method to set the value to attachment_source__s

		Parameters:
			attachment_source__s (string) : A string representing the attachment_source__s
		"""

		if attachment_source__s is not None and not isinstance(attachment_source__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachment_source__s EXPECTED TYPE: str', None, None)
		
		self.__attachment_source__s = attachment_source__s
		self.__key_modified['Attachment_Source__s'] = 1

	def get_file_id__s(self):
		"""
		The method to get the file_id__s

		Returns:
			string: A string representing the file_id__s
		"""

		return self.__file_id__s

	def set_file_id__s(self, file_id__s):
		"""
		The method to set the value to file_id__s

		Parameters:
			file_id__s (string) : A string representing the file_id__s
		"""

		if file_id__s is not None and not isinstance(file_id__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_id__s EXPECTED TYPE: str', None, None)
		
		self.__file_id__s = file_id__s
		self.__key_modified['File_Id__s'] = 1

	def get_field_states(self):
		"""
		The method to get the field_states

		Returns:
			string: A string representing the field_states
		"""

		return self.__field_states

	def set_field_states(self, field_states):
		"""
		The method to set the value to field_states

		Parameters:
			field_states (string) : A string representing the field_states
		"""

		if field_states is not None and not isinstance(field_states, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_states EXPECTED TYPE: str', None, None)
		
		self.__field_states = field_states
		self.__key_modified['$field_states'] = 1

	def get_zia_visions(self):
		"""
		The method to get the zia_visions

		Returns:
			string: A string representing the zia_visions
		"""

		return self.__zia_visions

	def set_zia_visions(self, zia_visions):
		"""
		The method to set the value to zia_visions

		Parameters:
			zia_visions (string) : A string representing the zia_visions
		"""

		if zia_visions is not None and not isinstance(zia_visions, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zia_visions EXPECTED TYPE: str', None, None)
		
		self.__zia_visions = zia_visions
		self.__key_modified['$zia_visions'] = 1

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
