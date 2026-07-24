try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class DataMap(object):
	def __init__(self):
		"""Creates an instance of DataMap"""

		self.__user = None
		self.__features_available = None
		self.__from_address = None
		self.__relay_domains = None
		self.__mergefieldsdata = None
		self.__key_modified = dict()

	def get_user(self):
		"""
		The method to get the user

		Returns:
			User: An instance of User
		"""

		return self.__user

	def set_user(self, user):
		"""
		The method to set the value to user

		Parameters:
			user (User) : An instance of User
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_compose_meta.user import User
		except Exception:
			from .user import User

		if user is not None and not isinstance(user, User):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user EXPECTED TYPE: User', None, None)
		
		self.__user = user
		self.__key_modified['user'] = 1

	def get_features_available(self):
		"""
		The method to get the features_available

		Returns:
			FeaturesAvailable: An instance of FeaturesAvailable
		"""

		return self.__features_available

	def set_features_available(self, features_available):
		"""
		The method to set the value to features_available

		Parameters:
			features_available (FeaturesAvailable) : An instance of FeaturesAvailable
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_compose_meta.features_available import FeaturesAvailable
		except Exception:
			from .features_available import FeaturesAvailable

		if features_available is not None and not isinstance(features_available, FeaturesAvailable):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: features_available EXPECTED TYPE: FeaturesAvailable', None, None)
		
		self.__features_available = features_available
		self.__key_modified['features_available'] = 1

	def get_from_address(self):
		"""
		The method to get the from_address

		Returns:
			list: An instance of list
		"""

		return self.__from_address

	def set_from_address(self, from_address):
		"""
		The method to set the value to from_address

		Parameters:
			from_address (list) : An instance of list
		"""

		if from_address is not None and not isinstance(from_address, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_address EXPECTED TYPE: list', None, None)
		
		self.__from_address = from_address
		self.__key_modified['from_address'] = 1

	def get_relay_domains(self):
		"""
		The method to get the relay_domains

		Returns:
			list: An instance of list
		"""

		return self.__relay_domains

	def set_relay_domains(self, relay_domains):
		"""
		The method to set the value to relay_domains

		Parameters:
			relay_domains (list) : An instance of list
		"""

		if relay_domains is not None and not isinstance(relay_domains, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: relay_domains EXPECTED TYPE: list', None, None)
		
		self.__relay_domains = relay_domains
		self.__key_modified['relay_domains'] = 1

	def get_mergefieldsdata(self):
		"""
		The method to get the mergefieldsdata

		Returns:
			string: A string representing the mergefieldsdata
		"""

		return self.__mergefieldsdata

	def set_mergefieldsdata(self, mergefieldsdata):
		"""
		The method to set the value to mergefieldsdata

		Parameters:
			mergefieldsdata (string) : A string representing the mergefieldsdata
		"""

		if mergefieldsdata is not None and not isinstance(mergefieldsdata, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: mergefieldsdata EXPECTED TYPE: str', None, None)
		
		self.__mergefieldsdata = mergefieldsdata
		self.__key_modified['mergeFieldsData'] = 1

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
