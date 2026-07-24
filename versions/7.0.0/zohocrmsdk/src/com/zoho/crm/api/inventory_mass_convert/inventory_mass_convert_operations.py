try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class InventoryMassConvertOperations(object):
	def __init__(self, module_api_name):
		"""
		Creates an instance of InventoryMassConvertOperations with the given parameters

		Parameters:
			module_api_name (string) : A string representing the module_api_name
		"""

		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		self.__module_api_name = module_api_name


	def mass_inventory_convert(self, request):
		"""
		The method to mass inventory convert

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.inventory_mass_convert.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/actions/mass_convert'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.inventory_mass_convert.action_response import ActionResponse
		except Exception:
			from .action_response import ActionResponse
		return handler_instance.api_call(ActionResponse.__module__, 'application/json')

	def get_scheduled_jobs_details(self, param_instance=None):
		"""
		The method to get scheduled jobs details

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
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/actions/mass_convert'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.inventory_mass_convert.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetScheduledJobsDetailsParam(object):
	job_id = Param('job_id', 'com.zoho.crm.api.InventoryMassConvert.GetScheduledJobsDetailsParam')
