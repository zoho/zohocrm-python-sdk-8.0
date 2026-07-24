try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Choice, Constants
except Exception:
	from ..exception import SDKException
	from ..util import Choice, Constants


class Territories(object):
	def __init__(self):
		"""Creates an instance of Territories"""

		self.__created_time = None
		self.__modified_time = None
		self.__manager = None
		self.__reporting_to = None
		self.__permission_type = None
		self.__modified_by = None
		self.__description = None
		self.__id = None
		self.__created_by = None
		self.__account_rule_criteria = None
		self.__deal_rule_criteria = None
		self.__lead_rule_criteria = None
		self.__name = None
		self.__api_name = None
		self.__key_modified = dict()

	def get_created_time(self):
		"""
		The method to get the created_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__created_time

	def set_created_time(self, created_time):
		"""
		The method to set the value to created_time

		Parameters:
			created_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if created_time is not None and not isinstance(created_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_time EXPECTED TYPE: datetime', None, None)
		
		self.__created_time = created_time
		self.__key_modified['created_time'] = 1

	def get_modified_time(self):
		"""
		The method to get the modified_time

		Returns:
			datetime: An instance of datetime
		"""

		return self.__modified_time

	def set_modified_time(self, modified_time):
		"""
		The method to set the value to modified_time

		Parameters:
			modified_time (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if modified_time is not None and not isinstance(modified_time, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_time EXPECTED TYPE: datetime', None, None)
		
		self.__modified_time = modified_time
		self.__key_modified['modified_time'] = 1

	def get_manager(self):
		"""
		The method to get the manager

		Returns:
			Manager: An instance of Manager
		"""

		return self.__manager

	def set_manager(self, manager):
		"""
		The method to set the value to manager

		Parameters:
			manager (Manager) : An instance of Manager
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.territories.manager import Manager
		except Exception:
			from .manager import Manager

		if manager is not None and not isinstance(manager, Manager):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: manager EXPECTED TYPE: Manager', None, None)
		
		self.__manager = manager
		self.__key_modified['manager'] = 1

	def get_reporting_to(self):
		"""
		The method to get the reporting_to

		Returns:
			ReportingTo: An instance of ReportingTo
		"""

		return self.__reporting_to

	def set_reporting_to(self, reporting_to):
		"""
		The method to set the value to reporting_to

		Parameters:
			reporting_to (ReportingTo) : An instance of ReportingTo
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.territories.reporting_to import ReportingTo
		except Exception:
			from .reporting_to import ReportingTo

		if reporting_to is not None and not isinstance(reporting_to, ReportingTo):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: reporting_to EXPECTED TYPE: ReportingTo', None, None)
		
		self.__reporting_to = reporting_to
		self.__key_modified['reporting_to'] = 1

	def get_permission_type(self):
		"""
		The method to get the permission_type

		Returns:
			Choice: An instance of Choice
		"""

		return self.__permission_type

	def set_permission_type(self, permission_type):
		"""
		The method to set the value to permission_type

		Parameters:
			permission_type (Choice) : An instance of Choice
		"""

		if permission_type is not None and not isinstance(permission_type, Choice):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: permission_type EXPECTED TYPE: Choice', None, None)
		
		self.__permission_type = permission_type
		self.__key_modified['permission_type'] = 1

	def get_modified_by(self):
		"""
		The method to get the modified_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__modified_by

	def set_modified_by(self, modified_by):
		"""
		The method to set the value to modified_by

		Parameters:
			modified_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if modified_by is not None and not isinstance(modified_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modified_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__modified_by = modified_by
		self.__key_modified['modified_by'] = 1

	def get_description(self):
		"""
		The method to get the description

		Returns:
			string: A string representing the description
		"""

		return self.__description

	def set_description(self, description):
		"""
		The method to set the value to description

		Parameters:
			description (string) : A string representing the description
		"""

		if description is not None and not isinstance(description, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: description EXPECTED TYPE: str', None, None)
		
		self.__description = description
		self.__key_modified['description'] = 1

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

	def get_created_by(self):
		"""
		The method to get the created_by

		Returns:
			MinifiedUser: An instance of MinifiedUser
		"""

		return self.__created_by

	def set_created_by(self, created_by):
		"""
		The method to set the value to created_by

		Parameters:
			created_by (MinifiedUser) : An instance of MinifiedUser
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.users import MinifiedUser
		except Exception:
			from ..users import MinifiedUser

		if created_by is not None and not isinstance(created_by, MinifiedUser):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: created_by EXPECTED TYPE: MinifiedUser', None, None)
		
		self.__created_by = created_by
		self.__key_modified['created_by'] = 1

	def get_account_rule_criteria(self):
		"""
		The method to get the account_rule_criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__account_rule_criteria

	def set_account_rule_criteria(self, account_rule_criteria):
		"""
		The method to set the value to account_rule_criteria

		Parameters:
			account_rule_criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.territories.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if account_rule_criteria is not None and not isinstance(account_rule_criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: account_rule_criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__account_rule_criteria = account_rule_criteria
		self.__key_modified['account_rule_criteria'] = 1

	def get_deal_rule_criteria(self):
		"""
		The method to get the deal_rule_criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__deal_rule_criteria

	def set_deal_rule_criteria(self, deal_rule_criteria):
		"""
		The method to set the value to deal_rule_criteria

		Parameters:
			deal_rule_criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.territories.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if deal_rule_criteria is not None and not isinstance(deal_rule_criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal_rule_criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__deal_rule_criteria = deal_rule_criteria
		self.__key_modified['deal_rule_criteria'] = 1

	def get_lead_rule_criteria(self):
		"""
		The method to get the lead_rule_criteria

		Returns:
			Criteria: An instance of Criteria
		"""

		return self.__lead_rule_criteria

	def set_lead_rule_criteria(self, lead_rule_criteria):
		"""
		The method to set the value to lead_rule_criteria

		Parameters:
			lead_rule_criteria (Criteria) : An instance of Criteria
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.territories.criteria import Criteria
		except Exception:
			from .criteria import Criteria

		if lead_rule_criteria is not None and not isinstance(lead_rule_criteria, Criteria):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lead_rule_criteria EXPECTED TYPE: Criteria', None, None)
		
		self.__lead_rule_criteria = lead_rule_criteria
		self.__key_modified['lead_rule_criteria'] = 1

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

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

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
