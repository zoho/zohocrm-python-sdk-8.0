try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
	from zohocrmsdk.src.com.zoho.crm.api.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants
	from ..record import Record


class RecordLock(Record):
	def __init__(self):
		"""Creates an instance of RecordLock"""
		super().__init__()


	def get_lock_source__s(self):
		"""
		The method to get the lock_source__s

		Returns:
			Choice: An instance of Choice
		"""

		return self.get_key_value('lock_source__s')

	def set_lock_source__s(self, lock_source__s):
		"""
		The method to set the value to lock_source__s

		Parameters:
			lock_source__s (Choice) : An instance of Choice
		"""

		if lock_source__s is not None and not isinstance(lock_source__s, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lock_source__s EXPECTED TYPE: Choice', None, None)
		
		self.add_key_value('lock_source__s', lock_source__s)

	def get_locked_by__s(self):
		"""
		The method to get the locked_by__s

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.get_key_value('locked_by__s')

	def set_locked_by__s(self, locked_by__s):
		"""
		The method to set the value to locked_by__s

		Parameters:
			locked_by__s (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if locked_by__s is not None and not isinstance(locked_by__s, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locked_by__s EXPECTED TYPE: MinifiedUser', None, None)
		
		self.add_key_value('locked_by__s', locked_by__s)

	def get_locked_for_s(self):
		"""
		The method to get the locked_for_s

		Returns:
			LockedForS: An instance of LockedForS
		"""

		return self.get_key_value('locked_for_s')

	def set_locked_for_s(self, locked_for_s):
		"""
		The method to set the value to locked_for_s

		Parameters:
			locked_for_s (LockedForS) : An instance of LockedForS
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking.locked_for_s import LockedForS
		except Exception:
			from .locked_for_s import LockedForS

		if locked_for_s is not None and not isinstance(locked_for_s, LockedForS):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locked_for_s EXPECTED TYPE: LockedForS', None, None)
		
		self.add_key_value('locked_for_s', locked_for_s)

	def get_locked_reason__s(self):
		"""
		The method to get the locked_reason__s

		Returns:
			string: A string representing the locked_reason__s
		"""

		return self.get_key_value('locked_reason__s')

	def set_locked_reason__s(self, locked_reason__s):
		"""
		The method to set the value to locked_reason__s

		Parameters:
			locked_reason__s (string) : A string representing the locked_reason__s
		"""

		if locked_reason__s is not None and not isinstance(locked_reason__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locked_reason__s EXPECTED TYPE: str', None, None)
		
		self.add_key_value('locked_reason__s', locked_reason__s)

	def get_locked_time__s(self):
		"""
		The method to get the locked_time__s

		Returns:
			string: A string representing the locked_time__s
		"""

		return self.get_key_value('Locked_time__s')

	def set_locked_time__s(self, locked_time__s):
		"""
		The method to set the value to locked_time__s

		Parameters:
			locked_time__s (string) : A string representing the locked_time__s
		"""

		if locked_time__s is not None and not isinstance(locked_time__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: locked_time__s EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Locked_time__s', locked_time__s)

	def get_record_locking_configuration_id__s(self):
		"""
		The method to get the record_locking_configuration_id__s

		Returns:
			int: An int representing the record_locking_configuration_id__s
		"""

		return self.get_key_value('record_locking_configuration_id__s')

	def set_record_locking_configuration_id__s(self, record_locking_configuration_id__s):
		"""
		The method to set the value to record_locking_configuration_id__s

		Parameters:
			record_locking_configuration_id__s (int) : An int representing the record_locking_configuration_id__s
		"""

		if record_locking_configuration_id__s is not None and not isinstance(record_locking_configuration_id__s, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_locking_configuration_id__s EXPECTED TYPE: int', None, None)
		
		self.add_key_value('record_locking_configuration_id__s', record_locking_configuration_id__s)

	def get_record_locking_rule_id__s(self):
		"""
		The method to get the record_locking_rule_id__s

		Returns:
			int: An int representing the record_locking_rule_id__s
		"""

		return self.get_key_value('record_locking_rule_id__s')

	def set_record_locking_rule_id__s(self, record_locking_rule_id__s):
		"""
		The method to set the value to record_locking_rule_id__s

		Parameters:
			record_locking_rule_id__s (int) : An int representing the record_locking_rule_id__s
		"""

		if record_locking_rule_id__s is not None and not isinstance(record_locking_rule_id__s, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_locking_rule_id__s EXPECTED TYPE: int', None, None)
		
		self.add_key_value('record_locking_rule_id__s', record_locking_rule_id__s)

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.get_key_value('id')

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.add_key_value('id', id)

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.get_key_value('Created_By')

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
		
		self.add_key_value('Created_By', created_by)

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.get_key_value('Created_Time')

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.add_key_value('Created_Time', created_time)

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.get_key_value('Modified_By')

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
		
		self.add_key_value('Modified_By', modified_by)

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.get_key_value('Modified_Time')

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.add_key_value('Modified_Time', modified_time)

	def get_tag(self):
		"""
		The method to get the tag

		Returns:
			list: An instance of list
		"""

		return self.get_key_value('Tag')

	def set_tag(self, tag):
		"""
		The method to set the value to tag

		Parameters:
			tag (list) : An instance of list
		"""

		if tag is not None and not isinstance(tag, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tag EXPECTED TYPE: list', None, None)
		
		self.add_key_value('Tag', tag)

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.get_key_value('name')

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.add_key_value('name', name)
