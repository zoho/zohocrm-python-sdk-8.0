try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class BaseCurrency(object):
	def __init__(self):
		"""Creates an instance of BaseCurrency"""

		self.__iso_code = None
		self.__symbol = None
		self.__created_time = None
		self.__is_active = None
		self.__exchange_rate = None
		self.__format = None
		self.__created_by = None
		self.__prefix_symbol = None
		self.__is_base = None
		self.__modified_time = None
		self.__name = None
		self.__modified_by = None
		self.__id = None
		self.__key_modified = dict()

	def get_iso_code(self):
		"""
		The method to get the iso_code

		Returns:
			string: A string representing the iso_code
		"""

		return self.__iso_code

	def set_iso_code(self, iso_code):
		"""
		The method to set the value to iso_code

		Parameters:
			iso_code (string) : A string representing the iso_code
		"""

		if iso_code is not None and not isinstance(iso_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: iso_code EXPECTED TYPE: str', None, None)
		
		self.__iso_code = iso_code
		self.__key_modified['iso_code'] = 1

	def get_symbol(self):
		"""
		The method to get the symbol

		Returns:
			string: A string representing the symbol
		"""

		return self.__symbol

	def set_symbol(self, symbol):
		"""
		The method to set the value to symbol

		Parameters:
			symbol (string) : A string representing the symbol
		"""

		if symbol is not None and not isinstance(symbol, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: symbol EXPECTED TYPE: str', None, None)
		
		self.__symbol = symbol
		self.__key_modified['symbol'] = 1

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_is_active(self):
		"""
		The method to get the is_active

		Returns:
			bool: A bool representing the is_active
		"""

		return self.__is_active

	def set_is_active(self, is_active):
		"""
		The method to set the value to is_active

		Parameters:
			is_active (bool) : A bool representing the is_active
		"""

		if is_active is not None and not isinstance(is_active, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: is_active EXPECTED TYPE: bool', None, None)
		
		self.__is_active = is_active
		self.__key_modified['is_active'] = 1

	def get_exchange_rate(self):
		"""
		The method to get the exchange_rate

		Returns:
			string: A string representing the exchange_rate
		"""

		return self.__exchange_rate

	def set_exchange_rate(self, exchange_rate):
		"""
		The method to set the value to exchange_rate

		Parameters:
			exchange_rate (string) : A string representing the exchange_rate
		"""

		if exchange_rate is not None and not isinstance(exchange_rate, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: exchange_rate EXPECTED TYPE: str', None, None)
		
		self.__exchange_rate = exchange_rate
		self.__key_modified['exchange_rate'] = 1

	def get_format(self):
		"""
		The method to get the format

		Returns:
			Format: An instance of Format
		"""

		return self.__format

	def set_format(self, format):
		"""
		The method to set the value to format

		Parameters:
			format (Format) : An instance of Format
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.format import Format
		except Exception:
			from .format import Format

		if format is not None and not isinstance(format, Format):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: format EXPECTED TYPE: Format', None, None)
		
		self.__format = format
		self.__key_modified['format'] = 1

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if created_by is not None and not isinstance(created_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_prefix_symbol(self):
		"""
		The method to get the prefix_symbol

		Returns:
			bool: A bool representing the prefix_symbol
		"""

		return self.__prefix_symbol

	def set_prefix_symbol(self, prefix_symbol):
		"""
		The method to set the value to prefix_symbol

		Parameters:
			prefix_symbol (bool) : A bool representing the prefix_symbol
		"""

		if prefix_symbol is not None and not isinstance(prefix_symbol, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: prefix_symbol EXPECTED TYPE: bool', None, None)
		
		self.__prefix_symbol = prefix_symbol
		self.__key_modified['prefix_symbol'] = 1

	def get_is_base(self):
		"""
		The method to get the is_base

		Returns:
			bool: A bool representing the is_base
		"""

		return self.__is_base

	def set_is_base(self, is_base):
		"""
		The method to set the value to is_base

		Parameters:
			is_base (bool) : A bool representing the is_base
		"""

		if is_base is not None and not isinstance(is_base, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: is_base EXPECTED TYPE: bool', None, None)
		
		self.__is_base = is_base
		self.__key_modified['is_base'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if modified_by is not None and not isinstance(modified_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

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
