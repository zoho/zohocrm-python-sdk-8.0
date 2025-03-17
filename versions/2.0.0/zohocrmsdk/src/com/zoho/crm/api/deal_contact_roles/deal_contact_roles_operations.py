try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Utility, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Utility, Constants
	from ..param import Param


class DealContactRolesOperations(object):
	def __init__(self):
		"""Creates an instance of DealContactRolesOperations"""
		pass

	def get_associated_contact_roles(self, deal, param_instance=None):
		"""
		The method to get associated contact roles

		Parameters:
			deal (int) : An int representing the deal
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

		if not isinstance(deal, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Deals/'
		api_path = api_path + str(deal)
		api_path = api_path + '/Contact_Roles'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_module_api_name("Contacts")
		Utility.get_fields("Contacts", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def delete_associated_contact_roles(self, deal, param_instance=None):
		"""
		The method to delete associated contact roles

		Parameters:
			deal (int) : An int representing the deal
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

		if not isinstance(deal, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Deals/'
		api_path = api_path + str(deal)
		api_path = api_path + '/Contact_Roles'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_associated_contact_roles_specific_to_contact(self, contact, deal):
		"""
		The method to get associated contact roles specific to contact

		Parameters:
			contact (int) : An int representing the contact
			deal (int) : An int representing the deal

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(contact, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact EXPECTED TYPE: int', None, None)
		
		if not isinstance(deal, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Deals/'
		api_path = api_path + str(deal)
		api_path = api_path + '/Contact_Roles/'
		api_path = api_path + str(contact)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_module_api_name("Contacts")
		Utility.get_fields("Contacts", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def associate_contact_role_to_deal(self, contact, deal, request):
		"""
		The method to associate contact role to deal

		Parameters:
			contact (int) : An int representing the contact
			deal (int) : An int representing the deal
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(contact, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact EXPECTED TYPE: int', None, None)
		
		if not isinstance(deal, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Deals/'
		api_path = api_path + str(deal)
		api_path = api_path + '/Contact_Roles/'
		api_path = api_path + str(contact)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_contact_role_relation(self, contact, deal):
		"""
		The method to delete contact role relation

		Parameters:
			contact (int) : An int representing the contact
			deal (int) : An int representing the deal

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(contact, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: contact EXPECTED TYPE: int', None, None)
		
		if not isinstance(deal, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: deal EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Deals/'
		api_path = api_path + str(deal)
		api_path = api_path + '/Contact_Roles/'
		api_path = api_path + str(contact)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.deal_contact_roles.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetAssociatedContactRolesParam(object):
	ids = Param('ids', 'com.zoho.crm.api.DealContactRoles.GetAssociatedContactRolesParam')
	fields = Param('fields', 'com.zoho.crm.api.DealContactRoles.GetAssociatedContactRolesParam')


class DeleteAssociatedContactRolesParam(object):
	ids = Param('ids', 'com.zoho.crm.api.DealContactRoles.DeleteAssociatedContactRolesParam')
