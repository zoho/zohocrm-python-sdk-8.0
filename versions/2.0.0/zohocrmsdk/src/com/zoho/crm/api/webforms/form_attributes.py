try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FormAttributes(object):
	def __init__(self):
		"""Creates an instance of FormAttributes"""

		self.__color = None
		self.__width = None
		self.__font_attributes = None
		self.__align = None
		self.__display_form_name = None
		self.__key_modified = dict()

	def get_color(self):
		"""
		The method to get the color

		Returns:
			string: A string representing the color
		"""

		return self.__color

	def set_color(self, color):
		"""
		The method to set the value to color

		Parameters:
			color (string) : A string representing the color
		"""

		if color is not None and not isinstance(color, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: color EXPECTED TYPE: str', None, None)
		
		self.__color = color
		self.__key_modified['color'] = 1

	def get_width(self):
		"""
		The method to get the width

		Returns:
			int: An int representing the width
		"""

		return self.__width

	def set_width(self, width):
		"""
		The method to set the value to width

		Parameters:
			width (int) : An int representing the width
		"""

		if width is not None and not isinstance(width, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: width EXPECTED TYPE: int', None, None)
		
		self.__width = width
		self.__key_modified['width'] = 1

	def get_font_attributes(self):
		"""
		The method to get the font_attributes

		Returns:
			FontAttributes: An instance of FontAttributes
		"""

		return self.__font_attributes

	def set_font_attributes(self, font_attributes):
		"""
		The method to set the value to font_attributes

		Parameters:
			font_attributes (FontAttributes) : An instance of FontAttributes
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.webforms.font_attributes import FontAttributes
		except Exception:
			from .font_attributes import FontAttributes

		if font_attributes is not None and not isinstance(font_attributes, FontAttributes):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: font_attributes EXPECTED TYPE: FontAttributes', None, None)
		
		self.__font_attributes = font_attributes
		self.__key_modified['font_attributes'] = 1

	def get_align(self):
		"""
		The method to get the align

		Returns:
			string: A string representing the align
		"""

		return self.__align

	def set_align(self, align):
		"""
		The method to set the value to align

		Parameters:
			align (string) : A string representing the align
		"""

		if align is not None and not isinstance(align, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: align EXPECTED TYPE: str', None, None)
		
		self.__align = align
		self.__key_modified['align'] = 1

	def get_display_form_name(self):
		"""
		The method to get the display_form_name

		Returns:
			string: A string representing the display_form_name
		"""

		return self.__display_form_name

	def set_display_form_name(self, display_form_name):
		"""
		The method to set the value to display_form_name

		Parameters:
			display_form_name (string) : A string representing the display_form_name
		"""

		if display_form_name is not None and not isinstance(display_form_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_form_name EXPECTED TYPE: str', None, None)
		
		self.__display_form_name = display_form_name
		self.__key_modified['display_form_name'] = 1

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
