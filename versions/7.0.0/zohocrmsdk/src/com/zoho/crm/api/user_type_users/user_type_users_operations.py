try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class UserTypeUsersOperations(object):
	def __init__(self, user_type_id, portal_name):
		"""
		Creates an instance of UserTypeUsersOperations with the given parameters

		Parameters:
			user_type_id (int) : An int representing the user_type_id
			portal_name (string) : A string representing the portal_name
		"""

		if not isinstance(user_type_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_type_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(portal_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: portal_name EXPECTED TYPE: str', None, None)
		
		self.__user_type_id = user_type_id
		self.__portal_name = portal_name


	def get_users_of_user_type(self, param_instance=None):
		"""
		The method to get users of user type

		Parameters:
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

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/portals/'
		api_path = api_path + str(self.__portal_name)
		api_path = api_path + '/user_type/'
		api_path = api_path + str(self.__user_type_id)
		api_path = api_path + '/users'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_type_users.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def delete_user_from_the_portal(self, param_instance=None):
		"""
		The method to delete user from the portal

		Parameters:
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

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/portals/'
		api_path = api_path + str(self.__portal_name)
		api_path = api_path + '/user_type/'
		api_path = api_path + str(self.__user_type_id)
		api_path = api_path + '/users'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_type_users.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def transfer_users_of_a_user_type(self, param_instance=None):
		"""
		The method to transfer users of a user type

		Parameters:
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

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/portals/'
		api_path = api_path + str(self.__portal_name)
		api_path = api_path + '/user_type/'
		api_path = api_path + str(self.__user_type_id)
		api_path = api_path + '/users/action/transfer'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_type_users.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def change_users_status(self, user_id, param_instance=None):
		"""
		The method to change users status

		Parameters:
			user_id (int) : An int representing the user_id
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

		if not isinstance(user_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/portals/'
		api_path = api_path + str(self.__portal_name)
		api_path = api_path + '/user_type/'
		api_path = api_path + str(self.__user_type_id)
		api_path = api_path + '/users/'
		api_path = api_path + str(user_id)
		api_path = api_path + '/actions/change_status'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_type_users.status_action_handler import StatusActionHandler
		except Exception:
			from .status_action_handler import StatusActionHandler
		return handler_instance.api_call(StatusActionHandler.__module__, 'application/json')


class GetUsersOfUserTypeParam(object):
	filters = Param('filters', 'com.zoho.crm.api.UserTypeUsers.GetUsersOfUserTypeParam')
	type = Param('type', 'com.zoho.crm.api.UserTypeUsers.GetUsersOfUserTypeParam')


class DeleteUserFromThePortalParam(object):
	personality_ids = Param('personality_ids', 'com.zoho.crm.api.UserTypeUsers.DeleteUserFromThePortalParam')


class TransferUsersOfAUserTypeParam(object):
	personality_ids = Param('personality_ids', 'com.zoho.crm.api.UserTypeUsers.TransferUsersOfAUserTypeParam')
	transfer_to = Param('transfer_To', 'com.zoho.crm.api.UserTypeUsers.TransferUsersOfAUserTypeParam')


class ChangeUsersStatusParam(object):
	active = Param('active', 'com.zoho.crm.api.UserTypeUsers.ChangeUsersStatusParam')
