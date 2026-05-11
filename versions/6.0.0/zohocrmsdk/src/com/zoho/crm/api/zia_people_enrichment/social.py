try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Social(object):
	def __init__(self):
		"""Creates an instance of Social"""

		self.__twitter = None
		self.__facebook = None
		self.__linkedin = None
		self.__key_modified = dict()

	def get_twitter(self):
		"""
		The method to get the twitter

		Returns:
			string: A string representing the twitter
		"""

		return self.__twitter

	def set_twitter(self, twitter):
		"""
		The method to set the value to twitter

		Parameters:
			twitter (string) : A string representing the twitter
		"""

		if twitter is not None and not isinstance(twitter, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: twitter EXPECTED TYPE: str', None, None)
		
		self.__twitter = twitter
		self.__key_modified['twitter'] = 1

	def get_facebook(self):
		"""
		The method to get the facebook

		Returns:
			string: A string representing the facebook
		"""

		return self.__facebook

	def set_facebook(self, facebook):
		"""
		The method to set the value to facebook

		Parameters:
			facebook (string) : A string representing the facebook
		"""

		if facebook is not None and not isinstance(facebook, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: facebook EXPECTED TYPE: str', None, None)
		
		self.__facebook = facebook
		self.__key_modified['facebook'] = 1

	def get_linkedin(self):
		"""
		The method to get the linkedin

		Returns:
			string: A string representing the linkedin
		"""

		return self.__linkedin

	def set_linkedin(self, linkedin):
		"""
		The method to set the value to linkedin

		Parameters:
			linkedin (string) : A string representing the linkedin
		"""

		if linkedin is not None and not isinstance(linkedin, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: linkedin EXPECTED TYPE: str', None, None)
		
		self.__linkedin = linkedin
		self.__key_modified['linkedin'] = 1

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
