try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class User(object):
	def __init__(self):
		"""Creates an instance of User"""

		self.__full_name = None
		self.__email = None
		self.__zuid = None
		self.__zgid = None
		self.__signature = None
		self.__key_modified = dict()

	def get_full_name(self):
		"""
		The method to get the full_name

		Returns:
			string: A string representing the full_name
		"""

		return self.__full_name

	def set_full_name(self, full_name):
		"""
		The method to set the value to full_name

		Parameters:
			full_name (string) : A string representing the full_name
		"""

		if full_name is not None and not isinstance(full_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: full_name EXPECTED TYPE: str', None, None)
		
		self.__full_name = full_name
		self.__key_modified['full_name'] = 1

	def get_email(self):
		"""
		The method to get the email

		Returns:
			string: A string representing the email
		"""

		return self.__email

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (string) : A string representing the email
		"""

		if email is not None and not isinstance(email, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: str', None, None)
		
		self.__email = email
		self.__key_modified['email'] = 1

	def get_zuid(self):
		"""
		The method to get the zuid

		Returns:
			string: A string representing the zuid
		"""

		return self.__zuid

	def set_zuid(self, zuid):
		"""
		The method to set the value to zuid

		Parameters:
			zuid (string) : A string representing the zuid
		"""

		if zuid is not None and not isinstance(zuid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zuid EXPECTED TYPE: str', None, None)
		
		self.__zuid = zuid
		self.__key_modified['zuid'] = 1

	def get_zgid(self):
		"""
		The method to get the zgid

		Returns:
			string: A string representing the zgid
		"""

		return self.__zgid

	def set_zgid(self, zgid):
		"""
		The method to set the value to zgid

		Parameters:
			zgid (string) : A string representing the zgid
		"""

		if zgid is not None and not isinstance(zgid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zgid EXPECTED TYPE: str', None, None)
		
		self.__zgid = zgid
		self.__key_modified['zgid'] = 1

	def get_signature(self):
		"""
		The method to get the signature

		Returns:
			Signature: An instance of Signature
		"""

		return self.__signature

	def set_signature(self, signature):
		"""
		The method to set the value to signature

		Parameters:
			signature (Signature) : An instance of Signature
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_compose_meta.signature import Signature
		except Exception:
			from .signature import Signature

		if signature is not None and not isinstance(signature, Signature):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: signature EXPECTED TYPE: Signature', None, None)
		
		self.__signature = signature
		self.__key_modified['signature'] = 1

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
