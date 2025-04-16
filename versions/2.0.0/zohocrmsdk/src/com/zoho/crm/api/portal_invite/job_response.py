try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class JobResponse(object):
	def __init__(self):
		"""Creates an instance of JobResponse"""

		self.__data = None
		self.__job_id = None
		self.__status = None
		self.__key_modified = dict()

	def get_data(self):
		"""
		The method to get the data

		Returns:
			list: An instance of list
		"""

		return self.__data

	def set_data(self, data):
		"""
		The method to set the value to data

		Parameters:
			data (list) : An instance of list
		"""

		if data is not None and not isinstance(data, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data EXPECTED TYPE: list', None, None)
		
		self.__data = data
		self.__key_modified['data'] = 1

	def get_job_id(self):
		"""
		The method to get the job_id

		Returns:
			int: An int representing the job_id
		"""

		return self.__job_id

	def set_job_id(self, job_id):
		"""
		The method to set the value to job_id

		Parameters:
			job_id (int) : An int representing the job_id
		"""

		if job_id is not None and not isinstance(job_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: job_id EXPECTED TYPE: int', None, None)
		
		self.__job_id = job_id
		self.__key_modified['job_id'] = 1

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
