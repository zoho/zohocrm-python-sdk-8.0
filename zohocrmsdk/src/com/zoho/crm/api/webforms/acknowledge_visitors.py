try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AcknowledgeVisitors(object):
	def __init__(self):
		"""Creates an instance of AcknowledgeVisitors"""

		self.__template_name = None
		self.__template_id = None
		self.__from_address = None
		self.__key_modified = dict()

	def get_template_name(self):
		"""
		The method to get the template_name

		Returns:
			string: A string representing the template_name
		"""

		return self.__template_name

	def set_template_name(self, template_name):
		"""
		The method to set the value to template_name

		Parameters:
			template_name (string) : A string representing the template_name
		"""

		if template_name is not None and not isinstance(template_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: template_name EXPECTED TYPE: str', None, None)
		
		self.__template_name = template_name
		self.__key_modified['template_name'] = 1

	def get_template_id(self):
		"""
		The method to get the template_id

		Returns:
			int: An int representing the template_id
		"""

		return self.__template_id

	def set_template_id(self, template_id):
		"""
		The method to set the value to template_id

		Parameters:
			template_id (int) : An int representing the template_id
		"""

		if template_id is not None and not isinstance(template_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: template_id EXPECTED TYPE: int', None, None)
		
		self.__template_id = template_id
		self.__key_modified['template_id'] = 1

	def get_from_address(self):
		"""
		The method to get the from_address

		Returns:
			FromAddress: An instance of FromAddress
		"""

		return self.__from_address

	def set_from_address(self, from_address):
		"""
		The method to set the value to from_address

		Parameters:
			from_address (FromAddress) : An instance of FromAddress
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.from_address import FromAddress
		except Exception:
			from .from_address import FromAddress

		if from_address is not None and not isinstance(from_address, FromAddress):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_address EXPECTED TYPE: FromAddress', None, None)
		
		self.__from_address = from_address
		self.__key_modified['from_address'] = 1

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
