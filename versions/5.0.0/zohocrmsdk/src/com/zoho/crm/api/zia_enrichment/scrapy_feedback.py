try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class ScrapyFeedback(object):
	def __init__(self):
		"""Creates an instance of ScrapyFeedback"""

		self.__enrich_id = None
		self.__type = None
		self.__feedback = None
		self.__comment = None
		self.__key_modified = dict()

	def get_enrich_id(self):
		"""
		The method to get the enrich_id

		Returns:
			Choice: An instance of Choice
		"""

		return self.__enrich_id

	def set_enrich_id(self, enrich_id):
		"""
		The method to set the value to enrich_id

		Parameters:
			enrich_id (Choice) : An instance of Choice
		"""

		if enrich_id is not None and not isinstance(enrich_id, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: enrich_id EXPECTED TYPE: Choice', None, None)
		
		self.__enrich_id = enrich_id
		self.__key_modified['enrich_id'] = 1

	def get_type(self):
		"""
		The method to get the type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__type

	def set_type(self, type):
		"""
		The method to set the value to type

		Parameters:
			type (Choice) : An instance of Choice
		"""

		if type is not None and not isinstance(type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: type EXPECTED TYPE: Choice', None, None)
		
		self.__type = type
		self.__key_modified['type'] = 1

	def get_feedback(self):
		"""
		The method to get the feedback

		Returns:
			Choice: An instance of Choice
		"""

		return self.__feedback

	def set_feedback(self, feedback):
		"""
		The method to set the value to feedback

		Parameters:
			feedback (Choice) : An instance of Choice
		"""

		if feedback is not None and not isinstance(feedback, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: feedback EXPECTED TYPE: Choice', None, None)
		
		self.__feedback = feedback
		self.__key_modified['feedback'] = 1

	def get_comment(self):
		"""
		The method to get the comment

		Returns:
			string: A string representing the comment
		"""

		return self.__comment

	def set_comment(self, comment):
		"""
		The method to set the value to comment

		Parameters:
			comment (string) : A string representing the comment
		"""

		if comment is not None and not isinstance(comment, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: comment EXPECTED TYPE: str', None, None)
		
		self.__comment = comment
		self.__key_modified['comment'] = 1

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
