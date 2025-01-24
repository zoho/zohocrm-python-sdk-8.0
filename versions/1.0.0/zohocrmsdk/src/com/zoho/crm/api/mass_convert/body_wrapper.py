try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__deals = None
		self.__move_attachments_to = None
		self.__assign_to = None
		self.__carry_over_tags = None
		self.__related_modules = None
		self.__portal_user_type = None
		self.__ids = None
		self.__apply_assignment_threshold = None
		self.__key_modified = dict()

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
			from zohocrmsdk.src.com.zoho.crm.api.mass_convert.move_attachments_to import MoveAttachmentsTo
		except Exception:
			from .move_attachments_to import MoveAttachmentsTo

		if move_attachments_to is not None and not isinstance(move_attachments_to, MoveAttachmentsTo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: move_attachments_to EXPECTED TYPE: MoveAttachmentsTo', None, None)
		
		self.__move_attachments_to = move_attachments_to
		self.__key_modified['move_attachments_to'] = 1

	def get_assign_to(self):
		"""
		The method to get the assign_to

		Returns:
			AssignTo: An instance of AssignTo
		"""

		return self.__assign_to

	def set_assign_to(self, assign_to):
		"""
		The method to set the value to assign_to

		Parameters:
			assign_to (AssignTo) : An instance of AssignTo
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mass_convert.assign_to import AssignTo
		except Exception:
			from .assign_to import AssignTo

		if assign_to is not None and not isinstance(assign_to, AssignTo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: assign_to EXPECTED TYPE: AssignTo', None, None)
		
		self.__assign_to = assign_to
		self.__key_modified['assign_to'] = 1

	def get_carry_over_tags(self):
		"""
		The method to get the carry_over_tags

		Returns:
			list: An instance of list
		"""

		return self.__carry_over_tags

	def set_carry_over_tags(self, carry_over_tags):
		"""
		The method to set the value to carry_over_tags

		Parameters:
			carry_over_tags (list) : An instance of list
		"""

		if carry_over_tags is not None and not isinstance(carry_over_tags, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: carry_over_tags EXPECTED TYPE: list', None, None)
		
		self.__carry_over_tags = carry_over_tags
		self.__key_modified['carry_over_tags'] = 1

	def get_related_modules(self):
		"""
		The method to get the related_modules

		Returns:
			list: An instance of list
		"""

		return self.__related_modules

	def set_related_modules(self, related_modules):
		"""
		The method to set the value to related_modules

		Parameters:
			related_modules (list) : An instance of list
		"""

		if related_modules is not None and not isinstance(related_modules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_modules EXPECTED TYPE: list', None, None)
		
		self.__related_modules = related_modules
		self.__key_modified['related_modules'] = 1

	def get_portal_user_type(self):
		"""
		The method to get the portal_user_type

		Returns:
			PortalUserType: An instance of PortalUserType
		"""

		return self.__portal_user_type

	def set_portal_user_type(self, portal_user_type):
		"""
		The method to set the value to portal_user_type

		Parameters:
			portal_user_type (PortalUserType) : An instance of PortalUserType
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mass_convert.portal_user_type import PortalUserType
		except Exception:
			from .portal_user_type import PortalUserType

		if portal_user_type is not None and not isinstance(portal_user_type, PortalUserType):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: portal_user_type EXPECTED TYPE: PortalUserType', None, None)
		
		self.__portal_user_type = portal_user_type
		self.__key_modified['portal_user_type'] = 1

	def get_ids(self):
		"""
		The method to get the ids

		Returns:
			list: An instance of list
		"""

		return self.__ids

	def set_ids(self, ids):
		"""
		The method to set the value to ids

		Parameters:
			ids (list) : An instance of list
		"""

		if ids is not None and not isinstance(ids, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ids EXPECTED TYPE: list', None, None)
		
		self.__ids = ids
		self.__key_modified['ids'] = 1

	def get_apply_assignment_threshold(self):
		"""
		The method to get the apply_assignment_threshold

		Returns:
			bool: A bool representing the apply_assignment_threshold
		"""

		return self.__apply_assignment_threshold

	def set_apply_assignment_threshold(self, apply_assignment_threshold):
		"""
		The method to set the value to apply_assignment_threshold

		Parameters:
			apply_assignment_threshold (bool) : A bool representing the apply_assignment_threshold
		"""

		if apply_assignment_threshold is not None and not isinstance(apply_assignment_threshold, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: apply_assignment_threshold EXPECTED TYPE: bool', None, None)
		
		self.__apply_assignment_threshold = apply_assignment_threshold
		self.__key_modified['apply_assignment_threshold'] = 1

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
