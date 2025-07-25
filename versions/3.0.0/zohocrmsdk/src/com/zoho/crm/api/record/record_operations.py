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


class RecordOperations(object):
	def __init__(self, module_api_name):
		"""
		Creates an instance of RecordOperations with the given parameters

		Parameters:
			module_api_name (string) : A string representing the module_api_name
		"""

		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		self.__module_api_name = module_api_name


	def get_record(self, id, param_instance=None, header_instance=None):
		"""
		The method to get record

		Parameters:
			id (int) : An int representing the id
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

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_record(self, id, request, header_instance=None):
		"""
		The method to update record

		Parameters:
			id (int) : An int representing the id
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_record(self, id, param_instance=None, header_instance=None):
		"""
		The method to delete record

		Parameters:
			id (int) : An int representing the id
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

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_records(self, param_instance=None, header_instance=None):
		"""
		The method to get records

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
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_records(self, request, header_instance=None):
		"""
		The method to create records

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_records(self, request, header_instance=None):
		"""
		The method to update records

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_records(self, param_instance=None, header_instance=None):
		"""
		The method to delete records

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
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def upsert_records(self, request, header_instance=None):
		"""
		The method to upsert records

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/upsert'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_deleted_records(self, param_instance=None, header_instance=None):
		"""
		The method to get deleted records

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
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/deleted'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.deleted_records_handler import DeletedRecordsHandler
		except Exception:
			from .deleted_records_handler import DeletedRecordsHandler
		return handler_instance.api_call(DeletedRecordsHandler.__module__, 'application/json')

	def search_records(self, param_instance=None, header_instance=None):
		"""
		The method to search records

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
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/search'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_photo(self, id):
		"""
		The method to get photo

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
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		api_path = api_path + '/photo'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.download_handler import DownloadHandler
		except Exception:
			from .download_handler import DownloadHandler
		return handler_instance.api_call(DownloadHandler.__module__, 'application/x-download')

	def upload_photo(self, id, request, param_instance=None):
		"""
		The method to upload photo

		Parameters:
			id (int) : An int representing the id
			request (FileBodyWrapper) : An instance of FileBodyWrapper
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.file_body_wrapper import FileBodyWrapper
		except Exception:
			from .file_body_wrapper import FileBodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, FileBodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: FileBodyWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		api_path = api_path + '/photo'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('multipart/form-data')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		Utility.verify_photo_support(self.__module_api_name)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.file_handler import FileHandler
		except Exception:
			from .file_handler import FileHandler
		return handler_instance.api_call(FileHandler.__module__, 'application/json')

	def delete_photo(self, id):
		"""
		The method to delete photo

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
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		api_path = api_path + '/photo'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.file_handler import FileHandler
		except Exception:
			from .file_handler import FileHandler
		return handler_instance.api_call(FileHandler.__module__, 'application/json')

	def mass_update_records(self, request):
		"""
		The method to mass update records

		Parameters:
			request (MassUpdateBodyWrapper) : An instance of MassUpdateBodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.mass_update_body_wrapper import MassUpdateBodyWrapper
		except Exception:
			from .mass_update_body_wrapper import MassUpdateBodyWrapper

		if request is not None and not isinstance(request, MassUpdateBodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: MassUpdateBodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/actions/mass_update'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.mass_update_action_handler import MassUpdateActionHandler
		except Exception:
			from .mass_update_action_handler import MassUpdateActionHandler
		return handler_instance.api_call(MassUpdateActionHandler.__module__, 'application/json')

	def get_mass_update_status(self, param_instance=None):
		"""
		The method to get mass update status

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
		api_path = api_path + '/actions/mass_update'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.mass_update_response_handler import MassUpdateResponseHandler
		except Exception:
			from .mass_update_response_handler import MassUpdateResponseHandler
		return handler_instance.api_call(MassUpdateResponseHandler.__module__, 'application/json')

	def assign_territories_to_multiple_records(self, request):
		"""
		The method to assign territories to multiple records

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/actions/assign_territories'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def assign_territory_to_record(self, id, request):
		"""
		The method to assign territory to record

		Parameters:
			id (int) : An int representing the id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		api_path = api_path + '/actions/assign_territories'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def remove_territories_from_multiple_records(self, request):
		"""
		The method to remove territories from multiple records

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/actions/remove_territories'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def remove_territories_from_record(self, id, request):
		"""
		The method to remove territories from record

		Parameters:
			id (int) : An int representing the id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		api_path = api_path + '/actions/remove_territories'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def record_count(self, param_instance=None):
		"""
		The method to record count

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
		api_path = api_path + '/actions/count'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.count_handler import CountHandler
		except Exception:
			from .count_handler import CountHandler
		return handler_instance.api_call(CountHandler.__module__, 'application/json')

	def get_record_using_external_id(self, external_field_value, param_instance=None, header_instance=None):
		"""
		The method to get record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
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
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_record_using_external_id(self, external_field_value, request, header_instance=None):
		"""
		The method to update record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
			request (BodyWrapper) : An instance of BodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if not isinstance(external_field_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: external_field_value EXPECTED TYPE: str', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_header(header_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_record_using_external_id(self, external_field_value, param_instance=None, header_instance=None):
		"""
		The method to delete record using external id

		Parameters:
			external_field_value (string) : A string representing the external_field_value
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
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(external_field_value)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_full_data_for_rich_text(self, id, param_instance=None):
		"""
		The method to get full data for rich text

		Parameters:
			id (int) : An int representing the id
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

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		api_path = api_path + '/actions/fetch_full_data'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_rich_text_records(self, param_instance=None):
		"""
		The method to get rich text records

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
		api_path = api_path + '/actions/fetch_full_data'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def clone_record(self, id):
		"""
		The method to clone record

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
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(id)
		api_path = api_path + '/actions/clone'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name(self.__module_api_name)
		Utility.get_fields(self.__module_api_name, handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetRecordParam(object):
	approved = Param('approved', 'com.zoho.crm.api.Record.GetRecordParam')
	converted = Param('converted', 'com.zoho.crm.api.Record.GetRecordParam')
	cvid = Param('cvid', 'com.zoho.crm.api.Record.GetRecordParam')
	uid = Param('uid', 'com.zoho.crm.api.Record.GetRecordParam')
	fields = Param('fields', 'com.zoho.crm.api.Record.GetRecordParam')
	startdatetime = Param('startDateTime', 'com.zoho.crm.api.Record.GetRecordParam')
	enddatetime = Param('endDateTime', 'com.zoho.crm.api.Record.GetRecordParam')
	territory_id = Param('territory_id', 'com.zoho.crm.api.Record.GetRecordParam')
	include_child = Param('include_child', 'com.zoho.crm.api.Record.GetRecordParam')
	on_demand_properties = Param('on_demand_properties', 'com.zoho.crm.api.Record.GetRecordParam')


class GetRecordHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.Record.GetRecordHeader')
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.GetRecordHeader')


class UpdateRecordHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.UpdateRecordHeader')


class DeleteRecordParam(object):
	wf_trigger = Param('wf_trigger', 'com.zoho.crm.api.Record.DeleteRecordParam')


class DeleteRecordHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.DeleteRecordHeader')


class GetRecordsParam(object):
	approved = Param('approved', 'com.zoho.crm.api.Record.GetRecordsParam')
	converted = Param('converted', 'com.zoho.crm.api.Record.GetRecordsParam')
	cvid = Param('cvid', 'com.zoho.crm.api.Record.GetRecordsParam')
	ids = Param('ids', 'com.zoho.crm.api.Record.GetRecordsParam')
	uid = Param('uid', 'com.zoho.crm.api.Record.GetRecordsParam')
	fields = Param('fields', 'com.zoho.crm.api.Record.GetRecordsParam')
	sort_by = Param('sort_by', 'com.zoho.crm.api.Record.GetRecordsParam')
	sort_order = Param('sort_order', 'com.zoho.crm.api.Record.GetRecordsParam')
	page = Param('page', 'com.zoho.crm.api.Record.GetRecordsParam')
	per_page = Param('per_page', 'com.zoho.crm.api.Record.GetRecordsParam')
	startdatetime = Param('startDateTime', 'com.zoho.crm.api.Record.GetRecordsParam')
	enddatetime = Param('endDateTime', 'com.zoho.crm.api.Record.GetRecordsParam')
	territory_id = Param('territory_id', 'com.zoho.crm.api.Record.GetRecordsParam')
	include_child = Param('include_child', 'com.zoho.crm.api.Record.GetRecordsParam')
	page_token = Param('page_token', 'com.zoho.crm.api.Record.GetRecordsParam')


class GetRecordsHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.Record.GetRecordsHeader')
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.GetRecordsHeader')


class CreateRecordsHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.CreateRecordsHeader')


class UpdateRecordsHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.UpdateRecordsHeader')


class DeleteRecordsParam(object):
	ids = Param('ids', 'com.zoho.crm.api.Record.DeleteRecordsParam')
	wf_trigger = Param('wf_trigger', 'com.zoho.crm.api.Record.DeleteRecordsParam')


class DeleteRecordsHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.DeleteRecordsHeader')


class UpsertRecordsHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.UpsertRecordsHeader')


class GetDeletedRecordsParam(object):
	type = Param('type', 'com.zoho.crm.api.Record.GetDeletedRecordsParam')
	page = Param('page', 'com.zoho.crm.api.Record.GetDeletedRecordsParam')
	per_page = Param('per_page', 'com.zoho.crm.api.Record.GetDeletedRecordsParam')


class GetDeletedRecordsHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.Record.GetDeletedRecordsHeader')


class SearchRecordsParam(object):
	criteria = Param('criteria', 'com.zoho.crm.api.Record.SearchRecordsParam')
	email = Param('email', 'com.zoho.crm.api.Record.SearchRecordsParam')
	phone = Param('phone', 'com.zoho.crm.api.Record.SearchRecordsParam')
	word = Param('word', 'com.zoho.crm.api.Record.SearchRecordsParam')
	converted = Param('converted', 'com.zoho.crm.api.Record.SearchRecordsParam')
	approved = Param('approved', 'com.zoho.crm.api.Record.SearchRecordsParam')
	page = Param('page', 'com.zoho.crm.api.Record.SearchRecordsParam')
	per_page = Param('per_page', 'com.zoho.crm.api.Record.SearchRecordsParam')
	fields = Param('fields', 'com.zoho.crm.api.Record.SearchRecordsParam')
	cvid = Param('cvid', 'com.zoho.crm.api.Record.SearchRecordsParam')
	type = Param('type', 'com.zoho.crm.api.Record.SearchRecordsParam')


class SearchRecordsHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.SearchRecordsHeader')


class UploadPhotoParam(object):
	restrict_triggers = Param('restrict_triggers', 'com.zoho.crm.api.Record.UploadPhotoParam')


class GetMassUpdateStatusParam(object):
	job_id = Param('job_id', 'com.zoho.crm.api.Record.GetMassUpdateStatusParam')


class RecordCountParam(object):
	cvid = Param('cvid', 'com.zoho.crm.api.Record.RecordCountParam')
	criteria = Param('criteria', 'com.zoho.crm.api.Record.RecordCountParam')
	email = Param('email', 'com.zoho.crm.api.Record.RecordCountParam')
	phone = Param('phone', 'com.zoho.crm.api.Record.RecordCountParam')
	word = Param('word', 'com.zoho.crm.api.Record.RecordCountParam')


class GetRecordUsingExternalIDParam(object):
	approved = Param('approved', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')
	converted = Param('converted', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')
	cvid = Param('cvid', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')
	uid = Param('uid', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')
	fields = Param('fields', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')
	startdatetime = Param('startDateTime', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')
	enddatetime = Param('endDateTime', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')
	territory_id = Param('territory_id', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')
	include_child = Param('include_child', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDParam')


class GetRecordUsingExternalIDHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDHeader')
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.GetRecordUsingExternalIDHeader')


class UpdateRecordUsingExternalIDHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.UpdateRecordUsingExternalIDHeader')


class DeleteRecordUsingExternalIDParam(object):
	wf_trigger = Param('wf_trigger', 'com.zoho.crm.api.Record.DeleteRecordUsingExternalIDParam')


class DeleteRecordUsingExternalIDHeader(object):
	x_external = Header('X-EXTERNAL', 'com.zoho.crm.api.Record.DeleteRecordUsingExternalIDHeader')


class GetFullDataForRichTextParam(object):
	fields = Param('fields', 'com.zoho.crm.api.Record.GetFullDataForRichTextParam')


class GetRichTextRecordsParam(object):
	ids = Param('ids', 'com.zoho.crm.api.Record.GetRichTextRecordsParam')
	fields = Param('fields', 'com.zoho.crm.api.Record.GetRichTextRecordsParam')
