try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
	from zohocrmsdk.src.com.zoho.crm.api.header import Header
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param
	from ..header import Header


class FunctionsOperations(object):
	def __init__(self, function_name, auth_type=None, arguments=None):
		"""
		Creates an instance of FunctionsOperations with the given parameters

		Parameters:
			function_name (string) : A string representing the function_name
			auth_type (string) : A string representing the auth_type
			arguments (dict) : An instance of dict
		"""

		if not isinstance(function_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: function_name EXPECTED TYPE: str', None, None)
		
		if auth_type is not None and not isinstance(auth_type, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: auth_type EXPECTED TYPE: str', None, None)
		
		if arguments is not None and not isinstance(arguments, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: arguments EXPECTED TYPE: dict', None, None)
		
		self.__function_name = function_name
		self.__auth_type = auth_type
		self.__arguments = arguments


	def execute_function_using_request_body(self, request, param_instance=None, header_instance=None):
		"""
		The method to execute function using request body

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.functions.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/functions/'
		api_path = api_path + str(self.__function_name)
		api_path = api_path + '/actions/execute'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('auth_type', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingRequestBodyParam'), self.__auth_type)
		handler_instance.add_param(Param('arguments', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingRequestBodyParam'), self.__arguments)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.functions.response_wrapper import ResponseWrapper
		except Exception:
			from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, 'application/json')

	def execute_function_using_parameters(self, param_instance=None, header_instance=None):
		"""
		The method to execute function using parameters

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/functions/'
		api_path = api_path + str(self.__function_name)
		api_path = api_path + '/actions/execute'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('auth_type', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingParametersParam'), self.__auth_type)
		handler_instance.add_param(Param('arguments', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingParametersParam'), self.__arguments)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.functions.response_wrapper import ResponseWrapper
		except Exception:
			from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, 'application/json')

	def execute_function_using_file(self, request, param_instance=None, header_instance=None):
		"""
		The method to execute function using file

		Parameters:
			request (FileBodyWrapper) : An instance of FileBodyWrapper
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.functions.file_body_wrapper import FileBodyWrapper
		except Exception:
			from .file_body_wrapper import FileBodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if request is not None and not isinstance(request, FileBodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: FileBodyWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/functions/'
		api_path = api_path + str(self.__function_name)
		api_path = api_path + '/actions/execute'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('multipart/form-data')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('auth_type', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingFileParam'), self.__auth_type)
		handler_instance.add_param(Param('arguments', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingFileParam'), self.__arguments)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.functions.response_wrapper import ResponseWrapper
		except Exception:
			from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, 'application/json')


class ExecuteFunctionUsingRequestBodyParam(object):
	custom_functions_param = Param('custom_functions_param', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingRequestBodyParam')


class ExecuteFunctionUsingRequestBodyHeader(object):
	custom_functions_header = Header('custom_functions_header', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingRequestBodyHeader')


class ExecuteFunctionUsingParametersParam(object):
	get_custom_functions_param = Param('get_custom_functions_param', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingParametersParam')


class ExecuteFunctionUsingParametersHeader(object):
	get_custom_functions_header = Header('get_custom_functions_header', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingParametersHeader')


class ExecuteFunctionUsingFileParam(object):
	upload_file_param = Param('upload_file_param', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingFileParam')


class ExecuteFunctionUsingFileHeader(object):
	upload_file_header = Header('upload_file_header', 'com.zoho.crm.api.Functions.ExecuteFunctionUsingFileHeader')
