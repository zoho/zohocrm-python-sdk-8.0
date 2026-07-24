try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class TerritoryUsersOperations(object):
	def __init__(self):
		"""Creates an instance of TerritoryUsersOperations"""
		pass

	def get_territory_users(self, territory):
		"""
		The method to get territory users

		Parameters:
			territory (int) : An int representing the territory

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/territories/'
		api_path = api_path + str(territory)
		api_path = api_path + '/users'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.territory_users.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_territory_users(self, territory, request):
		"""
		The method to update territory users

		Parameters:
			territory (int) : An int representing the territory
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.territory_users.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/territories/'
		api_path = api_path + str(territory)
		api_path = api_path + '/users'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.territory_users.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def deassociate_territory_users(self, territory, param_instance=None):
		"""
		The method to deassociate territory users

		Parameters:
			territory (int) : An int representing the territory
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/territories/'
		api_path = api_path + str(territory)
		api_path = api_path + '/users'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.territory_users.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_territory_user(self, user, territory):
		"""
		The method to get territory user

		Parameters:
			user (int) : An int representing the user
			territory (int) : An int representing the territory

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(user, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user EXPECTED TYPE: int', None, None)
		
		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/territories/'
		api_path = api_path + str(territory)
		api_path = api_path + '/users/'
		api_path = api_path + str(user)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.territory_users.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_territory_user(self, user, territory):
		"""
		The method to update territory user

		Parameters:
			user (int) : An int representing the user
			territory (int) : An int representing the territory

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(user, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user EXPECTED TYPE: int', None, None)
		
		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/territories/'
		api_path = api_path + str(territory)
		api_path = api_path + '/users/'
		api_path = api_path + str(user)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.territory_users.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def deassociate_territory_user(self, user, territory):
		"""
		The method to deassociate territory user

		Parameters:
			user (int) : An int representing the user
			territory (int) : An int representing the territory

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(user, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user EXPECTED TYPE: int', None, None)
		
		if not isinstance(territory, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: territory EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/territories/'
		api_path = api_path + str(territory)
		api_path = api_path + '/users/'
		api_path = api_path + str(user)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.territory_users.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class DeassociateTerritoryUsersParam(object):
	ids = Param('ids', 'com.zoho.crm.api.TerritoryUsers.DeassociateTerritoryUsersParam')
