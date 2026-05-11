try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class EmailDrafts(object):
	def __init__(self):
		"""Creates an instance of EmailDrafts"""

		self.__id = None
		self.__modified_time = None
		self.__created_time = None
		self.__from_1 = None
		self.__to = None
		self.__reply_to = None
		self.__cc = None
		self.__bcc = None
		self.__template = None
		self.__inventory_details = None
		self.__attachments = None
		self.__schedule_details = None
		self.__rich_text = None
		self.__email_opt_out = None
		self.__subject = None
		self.__content = None
		self.__summary = None
		self.__key_modified = dict()

	def get_id(self):
		"""
		The method to get the id

		Returns:
			string: A string representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (string) : A string representing the id
		"""

		if id is not None and not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_from(self):
		"""
		The method to get the from

		Returns:
			string: A string representing the from_1
		"""

		return self.__from_1

	def set_from(self, from_1):
		"""
		The method to set the value to from

		Parameters:
			from_1 (string) : A string representing the from_1
		"""

		if from_1 is not None and not isinstance(from_1, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_1 EXPECTED TYPE: str', None, None)
		
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

	def get_reply_to(self):
		"""
		The method to get the reply_to

		Returns:
			string: A string representing the reply_to
		"""

		return self.__reply_to

	def set_reply_to(self, reply_to):
		"""
		The method to set the value to reply_to

		Parameters:
			reply_to (string) : A string representing the reply_to
		"""

		if reply_to is not None and not isinstance(reply_to, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reply_to EXPECTED TYPE: str', None, None)
		
		self.__reply_to = reply_to
		self.__key_modified['reply_to'] = 1

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

	def get_template(self):
		"""
		The method to get the template

		Returns:
			Template: An instance of Template
		"""

		return self.__template

	def set_template(self, template):
		"""
		The method to set the value to template

		Parameters:
			template (Template) : An instance of Template
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_drafts.template import Template
		except Exception:
			from .template import Template

		if template is not None and not isinstance(template, Template):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: template EXPECTED TYPE: Template', None, None)
		
		self.__template = template
		self.__key_modified['template'] = 1

	def get_inventory_details(self):
		"""
		The method to get the inventory_details

		Returns:
			InventoryDetails: An instance of InventoryDetails
		"""

		return self.__inventory_details

	def set_inventory_details(self, inventory_details):
		"""
		The method to set the value to inventory_details

		Parameters:
			inventory_details (InventoryDetails) : An instance of InventoryDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_drafts.inventory_details import InventoryDetails
		except Exception:
			from .inventory_details import InventoryDetails

		if inventory_details is not None and not isinstance(inventory_details, InventoryDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: inventory_details EXPECTED TYPE: InventoryDetails', None, None)
		
		self.__inventory_details = inventory_details
		self.__key_modified['inventory_details'] = 1

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

	def get_schedule_details(self):
		"""
		The method to get the schedule_details

		Returns:
			ScheduleDetails: An instance of ScheduleDetails
		"""

		return self.__schedule_details

	def set_schedule_details(self, schedule_details):
		"""
		The method to set the value to schedule_details

		Parameters:
			schedule_details (ScheduleDetails) : An instance of ScheduleDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_drafts.schedule_details import ScheduleDetails
		except Exception:
			from .schedule_details import ScheduleDetails

		if schedule_details is not None and not isinstance(schedule_details, ScheduleDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: schedule_details EXPECTED TYPE: ScheduleDetails', None, None)
		
		self.__schedule_details = schedule_details
		self.__key_modified['schedule_details'] = 1

	def get_rich_text(self):
		"""
		The method to get the rich_text

		Returns:
			bool: A bool representing the rich_text
		"""

		return self.__rich_text

	def set_rich_text(self, rich_text):
		"""
		The method to set the value to rich_text

		Parameters:
			rich_text (bool) : A bool representing the rich_text
		"""

		if rich_text is not None and not isinstance(rich_text, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rich_text EXPECTED TYPE: bool', None, None)
		
		self.__rich_text = rich_text
		self.__key_modified['rich_text'] = 1

	def get_email_opt_out(self):
		"""
		The method to get the email_opt_out

		Returns:
			bool: A bool representing the email_opt_out
		"""

		return self.__email_opt_out

	def set_email_opt_out(self, email_opt_out):
		"""
		The method to set the value to email_opt_out

		Parameters:
			email_opt_out (bool) : A bool representing the email_opt_out
		"""

		if email_opt_out is not None and not isinstance(email_opt_out, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_opt_out EXPECTED TYPE: bool', None, None)
		
		self.__email_opt_out = email_opt_out
		self.__key_modified['email_opt_out'] = 1

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
