try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Assign(object):
	def __init__(self):
		"""Creates an instance of Assign"""

		self.__feature = None
		self.__related_entity_id = None
		self.__page = None
		self.__per_page = None
		self.__id = None
		self.__filters = None
		self.__key_modified = dict()

	def get_feature(self):
		"""
		The method to get the feature

		Returns:
			Choice: An instance of Choice
		"""

		return self.__feature

	def set_feature(self, feature):
		"""
		The method to set the value to feature

		Parameters:
			feature (Choice) : An instance of Choice
		"""

		if feature is not None and not isinstance(feature, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: feature EXPECTED TYPE: Choice', None, None)
		
		self.__feature = feature
		self.__key_modified['feature'] = 1

	def get_related_entity_id(self):
		"""
		The method to get the related_entity_id

		Returns:
			int: An int representing the related_entity_id
		"""

		return self.__related_entity_id

	def set_related_entity_id(self, related_entity_id):
		"""
		The method to set the value to related_entity_id

		Parameters:
			related_entity_id (int) : An int representing the related_entity_id
		"""

		if related_entity_id is not None and not isinstance(related_entity_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_entity_id EXPECTED TYPE: int', None, None)
		
		self.__related_entity_id = related_entity_id
		self.__key_modified['related_entity_id'] = 1

	def get_page(self):
		"""
		The method to get the page

		Returns:
			int: An int representing the page
		"""

		return self.__page

	def set_page(self, page):
		"""
		The method to set the value to page

		Parameters:
			page (int) : An int representing the page
		"""

		if page is not None and not isinstance(page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: page EXPECTED TYPE: int', None, None)
		
		self.__page = page
		self.__key_modified['page'] = 1

	def get_per_page(self):
		"""
		The method to get the per_page

		Returns:
			int: An int representing the per_page
		"""

		return self.__per_page

	def set_per_page(self, per_page):
		"""
		The method to set the value to per_page

		Parameters:
			per_page (int) : An int representing the per_page
		"""

		if per_page is not None and not isinstance(per_page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: per_page EXPECTED TYPE: int', None, None)
		
		self.__per_page = per_page
		self.__key_modified['per_page'] = 1

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

	def get_filters(self):
		"""
		The method to get the filters

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__filters

	def set_filters(self, filters):
		"""
		The method to set the value to filters

		Parameters:
			filters (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_groups.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if filters is not None and not isinstance(filters, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: filters EXPECTED TYPE: Criteria', None, None)
		
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
