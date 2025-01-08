try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ServicePreference(object):
	def __init__(self):
		"""Creates an instance of ServicePreference"""

		self.__job_sheet_enabled = None
		self.__key_modified = dict()

	def get_job_sheet_enabled(self):
		"""
		The method to get the job_sheet_enabled

		Returns:
			bool: A bool representing the job_sheet_enabled
		"""

		return self.__job_sheet_enabled

	def set_job_sheet_enabled(self, job_sheet_enabled):
		"""
		The method to set the value to job_sheet_enabled

		Parameters:
			job_sheet_enabled (bool) : A bool representing the job_sheet_enabled
		"""

		if job_sheet_enabled is not None and not isinstance(job_sheet_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: job_sheet_enabled EXPECTED TYPE: bool', None, None)
		
		self.__job_sheet_enabled = job_sheet_enabled
		self.__key_modified['job_sheet_enabled'] = 1

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
