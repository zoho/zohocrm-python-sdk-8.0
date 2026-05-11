try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Email(object):
	def __init__(self):
		"""Creates an instance of Email"""

		self.__attachments = None
		self.__thread_id = None
		self.__cc = None
		self.__summary = None
		self.__owner = None
		self.__read = None
		self.__content = None
		self.__sent = None
		self.__subject = None
		self.__activity_info = None
		self.__intent = None
		self.__sentiment_info = None
		self.__message_id = None
		self.__source = None
		self.__linked_record = None
		self.__sent_time = None
		self.__emotion = None
		self.__from_1 = None
		self.__to = None
		self.__time = None
		self.__status = None
		self.__has_attachment = None
		self.__has_thread_attachment = None
		self.__editable = None
		self.__mail_format = None
		self.__reply_to = None
		self.__key_modified = dict()

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

	def get_thread_id(self):
		"""
		The method to get the thread_id

		Returns:
			string: A string representing the thread_id
		"""

		return self.__thread_id

	def set_thread_id(self, thread_id):
		"""
		The method to set the value to thread_id

		Parameters:
			thread_id (string) : A string representing the thread_id
		"""

		if thread_id is not None and not isinstance(thread_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: thread_id EXPECTED TYPE: str', None, None)
		
		self.__thread_id = thread_id
		self.__key_modified['thread_id'] = 1

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

	def get_summary(self):
		"""
		The method to get the summary

		Returns:
			string: A string representing the summary
		"""

		return self.__summary

	def set_summary(self, summary):
		"""
		The method to set the value to summary

		Parameters:
			summary (string) : A string representing the summary
		"""

		if summary is not None and not isinstance(summary, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: summary EXPECTED TYPE: str', None, None)
		
		self.__summary = summary
		self.__key_modified['summary'] = 1

	def get_owner(self):
		"""
		The method to get the owner

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__owner

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
		
		self.__owner = owner
		self.__key_modified['owner'] = 1

	def get_read(self):
		"""
		The method to get the read

		Returns:
			bool: A bool representing the read
		"""

		return self.__read

	def set_read(self, read):
		"""
		The method to set the value to read

		Parameters:
			read (bool) : A bool representing the read
		"""

		if read is not None and not isinstance(read, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: read EXPECTED TYPE: bool', None, None)
		
		self.__read = read
		self.__key_modified['read'] = 1

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

	def get_activity_info(self):
		"""
		The method to get the activity_info

		Returns:
			Object: A Object representing the activity_info
		"""

		return self.__activity_info

	def set_activity_info(self, activity_info):
		"""
		The method to set the value to activity_info

		Parameters:
			activity_info (Object) : A Object representing the activity_info
		"""

		self.__activity_info = activity_info
		self.__key_modified['activity_info'] = 1

	def get_intent(self):
		"""
		The method to get the intent

		Returns:
			Choice: An instance of Choice
		"""

		return self.__intent

	def set_intent(self, intent):
		"""
		The method to set the value to intent

		Parameters:
			intent (Choice) : An instance of Choice
		"""

		if intent is not None and not isinstance(intent, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: intent EXPECTED TYPE: Choice', None, None)
		
		self.__intent = intent
		self.__key_modified['intent'] = 1

	def get_sentiment_info(self):
		"""
		The method to get the sentiment_info

		Returns:
			Choice: An instance of Choice
		"""

		return self.__sentiment_info

	def set_sentiment_info(self, sentiment_info):
		"""
		The method to set the value to sentiment_info

		Parameters:
			sentiment_info (Choice) : An instance of Choice
		"""

		if sentiment_info is not None and not isinstance(sentiment_info, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sentiment_info EXPECTED TYPE: Choice', None, None)
		
		self.__sentiment_info = sentiment_info
		self.__key_modified['sentiment_info'] = 1

	def get_message_id(self):
		"""
		The method to get the message_id

		Returns:
			string: A string representing the message_id
		"""

		return self.__message_id

	def set_message_id(self, message_id):
		"""
		The method to set the value to message_id

		Parameters:
			message_id (string) : A string representing the message_id
		"""

		if message_id is not None and not isinstance(message_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message_id EXPECTED TYPE: str', None, None)
		
		self.__message_id = message_id
		self.__key_modified['message_id'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.email_related_records.linked_record import LinkedRecord
		except Exception:
			from .linked_record import LinkedRecord

		if linked_record is not None and not isinstance(linked_record, LinkedRecord):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: linked_record EXPECTED TYPE: LinkedRecord', None, None)
		
		self.__linked_record = linked_record
		self.__key_modified['linked_record'] = 1

	def get_sent_time(self):
		"""
		The method to get the sent_time

		Returns:
			string: A string representing the sent_time
		"""

		return self.__sent_time

	def set_sent_time(self, sent_time):
		"""
		The method to set the value to sent_time

		Parameters:
			sent_time (string) : A string representing the sent_time
		"""

		if sent_time is not None and not isinstance(sent_time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sent_time EXPECTED TYPE: str', None, None)
		
		self.__sent_time = sent_time
		self.__key_modified['sent_time'] = 1

	def get_emotion(self):
		"""
		The method to get the emotion

		Returns:
			string: A string representing the emotion
		"""

		return self.__emotion

	def set_emotion(self, emotion):
		"""
		The method to set the value to emotion

		Parameters:
			emotion (string) : A string representing the emotion
		"""

		if emotion is not None and not isinstance(emotion, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: emotion EXPECTED TYPE: str', None, None)
		
		self.__emotion = emotion
		self.__key_modified['emotion'] = 1

	def get_from(self):
		"""
		The method to get the from

		Returns:
			UserDetails: An instance of UserDetails
		"""

		return self.__from_1

	def set_from(self, from_1):
		"""
		The method to set the value to from

		Parameters:
			from_1 (UserDetails) : An instance of UserDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_related_records.user_details import UserDetails
		except Exception:
			from .user_details import UserDetails

		if from_1 is not None and not isinstance(from_1, UserDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_1 EXPECTED TYPE: UserDetails', None, None)
		
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

	def get_time(self):
		"""
		The method to get the time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__time

	def set_time(self, time):
		"""
		The method to set the value to time

		Parameters:
			time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if time is not None and not isinstance(time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: time EXPECTED TYPE: datetime', None, None)
		
		self.__time = time
		self.__key_modified['time'] = 1

	def get_status(self):
		"""
		The method to get the status

		Returns:
			list: An instance of list
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (list) : An instance of list
		"""

		if status is not None and not isinstance(status, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: list', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def get_has_attachment(self):
		"""
		The method to get the has_attachment

		Returns:
			bool: A bool representing the has_attachment
		"""

		return self.__has_attachment

	def set_has_attachment(self, has_attachment):
		"""
		The method to set the value to has_attachment

		Parameters:
			has_attachment (bool) : A bool representing the has_attachment
		"""

		if has_attachment is not None and not isinstance(has_attachment, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: has_attachment EXPECTED TYPE: bool', None, None)
		
		self.__has_attachment = has_attachment
		self.__key_modified['has_attachment'] = 1

	def get_has_thread_attachment(self):
		"""
		The method to get the has_thread_attachment

		Returns:
			bool: A bool representing the has_thread_attachment
		"""

		return self.__has_thread_attachment

	def set_has_thread_attachment(self, has_thread_attachment):
		"""
		The method to set the value to has_thread_attachment

		Parameters:
			has_thread_attachment (bool) : A bool representing the has_thread_attachment
		"""

		if has_thread_attachment is not None and not isinstance(has_thread_attachment, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: has_thread_attachment EXPECTED TYPE: bool', None, None)
		
		self.__has_thread_attachment = has_thread_attachment
		self.__key_modified['has_thread_attachment'] = 1

	def get_editable(self):
		"""
		The method to get the editable

		Returns:
			bool: A bool representing the editable
		"""

		return self.__editable

	def set_editable(self, editable):
		"""
		The method to set the value to editable

		Parameters:
			editable (bool) : A bool representing the editable
		"""

		if editable is not None and not isinstance(editable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editable EXPECTED TYPE: bool', None, None)
		
		self.__editable = editable
		self.__key_modified['editable'] = 1

	def get_mail_format(self):
		"""
		The method to get the mail_format

		Returns:
			string: A string representing the mail_format
		"""

		return self.__mail_format

	def set_mail_format(self, mail_format):
		"""
		The method to set the value to mail_format

		Parameters:
			mail_format (string) : A string representing the mail_format
		"""

		if mail_format is not None and not isinstance(mail_format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mail_format EXPECTED TYPE: str', None, None)
		
		self.__mail_format = mail_format
		self.__key_modified['mail_format'] = 1

	def get_reply_to(self):
		"""
		The method to get the reply_to

		Returns:
			UserDetails: An instance of UserDetails
		"""

		return self.__reply_to

	def set_reply_to(self, reply_to):
		"""
		The method to set the value to reply_to

		Parameters:
			reply_to (UserDetails) : An instance of UserDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_related_records.user_details import UserDetails
		except Exception:
			from .user_details import UserDetails

		if reply_to is not None and not isinstance(reply_to, UserDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reply_to EXPECTED TYPE: UserDetails', None, None)
		
		self.__reply_to = reply_to
		self.__key_modified['reply_to'] = 1

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
