try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FormSection(object):
	def __init__(self):
		"""Creates an instance of FormSection"""

		self.__form_fields = None
		self.__name = None
		self.__description = None
		self.__help_message = None
		self.__id = None
		self.__key_modified = dict()

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

	def get_help_message(self):
		"""
		The method to get the help_message

		Returns:
			string: A string representing the help_message
		"""

		return self.__help_message

	def set_help_message(self, help_message):
		"""
		The method to set the value to help_message

		Parameters:
			help_message (string) : A string representing the help_message
		"""

		if help_message is not None and not isinstance(help_message, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: help_message EXPECTED TYPE: str', None, None)
		
		self.__help_message = help_message
		self.__key_modified['help_message'] = 1

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
