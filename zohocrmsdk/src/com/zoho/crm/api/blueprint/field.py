try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Field(object):
	def __init__(self):
		"""Creates an instance of Field"""

		self.__external = None
		self.__display_type = None
		self.__filterable = None
		self.__pick_list_values_sorted_lexically = None
		self.__sortable = None
		self.__ui_type = None
		self.__private = None
		self.__system_mandatory = None
		self.__webhook = None
		self.__json_type = None
		self.__crypt = None
		self.__field_label = None
		self.__tooltip = None
		self.__created_source = None
		self.__layouts = None
		self.__field_read_only = None
		self.__content = None
		self.__display_label = None
		self.__validation_rule = None
		self.__read_only = None
		self.__association_details = None
		self.__multi_module_lookup = None
		self.__currency = None
		self.__id = None
		self.__custom_field = None
		self.__lookup = None
		self.__convert_mapping = None
		self.__visible = None
		self.__length = None
		self.__column_name = None
		self.__type = None
		self.__view_type = None
		self.__transition_sequence = None
		self.__api_name = None
		self.__unique = None
		self.__history_tracking = None
		self.__data_type = None
		self.__formula = None
		self.__decimal_place = None
		self.__multiselectlookup = None
		self.__pick_list_values = None
		self.__auto_number = None
		self.__personality_name = None
		self.__mandatory = None
		self.__quick_sequence_number = None
		self.__profiles = None
		self.__key_modified = dict()

	def get_external(self):
		"""
		The method to get the external

		Returns:
			External: An instance of External
		"""

		return self.__external

	def set_external(self, external):
		"""
		The method to set the value to external

		Parameters:
			external (External) : An instance of External
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import External
		except Exception:
			from ..fields import External

		if external is not None and not isinstance(external, External):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external EXPECTED TYPE: External', None, None)
		
		self.__external = external
		self.__key_modified['external'] = 1

	def get_display_type(self):
		"""
		The method to get the display_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__display_type

	def set_display_type(self, display_type):
		"""
		The method to set the value to display_type

		Parameters:
			display_type (Choice) : An instance of Choice
		"""

		if display_type is not None and not isinstance(display_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_type EXPECTED TYPE: Choice', None, None)
		
		self.__display_type = display_type
		self.__key_modified['display_type'] = 1

	def get_filterable(self):
		"""
		The method to get the filterable

		Returns:
			bool: A bool representing the filterable
		"""

		return self.__filterable

	def set_filterable(self, filterable):
		"""
		The method to set the value to filterable

		Parameters:
			filterable (bool) : A bool representing the filterable
		"""

		if filterable is not None and not isinstance(filterable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: filterable EXPECTED TYPE: bool', None, None)
		
		self.__filterable = filterable
		self.__key_modified['filterable'] = 1

	def get_pick_list_values_sorted_lexically(self):
		"""
		The method to get the pick_list_values_sorted_lexically

		Returns:
			bool: A bool representing the pick_list_values_sorted_lexically
		"""

		return self.__pick_list_values_sorted_lexically

	def set_pick_list_values_sorted_lexically(self, pick_list_values_sorted_lexically):
		"""
		The method to set the value to pick_list_values_sorted_lexically

		Parameters:
			pick_list_values_sorted_lexically (bool) : A bool representing the pick_list_values_sorted_lexically
		"""

		if pick_list_values_sorted_lexically is not None and not isinstance(pick_list_values_sorted_lexically, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pick_list_values_sorted_lexically EXPECTED TYPE: bool', None, None)
		
		self.__pick_list_values_sorted_lexically = pick_list_values_sorted_lexically
		self.__key_modified['pick_list_values_sorted_lexically'] = 1

	def get_sortable(self):
		"""
		The method to get the sortable

		Returns:
			bool: A bool representing the sortable
		"""

		return self.__sortable

	def set_sortable(self, sortable):
		"""
		The method to set the value to sortable

		Parameters:
			sortable (bool) : A bool representing the sortable
		"""

		if sortable is not None and not isinstance(sortable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sortable EXPECTED TYPE: bool', None, None)
		
		self.__sortable = sortable
		self.__key_modified['sortable'] = 1

	def get_ui_type(self):
		"""
		The method to get the ui_type

		Returns:
			int: An int representing the ui_type
		"""

		return self.__ui_type

	def set_ui_type(self, ui_type):
		"""
		The method to set the value to ui_type

		Parameters:
			ui_type (int) : An int representing the ui_type
		"""

		if ui_type is not None and not isinstance(ui_type, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: ui_type EXPECTED TYPE: int', None, None)
		
		self.__ui_type = ui_type
		self.__key_modified['ui_type'] = 1

	def get_private(self):
		"""
		The method to get the private

		Returns:
			Private: An instance of Private
		"""

		return self.__private

	def set_private(self, private):
		"""
		The method to set the value to private

		Parameters:
			private (Private) : An instance of Private
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Private
		except Exception:
			from ..fields import Private

		if private is not None and not isinstance(private, Private):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: private EXPECTED TYPE: Private', None, None)
		
		self.__private = private
		self.__key_modified['private'] = 1

	def get_system_mandatory(self):
		"""
		The method to get the system_mandatory

		Returns:
			bool: A bool representing the system_mandatory
		"""

		return self.__system_mandatory

	def set_system_mandatory(self, system_mandatory):
		"""
		The method to set the value to system_mandatory

		Parameters:
			system_mandatory (bool) : A bool representing the system_mandatory
		"""

		if system_mandatory is not None and not isinstance(system_mandatory, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: system_mandatory EXPECTED TYPE: bool', None, None)
		
		self.__system_mandatory = system_mandatory
		self.__key_modified['system_mandatory'] = 1

	def get_webhook(self):
		"""
		The method to get the webhook

		Returns:
			bool: A bool representing the webhook
		"""

		return self.__webhook

	def set_webhook(self, webhook):
		"""
		The method to set the value to webhook

		Parameters:
			webhook (bool) : A bool representing the webhook
		"""

		if webhook is not None and not isinstance(webhook, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: webhook EXPECTED TYPE: bool', None, None)
		
		self.__webhook = webhook
		self.__key_modified['webhook'] = 1

	def get_json_type(self):
		"""
		The method to get the json_type

		Returns:
			string: A string representing the json_type
		"""

		return self.__json_type

	def set_json_type(self, json_type):
		"""
		The method to set the value to json_type

		Parameters:
			json_type (string) : A string representing the json_type
		"""

		if json_type is not None and not isinstance(json_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: json_type EXPECTED TYPE: str', None, None)
		
		self.__json_type = json_type
		self.__key_modified['json_type'] = 1

	def get_crypt(self):
		"""
		The method to get the crypt

		Returns:
			Crypt: An instance of Crypt
		"""

		return self.__crypt

	def set_crypt(self, crypt):
		"""
		The method to set the value to crypt

		Parameters:
			crypt (Crypt) : An instance of Crypt
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.crypt import Crypt
		except Exception:
			from .crypt import Crypt

		if crypt is not None and not isinstance(crypt, Crypt):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: crypt EXPECTED TYPE: Crypt', None, None)
		
		self.__crypt = crypt
		self.__key_modified['crypt'] = 1

	def get_field_label(self):
		"""
		The method to get the field_label

		Returns:
			string: A string representing the field_label
		"""

		return self.__field_label

	def set_field_label(self, field_label):
		"""
		The method to set the value to field_label

		Parameters:
			field_label (string) : A string representing the field_label
		"""

		if field_label is not None and not isinstance(field_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_label EXPECTED TYPE: str', None, None)
		
		self.__field_label = field_label
		self.__key_modified['field_label'] = 1

	def get_tooltip(self):
		"""
		The method to get the tooltip

		Returns:
			ToolTip: An instance of ToolTip
		"""

		return self.__tooltip

	def set_tooltip(self, tooltip):
		"""
		The method to set the value to tooltip

		Parameters:
			tooltip (ToolTip) : An instance of ToolTip
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.tool_tip import ToolTip
		except Exception:
			from .tool_tip import ToolTip

		if tooltip is not None and not isinstance(tooltip, ToolTip):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tooltip EXPECTED TYPE: ToolTip', None, None)
		
		self.__tooltip = tooltip
		self.__key_modified['tooltip'] = 1

	def get_created_source(self):
		"""
		The method to get the created_source

		Returns:
			string: A string representing the created_source
		"""

		return self.__created_source

	def set_created_source(self, created_source):
		"""
		The method to set the value to created_source

		Parameters:
			created_source (string) : A string representing the created_source
		"""

		if created_source is not None and not isinstance(created_source, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_source EXPECTED TYPE: str', None, None)
		
		self.__created_source = created_source
		self.__key_modified['created_source'] = 1

	def get_layouts(self):
		"""
		The method to get the layouts

		Returns:
			Layout: An instance of Layout
		"""

		return self.__layouts

	def set_layouts(self, layouts):
		"""
		The method to set the value to layouts

		Parameters:
			layouts (Layout) : An instance of Layout
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.layout import Layout
		except Exception:
			from .layout import Layout

		if layouts is not None and not isinstance(layouts, Layout):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layouts EXPECTED TYPE: Layout', None, None)
		
		self.__layouts = layouts
		self.__key_modified['layouts'] = 1

	def get_field_read_only(self):
		"""
		The method to get the field_read_only

		Returns:
			bool: A bool representing the field_read_only
		"""

		return self.__field_read_only

	def set_field_read_only(self, field_read_only):
		"""
		The method to set the value to field_read_only

		Parameters:
			field_read_only (bool) : A bool representing the field_read_only
		"""

		if field_read_only is not None and not isinstance(field_read_only, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_read_only EXPECTED TYPE: bool', None, None)
		
		self.__field_read_only = field_read_only
		self.__key_modified['field_read_only'] = 1

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

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

	def get_validation_rule(self):
		"""
		The method to get the validation_rule

		Returns:
			string: A string representing the validation_rule
		"""

		return self.__validation_rule

	def set_validation_rule(self, validation_rule):
		"""
		The method to set the value to validation_rule

		Parameters:
			validation_rule (string) : A string representing the validation_rule
		"""

		if validation_rule is not None and not isinstance(validation_rule, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: validation_rule EXPECTED TYPE: str', None, None)
		
		self.__validation_rule = validation_rule
		self.__key_modified['validation_rule'] = 1

	def get_read_only(self):
		"""
		The method to get the read_only

		Returns:
			bool: A bool representing the read_only
		"""

		return self.__read_only

	def set_read_only(self, read_only):
		"""
		The method to set the value to read_only

		Parameters:
			read_only (bool) : A bool representing the read_only
		"""

		if read_only is not None and not isinstance(read_only, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: read_only EXPECTED TYPE: bool', None, None)
		
		self.__read_only = read_only
		self.__key_modified['read_only'] = 1

	def get_association_details(self):
		"""
		The method to get the association_details

		Returns:
			AssociationDetails: An instance of AssociationDetails
		"""

		return self.__association_details

	def set_association_details(self, association_details):
		"""
		The method to set the value to association_details

		Parameters:
			association_details (AssociationDetails) : An instance of AssociationDetails
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.association_details import AssociationDetails
		except Exception:
			from .association_details import AssociationDetails

		if association_details is not None and not isinstance(association_details, AssociationDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: association_details EXPECTED TYPE: AssociationDetails', None, None)
		
		self.__association_details = association_details
		self.__key_modified['association_details'] = 1

	def get_multi_module_lookup(self):
		"""
		The method to get the multi_module_lookup

		Returns:
			MultiModuleLookup: An instance of MultiModuleLookup
		"""

		return self.__multi_module_lookup

	def set_multi_module_lookup(self, multi_module_lookup):
		"""
		The method to set the value to multi_module_lookup

		Parameters:
			multi_module_lookup (MultiModuleLookup) : An instance of MultiModuleLookup
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import MultiModuleLookup
		except Exception:
			from ..fields import MultiModuleLookup

		if multi_module_lookup is not None and not isinstance(multi_module_lookup, MultiModuleLookup):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: multi_module_lookup EXPECTED TYPE: MultiModuleLookup', None, None)
		
		self.__multi_module_lookup = multi_module_lookup
		self.__key_modified['multi_module_lookup'] = 1

	def get_currency(self):
		"""
		The method to get the currency

		Returns:
			Currency: An instance of Currency
		"""

		return self.__currency

	def set_currency(self, currency):
		"""
		The method to set the value to currency

		Parameters:
			currency (Currency) : An instance of Currency
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.currency import Currency
		except Exception:
			from .currency import Currency

		if currency is not None and not isinstance(currency, Currency):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency EXPECTED TYPE: Currency', None, None)
		
		self.__currency = currency
		self.__key_modified['currency'] = 1

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

	def get_custom_field(self):
		"""
		The method to get the custom_field

		Returns:
			bool: A bool representing the custom_field
		"""

		return self.__custom_field

	def set_custom_field(self, custom_field):
		"""
		The method to set the value to custom_field

		Parameters:
			custom_field (bool) : A bool representing the custom_field
		"""

		if custom_field is not None and not isinstance(custom_field, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: custom_field EXPECTED TYPE: bool', None, None)
		
		self.__custom_field = custom_field
		self.__key_modified['custom_field'] = 1

	def get_lookup(self):
		"""
		The method to get the lookup

		Returns:
			Module: An instance of Module
		"""

		return self.__lookup

	def set_lookup(self, lookup):
		"""
		The method to set the value to lookup

		Parameters:
			lookup (Module) : An instance of Module
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.module import Module
		except Exception:
			from .module import Module

		if lookup is not None and not isinstance(lookup, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lookup EXPECTED TYPE: Module', None, None)
		
		self.__lookup = lookup
		self.__key_modified['lookup'] = 1

	def get_convert_mapping(self):
		"""
		The method to get the convert_mapping

		Returns:
			dict: An instance of dict
		"""

		return self.__convert_mapping

	def set_convert_mapping(self, convert_mapping):
		"""
		The method to set the value to convert_mapping

		Parameters:
			convert_mapping (dict) : An instance of dict
		"""

		if convert_mapping is not None and not isinstance(convert_mapping, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: convert_mapping EXPECTED TYPE: dict', None, None)
		
		self.__convert_mapping = convert_mapping
		self.__key_modified['convert_mapping'] = 1

	def get_visible(self):
		"""
		The method to get the visible

		Returns:
			bool: A bool representing the visible
		"""

		return self.__visible

	def set_visible(self, visible):
		"""
		The method to set the value to visible

		Parameters:
			visible (bool) : A bool representing the visible
		"""

		if visible is not None and not isinstance(visible, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: visible EXPECTED TYPE: bool', None, None)
		
		self.__visible = visible
		self.__key_modified['visible'] = 1

	def get_length(self):
		"""
		The method to get the length

		Returns:
			int: An int representing the length
		"""

		return self.__length

	def set_length(self, length):
		"""
		The method to set the value to length

		Parameters:
			length (int) : An int representing the length
		"""

		if length is not None and not isinstance(length, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: length EXPECTED TYPE: int', None, None)
		
		self.__length = length
		self.__key_modified['length'] = 1

	def get_column_name(self):
		"""
		The method to get the column_name

		Returns:
			string: A string representing the column_name
		"""

		return self.__column_name

	def set_column_name(self, column_name):
		"""
		The method to set the value to column_name

		Parameters:
			column_name (string) : A string representing the column_name
		"""

		if column_name is not None and not isinstance(column_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: column_name EXPECTED TYPE: str', None, None)
		
		self.__column_name = column_name
		self.__key_modified['column_name'] = 1

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
		self.__key_modified['_type'] = 1

	def get_view_type(self):
		"""
		The method to get the view_type

		Returns:
			ViewType: An instance of ViewType
		"""

		return self.__view_type

	def set_view_type(self, view_type):
		"""
		The method to set the value to view_type

		Parameters:
			view_type (ViewType) : An instance of ViewType
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.view_type import ViewType
		except Exception:
			from .view_type import ViewType

		if view_type is not None and not isinstance(view_type, ViewType):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: view_type EXPECTED TYPE: ViewType', None, None)
		
		self.__view_type = view_type
		self.__key_modified['view_type'] = 1

	def get_transition_sequence(self):
		"""
		The method to get the transition_sequence

		Returns:
			int: An int representing the transition_sequence
		"""

		return self.__transition_sequence

	def set_transition_sequence(self, transition_sequence):
		"""
		The method to set the value to transition_sequence

		Parameters:
			transition_sequence (int) : An int representing the transition_sequence
		"""

		if transition_sequence is not None and not isinstance(transition_sequence, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: transition_sequence EXPECTED TYPE: int', None, None)
		
		self.__transition_sequence = transition_sequence
		self.__key_modified['transition_sequence'] = 1

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_unique(self):
		"""
		The method to get the unique

		Returns:
			Unique: An instance of Unique
		"""

		return self.__unique

	def set_unique(self, unique):
		"""
		The method to set the value to unique

		Parameters:
			unique (Unique) : An instance of Unique
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Unique
		except Exception:
			from ..fields import Unique

		if unique is not None and not isinstance(unique, Unique):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: unique EXPECTED TYPE: Unique', None, None)
		
		self.__unique = unique
		self.__key_modified['unique'] = 1

	def get_history_tracking(self):
		"""
		The method to get the history_tracking

		Returns:
			bool: A bool representing the history_tracking
		"""

		return self.__history_tracking

	def set_history_tracking(self, history_tracking):
		"""
		The method to set the value to history_tracking

		Parameters:
			history_tracking (bool) : A bool representing the history_tracking
		"""

		if history_tracking is not None and not isinstance(history_tracking, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: history_tracking EXPECTED TYPE: bool', None, None)
		
		self.__history_tracking = history_tracking
		self.__key_modified['history_tracking'] = 1

	def get_data_type(self):
		"""
		The method to get the data_type

		Returns:
			string: A string representing the data_type
		"""

		return self.__data_type

	def set_data_type(self, data_type):
		"""
		The method to set the value to data_type

		Parameters:
			data_type (string) : A string representing the data_type
		"""

		if data_type is not None and not isinstance(data_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_type EXPECTED TYPE: str', None, None)
		
		self.__data_type = data_type
		self.__key_modified['data_type'] = 1

	def get_formula(self):
		"""
		The method to get the formula

		Returns:
			Formula: An instance of Formula
		"""

		return self.__formula

	def set_formula(self, formula):
		"""
		The method to set the value to formula

		Parameters:
			formula (Formula) : An instance of Formula
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.formula import Formula
		except Exception:
			from .formula import Formula

		if formula is not None and not isinstance(formula, Formula):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: formula EXPECTED TYPE: Formula', None, None)
		
		self.__formula = formula
		self.__key_modified['formula'] = 1

	def get_decimal_place(self):
		"""
		The method to get the decimal_place

		Returns:
			string: A string representing the decimal_place
		"""

		return self.__decimal_place

	def set_decimal_place(self, decimal_place):
		"""
		The method to set the value to decimal_place

		Parameters:
			decimal_place (string) : A string representing the decimal_place
		"""

		if decimal_place is not None and not isinstance(decimal_place, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: decimal_place EXPECTED TYPE: str', None, None)
		
		self.__decimal_place = decimal_place
		self.__key_modified['decimal_place'] = 1

	def get_multiselectlookup(self):
		"""
		The method to get the multiselectlookup

		Returns:
			MultiSelectLookup: An instance of MultiSelectLookup
		"""

		return self.__multiselectlookup

	def set_multiselectlookup(self, multiselectlookup):
		"""
		The method to set the value to multiselectlookup

		Parameters:
			multiselectlookup (MultiSelectLookup) : An instance of MultiSelectLookup
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.multi_select_lookup import MultiSelectLookup
		except Exception:
			from .multi_select_lookup import MultiSelectLookup

		if multiselectlookup is not None and not isinstance(multiselectlookup, MultiSelectLookup):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: multiselectlookup EXPECTED TYPE: MultiSelectLookup', None, None)
		
		self.__multiselectlookup = multiselectlookup
		self.__key_modified['multiselectlookup'] = 1

	def get_pick_list_values(self):
		"""
		The method to get the pick_list_values

		Returns:
			list: An instance of list
		"""

		return self.__pick_list_values

	def set_pick_list_values(self, pick_list_values):
		"""
		The method to set the value to pick_list_values

		Parameters:
			pick_list_values (list) : An instance of list
		"""

		if pick_list_values is not None and not isinstance(pick_list_values, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pick_list_values EXPECTED TYPE: list', None, None)
		
		self.__pick_list_values = pick_list_values
		self.__key_modified['pick_list_values'] = 1

	def get_auto_number(self):
		"""
		The method to get the auto_number

		Returns:
			AutoNumber: An instance of AutoNumber
		"""

		return self.__auto_number

	def set_auto_number(self, auto_number):
		"""
		The method to set the value to auto_number

		Parameters:
			auto_number (AutoNumber) : An instance of AutoNumber
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.blueprint.auto_number import AutoNumber
		except Exception:
			from .auto_number import AutoNumber

		if auto_number is not None and not isinstance(auto_number, AutoNumber):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: auto_number EXPECTED TYPE: AutoNumber', None, None)
		
		self.__auto_number = auto_number
		self.__key_modified['auto_number'] = 1

	def get_personality_name(self):
		"""
		The method to get the personality_name

		Returns:
			string: A string representing the personality_name
		"""

		return self.__personality_name

	def set_personality_name(self, personality_name):
		"""
		The method to set the value to personality_name

		Parameters:
			personality_name (string) : A string representing the personality_name
		"""

		if personality_name is not None and not isinstance(personality_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: personality_name EXPECTED TYPE: str', None, None)
		
		self.__personality_name = personality_name
		self.__key_modified['personality_name'] = 1

	def get_mandatory(self):
		"""
		The method to get the mandatory

		Returns:
			bool: A bool representing the mandatory
		"""

		return self.__mandatory

	def set_mandatory(self, mandatory):
		"""
		The method to set the value to mandatory

		Parameters:
			mandatory (bool) : A bool representing the mandatory
		"""

		if mandatory is not None and not isinstance(mandatory, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mandatory EXPECTED TYPE: bool', None, None)
		
		self.__mandatory = mandatory
		self.__key_modified['mandatory'] = 1

	def get_quick_sequence_number(self):
		"""
		The method to get the quick_sequence_number

		Returns:
			int: An int representing the quick_sequence_number
		"""

		return self.__quick_sequence_number

	def set_quick_sequence_number(self, quick_sequence_number):
		"""
		The method to set the value to quick_sequence_number

		Parameters:
			quick_sequence_number (int) : An int representing the quick_sequence_number
		"""

		if quick_sequence_number is not None and not isinstance(quick_sequence_number, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: quick_sequence_number EXPECTED TYPE: int', None, None)
		
		self.__quick_sequence_number = quick_sequence_number
		self.__key_modified['quick_sequence_number'] = 1

	def get_profiles(self):
		"""
		The method to get the profiles

		Returns:
			list: An instance of list
		"""

		return self.__profiles

	def set_profiles(self, profiles):
		"""
		The method to set the value to profiles

		Parameters:
			profiles (list) : An instance of list
		"""

		if profiles is not None and not isinstance(profiles, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: profiles EXPECTED TYPE: list', None, None)
		
		self.__profiles = profiles
		self.__key_modified['profiles'] = 1

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
