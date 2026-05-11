try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ScrapyActionWrapper(object):
	def __init__(self):
		"""Creates an instance of ScrapyActionWrapper"""

		self.__scrapy_feedback = None
		self.__key_modified = dict()

	def get_scrapy_feedback(self):
		"""
		The method to get the scrapy_feedback

		Returns:
			ScrapyActionResponse: An instance of ScrapyActionResponse
		"""

		return self.__scrapy_feedback

	def set_scrapy_feedback(self, scrapy_feedback):
		"""
		The method to set the value to scrapy_feedback

		Parameters:
			scrapy_feedback (ScrapyActionResponse) : An instance of ScrapyActionResponse
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_enrichment.scrapy_action_response import ScrapyActionResponse
		except Exception:
			from .scrapy_action_response import ScrapyActionResponse

		if scrapy_feedback is not None and not isinstance(scrapy_feedback, ScrapyActionResponse):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: scrapy_feedback EXPECTED TYPE: ScrapyActionResponse', None, None)
		
		self.__scrapy_feedback = scrapy_feedback
		self.__key_modified['scrapy_feedback'] = 1

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
