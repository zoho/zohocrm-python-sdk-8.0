try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Fields(object):
	def __init__(self):
		"""Creates an instance of Fields"""

		self.__layout = None
		self.__help = None
		self.__field = None
		self.__module = None
		self.__secret_key = None
		self.__recaptcha_label = None
		self.__hidden = None
		self.__site_key = None
		self.__advanced = None
		self.__api_name = None
		self.__field_label = None
		self.__theme = None
		self.__id = None
		self.__required = None
		self.__field_name = None
		self.__date_format = None
		self.__key_modified = dict()

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

	def get_help(self):
		"""
		The method to get the help

		Returns:
			string: A string representing the help
		"""

		return self.__help

	def set_help(self, help):
		"""
		The method to set the value to help

		Parameters:
			help (string) : A string representing the help
		"""

		if help is not None and not isinstance(help, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: help EXPECTED TYPE: str', None, None)
		
		self.__help = help
		self.__key_modified['help'] = 1

	def get_field(self):
		"""
		The method to get the field

		Returns:
			Fields: An instance of Fields
		"""

		return self.__field

	def set_field(self, field):
		"""
		The method to set the value to field

		Parameters:
			field (Fields) : An instance of Fields
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.fields import Fields
		except Exception:
			from .fields import Fields

		if field is not None and not isinstance(field, Fields):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field EXPECTED TYPE: Fields', None, None)
		
		self.__field = field
		self.__key_modified['field'] = 1

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

	def get_secret_key(self):
		"""
		The method to get the secret_key

		Returns:
			string: A string representing the secret_key
		"""

		return self.__secret_key

	def set_secret_key(self, secret_key):
		"""
		The method to set the value to secret_key

		Parameters:
			secret_key (string) : A string representing the secret_key
		"""

		if secret_key is not None and not isinstance(secret_key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: secret_key EXPECTED TYPE: str', None, None)
		
		self.__secret_key = secret_key
		self.__key_modified['secret_key'] = 1

	def get_recaptcha_label(self):
		"""
		The method to get the recaptcha_label

		Returns:
			string: A string representing the recaptcha_label
		"""

		return self.__recaptcha_label

	def set_recaptcha_label(self, recaptcha_label):
		"""
		The method to set the value to recaptcha_label

		Parameters:
			recaptcha_label (string) : A string representing the recaptcha_label
		"""

		if recaptcha_label is not None and not isinstance(recaptcha_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: recaptcha_label EXPECTED TYPE: str', None, None)
		
		self.__recaptcha_label = recaptcha_label
		self.__key_modified['recaptcha_label'] = 1

	def get_hidden(self):
		"""
		The method to get the hidden

		Returns:
			bool: A bool representing the hidden
		"""

		return self.__hidden

	def set_hidden(self, hidden):
		"""
		The method to set the value to hidden

		Parameters:
			hidden (bool) : A bool representing the hidden
		"""

		if hidden is not None and not isinstance(hidden, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: hidden EXPECTED TYPE: bool', None, None)
		
		self.__hidden = hidden
		self.__key_modified['hidden'] = 1

	def get_site_key(self):
		"""
		The method to get the site_key

		Returns:
			string: A string representing the site_key
		"""

		return self.__site_key

	def set_site_key(self, site_key):
		"""
		The method to set the value to site_key

		Parameters:
			site_key (string) : A string representing the site_key
		"""

		if site_key is not None and not isinstance(site_key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: site_key EXPECTED TYPE: str', None, None)
		
		self.__site_key = site_key
		self.__key_modified['site_key'] = 1

	def get_advanced(self):
		"""
		The method to get the advanced

		Returns:
			bool: A bool representing the advanced
		"""

		return self.__advanced

	def set_advanced(self, advanced):
		"""
		The method to set the value to advanced

		Parameters:
			advanced (bool) : A bool representing the advanced
		"""

		if advanced is not None and not isinstance(advanced, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: advanced EXPECTED TYPE: bool', None, None)
		
		self.__advanced = advanced
		self.__key_modified['advanced'] = 1

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

	def get_theme(self):
		"""
		The method to get the theme

		Returns:
			string: A string representing the theme
		"""

		return self.__theme

	def set_theme(self, theme):
		"""
		The method to set the value to theme

		Parameters:
			theme (string) : A string representing the theme
		"""

		if theme is not None and not isinstance(theme, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: theme EXPECTED TYPE: str', None, None)
		
		self.__theme = theme
		self.__key_modified['theme'] = 1

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

	def get_required(self):
		"""
		The method to get the required

		Returns:
			bool: A bool representing the required
		"""

		return self.__required

	def set_required(self, required):
		"""
		The method to set the value to required

		Parameters:
			required (bool) : A bool representing the required
		"""

		if required is not None and not isinstance(required, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: required EXPECTED TYPE: bool', None, None)
		
		self.__required = required
		self.__key_modified['required'] = 1

	def get_field_name(self):
		"""
		The method to get the field_name

		Returns:
			string: A string representing the field_name
		"""

		return self.__field_name

	def set_field_name(self, field_name):
		"""
		The method to set the value to field_name

		Parameters:
			field_name (string) : A string representing the field_name
		"""

		if field_name is not None and not isinstance(field_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_name EXPECTED TYPE: str', None, None)
		
		self.__field_name = field_name
		self.__key_modified['field_name'] = 1

	def get_date_format(self):
		"""
		The method to get the date_format

		Returns:
			string: A string representing the date_format
		"""

		return self.__date_format

	def set_date_format(self, date_format):
		"""
		The method to set the value to date_format

		Parameters:
			date_format (string) : A string representing the date_format
		"""

		if date_format is not None and not isinstance(date_format, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: date_format EXPECTED TYPE: str', None, None)
		
		self.__date_format = date_format
		self.__key_modified['date_format'] = 1

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
