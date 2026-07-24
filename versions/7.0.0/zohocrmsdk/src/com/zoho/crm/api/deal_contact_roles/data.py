try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.record import Record
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from ..record import Record


class Data(Record):
	def __init__(self):
		"""Creates an instance of Data"""
		super().__init__()


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

	def get_contact_role(self):
		"""
		The method to get the contact_role

		Returns:
			ContactRole: An instance of ContactRole
		"""

		return self.get_key_value('Contact_Role')

	def set_contact_role(self, contact_role):
		"""
		The method to set the value to contact_role

		Parameters:
			contact_role (ContactRole) : An instance of ContactRole
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles.contact_role import ContactRole
		except Exception:
			from .contact_role import ContactRole

		if contact_role is not None and not isinstance(contact_role, ContactRole):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact_role EXPECTED TYPE: ContactRole', None, None)
		
		self.add_key_value('Contact_Role', contact_role)

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
