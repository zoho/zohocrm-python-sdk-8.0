try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class InventoryDetails(object):
	def __init__(self):
		"""Creates an instance of InventoryDetails"""

		self.__inventory_template = None
		self.__record = None
		self.__paper_type = None
		self.__view_type = None
		self.__key_modified = dict()

	def get_inventory_template(self):
		"""
		The method to get the inventory_template

		Returns:
			InventoryTemplate: An instance of InventoryTemplate
		"""

		return self.__inventory_template

	def set_inventory_template(self, inventory_template):
		"""
		The method to set the value to inventory_template

		Parameters:
			inventory_template (InventoryTemplate) : An instance of InventoryTemplate
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_drafts.inventory_template import InventoryTemplate
		except Exception:
			from .inventory_template import InventoryTemplate

		if inventory_template is not None and not isinstance(inventory_template, InventoryTemplate):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: inventory_template EXPECTED TYPE: InventoryTemplate', None, None)
		
		self.__inventory_template = inventory_template
		self.__key_modified['inventory_template'] = 1

	def get_record(self):
		"""
		The method to get the record

		Returns:
			Record: An instance of Record
		"""

		return self.__record

	def set_record(self, record):
		"""
		The method to set the value to record

		Parameters:
			record (Record) : An instance of Record
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record import Record
		except Exception:
			from ..record import Record

		if record is not None and not isinstance(record, Record):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record EXPECTED TYPE: Record', None, None)
		
		self.__record = record
		self.__key_modified['record'] = 1

	def get_paper_type(self):
		"""
		The method to get the paper_type

		Returns:
			string: A string representing the paper_type
		"""

		return self.__paper_type

	def set_paper_type(self, paper_type):
		"""
		The method to set the value to paper_type

		Parameters:
			paper_type (string) : A string representing the paper_type
		"""

		if paper_type is not None and not isinstance(paper_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: paper_type EXPECTED TYPE: str', None, None)
		
		self.__paper_type = paper_type
		self.__key_modified['paper_type'] = 1

	def get_view_type(self):
		"""
		The method to get the view_type

		Returns:
			string: A string representing the view_type
		"""

		return self.__view_type

	def set_view_type(self, view_type):
		"""
		The method to set the value to view_type

		Parameters:
			view_type (string) : A string representing the view_type
		"""

		if view_type is not None and not isinstance(view_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: view_type EXPECTED TYPE: str', None, None)
		
		self.__view_type = view_type
		self.__key_modified['view_type'] = 1

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
