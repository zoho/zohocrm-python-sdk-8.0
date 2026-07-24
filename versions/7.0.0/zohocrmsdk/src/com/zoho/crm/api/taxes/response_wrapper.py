try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.taxes.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class ResponseWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of ResponseWrapper"""
		super().__init__()

		self.__org_taxes = None
		self.__key_modified = dict()

	def get_org_taxes(self):
		"""
		The method to get the org_taxes

		Returns:
			OrgTax: An instance of OrgTax
		"""

		return self.__org_taxes

	def set_org_taxes(self, org_taxes):
		"""
		The method to set the value to org_taxes

		Parameters:
			org_taxes (OrgTax) : An instance of OrgTax
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.taxes.org_tax import OrgTax
		except Exception:
			from .org_tax import OrgTax

		if org_taxes is not None and not isinstance(org_taxes, OrgTax):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: org_taxes EXPECTED TYPE: OrgTax', None, None)
		
		self.__org_taxes = org_taxes
		self.__key_modified['org_taxes'] = 1

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
