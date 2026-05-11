try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Available(object):
	def __init__(self):
		"""Creates an instance of Available"""

		self.__available = None
		self.__record = None
		self.__linked_record = None
		self.__key_modified = dict()

	def get_available(self):
		"""
		The method to get the available

		Returns:
			bool: A bool representing the available
		"""

		return self.__available

	def set_available(self, available):
		"""
		The method to set the value to available

		Parameters:
			available (bool) : A bool representing the available
		"""

		if available is not None and not isinstance(available, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: available EXPECTED TYPE: bool', None, None)
		
		self.__available = available
		self.__key_modified['available'] = 1

	def get_record(self):
		"""
		The method to get the record

		Returns:
			Record: An instance of Record
		"""

		return self.__record

	def set_record(self, record):
		"""
		The method to set the value to record

		Parameters:
			record (Record) : An instance of Record
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.associate_email.record import Record
		except Exception:
			from .record import Record

		if record is not None and not isinstance(record, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record EXPECTED TYPE: Record', None, None)
		
		self.__record = record
		self.__key_modified['record'] = 1

	def get_linked_record(self):
		"""
		The method to get the linked_record

		Returns:
			LinkedRecord: An instance of LinkedRecord
		"""

		return self.__linked_record

	def set_linked_record(self, linked_record):
		"""
		The method to set the value to linked_record

		Parameters:
			linked_record (LinkedRecord) : An instance of LinkedRecord
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.associate_email.linked_record import LinkedRecord
		except Exception:
			from .linked_record import LinkedRecord

		if linked_record is not None and not isinstance(linked_record, LinkedRecord):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: linked_record EXPECTED TYPE: LinkedRecord', None, None)
		
		self.__linked_record = linked_record
		self.__key_modified['linked_record'] = 1

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
