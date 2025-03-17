try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class WebForm(object):
	def __init__(self):
		"""Creates an instance of WebForm"""

		self.__google_site = None
		self.__encrypted_form_id = None
		self.__owner = None
		self.__user_type = None
		self.__acknowledge_visitor = None
		self.__button_attributes = None
		self.__encrypted_zgid = None
		self.__created_time = None
		self.__analytics_data = None
		self.__module = None
		self.__encrypted_module = None
		self.__active = None
		self.__adword_enabled = None
		self.__notify_owner = None
		self.__created_by = None
		self.__form_attributes = None
		self.__location_url = None
		self.__landing_url = None
		self.__double_optin_enabled = None
		self.__layout = None
		self.__tags = None
		self.__approval_request = None
		self.__type = None
		self.__create_contact = None
		self.__assignment_rule = None
		self.__name = None
		self.__id = None
		self.__spam_control = None
		self.__fields = None
		self.__form_fields = None
		self.__abtesting = None
		self.__visitor_tracking = None
		self.__last_submitted_time = None
		self.__action_on_submit = None
		self.__action_value = None
		self.__suggestion = None
		self.__embed_code = None
		self.__code_formats = None
		self.__source_code = None
		self.__iframe_code = None
		self.__key_modified = dict()

	def get_google_site(self):
		"""
		The method to get the google_site

		Returns:
			string: A string representing the google_site
		"""

		return self.__google_site

	def set_google_site(self, google_site):
		"""
		The method to set the value to google_site

		Parameters:
			google_site (string) : A string representing the google_site
		"""

		if google_site is not None and not isinstance(google_site, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: google_site EXPECTED TYPE: str', None, None)
		
		self.__google_site = google_site
		self.__key_modified['google_site'] = 1

	def get_encrypted_form_id(self):
		"""
		The method to get the encrypted_form_id

		Returns:
			string: A string representing the encrypted_form_id
		"""

		return self.__encrypted_form_id

	def set_encrypted_form_id(self, encrypted_form_id):
		"""
		The method to set the value to encrypted_form_id

		Parameters:
			encrypted_form_id (string) : A string representing the encrypted_form_id
		"""

		if encrypted_form_id is not None and not isinstance(encrypted_form_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: encrypted_form_id EXPECTED TYPE: str', None, None)
		
		self.__encrypted_form_id = encrypted_form_id
		self.__key_modified['encrypted_form_id'] = 1

	def get_owner(self):
		"""
		The method to get the owner

		Returns:
			Owner: An instance of Owner
		"""

		return self.__owner

	def set_owner(self, owner):
		"""
		The method to set the value to owner

		Parameters:
			owner (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.owner import Owner
		except Exception:
			from .owner import Owner

		if owner is not None and not isinstance(owner, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: owner EXPECTED TYPE: Owner', None, None)
		
		self.__owner = owner
		self.__key_modified['owner'] = 1

	def get_user_type(self):
		"""
		The method to get the user_type

		Returns:
			User: An instance of User
		"""

		return self.__user_type

	def set_user_type(self, user_type):
		"""
		The method to set the value to user_type

		Parameters:
			user_type (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.user import User
		except Exception:
			from .user import User

		if user_type is not None and not isinstance(user_type, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_type EXPECTED TYPE: User', None, None)
		
		self.__user_type = user_type
		self.__key_modified['user_type'] = 1

	def get_acknowledge_visitor(self):
		"""
		The method to get the acknowledge_visitor

		Returns:
			AcknowledgeVisitors: An instance of AcknowledgeVisitors
		"""

		return self.__acknowledge_visitor

	def set_acknowledge_visitor(self, acknowledge_visitor):
		"""
		The method to set the value to acknowledge_visitor

		Parameters:
			acknowledge_visitor (AcknowledgeVisitors) : An instance of AcknowledgeVisitors
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.acknowledge_visitors import AcknowledgeVisitors
		except Exception:
			from .acknowledge_visitors import AcknowledgeVisitors

		if acknowledge_visitor is not None and not isinstance(acknowledge_visitor, AcknowledgeVisitors):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: acknowledge_visitor EXPECTED TYPE: AcknowledgeVisitors', None, None)
		
		self.__acknowledge_visitor = acknowledge_visitor
		self.__key_modified['acknowledge_visitor'] = 1

	def get_button_attributes(self):
		"""
		The method to get the button_attributes

		Returns:
			list: An instance of list
		"""

		return self.__button_attributes

	def set_button_attributes(self, button_attributes):
		"""
		The method to set the value to button_attributes

		Parameters:
			button_attributes (list) : An instance of list
		"""

		if button_attributes is not None and not isinstance(button_attributes, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: button_attributes EXPECTED TYPE: list', None, None)
		
		self.__button_attributes = button_attributes
		self.__key_modified['button_attributes'] = 1

	def get_encrypted_zgid(self):
		"""
		The method to get the encrypted_zgid

		Returns:
			string: A string representing the encrypted_zgid
		"""

		return self.__encrypted_zgid

	def set_encrypted_zgid(self, encrypted_zgid):
		"""
		The method to set the value to encrypted_zgid

		Parameters:
			encrypted_zgid (string) : A string representing the encrypted_zgid
		"""

		if encrypted_zgid is not None and not isinstance(encrypted_zgid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: encrypted_zgid EXPECTED TYPE: str', None, None)
		
		self.__encrypted_zgid = encrypted_zgid
		self.__key_modified['encrypted_zgid'] = 1

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

	def get_analytics_data(self):
		"""
		The method to get the analytics_data

		Returns:
			AnalyticsData: An instance of AnalyticsData
		"""

		return self.__analytics_data

	def set_analytics_data(self, analytics_data):
		"""
		The method to set the value to analytics_data

		Parameters:
			analytics_data (AnalyticsData) : An instance of AnalyticsData
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.analytics_data import AnalyticsData
		except Exception:
			from .analytics_data import AnalyticsData

		if analytics_data is not None and not isinstance(analytics_data, AnalyticsData):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: analytics_data EXPECTED TYPE: AnalyticsData', None, None)
		
		self.__analytics_data = analytics_data
		self.__key_modified['analytics_data'] = 1

	def get_module(self):
		"""
		The method to get the module

		Returns:
			Module: An instance of Module
		"""

		return self.__module

	def set_module(self, module):
		"""
		The method to set the value to module

		Parameters:
			module (Module) : An instance of Module
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

	def get_encrypted_module(self):
		"""
		The method to get the encrypted_module

		Returns:
			string: A string representing the encrypted_module
		"""

		return self.__encrypted_module

	def set_encrypted_module(self, encrypted_module):
		"""
		The method to set the value to encrypted_module

		Parameters:
			encrypted_module (string) : A string representing the encrypted_module
		"""

		if encrypted_module is not None and not isinstance(encrypted_module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: encrypted_module EXPECTED TYPE: str', None, None)
		
		self.__encrypted_module = encrypted_module
		self.__key_modified['encrypted_module'] = 1

	def get_active(self):
		"""
		The method to get the active

		Returns:
			bool: A bool representing the active
		"""

		return self.__active

	def set_active(self, active):
		"""
		The method to set the value to active

		Parameters:
			active (bool) : A bool representing the active
		"""

		if active is not None and not isinstance(active, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: active EXPECTED TYPE: bool', None, None)
		
		self.__active = active
		self.__key_modified['active'] = 1

	def get_adword_enabled(self):
		"""
		The method to get the adword_enabled

		Returns:
			bool: A bool representing the adword_enabled
		"""

		return self.__adword_enabled

	def set_adword_enabled(self, adword_enabled):
		"""
		The method to set the value to adword_enabled

		Parameters:
			adword_enabled (bool) : A bool representing the adword_enabled
		"""

		if adword_enabled is not None and not isinstance(adword_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: adword_enabled EXPECTED TYPE: bool', None, None)
		
		self.__adword_enabled = adword_enabled
		self.__key_modified['adword_enabled'] = 1

	def get_notify_owner(self):
		"""
		The method to get the notify_owner

		Returns:
			Owner: An instance of Owner
		"""

		return self.__notify_owner

	def set_notify_owner(self, notify_owner):
		"""
		The method to set the value to notify_owner

		Parameters:
			notify_owner (Owner) : An instance of Owner
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.owner import Owner
		except Exception:
			from .owner import Owner

		if notify_owner is not None and not isinstance(notify_owner, Owner):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: notify_owner EXPECTED TYPE: Owner', None, None)
		
		self.__notify_owner = notify_owner
		self.__key_modified['notify_owner'] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			User: An instance of User
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.user import User
		except Exception:
			from .user import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_form_attributes(self):
		"""
		The method to get the form_attributes

		Returns:
			FormAttributes: An instance of FormAttributes
		"""

		return self.__form_attributes

	def set_form_attributes(self, form_attributes):
		"""
		The method to set the value to form_attributes

		Parameters:
			form_attributes (FormAttributes) : An instance of FormAttributes
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.form_attributes import FormAttributes
		except Exception:
			from .form_attributes import FormAttributes

		if form_attributes is not None and not isinstance(form_attributes, FormAttributes):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: form_attributes EXPECTED TYPE: FormAttributes', None, None)
		
		self.__form_attributes = form_attributes
		self.__key_modified['form_attributes'] = 1

	def get_location_url(self):
		"""
		The method to get the location_url

		Returns:
			list: An instance of list
		"""

		return self.__location_url

	def set_location_url(self, location_url):
		"""
		The method to set the value to location_url

		Parameters:
			location_url (list) : An instance of list
		"""

		if location_url is not None and not isinstance(location_url, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: location_url EXPECTED TYPE: list', None, None)
		
		self.__location_url = location_url
		self.__key_modified['location_url'] = 1

	def get_landing_url(self):
		"""
		The method to get the landing_url

		Returns:
			string: A string representing the landing_url
		"""

		return self.__landing_url

	def set_landing_url(self, landing_url):
		"""
		The method to set the value to landing_url

		Parameters:
			landing_url (string) : A string representing the landing_url
		"""

		if landing_url is not None and not isinstance(landing_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: landing_url EXPECTED TYPE: str', None, None)
		
		self.__landing_url = landing_url
		self.__key_modified['landing_url'] = 1

	def get_double_optin_enabled(self):
		"""
		The method to get the double_optin_enabled

		Returns:
			bool: A bool representing the double_optin_enabled
		"""

		return self.__double_optin_enabled

	def set_double_optin_enabled(self, double_optin_enabled):
		"""
		The method to set the value to double_optin_enabled

		Parameters:
			double_optin_enabled (bool) : A bool representing the double_optin_enabled
		"""

		if double_optin_enabled is not None and not isinstance(double_optin_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: double_optin_enabled EXPECTED TYPE: bool', None, None)
		
		self.__double_optin_enabled = double_optin_enabled
		self.__key_modified['double_optin_enabled'] = 1

	def get_layout(self):
		"""
		The method to get the layout

		Returns:
			Layout: An instance of Layout
		"""

		return self.__layout

	def set_layout(self, layout):
		"""
		The method to set the value to layout

		Parameters:
			layout (Layout) : An instance of Layout
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.layout import Layout
		except Exception:
			from .layout import Layout

		if layout is not None and not isinstance(layout, Layout):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout EXPECTED TYPE: Layout', None, None)
		
		self.__layout = layout
		self.__key_modified['layout'] = 1

	def get_tags(self):
		"""
		The method to get the tags

		Returns:
			list: An instance of list
		"""

		return self.__tags

	def set_tags(self, tags):
		"""
		The method to set the value to tags

		Parameters:
			tags (list) : An instance of list
		"""

		if tags is not None and not isinstance(tags, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tags EXPECTED TYPE: list', None, None)
		
		self.__tags = tags
		self.__key_modified['tags'] = 1

	def get_approval_request(self):
		"""
		The method to get the approval_request

		Returns:
			bool: A bool representing the approval_request
		"""

		return self.__approval_request

	def set_approval_request(self, approval_request):
		"""
		The method to set the value to approval_request

		Parameters:
			approval_request (bool) : A bool representing the approval_request
		"""

		if approval_request is not None and not isinstance(approval_request, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: approval_request EXPECTED TYPE: bool', None, None)
		
		self.__approval_request = approval_request
		self.__key_modified['approval_request'] = 1

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

	def get_create_contact(self):
		"""
		The method to get the create_contact

		Returns:
			bool: A bool representing the create_contact
		"""

		return self.__create_contact

	def set_create_contact(self, create_contact):
		"""
		The method to set the value to create_contact

		Parameters:
			create_contact (bool) : A bool representing the create_contact
		"""

		if create_contact is not None and not isinstance(create_contact, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: create_contact EXPECTED TYPE: bool', None, None)
		
		self.__create_contact = create_contact
		self.__key_modified['create_contact'] = 1

	def get_assignment_rule(self):
		"""
		The method to get the assignment_rule

		Returns:
			AssignmentRule: An instance of AssignmentRule
		"""

		return self.__assignment_rule

	def set_assignment_rule(self, assignment_rule):
		"""
		The method to set the value to assignment_rule

		Parameters:
			assignment_rule (AssignmentRule) : An instance of AssignmentRule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.assignment_rule import AssignmentRule
		except Exception:
			from .assignment_rule import AssignmentRule

		if assignment_rule is not None and not isinstance(assignment_rule, AssignmentRule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: assignment_rule EXPECTED TYPE: AssignmentRule', None, None)
		
		self.__assignment_rule = assignment_rule
		self.__key_modified['assignment_rule'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_spam_control(self):
		"""
		The method to get the spam_control

		Returns:
			SpamControll: An instance of SpamControll
		"""

		return self.__spam_control

	def set_spam_control(self, spam_control):
		"""
		The method to set the value to spam_control

		Parameters:
			spam_control (SpamControll) : An instance of SpamControll
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.spam_controll import SpamControll
		except Exception:
			from .spam_controll import SpamControll

		if spam_control is not None and not isinstance(spam_control, SpamControll):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: spam_control EXPECTED TYPE: SpamControll', None, None)
		
		self.__spam_control = spam_control
		self.__key_modified['spam_control'] = 1

	def get_fields(self):
		"""
		The method to get the fields

		Returns:
			list: An instance of list
		"""

		return self.__fields

	def set_fields(self, fields):
		"""
		The method to set the value to fields

		Parameters:
			fields (list) : An instance of list
		"""

		if fields is not None and not isinstance(fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: list', None, None)
		
		self.__fields = fields
		self.__key_modified['fields'] = 1

	def get_form_fields(self):
		"""
		The method to get the form_fields

		Returns:
			list: An instance of list
		"""

		return self.__form_fields

	def set_form_fields(self, form_fields):
		"""
		The method to set the value to form_fields

		Parameters:
			form_fields (list) : An instance of list
		"""

		if form_fields is not None and not isinstance(form_fields, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: form_fields EXPECTED TYPE: list', None, None)
		
		self.__form_fields = form_fields
		self.__key_modified['form_fields'] = 1

	def get_abtesting(self):
		"""
		The method to get the abtesting

		Returns:
			list: An instance of list
		"""

		return self.__abtesting

	def set_abtesting(self, abtesting):
		"""
		The method to set the value to abtesting

		Parameters:
			abtesting (list) : An instance of list
		"""

		if abtesting is not None and not isinstance(abtesting, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: abtesting EXPECTED TYPE: list', None, None)
		
		self.__abtesting = abtesting
		self.__key_modified['abtesting'] = 1

	def get_visitor_tracking(self):
		"""
		The method to get the visitor_tracking

		Returns:
			string: A string representing the visitor_tracking
		"""

		return self.__visitor_tracking

	def set_visitor_tracking(self, visitor_tracking):
		"""
		The method to set the value to visitor_tracking

		Parameters:
			visitor_tracking (string) : A string representing the visitor_tracking
		"""

		if visitor_tracking is not None and not isinstance(visitor_tracking, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: visitor_tracking EXPECTED TYPE: str', None, None)
		
		self.__visitor_tracking = visitor_tracking
		self.__key_modified['visitor_tracking'] = 1

	def get_last_submitted_time(self):
		"""
		The method to get the last_submitted_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__last_submitted_time

	def set_last_submitted_time(self, last_submitted_time):
		"""
		The method to set the value to last_submitted_time

		Parameters:
			last_submitted_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if last_submitted_time is not None and not isinstance(last_submitted_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_submitted_time EXPECTED TYPE: datetime', None, None)
		
		self.__last_submitted_time = last_submitted_time
		self.__key_modified['last_submitted_time'] = 1

	def get_action_on_submit(self):
		"""
		The method to get the action_on_submit

		Returns:
			string: A string representing the action_on_submit
		"""

		return self.__action_on_submit

	def set_action_on_submit(self, action_on_submit):
		"""
		The method to set the value to action_on_submit

		Parameters:
			action_on_submit (string) : A string representing the action_on_submit
		"""

		if action_on_submit is not None and not isinstance(action_on_submit, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action_on_submit EXPECTED TYPE: str', None, None)
		
		self.__action_on_submit = action_on_submit
		self.__key_modified['action_on_submit'] = 1

	def get_action_value(self):
		"""
		The method to get the action_value

		Returns:
			string: A string representing the action_value
		"""

		return self.__action_value

	def set_action_value(self, action_value):
		"""
		The method to set the value to action_value

		Parameters:
			action_value (string) : A string representing the action_value
		"""

		if action_value is not None and not isinstance(action_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: action_value EXPECTED TYPE: str', None, None)
		
		self.__action_value = action_value
		self.__key_modified['action_value'] = 1

	def get_suggestion(self):
		"""
		The method to get the suggestion

		Returns:
			Suggestion: An instance of Suggestion
		"""

		return self.__suggestion

	def set_suggestion(self, suggestion):
		"""
		The method to set the value to suggestion

		Parameters:
			suggestion (Suggestion) : An instance of Suggestion
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.suggestion import Suggestion
		except Exception:
			from .suggestion import Suggestion

		if suggestion is not None and not isinstance(suggestion, Suggestion):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: suggestion EXPECTED TYPE: Suggestion', None, None)
		
		self.__suggestion = suggestion
		self.__key_modified['suggestion'] = 1

	def get_embed_code(self):
		"""
		The method to get the embed_code

		Returns:
			string: A string representing the embed_code
		"""

		return self.__embed_code

	def set_embed_code(self, embed_code):
		"""
		The method to set the value to embed_code

		Parameters:
			embed_code (string) : A string representing the embed_code
		"""

		if embed_code is not None and not isinstance(embed_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: embed_code EXPECTED TYPE: str', None, None)
		
		self.__embed_code = embed_code
		self.__key_modified['embed_code'] = 1

	def get_code_formats(self):
		"""
		The method to get the code_formats

		Returns:
			list: An instance of list
		"""

		return self.__code_formats

	def set_code_formats(self, code_formats):
		"""
		The method to set the value to code_formats

		Parameters:
			code_formats (list) : An instance of list
		"""

		if code_formats is not None and not isinstance(code_formats, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: code_formats EXPECTED TYPE: list', None, None)
		
		self.__code_formats = code_formats
		self.__key_modified['code_formats'] = 1

	def get_source_code(self):
		"""
		The method to get the source_code

		Returns:
			string: A string representing the source_code
		"""

		return self.__source_code

	def set_source_code(self, source_code):
		"""
		The method to set the value to source_code

		Parameters:
			source_code (string) : A string representing the source_code
		"""

		if source_code is not None and not isinstance(source_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: source_code EXPECTED TYPE: str', None, None)
		
		self.__source_code = source_code
		self.__key_modified['source_code'] = 1

	def get_iframe_code(self):
		"""
		The method to get the iframe_code

		Returns:
			string: A string representing the iframe_code
		"""

		return self.__iframe_code

	def set_iframe_code(self, iframe_code):
		"""
		The method to set the value to iframe_code

		Parameters:
			iframe_code (string) : A string representing the iframe_code
		"""

		if iframe_code is not None and not isinstance(iframe_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: iframe_code EXPECTED TYPE: str', None, None)
		
		self.__iframe_code = iframe_code
		self.__key_modified['iframe_code'] = 1

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
