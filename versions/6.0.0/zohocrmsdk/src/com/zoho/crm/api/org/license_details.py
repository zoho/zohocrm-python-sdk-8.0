try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class LicenseDetails(object):
	def __init__(self):
		"""Creates an instance of LicenseDetails"""

		self.__paid_expiry = None
		self.__users_license_purchased = None
		self.__trial_type = None
		self.__trial_expiry = None
		self.__paid = None
		self.__paid_type = None
		self.__trial_action = None
		self.__key_modified = dict()

	def get_paid_expiry(self):
		"""
		The method to get the paid_expiry

		Returns:
			datetime: An instance of datetime
		"""

		return self.__paid_expiry

	def set_paid_expiry(self, paid_expiry):
		"""
		The method to set the value to paid_expiry

		Parameters:
			paid_expiry (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if paid_expiry is not None and not isinstance(paid_expiry, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: paid_expiry EXPECTED TYPE: datetime', None, None)
		
		self.__paid_expiry = paid_expiry
		self.__key_modified['paid_expiry'] = 1

	def get_users_license_purchased(self):
		"""
		The method to get the users_license_purchased

		Returns:
			int: An int representing the users_license_purchased
		"""

		return self.__users_license_purchased

	def set_users_license_purchased(self, users_license_purchased):
		"""
		The method to set the value to users_license_purchased

		Parameters:
			users_license_purchased (int) : An int representing the users_license_purchased
		"""

		if users_license_purchased is not None and not isinstance(users_license_purchased, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: users_license_purchased EXPECTED TYPE: int', None, None)
		
		self.__users_license_purchased = users_license_purchased
		self.__key_modified['users_license_purchased'] = 1

	def get_trial_type(self):
		"""
		The method to get the trial_type

		Returns:
			string: A string representing the trial_type
		"""

		return self.__trial_type

	def set_trial_type(self, trial_type):
		"""
		The method to set the value to trial_type

		Parameters:
			trial_type (string) : A string representing the trial_type
		"""

		if trial_type is not None and not isinstance(trial_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: trial_type EXPECTED TYPE: str', None, None)
		
		self.__trial_type = trial_type
		self.__key_modified['trial_type'] = 1

	def get_trial_expiry(self):
		"""
		The method to get the trial_expiry

		Returns:
			string: A string representing the trial_expiry
		"""

		return self.__trial_expiry

	def set_trial_expiry(self, trial_expiry):
		"""
		The method to set the value to trial_expiry

		Parameters:
			trial_expiry (string) : A string representing the trial_expiry
		"""

		if trial_expiry is not None and not isinstance(trial_expiry, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: trial_expiry EXPECTED TYPE: str', None, None)
		
		self.__trial_expiry = trial_expiry
		self.__key_modified['trial_expiry'] = 1

	def get_paid(self):
		"""
		The method to get the paid

		Returns:
			bool: A bool representing the paid
		"""

		return self.__paid

	def set_paid(self, paid):
		"""
		The method to set the value to paid

		Parameters:
			paid (bool) : A bool representing the paid
		"""

		if paid is not None and not isinstance(paid, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: paid EXPECTED TYPE: bool', None, None)
		
		self.__paid = paid
		self.__key_modified['paid'] = 1

	def get_paid_type(self):
		"""
		The method to get the paid_type

		Returns:
			string: A string representing the paid_type
		"""

		return self.__paid_type

	def set_paid_type(self, paid_type):
		"""
		The method to set the value to paid_type

		Parameters:
			paid_type (string) : A string representing the paid_type
		"""

		if paid_type is not None and not isinstance(paid_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: paid_type EXPECTED TYPE: str', None, None)
		
		self.__paid_type = paid_type
		self.__key_modified['paid_type'] = 1

	def get_trial_action(self):
		"""
		The method to get the trial_action

		Returns:
			string: A string representing the trial_action
		"""

		return self.__trial_action

	def set_trial_action(self, trial_action):
		"""
		The method to set the value to trial_action

		Parameters:
			trial_action (string) : A string representing the trial_action
		"""

		if trial_action is not None and not isinstance(trial_action, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: trial_action EXPECTED TYPE: str', None, None)
		
		self.__trial_action = trial_action
		self.__key_modified['trial_action'] = 1

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
