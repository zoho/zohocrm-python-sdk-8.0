try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class MassDeleteCvidOperations(object):
	def __init__(self, module):
		"""
		Creates an instance of MassDeleteCvidOperations with the given parameters

		Parameters:
			module (string) : A string representing the module
		"""

		if not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module


	def mass_delete_by_cvid(self, request):
		"""
		The method to mass delete by cvid

		Parameters:
			request (CvidBodyWrapper) : An instance of CvidBodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mass_delete_cvid.cvid_body_wrapper import CvidBodyWrapper
		except Exception:
			from .cvid_body_wrapper import CvidBodyWrapper

		if request is not None and not isinstance(request, CvidBodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: CvidBodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module)
		api_path = api_path + '/actions/mass_delete'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.mass_delete_cvid.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def mass_delete_by_record_id(self, request):
		"""
		The method to mass delete by record id

		Parameters:
			request (RecordIdBodyWrapper) : An instance of RecordIdBodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mass_delete_cvid.record_id_body_wrapper import RecordIdBodyWrapper
		except Exception:
			from .record_id_body_wrapper import RecordIdBodyWrapper

		if request is not None and not isinstance(request, RecordIdBodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: RecordIdBodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module)
		api_path = api_path + '/actions/mass_delete'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.mass_delete_cvid.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_mass_delete_status(self, param_instance=None):
		"""
		The method to get mass delete status

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
		api_path = api_path + str(self.__module)
		api_path = api_path + '/actions/mass_delete'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.mass_delete_cvid.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetMassDeleteStatusParam(object):
	job_id = Param('job_id', 'com.zoho.crm.api.MassDeleteCvid.GetMassDeleteStatusParam')
