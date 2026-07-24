try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Timeline(object):
	def __init__(self):
		"""Creates an instance of Timeline"""

		self.__audited_time = None
		self.__action = None
		self.__id = None
		self.__source = None
		self.__extension = None
		self.__type = None
		self.__done_by = None
		self.__related_record = None
		self.__automation_details = None
		self.__record = None
		self.__field_history = None
		self.__key_modified = dict()

	def get_audited_time(self):
		"""
		The method to get the audited_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__audited_time

	def set_audited_time(self, audited_time):
		"""
		The method to set the value to audited_time

		Parameters:
			audited_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if audited_time is not None and not isinstance(audited_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: audited_time EXPECTED TYPE: datetime', None, None)
		
		self.__audited_time = audited_time
		self.__key_modified['audited_time'] = 1

	def get_action(self):
		"""
		The method to get the action

		Returns:
			string: A string representing the action
		"""

		return self.__action

	def set_action(self, action):
		"""
		The method to set the value to action

		Parameters:
			action (string) : A string representing the action
		"""

		if action is not None and not isinstance(action, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action EXPECTED TYPE: str', None, None)
		
		self.__action = action
		self.__key_modified['action'] = 1

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
			string: A string representing the source
		"""

		return self.__source

	def set_source(self, source):
		"""
		The method to set the value to source

		Parameters:
			source (string) : A string representing the source
		"""

		if source is not None and not isinstance(source, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: source EXPECTED TYPE: str', None, None)
		
		self.__source = source
		self.__key_modified['source'] = 1

	def get_extension(self):
		"""
		The method to get the extension

		Returns:
			string: A string representing the extension
		"""

		return self.__extension

	def set_extension(self, extension):
		"""
		The method to set the value to extension

		Parameters:
			extension (string) : A string representing the extension
		"""

		if extension is not None and not isinstance(extension, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: extension EXPECTED TYPE: str', None, None)
		
		self.__extension = extension
		self.__key_modified['extension'] = 1

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
		self.__key_modified['type'] = 1

	def get_done_by(self):
		"""
		The method to get the done_by

		Returns:
			NameIdStructure: An instance of NameIdStructure
		"""

		return self.__done_by

	def set_done_by(self, done_by):
		"""
		The method to set the value to done_by

		Parameters:
			done_by (NameIdStructure) : An instance of NameIdStructure
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.name_id_structure import NameIdStructure
		except Exception:
			from .name_id_structure import NameIdStructure

		if done_by is not None and not isinstance(done_by, NameIdStructure):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: done_by EXPECTED TYPE: NameIdStructure', None, None)
		
		self.__done_by = done_by
		self.__key_modified['done_by'] = 1

	def get_related_record(self):
		"""
		The method to get the related_record

		Returns:
			RelatedRecord: An instance of RelatedRecord
		"""

		return self.__related_record

	def set_related_record(self, related_record):
		"""
		The method to set the value to related_record

		Parameters:
			related_record (RelatedRecord) : An instance of RelatedRecord
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.related_record import RelatedRecord
		except Exception:
			from .related_record import RelatedRecord

		if related_record is not None and not isinstance(related_record, RelatedRecord):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record EXPECTED TYPE: RelatedRecord', None, None)
		
		self.__related_record = related_record
		self.__key_modified['related_record'] = 1

	def get_automation_details(self):
		"""
		The method to get the automation_details

		Returns:
			AutomationDetail: An instance of AutomationDetail
		"""

		return self.__automation_details

	def set_automation_details(self, automation_details):
		"""
		The method to set the value to automation_details

		Parameters:
			automation_details (AutomationDetail) : An instance of AutomationDetail
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.automation_detail import AutomationDetail
		except Exception:
			from .automation_detail import AutomationDetail

		if automation_details is not None and not isinstance(automation_details, AutomationDetail):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: automation_details EXPECTED TYPE: AutomationDetail', None, None)
		
		self.__automation_details = automation_details
		self.__key_modified['automation_details'] = 1

	def get_record(self):
		"""
		The method to get the record

		Returns:
			Record: An instance of Record
		"""

		return self.__record

	def set_record(self, record):
		"""
		The method to set the value to record

		Parameters:
			record (Record) : An instance of Record
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.record import Record
		except Exception:
			from .record import Record

		if record is not None and not isinstance(record, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record EXPECTED TYPE: Record', None, None)
		
		self.__record = record
		self.__key_modified['record'] = 1

	def get_field_history(self):
		"""
		The method to get the field_history

		Returns:
			list: An instance of list
		"""

		return self.__field_history

	def set_field_history(self, field_history):
		"""
		The method to set the value to field_history

		Parameters:
			field_history (list) : An instance of list
		"""

		if field_history is not None and not isinstance(field_history, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_history EXPECTED TYPE: list', None, None)
		
		self.__field_history = field_history
		self.__key_modified['field_history'] = 1

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
