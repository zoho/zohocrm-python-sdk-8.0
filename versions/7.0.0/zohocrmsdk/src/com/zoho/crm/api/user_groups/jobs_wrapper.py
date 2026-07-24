try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class JobsWrapper(object):
	def __init__(self):
		"""Creates an instance of JobsWrapper"""

		self.__deletion_jobs = None
		self.__key_modified = dict()

	def get_deletion_jobs(self):
		"""
		The method to get the deletion_jobs

		Returns:
			list: An instance of list
		"""

		return self.__deletion_jobs

	def set_deletion_jobs(self, deletion_jobs):
		"""
		The method to set the value to deletion_jobs

		Parameters:
			deletion_jobs (list) : An instance of list
		"""

		if deletion_jobs is not None and not isinstance(deletion_jobs, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deletion_jobs EXPECTED TYPE: list', None, None)
		
		self.__deletion_jobs = deletion_jobs
		self.__key_modified['deletion_jobs'] = 1

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
