try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Address(object):
	def __init__(self):
		"""Creates an instance of Address"""

		self.__country = None
		self.__city = None
		self.__pin_code = None
		self.__state = None
		self.__fill_address = None
		self.__key_modified = dict()

	def get_country(self):
		"""
		The method to get the country

		Returns:
			string: A string representing the country
		"""

		return self.__country

	def set_country(self, country):
		"""
		The method to set the value to country

		Parameters:
			country (string) : A string representing the country
		"""

		if country is not None and not isinstance(country, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: country EXPECTED TYPE: str', None, None)
		
		self.__country = country
		self.__key_modified['country'] = 1

	def get_city(self):
		"""
		The method to get the city

		Returns:
			string: A string representing the city
		"""

		return self.__city

	def set_city(self, city):
		"""
		The method to set the value to city

		Parameters:
			city (string) : A string representing the city
		"""

		if city is not None and not isinstance(city, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: city EXPECTED TYPE: str', None, None)
		
		self.__city = city
		self.__key_modified['city'] = 1

	def get_pin_code(self):
		"""
		The method to get the pin_code

		Returns:
			string: A string representing the pin_code
		"""

		return self.__pin_code

	def set_pin_code(self, pin_code):
		"""
		The method to set the value to pin_code

		Parameters:
			pin_code (string) : A string representing the pin_code
		"""

		if pin_code is not None and not isinstance(pin_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: pin_code EXPECTED TYPE: str', None, None)
		
		self.__pin_code = pin_code
		self.__key_modified['pin_code'] = 1

	def get_state(self):
		"""
		The method to get the state

		Returns:
			string: A string representing the state
		"""

		return self.__state

	def set_state(self, state):
		"""
		The method to set the value to state

		Parameters:
			state (string) : A string representing the state
		"""

		if state is not None and not isinstance(state, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: state EXPECTED TYPE: str', None, None)
		
		self.__state = state
		self.__key_modified['state'] = 1

	def get_fill_address(self):
		"""
		The method to get the fill_address

		Returns:
			string: A string representing the fill_address
		"""

		return self.__fill_address

	def set_fill_address(self, fill_address):
		"""
		The method to set the value to fill_address

		Parameters:
			fill_address (string) : A string representing the fill_address
		"""

		if fill_address is not None and not isinstance(fill_address, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fill_address EXPECTED TYPE: str', None, None)
		
		self.__fill_address = fill_address
		self.__key_modified['fill_address'] = 1

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
