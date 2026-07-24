try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class RecordLockingConfigurationOperations(object):
	def __init__(self, module=None):
		"""
		Creates an instance of RecordLockingConfigurationOperations with the given parameters

		Parameters:
			module (string) : A string representing the module
		"""

		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__module = module


	def get_record_locking_configurations(self, param_instance=None):
		"""
		The method to get record locking configurations

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
		api_path = api_path + '/crm/v8/settings/record_locking_configurations'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.RecordLockingConfiguration.GetRecordLockingConfigurationsParam'), self.__module)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking_configuration.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def add_record_locking_configuration(self, request):
		"""
		The method to add record locking configuration

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking_configuration.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/record_locking_configurations'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.RecordLockingConfiguration.AddRecordLockingConfigurationParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking_configuration.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_record_locking_configurations(self, request):
		"""
		The method to update record locking configurations

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking_configuration.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/record_locking_configurations'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.RecordLockingConfiguration.UpdateRecordLockingConfigurationsParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking_configuration.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_record_locking_configuration(self, record_locking_config_id, request):
		"""
		The method to update record locking configuration

		Parameters:
			record_locking_config_id (int) : An int representing the record_locking_config_id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking_configuration.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(record_locking_config_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_locking_config_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/record_locking_configurations/'
		api_path = api_path + str(record_locking_config_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.RecordLockingConfiguration.UpdateRecordLockingConfigurationParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking_configuration.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_record_locking_configuration(self, record_locking_config_id):
		"""
		The method to delete record locking configuration

		Parameters:
			record_locking_config_id (int) : An int representing the record_locking_config_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(record_locking_config_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_locking_config_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/record_locking_configurations/'
		api_path = api_path + str(record_locking_config_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.RecordLockingConfiguration.DeleteRecordLockingConfigurationParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.record_locking_configuration.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetRecordLockingConfigurationsParam(object):
	feature_type = Param('feature_type', 'com.zoho.crm.api.RecordLockingConfiguration.GetRecordLockingConfigurationsParam')


class AddRecordLockingConfigurationParam(object):
	pass


class UpdateRecordLockingConfigurationsParam(object):
	pass


class UpdateRecordLockingConfigurationParam(object):
	pass


class DeleteRecordLockingConfigurationParam(object):
	pass
