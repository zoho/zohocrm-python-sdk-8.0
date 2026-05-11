try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, Choice, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, Choice, CommonAPIHandler, Constants
	from ..param import Param


class ZiaOrgEnrichmentOperations(object):
	def __init__(self):
		"""Creates an instance of ZiaOrgEnrichmentOperations"""
		pass

	def get_zia_org_enrichments(self, param_instance=None):
		"""
		The method to get zia org enrichments

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
		api_path = api_path + '/crm/v8/__zia_org_enrichment'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_zia_org_enrichment(self, request, param_instance=None):
		"""
		The method to create zia org enrichment

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/__zia_org_enrichment'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_zia_org_enrichment(self, zia_org_enrichment_id):
		"""
		The method to get zia org enrichment

		Parameters:
			zia_org_enrichment_id (int) : An int representing the zia_org_enrichment_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(zia_org_enrichment_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: zia_org_enrichment_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/__zia_org_enrichment/'
		api_path = api_path + str(zia_org_enrichment_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.zia_org_enrichment.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetZiaOrgEnrichmentsParam(object):
	status = Param('status', 'com.zoho.crm.api.ZiaOrgEnrichment.GetZiaOrgEnrichmentsParam')
	sort_order = Param('sort_order', 'com.zoho.crm.api.ZiaOrgEnrichment.GetZiaOrgEnrichmentsParam')
	sort_by = Param('sort_by', 'com.zoho.crm.api.ZiaOrgEnrichment.GetZiaOrgEnrichmentsParam')
	page = Param('page', 'com.zoho.crm.api.ZiaOrgEnrichment.GetZiaOrgEnrichmentsParam')
	per_page = Param('per_page', 'com.zoho.crm.api.ZiaOrgEnrichment.GetZiaOrgEnrichmentsParam')


class CreateZiaOrgEnrichmentParam(object):
	module = Param('module', 'com.zoho.crm.api.ZiaOrgEnrichment.CreateZiaOrgEnrichmentParam')
	record_id = Param('record_id', 'com.zoho.crm.api.ZiaOrgEnrichment.CreateZiaOrgEnrichmentParam')
