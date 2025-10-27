try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Templates(object):
	def __init__(self):
		"""Creates an instance of Templates"""

		self.__folder = None
		self.__modified_by = None
		self.__module = None
		self.__modified_time = None
		self.__subject = None
		self.__name = None
		self.__consent_linked = None
		self.__favourite = None
		self.__attachment_present = None
		self.__id = None
		self.__key_modified = dict()

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
			from zohocrmsdk.src.com.zoho.crm.api.templates.folder import Folder
		except Exception:
			from .folder import Folder

		if folder is not None and not isinstance(folder, Folder):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: folder EXPECTED TYPE: Folder', None, None)
		
		self.__folder = folder
		self.__key_modified['folder'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			Folder: An instance of Folder
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (Folder) : An instance of Folder
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.templates.folder import Folder
		except Exception:
			from .folder import Folder

		if modified_by is not None and not isinstance(modified_by, Folder):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: Folder', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

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

	def get_subject(self):
		"""
		The method to get the subject

		Returns:
			string: A string representing the subject
		"""

		return self.__subject

	def set_subject(self, subject):
		"""
		The method to set the value to subject

		Parameters:
			subject (string) : A string representing the subject
		"""

		if subject is not None and not isinstance(subject, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subject EXPECTED TYPE: str', None, None)
		
		self.__subject = subject
		self.__key_modified['subject'] = 1

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

	def get_consent_linked(self):
		"""
		The method to get the consent_linked

		Returns:
			bool: A bool representing the consent_linked
		"""

		return self.__consent_linked

	def set_consent_linked(self, consent_linked):
		"""
		The method to set the value to consent_linked

		Parameters:
			consent_linked (bool) : A bool representing the consent_linked
		"""

		if consent_linked is not None and not isinstance(consent_linked, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_linked EXPECTED TYPE: bool', None, None)
		
		self.__consent_linked = consent_linked
		self.__key_modified['consent_linked'] = 1

	def get_favourite(self):
		"""
		The method to get the favourite

		Returns:
			bool: A bool representing the favourite
		"""

		return self.__favourite

	def set_favourite(self, favourite):
		"""
		The method to set the value to favourite

		Parameters:
			favourite (bool) : A bool representing the favourite
		"""

		if favourite is not None and not isinstance(favourite, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: favourite EXPECTED TYPE: bool', None, None)
		
		self.__favourite = favourite
		self.__key_modified['favourite'] = 1

	def get_attachment_present(self):
		"""
		The method to get the attachment_present

		Returns:
			bool: A bool representing the attachment_present
		"""

		return self.__attachment_present

	def set_attachment_present(self, attachment_present):
		"""
		The method to set the value to attachment_present

		Parameters:
			attachment_present (bool) : A bool representing the attachment_present
		"""

		if attachment_present is not None and not isinstance(attachment_present, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachment_present EXPECTED TYPE: bool', None, None)
		
		self.__attachment_present = attachment_present
		self.__key_modified['attachment_present'] = 1

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
