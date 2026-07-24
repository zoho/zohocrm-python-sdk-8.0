try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Utility, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Utility, Constants
	from ..param import Param


class RecordLockingOperations(object):
	def __init__(self, record_id, module_name):
		"""
		Creates an instance of RecordLockingOperations with the given parameters

		Parameters:
			record_id (int) : An int representing the record_id
			module_name (string) : A string representing the module_name
		"""

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(module_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_name EXPECTED TYPE: str', None, None)
		
		self.__record_id = record_id
		self.__module_name = module_name


	def get_record_locking_informations(self, param_instance=None):
		"""
		The method to get record locking informations

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
		api_path = api_path + str(self.__module_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/Locking_Information__s'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_module_api_name("Locking_Information__s")
		Utility.get_fields("Locking_Information__s", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def lock_records(self, request):
		"""
		The method to lock records

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/Locking_Information__s'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name("Locking_Information__s")
		Utility.get_fields("Locking_Information__s", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_record_locking_information(self, lock_id, param_instance=None):
		"""
		The method to get record locking information

		Parameters:
			lock_id (int) : An int representing the lock_id
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

		if not isinstance(lock_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lock_id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/Locking_Information__s/'
		api_path = api_path + str(lock_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		handler_instance.set_module_api_name("Locking_Information__s")
		Utility.get_fields("Locking_Information__s", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_record_locking_information(self, lock_id, request):
		"""
		The method to update record locking information

		Parameters:
			lock_id (int) : An int representing the lock_id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(lock_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lock_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/Locking_Information__s/'
		api_path = api_path + str(lock_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name("Locking_Information__s")
		Utility.get_fields("Locking_Information__s", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def unlock_record(self, lock_id):
		"""
		The method to unlock record

		Parameters:
			lock_id (int) : An int representing the lock_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(lock_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lock_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/Locking_Information__s/'
		api_path = api_path + str(lock_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_module_api_name("Locking_Information__s")
		Utility.get_fields("Locking_Information__s", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetRecordLockingInformationsParam(object):
	fields = Param('fields', 'com.zoho.crm.api.RecordLocking.GetRecordLockingInformationsParam')
	page_token = Param('page_token', 'com.zoho.crm.api.RecordLocking.GetRecordLockingInformationsParam')
	page = Param('page', 'com.zoho.crm.api.RecordLocking.GetRecordLockingInformationsParam')
	per_page = Param('per_page', 'com.zoho.crm.api.RecordLocking.GetRecordLockingInformationsParam')
	ids = Param('ids', 'com.zoho.crm.api.RecordLocking.GetRecordLockingInformationsParam')


class GetRecordLockingInformationParam(object):
	fields = Param('fields', 'com.zoho.crm.api.RecordLocking.GetRecordLockingInformationParam')
