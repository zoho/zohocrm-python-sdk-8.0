try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Approval(object):
	def __init__(self):
		"""Creates an instance of Approval"""

		self.__delegate = None
		self.__approve = None
		self.__reject = None
		self.__resubmit = None
		self.__key_modified = dict()

	def get_delegate(self):
		"""
		The method to get the delegate

		Returns:
			bool: A bool representing the delegate
		"""

		return self.__delegate

	def set_delegate(self, delegate):
		"""
		The method to set the value to delegate

		Parameters:
			delegate (bool) : A bool representing the delegate
		"""

		if delegate is not None and not isinstance(delegate, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delegate EXPECTED TYPE: bool', None, None)
		
		self.__delegate = delegate
		self.__key_modified['delegate'] = 1

	def get_approve(self):
		"""
		The method to get the approve

		Returns:
			bool: A bool representing the approve
		"""

		return self.__approve

	def set_approve(self, approve):
		"""
		The method to set the value to approve

		Parameters:
			approve (bool) : A bool representing the approve
		"""

		if approve is not None and not isinstance(approve, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: approve EXPECTED TYPE: bool', None, None)
		
		self.__approve = approve
		self.__key_modified['approve'] = 1

	def get_reject(self):
		"""
		The method to get the reject

		Returns:
			bool: A bool representing the reject
		"""

		return self.__reject

	def set_reject(self, reject):
		"""
		The method to set the value to reject

		Parameters:
			reject (bool) : A bool representing the reject
		"""

		if reject is not None and not isinstance(reject, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reject EXPECTED TYPE: bool', None, None)
		
		self.__reject = reject
		self.__key_modified['reject'] = 1

	def get_resubmit(self):
		"""
		The method to get the resubmit

		Returns:
			bool: A bool representing the resubmit
		"""

		return self.__resubmit

	def set_resubmit(self, resubmit):
		"""
		The method to set the value to resubmit

		Parameters:
			resubmit (bool) : A bool representing the resubmit
		"""

		if resubmit is not None and not isinstance(resubmit, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: resubmit EXPECTED TYPE: bool', None, None)
		
		self.__resubmit = resubmit
		self.__key_modified['resubmit'] = 1

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
