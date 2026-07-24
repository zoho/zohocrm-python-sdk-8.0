try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class EmailSignatures(object):
	def __init__(self):
		"""Creates an instance of EmailSignatures"""

		self.__name = None
		self.__from_1 = None
		self.__editor_mode = None
		self.__id = None
		self.__content = None
		self.__key_modified = dict()

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_from(self):
		"""
		The method to get the from

		Returns:
			list: An instance of list
		"""

		return self.__from_1

	def set_from(self, from_1):
		"""
		The method to set the value to from

		Parameters:
			from_1 (list) : An instance of list
		"""

		if from_1 is not None and not isinstance(from_1, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: from_1 EXPECTED TYPE: list', None, None)
		
		self.__from_1 = from_1
		self.__key_modified['from'] = 1

	def get_editor_mode(self):
		"""
		The method to get the editor_mode

		Returns:
			Choice: An instance of Choice
		"""

		return self.__editor_mode

	def set_editor_mode(self, editor_mode):
		"""
		The method to set the value to editor_mode

		Parameters:
			editor_mode (Choice) : An instance of Choice
		"""

		if editor_mode is not None and not isinstance(editor_mode, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: editor_mode EXPECTED TYPE: Choice', None, None)
		
		self.__editor_mode = editor_mode
		self.__key_modified['editor_mode'] = 1

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

	def get_content(self):
		"""
		The method to get the content

		Returns:
			string: A string representing the content
		"""

		return self.__content

	def set_content(self, content):
		"""
		The method to set the value to content

		Parameters:
			content (string) : A string representing the content
		"""

		if content is not None and not isinstance(content, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: content EXPECTED TYPE: str', None, None)
		
		self.__content = content
		self.__key_modified['content'] = 1

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
