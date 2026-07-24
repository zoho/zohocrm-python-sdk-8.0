try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class MailMerge(object):
	def __init__(self):
		"""Creates an instance of MailMerge"""

		self.__mail_merge_template = None
		self.__from_address = None
		self.__to_address = None
		self.__cc_email = None
		self.__bcc_email = None
		self.__subject = None
		self.__message = None
		self.__type = None
		self.__attachment_name = None
		self.__key_modified = dict()

	def get_mail_merge_template(self):
		"""
		The method to get the mail_merge_template

		Returns:
			MailMergeTemplate: An instance of MailMergeTemplate
		"""

		return self.__mail_merge_template

	def set_mail_merge_template(self, mail_merge_template):
		"""
		The method to set the value to mail_merge_template

		Parameters:
			mail_merge_template (MailMergeTemplate) : An instance of MailMergeTemplate
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.mail_merge_template import MailMergeTemplate
		except Exception:
			from .mail_merge_template import MailMergeTemplate

		if mail_merge_template is not None and not isinstance(mail_merge_template, MailMergeTemplate):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mail_merge_template EXPECTED TYPE: MailMergeTemplate', None, None)
		
		self.__mail_merge_template = mail_merge_template
		self.__key_modified['mail_merge_template'] = 1

	def get_from_address(self):
		"""
		The method to get the from_address

		Returns:
			Address: An instance of Address
		"""

		return self.__from_address

	def set_from_address(self, from_address):
		"""
		The method to set the value to from_address

		Parameters:
			from_address (Address) : An instance of Address
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.address import Address
		except Exception:
			from .address import Address

		if from_address is not None and not isinstance(from_address, Address):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_address EXPECTED TYPE: Address', None, None)
		
		self.__from_address = from_address
		self.__key_modified['from_address'] = 1

	def get_to_address(self):
		"""
		The method to get the to_address

		Returns:
			list: An instance of list
		"""

		return self.__to_address

	def set_to_address(self, to_address):
		"""
		The method to set the value to to_address

		Parameters:
			to_address (list) : An instance of list
		"""

		if to_address is not None and not isinstance(to_address, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: to_address EXPECTED TYPE: list', None, None)
		
		self.__to_address = to_address
		self.__key_modified['to_address'] = 1

	def get_cc_email(self):
		"""
		The method to get the cc_email

		Returns:
			list: An instance of list
		"""

		return self.__cc_email

	def set_cc_email(self, cc_email):
		"""
		The method to set the value to cc_email

		Parameters:
			cc_email (list) : An instance of list
		"""

		if cc_email is not None and not isinstance(cc_email, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cc_email EXPECTED TYPE: list', None, None)
		
		self.__cc_email = cc_email
		self.__key_modified['cc_email'] = 1

	def get_bcc_email(self):
		"""
		The method to get the bcc_email

		Returns:
			list: An instance of list
		"""

		return self.__bcc_email

	def set_bcc_email(self, bcc_email):
		"""
		The method to set the value to bcc_email

		Parameters:
			bcc_email (list) : An instance of list
		"""

		if bcc_email is not None and not isinstance(bcc_email, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: bcc_email EXPECTED TYPE: list', None, None)
		
		self.__bcc_email = bcc_email
		self.__key_modified['bcc_email'] = 1

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

	def get_message(self):
		"""
		The method to get the message

		Returns:
			string: A string representing the message
		"""

		return self.__message

	def set_message(self, message):
		"""
		The method to set the value to message

		Parameters:
			message (string) : A string representing the message
		"""

		if message is not None and not isinstance(message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message EXPECTED TYPE: str', None, None)
		
		self.__message = message
		self.__key_modified['message'] = 1

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

	def get_attachment_name(self):
		"""
		The method to get the attachment_name

		Returns:
			string: A string representing the attachment_name
		"""

		return self.__attachment_name

	def set_attachment_name(self, attachment_name):
		"""
		The method to set the value to attachment_name

		Parameters:
			attachment_name (string) : A string representing the attachment_name
		"""

		if attachment_name is not None and not isinstance(attachment_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachment_name EXPECTED TYPE: str', None, None)
		
		self.__attachment_name = attachment_name
		self.__key_modified['attachment_name'] = 1

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
