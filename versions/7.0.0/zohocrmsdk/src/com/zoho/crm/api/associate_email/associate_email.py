try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class AssociateEmail(object):
	def __init__(self):
		"""Creates an instance of AssociateEmail"""

		self.__from_1 = None
		self.__to = None
		self.__cc = None
		self.__bcc = None
		self.__attachments = None
		self.__content = None
		self.__mail_format = None
		self.__subject = None
		self.__original_message_id = None
		self.__sent = None
		self.__date_time = None
		self.__linked_record = None
		self.__key_modified = dict()

	def get_from(self):
		"""
		The method to get the from

		Returns:
			From: An instance of From
		"""

		return self.__from_1

	def set_from(self, from_1):
		"""
		The method to set the value to from

		Parameters:
			from_1 (From) : An instance of From
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.associate_email.from1 import From
		except Exception:
			from .from1 import From

		if from_1 is not None and not isinstance(from_1, From):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_1 EXPECTED TYPE: From', None, None)
		
		self.__from_1 = from_1
		self.__key_modified['from'] = 1

	def get_to(self):
		"""
		The method to get the to

		Returns:
			list: An instance of list
		"""

		return self.__to

	def set_to(self, to):
		"""
		The method to set the value to to

		Parameters:
			to (list) : An instance of list
		"""

		if to is not None and not isinstance(to, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: to EXPECTED TYPE: list', None, None)
		
		self.__to = to
		self.__key_modified['to'] = 1

	def get_cc(self):
		"""
		The method to get the cc

		Returns:
			list: An instance of list
		"""

		return self.__cc

	def set_cc(self, cc):
		"""
		The method to set the value to cc

		Parameters:
			cc (list) : An instance of list
		"""

		if cc is not None and not isinstance(cc, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cc EXPECTED TYPE: list', None, None)
		
		self.__cc = cc
		self.__key_modified['cc'] = 1

	def get_bcc(self):
		"""
		The method to get the bcc

		Returns:
			list: An instance of list
		"""

		return self.__bcc

	def set_bcc(self, bcc):
		"""
		The method to set the value to bcc

		Parameters:
			bcc (list) : An instance of list
		"""

		if bcc is not None and not isinstance(bcc, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: bcc EXPECTED TYPE: list', None, None)
		
		self.__bcc = bcc
		self.__key_modified['bcc'] = 1

	def get_attachments(self):
		"""
		The method to get the attachments

		Returns:
			list: An instance of list
		"""

		return self.__attachments

	def set_attachments(self, attachments):
		"""
		The method to set the value to attachments

		Parameters:
			attachments (list) : An instance of list
		"""

		if attachments is not None and not isinstance(attachments, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachments EXPECTED TYPE: list', None, None)
		
		self.__attachments = attachments
		self.__key_modified['attachments'] = 1

	def get_content(self):
		"""
		The method to get the content

		Returns:
			string: A string representing the content
		"""

		return self.__content

	def set_content(self, content):
		"""
		The method to set the value to content

		Parameters:
			content (string) : A string representing the content
		"""

		if content is not None and not isinstance(content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: content EXPECTED TYPE: str', None, None)
		
		self.__content = content
		self.__key_modified['content'] = 1

	def get_mail_format(self):
		"""
		The method to get the mail_format

		Returns:
			Choice: An instance of Choice
		"""

		return self.__mail_format

	def set_mail_format(self, mail_format):
		"""
		The method to set the value to mail_format

		Parameters:
			mail_format (Choice) : An instance of Choice
		"""

		if mail_format is not None and not isinstance(mail_format, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mail_format EXPECTED TYPE: Choice', None, None)
		
		self.__mail_format = mail_format
		self.__key_modified['mail_format'] = 1

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

	def get_original_message_id(self):
		"""
		The method to get the original_message_id

		Returns:
			string: A string representing the original_message_id
		"""

		return self.__original_message_id

	def set_original_message_id(self, original_message_id):
		"""
		The method to set the value to original_message_id

		Parameters:
			original_message_id (string) : A string representing the original_message_id
		"""

		if original_message_id is not None and not isinstance(original_message_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: original_message_id EXPECTED TYPE: str', None, None)
		
		self.__original_message_id = original_message_id
		self.__key_modified['original_message_id'] = 1

	def get_sent(self):
		"""
		The method to get the sent

		Returns:
			bool: A bool representing the sent
		"""

		return self.__sent

	def set_sent(self, sent):
		"""
		The method to set the value to sent

		Parameters:
			sent (bool) : A bool representing the sent
		"""

		if sent is not None and not isinstance(sent, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sent EXPECTED TYPE: bool', None, None)
		
		self.__sent = sent
		self.__key_modified['sent'] = 1

	def get_date_time(self):
		"""
		The method to get the date_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__date_time

	def set_date_time(self, date_time):
		"""
		The method to set the value to date_time

		Parameters:
			date_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if date_time is not None and not isinstance(date_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: date_time EXPECTED TYPE: datetime', None, None)
		
		self.__date_time = date_time
		self.__key_modified['date_time'] = 1

	def get_linked_record(self):
		"""
		The method to get the linked_record

		Returns:
			LinkedRecord: An instance of LinkedRecord
		"""

		return self.__linked_record

	def set_linked_record(self, linked_record):
		"""
		The method to set the value to linked_record

		Parameters:
			linked_record (LinkedRecord) : An instance of LinkedRecord
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.associate_email.linked_record import LinkedRecord
		except Exception:
			from .linked_record import LinkedRecord

		if linked_record is not None and not isinstance(linked_record, LinkedRecord):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: linked_record EXPECTED TYPE: LinkedRecord', None, None)
		
		self.__linked_record = linked_record
		self.__key_modified['linked_record'] = 1

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
