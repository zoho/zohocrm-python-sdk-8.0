try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, Choice, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, Choice, CommonAPIHandler, Constants
	from ..param import Param


class PortalInviteOperations(object):
	def __init__(self, module):
		"""
		Creates an instance of PortalInviteOperations with the given parameters

		Parameters:
			module (string) : A string representing the module
		"""

		if not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module


	def invite_users(self, record, param_instance=None):
		"""
		The method to invite users

		Parameters:
			record (int) : An int representing the record
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

		if not isinstance(record, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module)
		api_path = api_path + '/'
		api_path = api_path + str(record)
		api_path = api_path + '/actions/portal_invite'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.portal_invite.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class InviteUsersParam(object):
	user_type_id = Param('user_type_id', 'com.zoho.crm.api.PortalInvite.InviteUsersParam')
	type = Param('type', 'com.zoho.crm.api.PortalInvite.InviteUsersParam')
	language = Param('language', 'com.zoho.crm.api.PortalInvite.InviteUsersParam')
