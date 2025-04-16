try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Layouts(object):
	def __init__(self):
		"""Creates an instance of Layouts"""

		self.__display_type = None
		self.__api_name = None
		self.__has_more_profiles = None
		self.__created_time = None
		self.__modified_time = None
		self.__visible = None
		self.__source = None
		self.__id = None
		self.__name = None
		self.__display_label = None
		self.__mode = None
		self.__subform_properties = None
		self.__status = None
		self.__show_business_card = None
		self.__generated_type = None
		self.__created_for = None
		self.__convert_mapping = None
		self.__modified_by = None
		self.__profiles = None
		self.__created_by = None
		self.__sections = None
		self.__actions_allowed = None
		self.__key_modified = dict()

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

	def get_has_more_profiles(self):
		"""
		The method to get the has_more_profiles

		Returns:
			bool: A bool representing the has_more_profiles
		"""

		return self.__has_more_profiles

	def set_has_more_profiles(self, has_more_profiles):
		"""
		The method to set the value to has_more_profiles

		Parameters:
			has_more_profiles (bool) : A bool representing the has_more_profiles
		"""

		if has_more_profiles is not None and not isinstance(has_more_profiles, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: has_more_profiles EXPECTED TYPE: bool', None, None)
		
		self.__has_more_profiles = has_more_profiles
		self.__key_modified['has_more_profiles'] = 1

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

	def get_mode(self):
		"""
		The method to get the mode

		Returns:
			string: A string representing the mode
		"""

		return self.__mode

	def set_mode(self, mode):
		"""
		The method to set the value to mode

		Parameters:
			mode (string) : A string representing the mode
		"""

		if mode is not None and not isinstance(mode, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mode EXPECTED TYPE: str', None, None)
		
		self.__mode = mode
		self.__key_modified['mode'] = 1

	def get_subform_properties(self):
		"""
		The method to get the subform_properties

		Returns:
			SubformProperty: An instance of SubformProperty
		"""

		return self.__subform_properties

	def set_subform_properties(self, subform_properties):
		"""
		The method to set the value to subform_properties

		Parameters:
			subform_properties (SubformProperty) : An instance of SubformProperty
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.subform_property import SubformProperty
		except Exception:
			from .subform_property import SubformProperty

		if subform_properties is not None and not isinstance(subform_properties, SubformProperty):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: subform_properties EXPECTED TYPE: SubformProperty', None, None)
		
		self.__subform_properties = subform_properties
		self.__key_modified['subform_properties'] = 1

	def get_status(self):
		"""
		The method to get the status

		Returns:
			string: A string representing the status
		"""

		return self.__status

	def set_status(self, status):
		"""
		The method to set the value to status

		Parameters:
			status (string) : A string representing the status
		"""

		if status is not None and not isinstance(status, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: status EXPECTED TYPE: str', None, None)
		
		self.__status = status
		self.__key_modified['status'] = 1

	def get_show_business_card(self):
		"""
		The method to get the show_business_card

		Returns:
			bool: A bool representing the show_business_card
		"""

		return self.__show_business_card

	def set_show_business_card(self, show_business_card):
		"""
		The method to set the value to show_business_card

		Parameters:
			show_business_card (bool) : A bool representing the show_business_card
		"""

		if show_business_card is not None and not isinstance(show_business_card, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: show_business_card EXPECTED TYPE: bool', None, None)
		
		self.__show_business_card = show_business_card
		self.__key_modified['show_business_card'] = 1

	def get_generated_type(self):
		"""
		The method to get the generated_type

		Returns:
			string: A string representing the generated_type
		"""

		return self.__generated_type

	def set_generated_type(self, generated_type):
		"""
		The method to set the value to generated_type

		Parameters:
			generated_type (string) : A string representing the generated_type
		"""

		if generated_type is not None and not isinstance(generated_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: generated_type EXPECTED TYPE: str', None, None)
		
		self.__generated_type = generated_type
		self.__key_modified['generated_type'] = 1

	def get_created_for(self):
		"""
		The method to get the created_for

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__created_for

	def set_created_for(self, created_for):
		"""
		The method to set the value to created_for

		Parameters:
			created_for (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if created_for is not None and not isinstance(created_for, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_for EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__created_for = created_for
		self.__key_modified['created_for'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.layouts.convert_mapping import ConvertMapping
		except Exception:
			from .convert_mapping import ConvertMapping

		if convert_mapping is not None and not isinstance(convert_mapping, ConvertMapping):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: convert_mapping EXPECTED TYPE: ConvertMapping', None, None)
		
		self.__convert_mapping = convert_mapping
		self.__key_modified['convert_mapping'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if modified_by is not None and not isinstance(modified_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

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

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if created_by is not None and not isinstance(created_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_sections(self):
		"""
		The method to get the sections

		Returns:
			list: An instance of list
		"""

		return self.__sections

	def set_sections(self, sections):
		"""
		The method to set the value to sections

		Parameters:
			sections (list) : An instance of list
		"""

		if sections is not None and not isinstance(sections, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sections EXPECTED TYPE: list', None, None)
		
		self.__sections = sections
		self.__key_modified['sections'] = 1

	def get_actions_allowed(self):
		"""
		The method to get the actions_allowed

		Returns:
			ActionsAllowed: An instance of ActionsAllowed
		"""

		return self.__actions_allowed

	def set_actions_allowed(self, actions_allowed):
		"""
		The method to set the value to actions_allowed

		Parameters:
			actions_allowed (ActionsAllowed) : An instance of ActionsAllowed
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.layouts.actions_allowed import ActionsAllowed
		except Exception:
			from .actions_allowed import ActionsAllowed

		if actions_allowed is not None and not isinstance(actions_allowed, ActionsAllowed):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actions_allowed EXPECTED TYPE: ActionsAllowed', None, None)
		
		self.__actions_allowed = actions_allowed
		self.__key_modified['actions_allowed'] = 1

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
