try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AuditLogExport(object):
	def __init__(self):
		"""Creates an instance of AuditLogExport"""

		self.__criteria = None
		self.__id = None
		self.__status = None
		self.__created_by = None
		self.__download_links = None
		self.__job_start_time = None
		self.__job_end_time = None
		self.__expiry_date = None
		self.__key_modified = dict()

	def get_criteria(self):
		"""
		The method to get the criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__criteria

	def set_criteria(self, criteria):
		"""
		The method to set the value to criteria

		Parameters:
			criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if criteria is not None and not isinstance(criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__criteria = criteria
		self.__key_modified['criteria'] = 1

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
			from zohocrmsdk.src.com.zoho.crm.api.audit_log_export.user import User
		except Exception:
			from .user import User

		if created_by is not None and not isinstance(created_by, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: User', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_download_links(self):
		"""
		The method to get the download_links

		Returns:
			list: An instance of list
		"""

		return self.__download_links

	def set_download_links(self, download_links):
		"""
		The method to set the value to download_links

		Parameters:
			download_links (list) : An instance of list
		"""

		if download_links is not None and not isinstance(download_links, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: download_links EXPECTED TYPE: list', None, None)
		
		self.__download_links = download_links
		self.__key_modified['download_links'] = 1

	def get_job_start_time(self):
		"""
		The method to get the job_start_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__job_start_time

	def set_job_start_time(self, job_start_time):
		"""
		The method to set the value to job_start_time

		Parameters:
			job_start_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if job_start_time is not None and not isinstance(job_start_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: job_start_time EXPECTED TYPE: datetime', None, None)
		
		self.__job_start_time = job_start_time
		self.__key_modified['job_start_time'] = 1

	def get_job_end_time(self):
		"""
		The method to get the job_end_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__job_end_time

	def set_job_end_time(self, job_end_time):
		"""
		The method to set the value to job_end_time

		Parameters:
			job_end_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if job_end_time is not None and not isinstance(job_end_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: job_end_time EXPECTED TYPE: datetime', None, None)
		
		self.__job_end_time = job_end_time
		self.__key_modified['job_end_time'] = 1

	def get_expiry_date(self):
		"""
		The method to get the expiry_date

		Returns:
			datetime: An instance of datetime
		"""

		return self.__expiry_date

	def set_expiry_date(self, expiry_date):
		"""
		The method to set the value to expiry_date

		Parameters:
			expiry_date (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if expiry_date is not None and not isinstance(expiry_date, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: expiry_date EXPECTED TYPE: datetime', None, None)
		
		self.__expiry_date = expiry_date
		self.__key_modified['expiry_date'] = 1

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
