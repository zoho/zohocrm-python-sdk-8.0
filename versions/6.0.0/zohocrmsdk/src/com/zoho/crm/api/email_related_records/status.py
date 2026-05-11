try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Status(object):
	def __init__(self):
		"""Creates an instance of Status"""

		self.__first_open = None
		self.__count = None
		self.__type = None
		self.__last_open = None
		self.__bounced_time = None
		self.__bounced_reason = None
		self.__category = None
		self.__sub_category = None
		self.__key_modified = dict()

	def get_first_open(self):
		"""
		The method to get the first_open

		Returns:
			datetime: An instance of datetime
		"""

		return self.__first_open

	def set_first_open(self, first_open):
		"""
		The method to set the value to first_open

		Parameters:
			first_open (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if first_open is not None and not isinstance(first_open, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: first_open EXPECTED TYPE: datetime', None, None)
		
		self.__first_open = first_open
		self.__key_modified['first_open'] = 1

	def get_count(self):
		"""
		The method to get the count

		Returns:
			string: A string representing the count
		"""

		return self.__count

	def set_count(self, count):
		"""
		The method to set the value to count

		Parameters:
			count (string) : A string representing the count
		"""

		if count is not None and not isinstance(count, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: count EXPECTED TYPE: str', None, None)
		
		self.__count = count
		self.__key_modified['count'] = 1

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

	def get_last_open(self):
		"""
		The method to get the last_open

		Returns:
			datetime: An instance of datetime
		"""

		return self.__last_open

	def set_last_open(self, last_open):
		"""
		The method to set the value to last_open

		Parameters:
			last_open (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if last_open is not None and not isinstance(last_open, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_open EXPECTED TYPE: datetime', None, None)
		
		self.__last_open = last_open
		self.__key_modified['last_open'] = 1

	def get_bounced_time(self):
		"""
		The method to get the bounced_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__bounced_time

	def set_bounced_time(self, bounced_time):
		"""
		The method to set the value to bounced_time

		Parameters:
			bounced_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if bounced_time is not None and not isinstance(bounced_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: bounced_time EXPECTED TYPE: datetime', None, None)
		
		self.__bounced_time = bounced_time
		self.__key_modified['bounced_time'] = 1

	def get_bounced_reason(self):
		"""
		The method to get the bounced_reason

		Returns:
			string: A string representing the bounced_reason
		"""

		return self.__bounced_reason

	def set_bounced_reason(self, bounced_reason):
		"""
		The method to set the value to bounced_reason

		Parameters:
			bounced_reason (string) : A string representing the bounced_reason
		"""

		if bounced_reason is not None and not isinstance(bounced_reason, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: bounced_reason EXPECTED TYPE: str', None, None)
		
		self.__bounced_reason = bounced_reason
		self.__key_modified['bounced_reason'] = 1

	def get_category(self):
		"""
		The method to get the category

		Returns:
			string: A string representing the category
		"""

		return self.__category

	def set_category(self, category):
		"""
		The method to set the value to category

		Parameters:
			category (string) : A string representing the category
		"""

		if category is not None and not isinstance(category, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: str', None, None)
		
		self.__category = category
		self.__key_modified['category'] = 1

	def get_sub_category(self):
		"""
		The method to get the sub_category

		Returns:
			string: A string representing the sub_category
		"""

		return self.__sub_category

	def set_sub_category(self, sub_category):
		"""
		The method to set the value to sub_category

		Parameters:
			sub_category (string) : A string representing the sub_category
		"""

		if sub_category is not None and not isinstance(sub_category, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sub_category EXPECTED TYPE: str', None, None)
		
		self.__sub_category = sub_category
		self.__key_modified['sub_category'] = 1

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
