try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.fields import Fields
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from ..fields import Fields


class ModuleFields(Fields):
	def __init__(self):
		"""Creates an instance of ModuleFields"""
		super().__init__()

		self.__blueprint_supported = None
		self.__json_type = None
		self.__length = None
		self.__decimal_place = None
		self.__multi_module_lookup = None
		self.__sharing_properties = None
		self.__currency = None
		self.__file_upolad_optionlist = None
		self.__lookup = None
		self.__subform = None
		self.__formula = None
		self.__multiselectlookup = None
		self.__multiuserlookup = None
		self.__pick_list_values = None
		self.__allowed_modules = None
		self.__hipaa_compliance_enabled = None
		self.__hipaa_compliance = None
		self.__associated_module = None
		self.__data_type = None
		self.__operation_type = None
		self.__system_mandatory = None
		self.__webhook = None
		self.__sequence_number = None
		self.__default_value = None
		self.__virtual_field = None
		self.__field_read_only = None
		self.__customizable_properties = None
		self.__read_only = None
		self.__custom_field = None
		self.__businesscard_supported = None
		self.__filterable = None
		self.__visible = None
		self.__available_in_user_layout = None
		self.__display_field = None
		self.__pick_list_values_sorted_lexically = None
		self.__sortable = None
		self.__layout_associations = None
		self.__separator = None
		self.__searchable = None
		self.__enable_colour_code = None
		self.__mass_update = None
		self.__created_source = None
		self.__type = None
		self.__display_label = None
		self.__column_name = None
		self.__api_name = None
		self.__display_type = None
		self.__ui_type = None
		self.__colour_code_enabled_by_system = None
		self.__quick_sequence_number = None
		self.__email_parser = None
		self.__rollup_summary = None
		self.__refer_from_field = None
		self.__created_time = None
		self.__modified_time = None
		self.__show_type = None
		self.__category = None
		self.__id = None
		self.__profiles = None
		self.__view_type = None
		self.__unique = None
		self.__sub_module = None
		self.__external = None
		self.__private = None
		self.__convert_mapping = None
		self.__autonumber = None
		self.__auto_number_65 = None
		self.__crypt = None
		self.__tooltip = None
		self.__history_tracking_enabled = None
		self.__history_tracking = None
		self.__association_details = None
		self.__additional_column = None
		self.__field_label = None
		self.__global_picklist = None
		self.__update_existing_records = None
		self.__number_separator = None
		self.__textarea = None
		self.__static_field = None
		self.__key_modified = dict()

	def get_blueprint_supported(self):
		"""
		The method to get the blueprint_supported

		Returns:
			bool: A bool representing the blueprint_supported
		"""

		return self.__blueprint_supported

	def set_blueprint_supported(self, blueprint_supported):
		"""
		The method to set the value to blueprint_supported

		Parameters:
			blueprint_supported (bool) : A bool representing the blueprint_supported
		"""

		if blueprint_supported is not None and not isinstance(blueprint_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: blueprint_supported EXPECTED TYPE: bool', None, None)
		
		self.__blueprint_supported = blueprint_supported
		self.__key_modified['blueprint_supported'] = 1

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

	def get_decimal_place(self):
		"""
		The method to get the decimal_place

		Returns:
			int: An int representing the decimal_place
		"""

		return self.__decimal_place

	def set_decimal_place(self, decimal_place):
		"""
		The method to set the value to decimal_place

		Parameters:
			decimal_place (int) : An int representing the decimal_place
		"""

		if decimal_place is not None and not isinstance(decimal_place, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: decimal_place EXPECTED TYPE: int', None, None)
		
		self.__decimal_place = decimal_place
		self.__key_modified['decimal_place'] = 1

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

	def get_sharing_properties(self):
		"""
		The method to get the sharing_properties

		Returns:
			SharingProperties: An instance of SharingProperties
		"""

		return self.__sharing_properties

	def set_sharing_properties(self, sharing_properties):
		"""
		The method to set the value to sharing_properties

		Parameters:
			sharing_properties (SharingProperties) : An instance of SharingProperties
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules.sharing_properties import SharingProperties
		except Exception:
			from .sharing_properties import SharingProperties

		if sharing_properties is not None and not isinstance(sharing_properties, SharingProperties):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sharing_properties EXPECTED TYPE: SharingProperties', None, None)
		
		self.__sharing_properties = sharing_properties
		self.__key_modified['sharing_properties'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.fields import Currency
		except Exception:
			from ..fields import Currency

		if currency is not None and not isinstance(currency, Currency):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency EXPECTED TYPE: Currency', None, None)
		
		self.__currency = currency
		self.__key_modified['currency'] = 1

	def get_file_upolad_optionlist(self):
		"""
		The method to get the file_upolad_optionlist

		Returns:
			list: An instance of list
		"""

		return self.__file_upolad_optionlist

	def set_file_upolad_optionlist(self, file_upolad_optionlist):
		"""
		The method to set the value to file_upolad_optionlist

		Parameters:
			file_upolad_optionlist (list) : An instance of list
		"""

		if file_upolad_optionlist is not None and not isinstance(file_upolad_optionlist, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_upolad_optionlist EXPECTED TYPE: list', None, None)
		
		self.__file_upolad_optionlist = file_upolad_optionlist
		self.__key_modified['file_upolad_optionlist'] = 1

	def get_lookup(self):
		"""
		The method to get the lookup

		Returns:
			Lookup: An instance of Lookup
		"""

		return self.__lookup

	def set_lookup(self, lookup):
		"""
		The method to set the value to lookup

		Parameters:
			lookup (Lookup) : An instance of Lookup
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Lookup
		except Exception:
			from ..fields import Lookup

		if lookup is not None and not isinstance(lookup, Lookup):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lookup EXPECTED TYPE: Lookup', None, None)
		
		self.__lookup = lookup
		self.__key_modified['lookup'] = 1

	def get_subform(self):
		"""
		The method to get the subform

		Returns:
			Subform: An instance of Subform
		"""

		return self.__subform

	def set_subform(self, subform):
		"""
		The method to set the value to subform

		Parameters:
			subform (Subform) : An instance of Subform
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Subform
		except Exception:
			from ..fields import Subform

		if subform is not None and not isinstance(subform, Subform):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subform EXPECTED TYPE: Subform', None, None)
		
		self.__subform = subform
		self.__key_modified['subform'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.fields import Formula
		except Exception:
			from ..fields import Formula

		if formula is not None and not isinstance(formula, Formula):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: formula EXPECTED TYPE: Formula', None, None)
		
		self.__formula = formula
		self.__key_modified['formula'] = 1

	def get_multiselectlookup(self):
		"""
		The method to get the multiselectlookup

		Returns:
			Multiselectlookup: An instance of Multiselectlookup
		"""

		return self.__multiselectlookup

	def set_multiselectlookup(self, multiselectlookup):
		"""
		The method to set the value to multiselectlookup

		Parameters:
			multiselectlookup (Multiselectlookup) : An instance of Multiselectlookup
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Multiselectlookup
		except Exception:
			from ..fields import Multiselectlookup

		if multiselectlookup is not None and not isinstance(multiselectlookup, Multiselectlookup):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: multiselectlookup EXPECTED TYPE: Multiselectlookup', None, None)
		
		self.__multiselectlookup = multiselectlookup
		self.__key_modified['multiselectlookup'] = 1

	def get_multiuserlookup(self):
		"""
		The method to get the multiuserlookup

		Returns:
			Multiselectlookup: An instance of Multiselectlookup
		"""

		return self.__multiuserlookup

	def set_multiuserlookup(self, multiuserlookup):
		"""
		The method to set the value to multiuserlookup

		Parameters:
			multiuserlookup (Multiselectlookup) : An instance of Multiselectlookup
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Multiselectlookup
		except Exception:
			from ..fields import Multiselectlookup

		if multiuserlookup is not None and not isinstance(multiuserlookup, Multiselectlookup):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: multiuserlookup EXPECTED TYPE: Multiselectlookup', None, None)
		
		self.__multiuserlookup = multiuserlookup
		self.__key_modified['multiuserlookup'] = 1

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

	def get_allowed_modules(self):
		"""
		The method to get the allowed_modules

		Returns:
			list: An instance of list
		"""

		return self.__allowed_modules

	def set_allowed_modules(self, allowed_modules):
		"""
		The method to set the value to allowed_modules

		Parameters:
			allowed_modules (list) : An instance of list
		"""

		if allowed_modules is not None and not isinstance(allowed_modules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: allowed_modules EXPECTED TYPE: list', None, None)
		
		self.__allowed_modules = allowed_modules
		self.__key_modified['allowed_modules'] = 1

	def get_hipaa_compliance_enabled(self):
		"""
		The method to get the hipaa_compliance_enabled

		Returns:
			bool: A bool representing the hipaa_compliance_enabled
		"""

		return self.__hipaa_compliance_enabled

	def set_hipaa_compliance_enabled(self, hipaa_compliance_enabled):
		"""
		The method to set the value to hipaa_compliance_enabled

		Parameters:
			hipaa_compliance_enabled (bool) : A bool representing the hipaa_compliance_enabled
		"""

		if hipaa_compliance_enabled is not None and not isinstance(hipaa_compliance_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: hipaa_compliance_enabled EXPECTED TYPE: bool', None, None)
		
		self.__hipaa_compliance_enabled = hipaa_compliance_enabled
		self.__key_modified['hipaa_compliance_enabled'] = 1

	def get_hipaa_compliance(self):
		"""
		The method to get the hipaa_compliance

		Returns:
			HipaaCompliance: An instance of HipaaCompliance
		"""

		return self.__hipaa_compliance

	def set_hipaa_compliance(self, hipaa_compliance):
		"""
		The method to set the value to hipaa_compliance

		Parameters:
			hipaa_compliance (HipaaCompliance) : An instance of HipaaCompliance
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import HipaaCompliance
		except Exception:
			from ..fields import HipaaCompliance

		if hipaa_compliance is not None and not isinstance(hipaa_compliance, HipaaCompliance):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: hipaa_compliance EXPECTED TYPE: HipaaCompliance', None, None)
		
		self.__hipaa_compliance = hipaa_compliance
		self.__key_modified['hipaa_compliance'] = 1

	def get_associated_module(self):
		"""
		The method to get the associated_module

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__associated_module

	def set_associated_module(self, associated_module):
		"""
		The method to set the value to associated_module

		Parameters:
			associated_module (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules.minified_module import MinifiedModule
		except Exception:
			from .minified_module import MinifiedModule

		if associated_module is not None and not isinstance(associated_module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: associated_module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__associated_module = associated_module
		self.__key_modified['associated_module'] = 1

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

	def get_operation_type(self):
		"""
		The method to get the operation_type

		Returns:
			OperationType: An instance of OperationType
		"""

		return self.__operation_type

	def set_operation_type(self, operation_type):
		"""
		The method to set the value to operation_type

		Parameters:
			operation_type (OperationType) : An instance of OperationType
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import OperationType
		except Exception:
			from ..fields import OperationType

		if operation_type is not None and not isinstance(operation_type, OperationType):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: operation_type EXPECTED TYPE: OperationType', None, None)
		
		self.__operation_type = operation_type
		self.__key_modified['operation_type'] = 1

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

	def get_sequence_number(self):
		"""
		The method to get the sequence_number

		Returns:
			int: An int representing the sequence_number
		"""

		return self.__sequence_number

	def set_sequence_number(self, sequence_number):
		"""
		The method to set the value to sequence_number

		Parameters:
			sequence_number (int) : An int representing the sequence_number
		"""

		if sequence_number is not None and not isinstance(sequence_number, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sequence_number EXPECTED TYPE: int', None, None)
		
		self.__sequence_number = sequence_number
		self.__key_modified['sequence_number'] = 1

	def get_default_value(self):
		"""
		The method to get the default_value

		Returns:
			string: A string representing the default_value
		"""

		return self.__default_value

	def set_default_value(self, default_value):
		"""
		The method to set the value to default_value

		Parameters:
			default_value (string) : A string representing the default_value
		"""

		if default_value is not None and not isinstance(default_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_value EXPECTED TYPE: str', None, None)
		
		self.__default_value = default_value
		self.__key_modified['default_value'] = 1

	def get_virtual_field(self):
		"""
		The method to get the virtual_field

		Returns:
			bool: A bool representing the virtual_field
		"""

		return self.__virtual_field

	def set_virtual_field(self, virtual_field):
		"""
		The method to set the value to virtual_field

		Parameters:
			virtual_field (bool) : A bool representing the virtual_field
		"""

		if virtual_field is not None and not isinstance(virtual_field, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: virtual_field EXPECTED TYPE: bool', None, None)
		
		self.__virtual_field = virtual_field
		self.__key_modified['virtual_field'] = 1

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

	def get_customizable_properties(self):
		"""
		The method to get the customizable_properties

		Returns:
			list: An instance of list
		"""

		return self.__customizable_properties

	def set_customizable_properties(self, customizable_properties):
		"""
		The method to set the value to customizable_properties

		Parameters:
			customizable_properties (list) : An instance of list
		"""

		if customizable_properties is not None and not isinstance(customizable_properties, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: customizable_properties EXPECTED TYPE: list', None, None)
		
		self.__customizable_properties = customizable_properties
		self.__key_modified['customizable_properties'] = 1

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

	def get_businesscard_supported(self):
		"""
		The method to get the businesscard_supported

		Returns:
			bool: A bool representing the businesscard_supported
		"""

		return self.__businesscard_supported

	def set_businesscard_supported(self, businesscard_supported):
		"""
		The method to set the value to businesscard_supported

		Parameters:
			businesscard_supported (bool) : A bool representing the businesscard_supported
		"""

		if businesscard_supported is not None and not isinstance(businesscard_supported, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: businesscard_supported EXPECTED TYPE: bool', None, None)
		
		self.__businesscard_supported = businesscard_supported
		self.__key_modified['businesscard_supported'] = 1

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

	def get_available_in_user_layout(self):
		"""
		The method to get the available_in_user_layout

		Returns:
			bool: A bool representing the available_in_user_layout
		"""

		return self.__available_in_user_layout

	def set_available_in_user_layout(self, available_in_user_layout):
		"""
		The method to set the value to available_in_user_layout

		Parameters:
			available_in_user_layout (bool) : A bool representing the available_in_user_layout
		"""

		if available_in_user_layout is not None and not isinstance(available_in_user_layout, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: available_in_user_layout EXPECTED TYPE: bool', None, None)
		
		self.__available_in_user_layout = available_in_user_layout
		self.__key_modified['available_in_user_layout'] = 1

	def get_display_field(self):
		"""
		The method to get the display_field

		Returns:
			bool: A bool representing the display_field
		"""

		return self.__display_field

	def set_display_field(self, display_field):
		"""
		The method to set the value to display_field

		Parameters:
			display_field (bool) : A bool representing the display_field
		"""

		if display_field is not None and not isinstance(display_field, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_field EXPECTED TYPE: bool', None, None)
		
		self.__display_field = display_field
		self.__key_modified['display_field'] = 1

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

	def get_layout_associations(self):
		"""
		The method to get the layout_associations

		Returns:
			list: An instance of list
		"""

		return self.__layout_associations

	def set_layout_associations(self, layout_associations):
		"""
		The method to set the value to layout_associations

		Parameters:
			layout_associations (list) : An instance of list
		"""

		if layout_associations is not None and not isinstance(layout_associations, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout_associations EXPECTED TYPE: list', None, None)
		
		self.__layout_associations = layout_associations
		self.__key_modified['layout_associations'] = 1

	def get_separator(self):
		"""
		The method to get the separator

		Returns:
			bool: A bool representing the separator
		"""

		return self.__separator

	def set_separator(self, separator):
		"""
		The method to set the value to separator

		Parameters:
			separator (bool) : A bool representing the separator
		"""

		if separator is not None and not isinstance(separator, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: separator EXPECTED TYPE: bool', None, None)
		
		self.__separator = separator
		self.__key_modified['separator'] = 1

	def get_searchable(self):
		"""
		The method to get the searchable

		Returns:
			bool: A bool representing the searchable
		"""

		return self.__searchable

	def set_searchable(self, searchable):
		"""
		The method to set the value to searchable

		Parameters:
			searchable (bool) : A bool representing the searchable
		"""

		if searchable is not None and not isinstance(searchable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: searchable EXPECTED TYPE: bool', None, None)
		
		self.__searchable = searchable
		self.__key_modified['searchable'] = 1

	def get_enable_colour_code(self):
		"""
		The method to get the enable_colour_code

		Returns:
			bool: A bool representing the enable_colour_code
		"""

		return self.__enable_colour_code

	def set_enable_colour_code(self, enable_colour_code):
		"""
		The method to set the value to enable_colour_code

		Parameters:
			enable_colour_code (bool) : A bool representing the enable_colour_code
		"""

		if enable_colour_code is not None and not isinstance(enable_colour_code, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enable_colour_code EXPECTED TYPE: bool', None, None)
		
		self.__enable_colour_code = enable_colour_code
		self.__key_modified['enable_colour_code'] = 1

	def get_mass_update(self):
		"""
		The method to get the mass_update

		Returns:
			bool: A bool representing the mass_update
		"""

		return self.__mass_update

	def set_mass_update(self, mass_update):
		"""
		The method to set the value to mass_update

		Parameters:
			mass_update (bool) : A bool representing the mass_update
		"""

		if mass_update is not None and not isinstance(mass_update, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mass_update EXPECTED TYPE: bool', None, None)
		
		self.__mass_update = mass_update
		self.__key_modified['mass_update'] = 1

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

	def get_display_type(self):
		"""
		The method to get the display_type

		Returns:
			int: An int representing the display_type
		"""

		return self.__display_type

	def set_display_type(self, display_type):
		"""
		The method to set the value to display_type

		Parameters:
			display_type (int) : An int representing the display_type
		"""

		if display_type is not None and not isinstance(display_type, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_type EXPECTED TYPE: int', None, None)
		
		self.__display_type = display_type
		self.__key_modified['display_type'] = 1

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

	def get_colour_code_enabled_by_system(self):
		"""
		The method to get the colour_code_enabled_by_system

		Returns:
			bool: A bool representing the colour_code_enabled_by_system
		"""

		return self.__colour_code_enabled_by_system

	def set_colour_code_enabled_by_system(self, colour_code_enabled_by_system):
		"""
		The method to set the value to colour_code_enabled_by_system

		Parameters:
			colour_code_enabled_by_system (bool) : A bool representing the colour_code_enabled_by_system
		"""

		if colour_code_enabled_by_system is not None and not isinstance(colour_code_enabled_by_system, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: colour_code_enabled_by_system EXPECTED TYPE: bool', None, None)
		
		self.__colour_code_enabled_by_system = colour_code_enabled_by_system
		self.__key_modified['colour_code_enabled_by_system'] = 1

	def get_quick_sequence_number(self):
		"""
		The method to get the quick_sequence_number

		Returns:
			string: A string representing the quick_sequence_number
		"""

		return self.__quick_sequence_number

	def set_quick_sequence_number(self, quick_sequence_number):
		"""
		The method to set the value to quick_sequence_number

		Parameters:
			quick_sequence_number (string) : A string representing the quick_sequence_number
		"""

		if quick_sequence_number is not None and not isinstance(quick_sequence_number, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: quick_sequence_number EXPECTED TYPE: str', None, None)
		
		self.__quick_sequence_number = quick_sequence_number
		self.__key_modified['quick_sequence_number'] = 1

	def get_email_parser(self):
		"""
		The method to get the email_parser

		Returns:
			EmailParser: An instance of EmailParser
		"""

		return self.__email_parser

	def set_email_parser(self, email_parser):
		"""
		The method to set the value to email_parser

		Parameters:
			email_parser (EmailParser) : An instance of EmailParser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import EmailParser
		except Exception:
			from ..fields import EmailParser

		if email_parser is not None and not isinstance(email_parser, EmailParser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_parser EXPECTED TYPE: EmailParser', None, None)
		
		self.__email_parser = email_parser
		self.__key_modified['email_parser'] = 1

	def get_rollup_summary(self):
		"""
		The method to get the rollup_summary

		Returns:
			RollupSummary: An instance of RollupSummary
		"""

		return self.__rollup_summary

	def set_rollup_summary(self, rollup_summary):
		"""
		The method to set the value to rollup_summary

		Parameters:
			rollup_summary (RollupSummary) : An instance of RollupSummary
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import RollupSummary
		except Exception:
			from ..fields import RollupSummary

		if rollup_summary is not None and not isinstance(rollup_summary, RollupSummary):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rollup_summary EXPECTED TYPE: RollupSummary', None, None)
		
		self.__rollup_summary = rollup_summary
		self.__key_modified['rollup_summary'] = 1

	def get_refer_from_field(self):
		"""
		The method to get the refer_from_field

		Returns:
			ReferFromField: An instance of ReferFromField
		"""

		return self.__refer_from_field

	def set_refer_from_field(self, refer_from_field):
		"""
		The method to set the value to refer_from_field

		Parameters:
			refer_from_field (ReferFromField) : An instance of ReferFromField
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import ReferFromField
		except Exception:
			from ..fields import ReferFromField

		if refer_from_field is not None and not isinstance(refer_from_field, ReferFromField):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: refer_from_field EXPECTED TYPE: ReferFromField', None, None)
		
		self.__refer_from_field = refer_from_field
		self.__key_modified['refer_from_field'] = 1

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

	def get_show_type(self):
		"""
		The method to get the show_type

		Returns:
			int: An int representing the show_type
		"""

		return self.__show_type

	def set_show_type(self, show_type):
		"""
		The method to set the value to show_type

		Parameters:
			show_type (int) : An int representing the show_type
		"""

		if show_type is not None and not isinstance(show_type, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_type EXPECTED TYPE: int', None, None)
		
		self.__show_type = show_type
		self.__key_modified['show_type'] = 1

	def get_category(self):
		"""
		The method to get the category

		Returns:
			int: An int representing the category
		"""

		return self.__category

	def set_category(self, category):
		"""
		The method to set the value to category

		Parameters:
			category (int) : An int representing the category
		"""

		if category is not None and not isinstance(category, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: int', None, None)
		
		self.__category = category
		self.__key_modified['category'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.fields import ViewType
		except Exception:
			from ..fields import ViewType

		if view_type is not None and not isinstance(view_type, ViewType):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: view_type EXPECTED TYPE: ViewType', None, None)
		
		self.__view_type = view_type
		self.__key_modified['view_type'] = 1

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

	def get_sub_module(self):
		"""
		The method to get the sub_module

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__sub_module

	def set_sub_module(self, sub_module):
		"""
		The method to set the value to sub_module

		Parameters:
			sub_module (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules.minified_module import MinifiedModule
		except Exception:
			from .minified_module import MinifiedModule

		if sub_module is not None and not isinstance(sub_module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sub_module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__sub_module = sub_module
		self.__key_modified['sub_module'] = 1

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

	def get_convert_mapping(self):
		"""
		The method to get the convert_mapping

		Returns:
			ConvertMapping: An instance of ConvertMapping
		"""

		return self.__convert_mapping

	def set_convert_mapping(self, convert_mapping):
		"""
		The method to set the value to convert_mapping

		Parameters:
			convert_mapping (ConvertMapping) : An instance of ConvertMapping
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import ConvertMapping
		except Exception:
			from ..fields import ConvertMapping

		if convert_mapping is not None and not isinstance(convert_mapping, ConvertMapping):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: convert_mapping EXPECTED TYPE: ConvertMapping', None, None)
		
		self.__convert_mapping = convert_mapping
		self.__key_modified['convert_mapping'] = 1

	def get_autonumber(self):
		"""
		The method to get the autonumber

		Returns:
			AutoNumber: An instance of AutoNumber
		"""

		return self.__autonumber

	def set_autonumber(self, autonumber):
		"""
		The method to set the value to autonumber

		Parameters:
			autonumber (AutoNumber) : An instance of AutoNumber
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import AutoNumber
		except Exception:
			from ..fields import AutoNumber

		if autonumber is not None and not isinstance(autonumber, AutoNumber):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: autonumber EXPECTED TYPE: AutoNumber', None, None)
		
		self.__autonumber = autonumber
		self.__key_modified['autonumber'] = 1

	def get_auto_number_65(self):
		"""
		The method to get the auto_number_65

		Returns:
			AutoNumber: An instance of AutoNumber
		"""

		return self.__auto_number_65

	def set_auto_number_65(self, auto_number_65):
		"""
		The method to set the value to auto_number_65

		Parameters:
			auto_number_65 (AutoNumber) : An instance of AutoNumber
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import AutoNumber
		except Exception:
			from ..fields import AutoNumber

		if auto_number_65 is not None and not isinstance(auto_number_65, AutoNumber):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: auto_number_65 EXPECTED TYPE: AutoNumber', None, None)
		
		self.__auto_number_65 = auto_number_65
		self.__key_modified['auto_number'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.fields import Crypt
		except Exception:
			from ..fields import Crypt

		if crypt is not None and not isinstance(crypt, Crypt):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: crypt EXPECTED TYPE: Crypt', None, None)
		
		self.__crypt = crypt
		self.__key_modified['crypt'] = 1

	def get_tooltip(self):
		"""
		The method to get the tooltip

		Returns:
			Tooltip: An instance of Tooltip
		"""

		return self.__tooltip

	def set_tooltip(self, tooltip):
		"""
		The method to set the value to tooltip

		Parameters:
			tooltip (Tooltip) : An instance of Tooltip
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Tooltip
		except Exception:
			from ..fields import Tooltip

		if tooltip is not None and not isinstance(tooltip, Tooltip):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tooltip EXPECTED TYPE: Tooltip', None, None)
		
		self.__tooltip = tooltip
		self.__key_modified['tooltip'] = 1

	def get_history_tracking_enabled(self):
		"""
		The method to get the history_tracking_enabled

		Returns:
			bool: A bool representing the history_tracking_enabled
		"""

		return self.__history_tracking_enabled

	def set_history_tracking_enabled(self, history_tracking_enabled):
		"""
		The method to set the value to history_tracking_enabled

		Parameters:
			history_tracking_enabled (bool) : A bool representing the history_tracking_enabled
		"""

		if history_tracking_enabled is not None and not isinstance(history_tracking_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: history_tracking_enabled EXPECTED TYPE: bool', None, None)
		
		self.__history_tracking_enabled = history_tracking_enabled
		self.__key_modified['history_tracking_enabled'] = 1

	def get_history_tracking(self):
		"""
		The method to get the history_tracking

		Returns:
			HistoryTracking: An instance of HistoryTracking
		"""

		return self.__history_tracking

	def set_history_tracking(self, history_tracking):
		"""
		The method to set the value to history_tracking

		Parameters:
			history_tracking (HistoryTracking) : An instance of HistoryTracking
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import HistoryTracking
		except Exception:
			from ..fields import HistoryTracking

		if history_tracking is not None and not isinstance(history_tracking, HistoryTracking):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: history_tracking EXPECTED TYPE: HistoryTracking', None, None)
		
		self.__history_tracking = history_tracking
		self.__key_modified['history_tracking'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.fields import AssociationDetails
		except Exception:
			from ..fields import AssociationDetails

		if association_details is not None and not isinstance(association_details, AssociationDetails):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: association_details EXPECTED TYPE: AssociationDetails', None, None)
		
		self.__association_details = association_details
		self.__key_modified['association_details'] = 1

	def get_additional_column(self):
		"""
		The method to get the additional_column

		Returns:
			string: A string representing the additional_column
		"""

		return self.__additional_column

	def set_additional_column(self, additional_column):
		"""
		The method to set the value to additional_column

		Parameters:
			additional_column (string) : A string representing the additional_column
		"""

		if additional_column is not None and not isinstance(additional_column, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: additional_column EXPECTED TYPE: str', None, None)
		
		self.__additional_column = additional_column
		self.__key_modified['additional_column'] = 1

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

	def get_global_picklist(self):
		"""
		The method to get the global_picklist

		Returns:
			Picklist: An instance of Picklist
		"""

		return self.__global_picklist

	def set_global_picklist(self, global_picklist):
		"""
		The method to set the value to global_picklist

		Parameters:
			global_picklist (Picklist) : An instance of Picklist
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.global_picklists import Picklist
		except Exception:
			from ..global_picklists import Picklist

		if global_picklist is not None and not isinstance(global_picklist, Picklist):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: global_picklist EXPECTED TYPE: Picklist', None, None)
		
		self.__global_picklist = global_picklist
		self.__key_modified['global_picklist'] = 1

	def get_update_existing_records(self):
		"""
		The method to get the update_existing_records

		Returns:
			bool: A bool representing the update_existing_records
		"""

		return self.__update_existing_records

	def set_update_existing_records(self, update_existing_records):
		"""
		The method to set the value to update_existing_records

		Parameters:
			update_existing_records (bool) : A bool representing the update_existing_records
		"""

		if update_existing_records is not None and not isinstance(update_existing_records, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: update_existing_records EXPECTED TYPE: bool', None, None)
		
		self.__update_existing_records = update_existing_records
		self.__key_modified['_update_existing_records'] = 1

	def get_number_separator(self):
		"""
		The method to get the number_separator

		Returns:
			bool: A bool representing the number_separator
		"""

		return self.__number_separator

	def set_number_separator(self, number_separator):
		"""
		The method to set the value to number_separator

		Parameters:
			number_separator (bool) : A bool representing the number_separator
		"""

		if number_separator is not None and not isinstance(number_separator, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: number_separator EXPECTED TYPE: bool', None, None)
		
		self.__number_separator = number_separator
		self.__key_modified['number_separator'] = 1

	def get_textarea(self):
		"""
		The method to get the textarea

		Returns:
			Textarea: An instance of Textarea
		"""

		return self.__textarea

	def set_textarea(self, textarea):
		"""
		The method to set the value to textarea

		Parameters:
			textarea (Textarea) : An instance of Textarea
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields import Textarea
		except Exception:
			from ..fields import Textarea

		if textarea is not None and not isinstance(textarea, Textarea):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: textarea EXPECTED TYPE: Textarea', None, None)
		
		self.__textarea = textarea
		self.__key_modified['textarea'] = 1

	def get_static_field(self):
		"""
		The method to get the static_field

		Returns:
			bool: A bool representing the static_field
		"""

		return self.__static_field

	def set_static_field(self, static_field):
		"""
		The method to set the value to static_field

		Parameters:
			static_field (bool) : A bool representing the static_field
		"""

		if static_field is not None and not isinstance(static_field, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: static_field EXPECTED TYPE: bool', None, None)
		
		self.__static_field = static_field
		self.__key_modified['static_field'] = 1

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
