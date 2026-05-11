try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ExecutionDetail(object):
	def __init__(self):
		"""Creates an instance of ExecutionDetail"""

		self.__unenroll_properties = None
		self.__end_date = None
		self.__automatic_unenroll = None
		self.__type = None
		self.__execute_every = None
		self.__key_modified = dict()

	def get_unenroll_properties(self):
		"""
		The method to get the unenroll_properties

		Returns:
			UnenrollProperty: An instance of UnenrollProperty
		"""

		return self.__unenroll_properties

	def set_unenroll_properties(self, unenroll_properties):
		"""
		The method to set the value to unenroll_properties

		Parameters:
			unenroll_properties (UnenrollProperty) : An instance of UnenrollProperty
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences.unenroll_property import UnenrollProperty
		except Exception:
			from .unenroll_property import UnenrollProperty

		if unenroll_properties is not None and not isinstance(unenroll_properties, UnenrollProperty):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: unenroll_properties EXPECTED TYPE: UnenrollProperty', None, None)
		
		self.__unenroll_properties = unenroll_properties
		self.__key_modified['unenroll_properties'] = 1

	def get_end_date(self):
		"""
		The method to get the end_date

		Returns:
			string: A string representing the end_date
		"""

		return self.__end_date

	def set_end_date(self, end_date):
		"""
		The method to set the value to end_date

		Parameters:
			end_date (string) : A string representing the end_date
		"""

		if end_date is not None and not isinstance(end_date, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: end_date EXPECTED TYPE: str', None, None)
		
		self.__end_date = end_date
		self.__key_modified['end_date'] = 1

	def get_automatic_unenroll(self):
		"""
		The method to get the automatic_unenroll

		Returns:
			bool: A bool representing the automatic_unenroll
		"""

		return self.__automatic_unenroll

	def set_automatic_unenroll(self, automatic_unenroll):
		"""
		The method to set the value to automatic_unenroll

		Parameters:
			automatic_unenroll (bool) : A bool representing the automatic_unenroll
		"""

		if automatic_unenroll is not None and not isinstance(automatic_unenroll, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: automatic_unenroll EXPECTED TYPE: bool', None, None)
		
		self.__automatic_unenroll = automatic_unenroll
		self.__key_modified['automatic_unenroll'] = 1

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

	def get_execute_every(self):
		"""
		The method to get the execute_every

		Returns:
			ExecuteEvery: An instance of ExecuteEvery
		"""

		return self.__execute_every

	def set_execute_every(self, execute_every):
		"""
		The method to set the value to execute_every

		Parameters:
			execute_every (ExecuteEvery) : An instance of ExecuteEvery
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cadences.execute_every import ExecuteEvery
		except Exception:
			from .execute_every import ExecuteEvery

		if execute_every is not None and not isinstance(execute_every, ExecuteEvery):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: execute_every EXPECTED TYPE: ExecuteEvery', None, None)
		
		self.__execute_every = execute_every
		self.__key_modified['execute_every'] = 1

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
