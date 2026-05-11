try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AnalyticsAlert(object):
	def __init__(self):
		"""Creates an instance of AnalyticsAlert"""

		self.__email_count = None
		self.__cliked_email_count = None
		self.__bounced_email_count = None
		self.__replied_email_count = None
		self.__email_spam_count = None
		self.__sent_email_count = None
		self.__unsent_email_count = None
		self.__opened_email_count = None
		self.__unsubscribed_email_count = None
		self.__key_modified = dict()

	def get_email_count(self):
		"""
		The method to get the email_count

		Returns:
			int: An int representing the email_count
		"""

		return self.__email_count

	def set_email_count(self, email_count):
		"""
		The method to set the value to email_count

		Parameters:
			email_count (int) : An int representing the email_count
		"""

		if email_count is not None and not isinstance(email_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_count EXPECTED TYPE: int', None, None)
		
		self.__email_count = email_count
		self.__key_modified['email_count'] = 1

	def get_cliked_email_count(self):
		"""
		The method to get the cliked_email_count

		Returns:
			int: An int representing the cliked_email_count
		"""

		return self.__cliked_email_count

	def set_cliked_email_count(self, cliked_email_count):
		"""
		The method to set the value to cliked_email_count

		Parameters:
			cliked_email_count (int) : An int representing the cliked_email_count
		"""

		if cliked_email_count is not None and not isinstance(cliked_email_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cliked_email_count EXPECTED TYPE: int', None, None)
		
		self.__cliked_email_count = cliked_email_count
		self.__key_modified['cliked_email_count'] = 1

	def get_bounced_email_count(self):
		"""
		The method to get the bounced_email_count

		Returns:
			int: An int representing the bounced_email_count
		"""

		return self.__bounced_email_count

	def set_bounced_email_count(self, bounced_email_count):
		"""
		The method to set the value to bounced_email_count

		Parameters:
			bounced_email_count (int) : An int representing the bounced_email_count
		"""

		if bounced_email_count is not None and not isinstance(bounced_email_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: bounced_email_count EXPECTED TYPE: int', None, None)
		
		self.__bounced_email_count = bounced_email_count
		self.__key_modified['bounced_email_count'] = 1

	def get_replied_email_count(self):
		"""
		The method to get the replied_email_count

		Returns:
			int: An int representing the replied_email_count
		"""

		return self.__replied_email_count

	def set_replied_email_count(self, replied_email_count):
		"""
		The method to set the value to replied_email_count

		Parameters:
			replied_email_count (int) : An int representing the replied_email_count
		"""

		if replied_email_count is not None and not isinstance(replied_email_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: replied_email_count EXPECTED TYPE: int', None, None)
		
		self.__replied_email_count = replied_email_count
		self.__key_modified['replied_email_count'] = 1

	def get_email_spam_count(self):
		"""
		The method to get the email_spam_count

		Returns:
			int: An int representing the email_spam_count
		"""

		return self.__email_spam_count

	def set_email_spam_count(self, email_spam_count):
		"""
		The method to set the value to email_spam_count

		Parameters:
			email_spam_count (int) : An int representing the email_spam_count
		"""

		if email_spam_count is not None and not isinstance(email_spam_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_spam_count EXPECTED TYPE: int', None, None)
		
		self.__email_spam_count = email_spam_count
		self.__key_modified['email_spam_count'] = 1

	def get_sent_email_count(self):
		"""
		The method to get the sent_email_count

		Returns:
			int: An int representing the sent_email_count
		"""

		return self.__sent_email_count

	def set_sent_email_count(self, sent_email_count):
		"""
		The method to set the value to sent_email_count

		Parameters:
			sent_email_count (int) : An int representing the sent_email_count
		"""

		if sent_email_count is not None and not isinstance(sent_email_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sent_email_count EXPECTED TYPE: int', None, None)
		
		self.__sent_email_count = sent_email_count
		self.__key_modified['sent_email_count'] = 1

	def get_unsent_email_count(self):
		"""
		The method to get the unsent_email_count

		Returns:
			int: An int representing the unsent_email_count
		"""

		return self.__unsent_email_count

	def set_unsent_email_count(self, unsent_email_count):
		"""
		The method to set the value to unsent_email_count

		Parameters:
			unsent_email_count (int) : An int representing the unsent_email_count
		"""

		if unsent_email_count is not None and not isinstance(unsent_email_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: unsent_email_count EXPECTED TYPE: int', None, None)
		
		self.__unsent_email_count = unsent_email_count
		self.__key_modified['unsent_email_count'] = 1

	def get_opened_email_count(self):
		"""
		The method to get the opened_email_count

		Returns:
			int: An int representing the opened_email_count
		"""

		return self.__opened_email_count

	def set_opened_email_count(self, opened_email_count):
		"""
		The method to set the value to opened_email_count

		Parameters:
			opened_email_count (int) : An int representing the opened_email_count
		"""

		if opened_email_count is not None and not isinstance(opened_email_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: opened_email_count EXPECTED TYPE: int', None, None)
		
		self.__opened_email_count = opened_email_count
		self.__key_modified['opened_email_count'] = 1

	def get_unsubscribed_email_count(self):
		"""
		The method to get the unsubscribed_email_count

		Returns:
			int: An int representing the unsubscribed_email_count
		"""

		return self.__unsubscribed_email_count

	def set_unsubscribed_email_count(self, unsubscribed_email_count):
		"""
		The method to set the value to unsubscribed_email_count

		Parameters:
			unsubscribed_email_count (int) : An int representing the unsubscribed_email_count
		"""

		if unsubscribed_email_count is not None and not isinstance(unsubscribed_email_count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: unsubscribed_email_count EXPECTED TYPE: int', None, None)
		
		self.__unsubscribed_email_count = unsubscribed_email_count
		self.__key_modified['unsubscribed_email_count'] = 1

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
