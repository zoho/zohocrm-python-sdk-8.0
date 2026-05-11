try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class LastVersionStatistics(object):
	def __init__(self):
		"""Creates an instance of LastVersionStatistics"""

		self.__tracked = None
		self.__delivered = None
		self.__opened = None
		self.__bounced = None
		self.__sent = None
		self.__clicked = None
		self.__key_modified = dict()

	def get_tracked(self):
		"""
		The method to get the tracked

		Returns:
			int: An int representing the tracked
		"""

		return self.__tracked

	def set_tracked(self, tracked):
		"""
		The method to set the value to tracked

		Parameters:
			tracked (int) : An int representing the tracked
		"""

		if tracked is not None and not isinstance(tracked, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: tracked EXPECTED TYPE: int', None, None)
		
		self.__tracked = tracked
		self.__key_modified['tracked'] = 1

	def get_delivered(self):
		"""
		The method to get the delivered

		Returns:
			int: An int representing the delivered
		"""

		return self.__delivered

	def set_delivered(self, delivered):
		"""
		The method to set the value to delivered

		Parameters:
			delivered (int) : An int representing the delivered
		"""

		if delivered is not None and not isinstance(delivered, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delivered EXPECTED TYPE: int', None, None)
		
		self.__delivered = delivered
		self.__key_modified['delivered'] = 1

	def get_opened(self):
		"""
		The method to get the opened

		Returns:
			int: An int representing the opened
		"""

		return self.__opened

	def set_opened(self, opened):
		"""
		The method to set the value to opened

		Parameters:
			opened (int) : An int representing the opened
		"""

		if opened is not None and not isinstance(opened, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: opened EXPECTED TYPE: int', None, None)
		
		self.__opened = opened
		self.__key_modified['opened'] = 1

	def get_bounced(self):
		"""
		The method to get the bounced

		Returns:
			int: An int representing the bounced
		"""

		return self.__bounced

	def set_bounced(self, bounced):
		"""
		The method to set the value to bounced

		Parameters:
			bounced (int) : An int representing the bounced
		"""

		if bounced is not None and not isinstance(bounced, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: bounced EXPECTED TYPE: int', None, None)
		
		self.__bounced = bounced
		self.__key_modified['bounced'] = 1

	def get_sent(self):
		"""
		The method to get the sent

		Returns:
			int: An int representing the sent
		"""

		return self.__sent

	def set_sent(self, sent):
		"""
		The method to set the value to sent

		Parameters:
			sent (int) : An int representing the sent
		"""

		if sent is not None and not isinstance(sent, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: sent EXPECTED TYPE: int', None, None)
		
		self.__sent = sent
		self.__key_modified['sent'] = 1

	def get_clicked(self):
		"""
		The method to get the clicked

		Returns:
			int: An int representing the clicked
		"""

		return self.__clicked

	def set_clicked(self, clicked):
		"""
		The method to set the value to clicked

		Parameters:
			clicked (int) : An int representing the clicked
		"""

		if clicked is not None and not isinstance(clicked, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: clicked EXPECTED TYPE: int', None, None)
		
		self.__clicked = clicked
		self.__key_modified['clicked'] = 1

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
