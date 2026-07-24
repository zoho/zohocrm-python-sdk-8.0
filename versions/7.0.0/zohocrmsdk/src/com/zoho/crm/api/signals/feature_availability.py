try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FeatureAvailability(object):
	def __init__(self):
		"""Creates an instance of FeatureAvailability"""

		self.__scoring = None
		self.__signals = None
		self.__key_modified = dict()

	def get_scoring(self):
		"""
		The method to get the scoring

		Returns:
			bool: A bool representing the scoring
		"""

		return self.__scoring

	def set_scoring(self, scoring):
		"""
		The method to set the value to scoring

		Parameters:
			scoring (bool) : A bool representing the scoring
		"""

		if scoring is not None and not isinstance(scoring, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: scoring EXPECTED TYPE: bool', None, None)
		
		self.__scoring = scoring
		self.__key_modified['scoring'] = 1

	def get_signals(self):
		"""
		The method to get the signals

		Returns:
			bool: A bool representing the signals
		"""

		return self.__signals

	def set_signals(self, signals):
		"""
		The method to set the value to signals

		Parameters:
			signals (bool) : A bool representing the signals
		"""

		if signals is not None and not isinstance(signals, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: signals EXPECTED TYPE: bool', None, None)
		
		self.__signals = signals
		self.__key_modified['signals'] = 1

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
