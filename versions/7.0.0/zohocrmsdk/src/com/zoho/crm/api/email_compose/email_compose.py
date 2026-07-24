try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class EmailCompose(object):
	def __init__(self):
		"""Creates an instance of EmailCompose"""

		self.__default_from_address = None
		self.__default_replyto_address = None
		self.__font = None
		self.__type = None
		self.__key_modified = dict()

	def get_default_from_address(self):
		"""
		The method to get the default_from_address

		Returns:
			DefaultFromAddress: An instance of DefaultFromAddress
		"""

		return self.__default_from_address

	def set_default_from_address(self, default_from_address):
		"""
		The method to set the value to default_from_address

		Parameters:
			default_from_address (DefaultFromAddress) : An instance of DefaultFromAddress
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_compose.default_from_address import DefaultFromAddress
		except Exception:
			from .default_from_address import DefaultFromAddress

		if default_from_address is not None and not isinstance(default_from_address, DefaultFromAddress):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_from_address EXPECTED TYPE: DefaultFromAddress', None, None)
		
		self.__default_from_address = default_from_address
		self.__key_modified['default_from_address'] = 1

	def get_default_replyto_address(self):
		"""
		The method to get the default_replyto_address

		Returns:
			DefaultReplytoAddress: An instance of DefaultReplytoAddress
		"""

		return self.__default_replyto_address

	def set_default_replyto_address(self, default_replyto_address):
		"""
		The method to set the value to default_replyto_address

		Parameters:
			default_replyto_address (DefaultReplytoAddress) : An instance of DefaultReplytoAddress
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_compose.default_replyto_address import DefaultReplytoAddress
		except Exception:
			from .default_replyto_address import DefaultReplytoAddress

		if default_replyto_address is not None and not isinstance(default_replyto_address, DefaultReplytoAddress):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_replyto_address EXPECTED TYPE: DefaultReplytoAddress', None, None)
		
		self.__default_replyto_address = default_replyto_address
		self.__key_modified['default_replyto_address'] = 1

	def get_font(self):
		"""
		The method to get the font

		Returns:
			Font: An instance of Font
		"""

		return self.__font

	def set_font(self, font):
		"""
		The method to set the value to font

		Parameters:
			font (Font) : An instance of Font
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_compose.font import Font
		except Exception:
			from .font import Font

		if font is not None and not isinstance(font, Font):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: font EXPECTED TYPE: Font', None, None)
		
		self.__font = font
		self.__key_modified['font'] = 1

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
