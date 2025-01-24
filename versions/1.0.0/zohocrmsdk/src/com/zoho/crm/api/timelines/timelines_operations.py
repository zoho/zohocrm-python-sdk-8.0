try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, Choice, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, Choice, CommonAPIHandler, Constants
	from ..param import Param


class TimelinesOperations(object):
	def __init__(self):
		"""Creates an instance of TimelinesOperations"""
		pass

	def get_timelines(self, module, record_id, param_instance=None):
		"""
		The method to get timelines

		Parameters:
			module (string) : A string representing the module
			record_id (string) : A string representing the record_id
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

		if not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		if not isinstance(record_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: str', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(module)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/__timeline'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.timelines.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetTimelinesParam(object):
	include_inner_details = Param('include_inner_details', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
	sort_by = Param('sort_by', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
	sort_order = Param('sort_order', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
	include_timeline_type = Param('include_timeline_type', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
	include = Param('include', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
	filters = Param('filters', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
	per_page = Param('per_page', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
	page = Param('page', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
	page_token = Param('page_token', 'com.zoho.crm.api.Timelines.GetTimelinesParam')
