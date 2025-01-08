try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class LeadConverter(object):
	def __init__(self):
		"""Creates an instance of LeadConverter"""

		self.__overwrite = None
		self.__notify_lead_owner = None
		self.__notify_new_entity_owner = None
		self.__move_attachments_to = None
		self.__accounts = None
		self.__contacts = None
		self.__assign_to = None
		self.__deals = None
		self.__add_to_existing_record = None
		self.__carry_over_tags = None
		self.__key_modified = dict()

	def get_overwrite(self):
		"""
		The method to get the overwrite

		Returns:
			bool: A bool representing the overwrite
		"""

		return self.__overwrite

	def set_overwrite(self, overwrite):
		"""
		The method to set the value to overwrite

		Parameters:
			overwrite (bool) : A bool representing the overwrite
		"""

		if overwrite is not None and not isinstance(overwrite, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: overwrite EXPECTED TYPE: bool', None, None)
		
		self.__overwrite = overwrite
		self.__key_modified['overwrite'] = 1

	def get_notify_lead_owner(self):
		"""
		The method to get the notify_lead_owner

		Returns:
			bool: A bool representing the notify_lead_owner
		"""

		return self.__notify_lead_owner

	def set_notify_lead_owner(self, notify_lead_owner):
		"""
		The method to set the value to notify_lead_owner

		Parameters:
			notify_lead_owner (bool) : A bool representing the notify_lead_owner
		"""

		if notify_lead_owner is not None and not isinstance(notify_lead_owner, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notify_lead_owner EXPECTED TYPE: bool', None, None)
		
		self.__notify_lead_owner = notify_lead_owner
		self.__key_modified['notify_lead_owner'] = 1

	def get_notify_new_entity_owner(self):
		"""
		The method to get the notify_new_entity_owner

		Returns:
			bool: A bool representing the notify_new_entity_owner
		"""

		return self.__notify_new_entity_owner

	def set_notify_new_entity_owner(self, notify_new_entity_owner):
		"""
		The method to set the value to notify_new_entity_owner

		Parameters:
			notify_new_entity_owner (bool) : A bool representing the notify_new_entity_owner
		"""

		if notify_new_entity_owner is not None and not isinstance(notify_new_entity_owner, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notify_new_entity_owner EXPECTED TYPE: bool', None, None)
		
		self.__notify_new_entity_owner = notify_new_entity_owner
		self.__key_modified['notify_new_entity_owner'] = 1

	def get_move_attachments_to(self):
		"""
		The method to get the move_attachments_to

		Returns:
			MoveAttachmentsTo: An instance of MoveAttachmentsTo
		"""

		return self.__move_attachments_to

	def set_move_attachments_to(self, move_attachments_to):
		"""
		The method to set the value to move_attachments_to

		Parameters:
			move_attachments_to (MoveAttachmentsTo) : An instance of MoveAttachmentsTo
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.convert_lead.move_attachments_to import MoveAttachmentsTo
		except Exception:
			from .move_attachments_to import MoveAttachmentsTo

		if move_attachments_to is not None and not isinstance(move_attachments_to, MoveAttachmentsTo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: move_attachments_to EXPECTED TYPE: MoveAttachmentsTo', None, None)
		
		self.__move_attachments_to = move_attachments_to
		self.__key_modified['move_attachments_to'] = 1

	def get_accounts(self):
		"""
		The method to get the accounts

		Returns:
			Record: An instance of Record
		"""

		return self.__accounts

	def set_accounts(self, accounts):
		"""
		The method to set the value to accounts

		Parameters:
			accounts (Record) : An instance of Record
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record import Record
		except Exception:
			from ..record import Record

		if accounts is not None and not isinstance(accounts, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: accounts EXPECTED TYPE: Record', None, None)
		
		self.__accounts = accounts
		self.__key_modified['Accounts'] = 1

	def get_contacts(self):
		"""
		The method to get the contacts

		Returns:
			Record: An instance of Record
		"""

		return self.__contacts

	def set_contacts(self, contacts):
		"""
		The method to set the value to contacts

		Parameters:
			contacts (Record) : An instance of Record
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record import Record
		except Exception:
			from ..record import Record

		if contacts is not None and not isinstance(contacts, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contacts EXPECTED TYPE: Record', None, None)
		
		self.__contacts = contacts
		self.__key_modified['Contacts'] = 1

	def get_assign_to(self):
		"""
		The method to get the assign_to

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__assign_to

	def set_assign_to(self, assign_to):
		"""
		The method to set the value to assign_to

		Parameters:
			assign_to (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if assign_to is not None and not isinstance(assign_to, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: assign_to EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__assign_to = assign_to
		self.__key_modified['assign_to'] = 1

	def get_deals(self):
		"""
		The method to get the deals

		Returns:
			Record: An instance of Record
		"""

		return self.__deals

	def set_deals(self, deals):
		"""
		The method to set the value to deals

		Parameters:
			deals (Record) : An instance of Record
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record import Record
		except Exception:
			from ..record import Record

		if deals is not None and not isinstance(deals, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deals EXPECTED TYPE: Record', None, None)
		
		self.__deals = deals
		self.__key_modified['Deals'] = 1

	def get_add_to_existing_record(self):
		"""
		The method to get the add_to_existing_record

		Returns:
			Choice: An instance of Choice
		"""

		return self.__add_to_existing_record

	def set_add_to_existing_record(self, add_to_existing_record):
		"""
		The method to set the value to add_to_existing_record

		Parameters:
			add_to_existing_record (Choice) : An instance of Choice
		"""

		if add_to_existing_record is not None and not isinstance(add_to_existing_record, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: add_to_existing_record EXPECTED TYPE: Choice', None, None)
		
		self.__add_to_existing_record = add_to_existing_record
		self.__key_modified['add_to_existing_record'] = 1

	def get_carry_over_tags(self):
		"""
		The method to get the carry_over_tags

		Returns:
			CarryOverTags: An instance of CarryOverTags
		"""

		return self.__carry_over_tags

	def set_carry_over_tags(self, carry_over_tags):
		"""
		The method to set the value to carry_over_tags

		Parameters:
			carry_over_tags (CarryOverTags) : An instance of CarryOverTags
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.convert_lead.carry_over_tags import CarryOverTags
		except Exception:
			from .carry_over_tags import CarryOverTags

		if carry_over_tags is not None and not isinstance(carry_over_tags, CarryOverTags):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: carry_over_tags EXPECTED TYPE: CarryOverTags', None, None)
		
		self.__carry_over_tags = carry_over_tags
		self.__key_modified['carry_over_tags'] = 1

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
