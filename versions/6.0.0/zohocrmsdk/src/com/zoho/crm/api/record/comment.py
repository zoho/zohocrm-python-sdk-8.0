try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Comment(object):
	def __init__(self):
		"""Creates an instance of Comment"""

		self.__commented_by = None
		self.__commented_time = None
		self.__comment_content = None
		self.__id = None
		self.__key_modified = dict()

	def get_commented_by(self):
		"""
		The method to get the commented_by

		Returns:
			string: A string representing the commented_by
		"""

		return self.__commented_by

	def set_commented_by(self, commented_by):
		"""
		The method to set the value to commented_by

		Parameters:
			commented_by (string) : A string representing the commented_by
		"""

		if commented_by is not None and not isinstance(commented_by, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: commented_by EXPECTED TYPE: str', None, None)
		
		self.__commented_by = commented_by
		self.__key_modified['commented_by'] = 1

	def get_commented_time(self):
		"""
		The method to get the commented_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__commented_time

	def set_commented_time(self, commented_time):
		"""
		The method to set the value to commented_time

		Parameters:
			commented_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if commented_time is not None and not isinstance(commented_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: commented_time EXPECTED TYPE: datetime', None, None)
		
		self.__commented_time = commented_time
		self.__key_modified['commented_time'] = 1

	def get_comment_content(self):
		"""
		The method to get the comment_content

		Returns:
			string: A string representing the comment_content
		"""

		return self.__comment_content

	def set_comment_content(self, comment_content):
		"""
		The method to set the value to comment_content

		Parameters:
			comment_content (string) : A string representing the comment_content
		"""

		if comment_content is not None and not isinstance(comment_content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: comment_content EXPECTED TYPE: str', None, None)
		
		self.__comment_content = comment_content
		self.__key_modified['comment_content'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

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
