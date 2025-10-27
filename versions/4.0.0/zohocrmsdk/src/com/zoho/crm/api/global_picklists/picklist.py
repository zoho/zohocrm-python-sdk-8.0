try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Picklist(object):
	def __init__(self):
		"""Creates an instance of Picklist"""

		self.__display_label = None
		self.__created_time = None
		self.__modified_time = None
		self.__id = None
		self.__api_name = None
		self.__actual_label = None
		self.__description = None
		self.__modified_by = None
		self.__created_by = None
		self.__presence = None
		self.__pick_list_values_sorted_lexically = None
		self.__pick_list_values = None
		self.__associated_fields_count = None
		self.__used_in_modules = None
		self.__customizable = None
		self.__key_modified = dict()

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

	def get_actual_label(self):
		"""
		The method to get the actual_label

		Returns:
			string: A string representing the actual_label
		"""

		return self.__actual_label

	def set_actual_label(self, actual_label):
		"""
		The method to set the value to actual_label

		Parameters:
			actual_label (string) : A string representing the actual_label
		"""

		if actual_label is not None and not isinstance(actual_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actual_label EXPECTED TYPE: str', None, None)
		
		self.__actual_label = actual_label
		self.__key_modified['actual_label'] = 1

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

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

	def get_presence(self):
		"""
		The method to get the presence

		Returns:
			bool: A bool representing the presence
		"""

		return self.__presence

	def set_presence(self, presence):
		"""
		The method to set the value to presence

		Parameters:
			presence (bool) : A bool representing the presence
		"""

		if presence is not None and not isinstance(presence, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: presence EXPECTED TYPE: bool', None, None)
		
		self.__presence = presence
		self.__key_modified['presence'] = 1

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

	def get_associated_fields_count(self):
		"""
		The method to get the associated_fields_count

		Returns:
			int: An int representing the associated_fields_count
		"""

		return self.__associated_fields_count

	def set_associated_fields_count(self, associated_fields_count):
		"""
		The method to set the value to associated_fields_count

		Parameters:
			associated_fields_count (int) : An int representing the associated_fields_count
		"""

		if associated_fields_count is not None and not isinstance(associated_fields_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: associated_fields_count EXPECTED TYPE: int', None, None)
		
		self.__associated_fields_count = associated_fields_count
		self.__key_modified['associated_fields_count'] = 1

	def get_used_in_modules(self):
		"""
		The method to get the used_in_modules

		Returns:
			list: An instance of list
		"""

		return self.__used_in_modules

	def set_used_in_modules(self, used_in_modules):
		"""
		The method to set the value to used_in_modules

		Parameters:
			used_in_modules (list) : An instance of list
		"""

		if used_in_modules is not None and not isinstance(used_in_modules, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: used_in_modules EXPECTED TYPE: list', None, None)
		
		self.__used_in_modules = used_in_modules
		self.__key_modified['used_in_modules'] = 1

	def get_customizable(self):
		"""
		The method to get the customizable

		Returns:
			bool: A bool representing the customizable
		"""

		return self.__customizable

	def set_customizable(self, customizable):
		"""
		The method to set the value to customizable

		Parameters:
			customizable (bool) : A bool representing the customizable
		"""

		if customizable is not None and not isinstance(customizable, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: customizable EXPECTED TYPE: bool', None, None)
		
		self.__customizable = customizable
		self.__key_modified['customizable'] = 1

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
