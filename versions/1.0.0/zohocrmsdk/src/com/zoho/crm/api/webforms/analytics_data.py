try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class AnalyticsData(object):
	def __init__(self):
		"""Creates an instance of AnalyticsData"""

		self.__iframe_url_tracking_code = None
		self.__url_analytics_enabled = None
		self.__analytics_enabled = None
		self.__analytics_enabled_time = None
		self.__tracking_code = None
		self.__key_modified = dict()

	def get_iframe_url_tracking_code(self):
		"""
		The method to get the iframe_url_tracking_code

		Returns:
			string: A string representing the iframe_url_tracking_code
		"""

		return self.__iframe_url_tracking_code

	def set_iframe_url_tracking_code(self, iframe_url_tracking_code):
		"""
		The method to set the value to iframe_url_tracking_code

		Parameters:
			iframe_url_tracking_code (string) : A string representing the iframe_url_tracking_code
		"""

		if iframe_url_tracking_code is not None and not isinstance(iframe_url_tracking_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: iframe_url_tracking_code EXPECTED TYPE: str', None, None)
		
		self.__iframe_url_tracking_code = iframe_url_tracking_code
		self.__key_modified['iframe_url_tracking_code'] = 1

	def get_url_analytics_enabled(self):
		"""
		The method to get the url_analytics_enabled

		Returns:
			bool: A bool representing the url_analytics_enabled
		"""

		return self.__url_analytics_enabled

	def set_url_analytics_enabled(self, url_analytics_enabled):
		"""
		The method to set the value to url_analytics_enabled

		Parameters:
			url_analytics_enabled (bool) : A bool representing the url_analytics_enabled
		"""

		if url_analytics_enabled is not None and not isinstance(url_analytics_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: url_analytics_enabled EXPECTED TYPE: bool', None, None)
		
		self.__url_analytics_enabled = url_analytics_enabled
		self.__key_modified['url_analytics_enabled'] = 1

	def get_analytics_enabled(self):
		"""
		The method to get the analytics_enabled

		Returns:
			bool: A bool representing the analytics_enabled
		"""

		return self.__analytics_enabled

	def set_analytics_enabled(self, analytics_enabled):
		"""
		The method to set the value to analytics_enabled

		Parameters:
			analytics_enabled (bool) : A bool representing the analytics_enabled
		"""

		if analytics_enabled is not None and not isinstance(analytics_enabled, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: analytics_enabled EXPECTED TYPE: bool', None, None)
		
		self.__analytics_enabled = analytics_enabled
		self.__key_modified['analytics_enabled'] = 1

	def get_analytics_enabled_time(self):
		"""
		The method to get the analytics_enabled_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__analytics_enabled_time

	def set_analytics_enabled_time(self, analytics_enabled_time):
		"""
		The method to set the value to analytics_enabled_time

		Parameters:
			analytics_enabled_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if analytics_enabled_time is not None and not isinstance(analytics_enabled_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: analytics_enabled_time EXPECTED TYPE: datetime', None, None)
		
		self.__analytics_enabled_time = analytics_enabled_time
		self.__key_modified['analytics_enabled_time'] = 1

	def get_tracking_code(self):
		"""
		The method to get the tracking_code

		Returns:
			string: A string representing the tracking_code
		"""

		return self.__tracking_code

	def set_tracking_code(self, tracking_code):
		"""
		The method to set the value to tracking_code

		Parameters:
			tracking_code (string) : A string representing the tracking_code
		"""

		if tracking_code is not None and not isinstance(tracking_code, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tracking_code EXPECTED TYPE: str', None, None)
		
		self.__tracking_code = tracking_code
		self.__key_modified['tracking_code'] = 1

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
