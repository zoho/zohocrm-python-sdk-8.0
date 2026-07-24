try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BodyWrapper(object):
	def __init__(self):
		"""Creates an instance of BodyWrapper"""

		self.__backup = None
		self.__key_modified = dict()

	def get_backup(self):
		"""
		The method to get the backup

		Returns:
			Backup: An instance of Backup
		"""

		return self.__backup

	def set_backup(self, backup):
		"""
		The method to set the value to backup

		Parameters:
			backup (Backup) : An instance of Backup
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.backup.backup import Backup
		except Exception:
			from .backup import Backup

		if backup is not None and not isinstance(backup, Backup):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: backup EXPECTED TYPE: Backup', None, None)
		
		self.__backup = backup
		self.__key_modified['backup'] = 1

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
