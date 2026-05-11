try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Params(object):
	def __init__(self):
		"""Creates an instance of Params"""

		self.__approved = None
		self.__converted = None
		self.__associated = None
		self.__category = None
		self.__approval_state = None
		self.__filters = None
		self.__key_modified = dict()

	def get_approved(self):
		"""
		The method to get the approved

		Returns:
			bool: A bool representing the approved
		"""

		return self.__approved

	def set_approved(self, approved):
		"""
		The method to set the value to approved

		Parameters:
			approved (bool) : A bool representing the approved
		"""

		if approved is not None and not isinstance(approved, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: approved EXPECTED TYPE: bool', None, None)
		
		self.__approved = approved
		self.__key_modified['approved'] = 1

	def get_converted(self):
		"""
		The method to get the converted

		Returns:
			bool: A bool representing the converted
		"""

		return self.__converted

	def set_converted(self, converted):
		"""
		The method to set the value to converted

		Parameters:
			converted (bool) : A bool representing the converted
		"""

		if converted is not None and not isinstance(converted, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: converted EXPECTED TYPE: bool', None, None)
		
		self.__converted = converted
		self.__key_modified['converted'] = 1

	def get_associated(self):
		"""
		The method to get the associated

		Returns:
			bool: A bool representing the associated
		"""

		return self.__associated

	def set_associated(self, associated):
		"""
		The method to set the value to associated

		Parameters:
			associated (bool) : A bool representing the associated
		"""

		if associated is not None and not isinstance(associated, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: associated EXPECTED TYPE: bool', None, None)
		
		self.__associated = associated
		self.__key_modified['associated'] = 1

	def get_category(self):
		"""
		The method to get the category

		Returns:
			Choice: An instance of Choice
		"""

		return self.__category

	def set_category(self, category):
		"""
		The method to set the value to category

		Parameters:
			category (Choice) : An instance of Choice
		"""

		if category is not None and not isinstance(category, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: category EXPECTED TYPE: Choice', None, None)
		
		self.__category = category
		self.__key_modified['category'] = 1

	def get_approval_state(self):
		"""
		The method to get the approval_state

		Returns:
			Choice: An instance of Choice
		"""

		return self.__approval_state

	def set_approval_state(self, approval_state):
		"""
		The method to set the value to approval_state

		Parameters:
			approval_state (Choice) : An instance of Choice
		"""

		if approval_state is not None and not isinstance(approval_state, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: approval_state EXPECTED TYPE: Choice', None, None)
		
		self.__approval_state = approval_state
		self.__key_modified['approval_state'] = 1

	def get_filters(self):
		"""
		The method to get the filters

		Returns:
			Filters: An instance of Filters
		"""

		return self.__filters

	def set_filters(self, filters):
		"""
		The method to set the value to filters

		Parameters:
			filters (Filters) : An instance of Filters
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.get_related_records_count.filters import Filters
		except Exception:
			from .filters import Filters

		if filters is not None and not isinstance(filters, Filters):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: filters EXPECTED TYPE: Filters', None, None)
		
		self.__filters = filters
		self.__key_modified['filters'] = 1

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
