try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ButtonAttributes(object):
	def __init__(self):
		"""Creates an instance of ButtonAttributes"""

		self.__color = None
		self.__name = None
		self.__align = None
		self.__border_radius_px = None
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

	def get_border_radius_px(self):
		"""
		The method to get the border_radius_px

		Returns:
			string: A string representing the border_radius_px
		"""

		return self.__border_radius_px

	def set_border_radius_px(self, border_radius_px):
		"""
		The method to set the value to border_radius_px

		Parameters:
			border_radius_px (string) : A string representing the border_radius_px
		"""

		if border_radius_px is not None and not isinstance(border_radius_px, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: border_radius_px EXPECTED TYPE: str', None, None)
		
		self.__border_radius_px = border_radius_px
		self.__key_modified['border_radius_px'] = 1

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
