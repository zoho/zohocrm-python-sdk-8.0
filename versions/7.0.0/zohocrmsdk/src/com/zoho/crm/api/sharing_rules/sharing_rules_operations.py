try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class SharingRulesOperations(object):
	def __init__(self, module=None):
		"""
		Creates an instance of SharingRulesOperations with the given parameters

		Parameters:
			module (string) : A string representing the module
		"""

		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module


	def get_sharing_rules(self, param_instance=None):
		"""
		The method to get sharing rules

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
		api_path = api_path + '/crm/v8/settings/data_sharing/rules'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.GetSharingRulesParam'), self.__module)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_sharing_rules(self, request):
		"""
		The method to create sharing rules

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.CreateSharingRulesParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_sharing_rules(self, request):
		"""
		The method to update sharing rules

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.UpdateSharingRulesParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_sharing_rule(self, id):
		"""
		The method to get sharing rule

		Parameters:
			id (int) : An int representing the id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.GetSharingRuleParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_sharing_rule(self, id, request):
		"""
		The method to update sharing rule

		Parameters:
			id (int) : An int representing the id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.UpdateSharingRuleParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_sharing_rule(self, id):
		"""
		The method to delete sharing rule

		Parameters:
			id (int) : An int representing the id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.DeleteSharingRuleParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def search_sharing_rules(self, request, param_instance=None):
		"""
		The method to search sharing rules

		Parameters:
			request (FiltersBody) : An instance of FiltersBody
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.filters_body import FiltersBody
		except Exception:
			from .filters_body import FiltersBody

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if request is not None and not isinstance(request, FiltersBody):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: FiltersBody', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/search'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.SearchSharingRulesParam'), self.__module)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def deactivate_sharing_rule(self, id):
		"""
		The method to deactivate sharing rule

		Parameters:
			id (int) : An int representing the id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/'
		api_path = api_path + str(id)
		api_path = api_path + '/actions/activate'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.DeactivateSharingRuleParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def activate_sharing_rule(self, id):
		"""
		The method to activate sharing rule

		Parameters:
			id (int) : An int representing the id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/'
		api_path = api_path + str(id)
		api_path = api_path + '/actions/activate'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.ActivateSharingRuleParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_sharing_rule_summary(self):
		"""
		The method to get sharing rule summary

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/actions/summary'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.GetSharingRuleSummaryParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.summary_response_handler import SummaryResponseHandler
		except Exception:
			from .summary_response_handler import SummaryResponseHandler
		return handler_instance.api_call(SummaryResponseHandler.__module__, 'application/json')

	def search_sharing_rules_summary(self, request):
		"""
		The method to search sharing rules summary

		Parameters:
			request (FiltersBody) : An instance of FiltersBody

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.filters_body import FiltersBody
		except Exception:
			from .filters_body import FiltersBody

		if request is not None and not isinstance(request, FiltersBody):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: FiltersBody', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/actions/summary'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.SearchSharingRulesSummaryParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.summary_response_handler import SummaryResponseHandler
		except Exception:
			from .summary_response_handler import SummaryResponseHandler
		return handler_instance.api_call(SummaryResponseHandler.__module__, 'application/json')

	def rerun_sharing_rules(self):
		"""
		The method to rerun sharing rules

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/data_sharing/rules/actions/run'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.SharingRules.RerunSharingRulesParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.sharing_rules.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetSharingRulesParam(object):
	page = Param('page', 'com.zoho.crm.api.SharingRules.GetSharingRulesParam')
	per_page = Param('per_page', 'com.zoho.crm.api.SharingRules.GetSharingRulesParam')


class CreateSharingRulesParam(object):
	pass


class UpdateSharingRulesParam(object):
	pass


class GetSharingRuleParam(object):
	pass


class UpdateSharingRuleParam(object):
	pass


class DeleteSharingRuleParam(object):
	pass


class SearchSharingRulesParam(object):
	page = Param('page', 'com.zoho.crm.api.SharingRules.SearchSharingRulesParam')
	per_page = Param('per_page', 'com.zoho.crm.api.SharingRules.SearchSharingRulesParam')


class DeactivateSharingRuleParam(object):
	pass


class ActivateSharingRuleParam(object):
	pass


class GetSharingRuleSummaryParam(object):
	pass


class SearchSharingRulesSummaryParam(object):
	pass


class RerunSharingRulesParam(object):
	pass
