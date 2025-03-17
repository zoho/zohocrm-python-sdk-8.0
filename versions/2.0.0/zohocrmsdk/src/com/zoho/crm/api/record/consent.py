try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.record.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .record import Record


class Consent(Record):
	def __init__(self):
		"""Creates an instance of Consent"""
		super().__init__()


	def get_owner(self):
		"""
		The method to get the owner

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.get_key_value('Owner')

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
		
		self.add_key_value('Owner', owner)

	def get_contact_through_email(self):
		"""
		The method to get the contact_through_email

		Returns:
			bool: A bool representing the contact_through_email
		"""

		return self.get_key_value('Contact_Through_Email')

	def set_contact_through_email(self, contact_through_email):
		"""
		The method to set the value to contact_through_email

		Parameters:
			contact_through_email (bool) : A bool representing the contact_through_email
		"""

		if contact_through_email is not None and not isinstance(contact_through_email, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_through_email EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Contact_Through_Email', contact_through_email)

	def get_contact_through_social(self):
		"""
		The method to get the contact_through_social

		Returns:
			bool: A bool representing the contact_through_social
		"""

		return self.get_key_value('Contact_Through_Social')

	def set_contact_through_social(self, contact_through_social):
		"""
		The method to set the value to contact_through_social

		Parameters:
			contact_through_social (bool) : A bool representing the contact_through_social
		"""

		if contact_through_social is not None and not isinstance(contact_through_social, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_through_social EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Contact_Through_Social', contact_through_social)

	def get_contact_through_survey(self):
		"""
		The method to get the contact_through_survey

		Returns:
			bool: A bool representing the contact_through_survey
		"""

		return self.get_key_value('Contact_Through_Survey')

	def set_contact_through_survey(self, contact_through_survey):
		"""
		The method to set the value to contact_through_survey

		Parameters:
			contact_through_survey (bool) : A bool representing the contact_through_survey
		"""

		if contact_through_survey is not None and not isinstance(contact_through_survey, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_through_survey EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Contact_Through_Survey', contact_through_survey)

	def get_contact_through_phone(self):
		"""
		The method to get the contact_through_phone

		Returns:
			bool: A bool representing the contact_through_phone
		"""

		return self.get_key_value('Contact_Through_Phone')

	def set_contact_through_phone(self, contact_through_phone):
		"""
		The method to set the value to contact_through_phone

		Parameters:
			contact_through_phone (bool) : A bool representing the contact_through_phone
		"""

		if contact_through_phone is not None and not isinstance(contact_through_phone, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_through_phone EXPECTED TYPE: bool', None, None)
		
		self.add_key_value('Contact_Through_Phone', contact_through_phone)

	def get_mail_sent_time(self):
		"""
		The method to get the mail_sent_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.get_key_value('Mail_Sent_Time')

	def set_mail_sent_time(self, mail_sent_time):
		"""
		The method to set the value to mail_sent_time

		Parameters:
			mail_sent_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if mail_sent_time is not None and not isinstance(mail_sent_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mail_sent_time EXPECTED TYPE: datetime', None, None)
		
		self.add_key_value('Mail_Sent_Time', mail_sent_time)

	def get_consent_date(self):
		"""
		The method to get the consent_date

		Returns:
			date: An instance of date
		"""

		return self.get_key_value('Consent_Date')

	def set_consent_date(self, consent_date):
		"""
		The method to set the value to consent_date

		Parameters:
			consent_date (date) : An instance of date
		"""

		from datetime import date as date1

		if consent_date is not None and not isinstance(consent_date, date1):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_date EXPECTED TYPE: date1', None, None)
		
		self.add_key_value('Consent_Date', consent_date)

	def get_consent_remarks(self):
		"""
		The method to get the consent_remarks

		Returns:
			string: A string representing the consent_remarks
		"""

		return self.get_key_value('Consent_Remarks')

	def set_consent_remarks(self, consent_remarks):
		"""
		The method to set the value to consent_remarks

		Parameters:
			consent_remarks (string) : A string representing the consent_remarks
		"""

		if consent_remarks is not None and not isinstance(consent_remarks, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_remarks EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Consent_Remarks', consent_remarks)

	def get_consent_through(self):
		"""
		The method to get the consent_through

		Returns:
			string: A string representing the consent_through
		"""

		return self.get_key_value('Consent_Through')

	def set_consent_through(self, consent_through):
		"""
		The method to set the value to consent_through

		Parameters:
			consent_through (string) : A string representing the consent_through
		"""

		if consent_through is not None and not isinstance(consent_through, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: consent_through EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Consent_Through', consent_through)

	def get_data_processing_basis(self):
		"""
		The method to get the data_processing_basis

		Returns:
			string: A string representing the data_processing_basis
		"""

		return self.get_key_value('Data_Processing_Basis')

	def set_data_processing_basis(self, data_processing_basis):
		"""
		The method to set the value to data_processing_basis

		Parameters:
			data_processing_basis (string) : A string representing the data_processing_basis
		"""

		if data_processing_basis is not None and not isinstance(data_processing_basis, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_processing_basis EXPECTED TYPE: str', None, None)
		
		self.add_key_value('Data_Processing_Basis', data_processing_basis)

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
