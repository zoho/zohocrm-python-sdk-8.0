try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Users(object):
	def __init__(self):
		"""Creates an instance of Users"""

		self.__role = None
		self.__name = None
		self.__id = None
		self.__email = None
		self.__zuid = None
		self.__effective_from = None
		self.__key_modified = dict()

	def get_role(self):
		"""
		The method to get the role

		Returns:
			Role: An instance of Role
		"""

		return self.__role

	def set_role(self, role):
		"""
		The method to set the value to role

		Parameters:
			role (Role) : An instance of Role
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.role import Role
		except Exception:
			from .role import Role

		if role is not None and not isinstance(role, Role):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: role EXPECTED TYPE: Role', None, None)
		
		self.__role = role
		self.__key_modified['role'] = 1

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

	def get_email(self):
		"""
		The method to get the email

		Returns:
			string: A string representing the email
		"""

		return self.__email

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (string) : A string representing the email
		"""

		if email is not None and not isinstance(email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: str', None, None)
		
		self.__email = email
		self.__key_modified['email'] = 1

	def get_zuid(self):
		"""
		The method to get the zuid

		Returns:
			string: A string representing the zuid
		"""

		return self.__zuid

	def set_zuid(self, zuid):
		"""
		The method to set the value to zuid

		Parameters:
			zuid (string) : A string representing the zuid
		"""

		if zuid is not None and not isinstance(zuid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zuid EXPECTED TYPE: str', None, None)
		
		self.__zuid = zuid
		self.__key_modified['zuid'] = 1

	def get_effective_from(self):
		"""
		The method to get the effective_from

		Returns:
			date: An instance of date
		"""

		return self.__effective_from

	def set_effective_from(self, effective_from):
		"""
		The method to set the value to effective_from

		Parameters:
			effective_from (date) : An instance of date
		"""

		from datetime import date as date1

		if effective_from is not None and not isinstance(effective_from, date1):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: effective_from EXPECTED TYPE: date1', None, None)
		
		self.__effective_from = effective_from
		self.__key_modified['effective_from'] = 1

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
