try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Backup(object):
	def __init__(self):
		"""Creates an instance of Backup"""

		self.__rrule = None
		self.__id = None
		self.__start_date = None
		self.__scheduled_date = None
		self.__status = None
		self.__requester = None
		self.__key_modified = dict()

	def get_rrule(self):
		"""
		The method to get the rrule

		Returns:
			string: A string representing the rrule
		"""

		return self.__rrule

	def set_rrule(self, rrule):
		"""
		The method to set the value to rrule

		Parameters:
			rrule (string) : A string representing the rrule
		"""

		if rrule is not None and not isinstance(rrule, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: rrule EXPECTED TYPE: str', None, None)
		
		self.__rrule = rrule
		self.__key_modified['rrule'] = 1

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

	def get_start_date(self):
		"""
		The method to get the start_date

		Returns:
			datetime: An instance of datetime
		"""

		return self.__start_date

	def set_start_date(self, start_date):
		"""
		The method to set the value to start_date

		Parameters:
			start_date (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if start_date is not None and not isinstance(start_date, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: start_date EXPECTED TYPE: datetime', None, None)
		
		self.__start_date = start_date
		self.__key_modified['start_date'] = 1

	def get_scheduled_date(self):
		"""
		The method to get the scheduled_date

		Returns:
			datetime: An instance of datetime
		"""

		return self.__scheduled_date

	def set_scheduled_date(self, scheduled_date):
		"""
		The method to set the value to scheduled_date

		Parameters:
			scheduled_date (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if scheduled_date is not None and not isinstance(scheduled_date, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: scheduled_date EXPECTED TYPE: datetime', None, None)
		
		self.__scheduled_date = scheduled_date
		self.__key_modified['scheduled_date'] = 1

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

	def get_requester(self):
		"""
		The method to get the requester

		Returns:
			Requester: An instance of Requester
		"""

		return self.__requester

	def set_requester(self, requester):
		"""
		The method to set the value to requester

		Parameters:
			requester (Requester) : An instance of Requester
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.backup.requester import Requester
		except Exception:
			from .requester import Requester

		if requester is not None and not isinstance(requester, Requester):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: requester EXPECTED TYPE: Requester', None, None)
		
		self.__requester = requester
		self.__key_modified['requester'] = 1

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
