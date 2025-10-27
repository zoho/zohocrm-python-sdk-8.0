try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Urls(object):
	def __init__(self):
		"""Creates an instance of Urls"""

		self.__data_links = None
		self.__attachment_links = None
		self.__expiry_date = None
		self.__key_modified = dict()

	def get_data_links(self):
		"""
		The method to get the data_links

		Returns:
			list: An instance of list
		"""

		return self.__data_links

	def set_data_links(self, data_links):
		"""
		The method to set the value to data_links

		Parameters:
			data_links (list) : An instance of list
		"""

		if data_links is not None and not isinstance(data_links, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: data_links EXPECTED TYPE: list', None, None)
		
		self.__data_links = data_links
		self.__key_modified['data_links'] = 1

	def get_attachment_links(self):
		"""
		The method to get the attachment_links

		Returns:
			list: An instance of list
		"""

		return self.__attachment_links

	def set_attachment_links(self, attachment_links):
		"""
		The method to set the value to attachment_links

		Parameters:
			attachment_links (list) : An instance of list
		"""

		if attachment_links is not None and not isinstance(attachment_links, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: attachment_links EXPECTED TYPE: list', None, None)
		
		self.__attachment_links = attachment_links
		self.__key_modified['attachment_links'] = 1

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
