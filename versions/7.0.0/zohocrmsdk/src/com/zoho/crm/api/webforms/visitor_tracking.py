try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class VisitorTracking(object):
	def __init__(self):
		"""Creates an instance of VisitorTracking"""

		self.__portal_name = None
		self.__tracking_code = None
		self.__key_modified = dict()

	def get_portal_name(self):
		"""
		The method to get the portal_name

		Returns:
			string: A string representing the portal_name
		"""

		return self.__portal_name

	def set_portal_name(self, portal_name):
		"""
		The method to set the value to portal_name

		Parameters:
			portal_name (string) : A string representing the portal_name
		"""

		if portal_name is not None and not isinstance(portal_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: portal_name EXPECTED TYPE: str', None, None)
		
		self.__portal_name = portal_name
		self.__key_modified['portal_name'] = 1

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
