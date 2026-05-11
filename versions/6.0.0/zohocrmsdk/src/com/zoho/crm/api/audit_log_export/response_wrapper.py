try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__audit_log_export = None
		self.__key_modified = dict()

	def get_audit_log_export(self):
		"""
		The method to get the audit_log_export

		Returns:
			list: An instance of list
		"""

		return self.__audit_log_export

	def set_audit_log_export(self, audit_log_export):
		"""
		The method to set the value to audit_log_export

		Parameters:
			audit_log_export (list) : An instance of list
		"""

		if audit_log_export is not None and not isinstance(audit_log_export, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: audit_log_export EXPECTED TYPE: list', None, None)
		
		self.__audit_log_export = audit_log_export
		self.__key_modified['audit_log_export'] = 1

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
