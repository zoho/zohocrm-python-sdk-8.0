try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.record.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .record import Record


class Participants(Record):
	def __init__(self):
		"""Creates an instance of Participants"""
		super().__init__()


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

	def get_email(self):
		"""
		The method to get the email

		Returns:
			string: A string representing the email
		"""

		return self.get_key_value('Email')

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (string) : A string representing the email
		"""

		if email is not None and not isinstance(email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Email', email)

	def get_invited(self):
		"""
		The method to get the invited

		Returns:
			bool: A bool representing the invited
		"""

		return self.get_key_value('invited')

	def set_invited(self, invited):
		"""
		The method to set the value to invited

		Parameters:
			invited (bool) : A bool representing the invited
		"""

		if invited is not None and not isinstance(invited, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: invited EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('invited', invited)

	def get_type(self):
		"""
		The method to get the type

		Returns:
			string: A string representing the type
		"""

		return self.get_key_value('type')

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (string) : A string representing the type
		"""

		if type is not None and not isinstance(type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: str', None, None)
		
		self.add_key_value('type', type)

	def get_participant(self):
		"""
		The method to get the participant

		Returns:
			string: A string representing the participant
		"""

		return self.get_key_value('participant')

	def set_participant(self, participant):
		"""
		The method to set the value to participant

		Parameters:
			participant (string) : A string representing the participant
		"""

		if participant is not None and not isinstance(participant, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: participant EXPECTED TYPE: str', None, None)
		
		self.add_key_value('participant', participant)

	def get_status(self):
		"""
		The method to get the status

		Returns:
			string: A string representing the status
		"""

		return self.get_key_value('status')

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (string) : A string representing the status
		"""

		if status is not None and not isinstance(status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: str', None, None)
		
		self.add_key_value('status', status)

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
