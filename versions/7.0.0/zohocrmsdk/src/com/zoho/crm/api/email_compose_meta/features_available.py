try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class FeaturesAvailable(object):
	def __init__(self):
		"""Creates an instance of FeaturesAvailable"""

		self.__zsurvey_enabled = None
		self.__inline_compose_window = None
		self.__schedule_mail = None
		self.__email_cloud_picker = None
		self.__form_integration_enabled = None
		self.__isprivacyenabled = None
		self.__auto_suggestion = None
		self.__unsubscribe_link = None
		self.__best_time_to_contact = None
		self.__attach_teamdrive = None
		self.__islivedeskenabled = None
		self.__subject_line_suggestion = None
		self.__email_preference = None
		self.__attachment = None
		self.__mandateunsublink = None
		self.__old_compose_revert = None
		self.__key_modified = dict()

	def get_zsurvey_enabled(self):
		"""
		The method to get the zsurvey_enabled

		Returns:
			Choice: An instance of Choice
		"""

		return self.__zsurvey_enabled

	def set_zsurvey_enabled(self, zsurvey_enabled):
		"""
		The method to set the value to zsurvey_enabled

		Parameters:
			zsurvey_enabled (Choice) : An instance of Choice
		"""

		if zsurvey_enabled is not None and not isinstance(zsurvey_enabled, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zsurvey_enabled EXPECTED TYPE: Choice', None, None)
		
		self.__zsurvey_enabled = zsurvey_enabled
		self.__key_modified['zsurvey_enabled'] = 1

	def get_inline_compose_window(self):
		"""
		The method to get the inline_compose_window

		Returns:
			Choice: An instance of Choice
		"""

		return self.__inline_compose_window

	def set_inline_compose_window(self, inline_compose_window):
		"""
		The method to set the value to inline_compose_window

		Parameters:
			inline_compose_window (Choice) : An instance of Choice
		"""

		if inline_compose_window is not None and not isinstance(inline_compose_window, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: inline_compose_window EXPECTED TYPE: Choice', None, None)
		
		self.__inline_compose_window = inline_compose_window
		self.__key_modified['inline_compose_window'] = 1

	def get_schedule_mail(self):
		"""
		The method to get the schedule_mail

		Returns:
			Choice: An instance of Choice
		"""

		return self.__schedule_mail

	def set_schedule_mail(self, schedule_mail):
		"""
		The method to set the value to schedule_mail

		Parameters:
			schedule_mail (Choice) : An instance of Choice
		"""

		if schedule_mail is not None and not isinstance(schedule_mail, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: schedule_mail EXPECTED TYPE: Choice', None, None)
		
		self.__schedule_mail = schedule_mail
		self.__key_modified['Schedule_Mail'] = 1

	def get_email_cloud_picker(self):
		"""
		The method to get the email_cloud_picker

		Returns:
			Choice: An instance of Choice
		"""

		return self.__email_cloud_picker

	def set_email_cloud_picker(self, email_cloud_picker):
		"""
		The method to set the value to email_cloud_picker

		Parameters:
			email_cloud_picker (Choice) : An instance of Choice
		"""

		if email_cloud_picker is not None and not isinstance(email_cloud_picker, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_cloud_picker EXPECTED TYPE: Choice', None, None)
		
		self.__email_cloud_picker = email_cloud_picker
		self.__key_modified['EMAIL_CLOUD_PICKER'] = 1

	def get_form_integration_enabled(self):
		"""
		The method to get the form_integration_enabled

		Returns:
			Choice: An instance of Choice
		"""

		return self.__form_integration_enabled

	def set_form_integration_enabled(self, form_integration_enabled):
		"""
		The method to set the value to form_integration_enabled

		Parameters:
			form_integration_enabled (Choice) : An instance of Choice
		"""

		if form_integration_enabled is not None and not isinstance(form_integration_enabled, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: form_integration_enabled EXPECTED TYPE: Choice', None, None)
		
		self.__form_integration_enabled = form_integration_enabled
		self.__key_modified['form_integration_enabled'] = 1

	def get_isprivacyenabled(self):
		"""
		The method to get the isprivacyenabled

		Returns:
			Choice: An instance of Choice
		"""

		return self.__isprivacyenabled

	def set_isprivacyenabled(self, isprivacyenabled):
		"""
		The method to set the value to isprivacyenabled

		Parameters:
			isprivacyenabled (Choice) : An instance of Choice
		"""

		if isprivacyenabled is not None and not isinstance(isprivacyenabled, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: isprivacyenabled EXPECTED TYPE: Choice', None, None)
		
		self.__isprivacyenabled = isprivacyenabled
		self.__key_modified['isPrivacyEnabled'] = 1

	def get_auto_suggestion(self):
		"""
		The method to get the auto_suggestion

		Returns:
			Choice: An instance of Choice
		"""

		return self.__auto_suggestion

	def set_auto_suggestion(self, auto_suggestion):
		"""
		The method to set the value to auto_suggestion

		Parameters:
			auto_suggestion (Choice) : An instance of Choice
		"""

		if auto_suggestion is not None and not isinstance(auto_suggestion, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: auto_suggestion EXPECTED TYPE: Choice', None, None)
		
		self.__auto_suggestion = auto_suggestion
		self.__key_modified['auto_suggestion'] = 1

	def get_unsubscribe_link(self):
		"""
		The method to get the unsubscribe_link

		Returns:
			Choice: An instance of Choice
		"""

		return self.__unsubscribe_link

	def set_unsubscribe_link(self, unsubscribe_link):
		"""
		The method to set the value to unsubscribe_link

		Parameters:
			unsubscribe_link (Choice) : An instance of Choice
		"""

		if unsubscribe_link is not None and not isinstance(unsubscribe_link, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: unsubscribe_link EXPECTED TYPE: Choice', None, None)
		
		self.__unsubscribe_link = unsubscribe_link
		self.__key_modified['UNSUBSCRIBE_LINK'] = 1

	def get_best_time_to_contact(self):
		"""
		The method to get the best_time_to_contact

		Returns:
			Choice: An instance of Choice
		"""

		return self.__best_time_to_contact

	def set_best_time_to_contact(self, best_time_to_contact):
		"""
		The method to set the value to best_time_to_contact

		Parameters:
			best_time_to_contact (Choice) : An instance of Choice
		"""

		if best_time_to_contact is not None and not isinstance(best_time_to_contact, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: best_time_to_contact EXPECTED TYPE: Choice', None, None)
		
		self.__best_time_to_contact = best_time_to_contact
		self.__key_modified['best_time_to_contact'] = 1

	def get_attach_teamdrive(self):
		"""
		The method to get the attach_teamdrive

		Returns:
			Choice: An instance of Choice
		"""

		return self.__attach_teamdrive

	def set_attach_teamdrive(self, attach_teamdrive):
		"""
		The method to set the value to attach_teamdrive

		Parameters:
			attach_teamdrive (Choice) : An instance of Choice
		"""

		if attach_teamdrive is not None and not isinstance(attach_teamdrive, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attach_teamdrive EXPECTED TYPE: Choice', None, None)
		
		self.__attach_teamdrive = attach_teamdrive
		self.__key_modified['attach_teamdrive'] = 1

	def get_islivedeskenabled(self):
		"""
		The method to get the islivedeskenabled

		Returns:
			Choice: An instance of Choice
		"""

		return self.__islivedeskenabled

	def set_islivedeskenabled(self, islivedeskenabled):
		"""
		The method to set the value to islivedeskenabled

		Parameters:
			islivedeskenabled (Choice) : An instance of Choice
		"""

		if islivedeskenabled is not None and not isinstance(islivedeskenabled, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: islivedeskenabled EXPECTED TYPE: Choice', None, None)
		
		self.__islivedeskenabled = islivedeskenabled
		self.__key_modified['isLiveDeskEnabled'] = 1

	def get_subject_line_suggestion(self):
		"""
		The method to get the subject_line_suggestion

		Returns:
			bool: A bool representing the subject_line_suggestion
		"""

		return self.__subject_line_suggestion

	def set_subject_line_suggestion(self, subject_line_suggestion):
		"""
		The method to set the value to subject_line_suggestion

		Parameters:
			subject_line_suggestion (bool) : A bool representing the subject_line_suggestion
		"""

		if subject_line_suggestion is not None and not isinstance(subject_line_suggestion, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subject_line_suggestion EXPECTED TYPE: bool', None, None)
		
		self.__subject_line_suggestion = subject_line_suggestion
		self.__key_modified['subject_line_suggestion'] = 1

	def get_email_preference(self):
		"""
		The method to get the email_preference

		Returns:
			bool: A bool representing the email_preference
		"""

		return self.__email_preference

	def set_email_preference(self, email_preference):
		"""
		The method to set the value to email_preference

		Parameters:
			email_preference (bool) : A bool representing the email_preference
		"""

		if email_preference is not None and not isinstance(email_preference, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_preference EXPECTED TYPE: bool', None, None)
		
		self.__email_preference = email_preference
		self.__key_modified['EMAIL_PREFERENCE'] = 1

	def get_attachment(self):
		"""
		The method to get the attachment

		Returns:
			bool: A bool representing the attachment
		"""

		return self.__attachment

	def set_attachment(self, attachment):
		"""
		The method to set the value to attachment

		Parameters:
			attachment (bool) : A bool representing the attachment
		"""

		if attachment is not None and not isinstance(attachment, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachment EXPECTED TYPE: bool', None, None)
		
		self.__attachment = attachment
		self.__key_modified['ATTACHMENT'] = 1

	def get_mandateunsublink(self):
		"""
		The method to get the mandateunsublink

		Returns:
			bool: A bool representing the mandateunsublink
		"""

		return self.__mandateunsublink

	def set_mandateunsublink(self, mandateunsublink):
		"""
		The method to set the value to mandateunsublink

		Parameters:
			mandateunsublink (bool) : A bool representing the mandateunsublink
		"""

		if mandateunsublink is not None and not isinstance(mandateunsublink, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mandateunsublink EXPECTED TYPE: bool', None, None)
		
		self.__mandateunsublink = mandateunsublink
		self.__key_modified['mandateUnsubLink'] = 1

	def get_old_compose_revert(self):
		"""
		The method to get the old_compose_revert

		Returns:
			bool: A bool representing the old_compose_revert
		"""

		return self.__old_compose_revert

	def set_old_compose_revert(self, old_compose_revert):
		"""
		The method to set the value to old_compose_revert

		Parameters:
			old_compose_revert (bool) : A bool representing the old_compose_revert
		"""

		if old_compose_revert is not None and not isinstance(old_compose_revert, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: old_compose_revert EXPECTED TYPE: bool', None, None)
		
		self.__old_compose_revert = old_compose_revert
		self.__key_modified['OLD_COMPOSE_REVERT'] = 1

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
