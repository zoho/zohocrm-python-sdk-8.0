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
			from zohocrmsdk.src.com.zoho.crm.api.send_mail.inventory_template import InventoryTemplate
		except Exception:
			from .inventory_template import InventoryTemplate

		if inventory_template is not None and not isinstance(inventory_template, InventoryTemplate):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: inventory_template EXPECTED TYPE: InventoryTemplate', None, None)
		
		self.__inventory_template = inventory_template
		self.__key_modified['inventory_template'] = 1

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
