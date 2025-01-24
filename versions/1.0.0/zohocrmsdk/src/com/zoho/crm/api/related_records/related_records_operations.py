try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Utility, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
	from zohocrmsdk.src.com.zoho.crm.api.header import Header
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Utility, Constants
	from ..param import Param
	from ..header import Header


class RelatedRecordsOperations(object):
	def __init__(self, related_list_api_name, module_api_name):
		"""
		Creates an instance of RelatedRecordsOperations with the given parameters

		Parameters:
			related_list_api_name (string) : A string representing the related_list_api_name
			module_api_name (string) : A string representing the module_api_name
		"""

		if not isinstance(related_list_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_list_api_name EXPECTED TYPE: str', None, None)
		
		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		self.__related_list_api_name = related_list_api_name
		self.__module_api_name = module_api_name


	def get_related_records(self, record_id, param_instance=None, header_instance=None):
		"""
		The method to get related records

		Parameters:
			record_id (int) : An int representing the record_id
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

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_records(self, record_id, request, header_instance=None):
		"""
		The method to update related records

		Parameters:
			record_id (int) : An int representing the record_id
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delink_records(self, record_id, param_instance=None, header_instance=None):
		"""
		The method to delink records

		Parameters:
			record_id (int) : An int representing the record_id
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

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_related_records_using_external_id(self, external_value, param_instance=None, header_instance=None):
		"""
		The method to get related records using external id

		Parameters:
			external_value (string) : A string representing the external_value
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

		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_records_using_external_id(self, external_value, request, header_instance=None):
		"""
		The method to update related records using external id

		Parameters:
			external_value (string) : A string representing the external_value
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_related_records_using_external_id(self, external_value, param_instance=None, header_instance=None):
		"""
		The method to delete related records using external id

		Parameters:
			external_value (string) : A string representing the external_value
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

		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_related_record(self, related_record_id, record_id, param_instance=None, header_instance=None):
		"""
		The method to get related record

		Parameters:
			related_record_id (int) : An int representing the related_record_id
			record_id (int) : An int representing the record_id
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

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_record(self, related_record_id, record_id, request, header_instance=None):
		"""
		The method to update related record

		Parameters:
			related_record_id (int) : An int representing the related_record_id
			record_id (int) : An int representing the record_id
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delink_record(self, related_record_id, record_id, header_instance=None):
		"""
		The method to delink record

		Parameters:
			related_record_id (int) : An int representing the related_record_id
			record_id (int) : An int representing the record_id
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if not isinstance(related_record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: related_record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(related_record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_header(header_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_related_record_using_external_id(self, external_field_value, external_value, param_instance=None, header_instance=None):
		"""
		The method to get related record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
			external_value (string) : A string representing the external_value
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

		if not isinstance(external_field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_field_value EXPECTED TYPE: str', None, None)
		
		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_related_record_using_external_id(self, external_field_value, external_value, request, header_instance=None):
		"""
		The method to update related record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
			external_value (string) : A string representing the external_value
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if not isinstance(external_field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_field_value EXPECTED TYPE: str', None, None)
		
		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_related_record_using_external_id(self, external_field_value, external_value, header_instance=None):
		"""
		The method to delete related record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
			external_value (string) : A string representing the external_value
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if not isinstance(external_field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_field_value EXPECTED TYPE: str', None, None)
		
		if not isinstance(external_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_value EXPECTED TYPE: str', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_value)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_header(header_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_deleted_parent_records_related_record(self, record_id, param_instance=None):
		"""
		The method to get deleted parent records related record

		Parameters:
			record_id (int) : An int representing the record_id
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

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/deleted/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/'
		api_path = api_path + str(self.__related_list_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		Utility.get_related_lists(self.__related_list_api_name, self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetRelatedRecordsParam(object):
	page = Param('page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsParam')
	per_page = Param('per_page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsParam')
	fields = Param('fields', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsParam')


class GetRelatedRecordsHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsHeader')
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsHeader')


class UpdateRelatedRecordsHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.UpdateRelatedRecordsHeader')


class DelinkRecordsParam(object):
	ids = Param('ids', 'com.zoho.crm.api.RelatedRecords.DelinkRecordsParam')


class DelinkRecordsHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.DelinkRecordsHeader')


class GetRelatedRecordsUsingExternalIDParam(object):
	page = Param('page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDParam')
	per_page = Param('per_page', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDParam')
	fields = Param('fields', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDParam')


class GetRelatedRecordsUsingExternalIDHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDHeader')
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordsUsingExternalIDHeader')


class UpdateRelatedRecordsUsingExternalIDHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.UpdateRelatedRecordsUsingExternalIDHeader')


class DeleteRelatedRecordsUsingExternalIDParam(object):
	ids = Param('ids', 'com.zoho.crm.api.RelatedRecords.DeleteRelatedRecordsUsingExternalIDParam')


class DeleteRelatedRecordsUsingExternalIDHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.DeleteRelatedRecordsUsingExternalIDHeader')


class GetRelatedRecordParam(object):
	fields = Param('fields', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordParam')


class GetRelatedRecordHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordHeader')
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordHeader')


class UpdateRelatedRecordHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.UpdateRelatedRecordHeader')


class DelinkRecordHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.DelinkRecordHeader')


class GetRelatedRecordUsingExternalIDParam(object):
	fields = Param('fields', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordUsingExternalIDParam')


class GetRelatedRecordUsingExternalIDHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordUsingExternalIDHeader')
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.GetRelatedRecordUsingExternalIDHeader')


class UpdateRelatedRecordUsingExternalIDHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.UpdateRelatedRecordUsingExternalIDHeader')


class DeleteRelatedRecordUsingExternalIDHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.RelatedRecords.DeleteRelatedRecordUsingExternalIDHeader')


class GetDeletedParentRecordsRelatedRecordParam(object):
	fields = Param('fields', 'com.zoho.crm.api.RelatedRecords.GetDeletedParentRecordsRelatedRecordParam')
	page = Param('page', 'com.zoho.crm.api.RelatedRecords.GetDeletedParentRecordsRelatedRecordParam')
	per_page = Param('per_page', 'com.zoho.crm.api.RelatedRecords.GetDeletedParentRecordsRelatedRecordParam')
	ids = Param('ids', 'com.zoho.crm.api.RelatedRecords.GetDeletedParentRecordsRelatedRecordParam')
