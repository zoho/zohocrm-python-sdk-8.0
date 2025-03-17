try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Cadences(object):
	def __init__(self):
		"""Creates an instance of Cadences"""

		self.__summary = None
		self.__created_time = None
		self.__module = None
		self.__active = None
		self.__execution_details = None
		self.__published = None
		self.__type = None
		self.__created_by = None
		self.__modified_time = None
		self.__name = None
		self.__modified_by = None
		self.__id = None
		self.__custom_view = None
		self.__status = None
		self.__key_modified = dict()

	def get_summary(self):
		"""
		The method to get the summary

		Returns:
			Summary: An instance of Summary
		"""

		return self.__summary

	def set_summary(self, summary):
		"""
		The method to set the value to summary

		Parameters:
			summary (Summary) : An instance of Summary
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences.summary import Summary
		except Exception:
			from .summary import Summary

		if summary is not None and not isinstance(summary, Summary):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: summary EXPECTED TYPE: Summary', None, None)
		
		self.__summary = summary
		self.__key_modified['summary'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			string: A string representing the created_time
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (string) : A string representing the created_time
		"""

		if created_time is not None and not isinstance(created_time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: str', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.cadences.module import Module
		except Exception:
			from .module import Module

		if module is not None and not isinstance(module, Module):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: Module', None, None)
		
		self.__module = module
		self.__key_modified['module'] = 1

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

	def get_execution_details(self):
		"""
		The method to get the execution_details

		Returns:
			ExecutionDetail: An instance of ExecutionDetail
		"""

		return self.__execution_details

	def set_execution_details(self, execution_details):
		"""
		The method to set the value to execution_details

		Parameters:
			execution_details (ExecutionDetail) : An instance of ExecutionDetail
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences.execution_detail import ExecutionDetail
		except Exception:
			from .execution_detail import ExecutionDetail

		if execution_details is not None and not isinstance(execution_details, ExecutionDetail):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: execution_details EXPECTED TYPE: ExecutionDetail', None, None)
		
		self.__execution_details = execution_details
		self.__key_modified['execution_details'] = 1

	def get_published(self):
		"""
		The method to get the published

		Returns:
			bool: A bool representing the published
		"""

		return self.__published

	def set_published(self, published):
		"""
		The method to set the value to published

		Parameters:
			published (bool) : A bool representing the published
		"""

		if published is not None and not isinstance(published, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: published EXPECTED TYPE: bool', None, None)
		
		self.__published = published
		self.__key_modified['published'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.cadences.user import User
		except Exception:
			from .user import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			string: A string representing the modified_time
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (string) : A string representing the modified_time
		"""

		if modified_time is not None and not isinstance(modified_time, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: str', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

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

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			User: An instance of User
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences.user import User
		except Exception:
			from .user import User

		if modified_by is not None and not isinstance(modified_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: User', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

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

	def get_custom_view(self):
		"""
		The method to get the custom_view

		Returns:
			CustomView: An instance of CustomView
		"""

		return self.__custom_view

	def set_custom_view(self, custom_view):
		"""
		The method to set the value to custom_view

		Parameters:
			custom_view (CustomView) : An instance of CustomView
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences.custom_view import CustomView
		except Exception:
			from .custom_view import CustomView

		if custom_view is not None and not isinstance(custom_view, CustomView):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: custom_view EXPECTED TYPE: CustomView', None, None)
		
		self.__custom_view = custom_view
		self.__key_modified['custom_view'] = 1

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
