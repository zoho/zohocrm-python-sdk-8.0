try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Currency(object):
	def __init__(self):
		"""Creates an instance of Currency"""

		self.__display_value = None
		self.__decimal_separator = None
		self.__symbol = None
		self.__thousand_separator = None
		self.__display_name = None
		self.__iso_code = None
		self.__decimal_places = None
		self.__key_modified = dict()

	def get_display_value(self):
		"""
		The method to get the display_value

		Returns:
			string: A string representing the display_value
		"""

		return self.__display_value

	def set_display_value(self, display_value):
		"""
		The method to set the value to display_value

		Parameters:
			display_value (string) : A string representing the display_value
		"""

		if display_value is not None and not isinstance(display_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_value EXPECTED TYPE: str', None, None)
		
		self.__display_value = display_value
		self.__key_modified['display_value'] = 1

	def get_decimal_separator(self):
		"""
		The method to get the decimal_separator

		Returns:
			string: A string representing the decimal_separator
		"""

		return self.__decimal_separator

	def set_decimal_separator(self, decimal_separator):
		"""
		The method to set the value to decimal_separator

		Parameters:
			decimal_separator (string) : A string representing the decimal_separator
		"""

		if decimal_separator is not None and not isinstance(decimal_separator, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: decimal_separator EXPECTED TYPE: str', None, None)
		
		self.__decimal_separator = decimal_separator
		self.__key_modified['decimal_separator'] = 1

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

	def get_thousand_separator(self):
		"""
		The method to get the thousand_separator

		Returns:
			string: A string representing the thousand_separator
		"""

		return self.__thousand_separator

	def set_thousand_separator(self, thousand_separator):
		"""
		The method to set the value to thousand_separator

		Parameters:
			thousand_separator (string) : A string representing the thousand_separator
		"""

		if thousand_separator is not None and not isinstance(thousand_separator, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: thousand_separator EXPECTED TYPE: str', None, None)
		
		self.__thousand_separator = thousand_separator
		self.__key_modified['thousand_separator'] = 1

	def get_display_name(self):
		"""
		The method to get the display_name

		Returns:
			string: A string representing the display_name
		"""

		return self.__display_name

	def set_display_name(self, display_name):
		"""
		The method to set the value to display_name

		Parameters:
			display_name (string) : A string representing the display_name
		"""

		if display_name is not None and not isinstance(display_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_name EXPECTED TYPE: str', None, None)
		
		self.__display_name = display_name
		self.__key_modified['display_name'] = 1

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

	def get_decimal_places(self):
		"""
		The method to get the decimal_places

		Returns:
			string: A string representing the decimal_places
		"""

		return self.__decimal_places

	def set_decimal_places(self, decimal_places):
		"""
		The method to set the value to decimal_places

		Parameters:
			decimal_places (string) : A string representing the decimal_places
		"""

		if decimal_places is not None and not isinstance(decimal_places, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: decimal_places EXPECTED TYPE: str', None, None)
		
		self.__decimal_places = decimal_places
		self.__key_modified['decimal_places'] = 1

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
