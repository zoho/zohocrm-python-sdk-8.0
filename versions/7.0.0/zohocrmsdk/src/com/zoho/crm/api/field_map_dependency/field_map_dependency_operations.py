try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class FieldMapDependencyOperations(object):
	def __init__(self, layout_id, module=None):
		"""
		Creates an instance of FieldMapDependencyOperations with the given parameters

		Parameters:
			layout_id (int) : An int representing the layout_id
			module (string) : A string representing the module
		"""

		if not isinstance(layout_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout_id EXPECTED TYPE: int', None, None)
		
		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__layout_id = layout_id
		self.__module = module


	def create_map_dependency(self, request):
		"""
		The method to create map dependency

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/layouts/'
		api_path = api_path + str(self.__layout_id)
		api_path = api_path + '/map_dependency'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.FieldMapDependency.CreateMapDependencyParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_map_dependencies(self, param_instance=None):
		"""
		The method to get map dependencies

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
		api_path = api_path + '/crm/v8/settings/layouts/'
		api_path = api_path + str(self.__layout_id)
		api_path = api_path + '/map_dependency'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.FieldMapDependency.GetMapDependenciesParam'), self.__module)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_map_dependency(self, dependency_id, request):
		"""
		The method to update map dependency

		Parameters:
			dependency_id (int) : An int representing the dependency_id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(dependency_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: dependency_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/layouts/'
		api_path = api_path + str(self.__layout_id)
		api_path = api_path + '/map_dependency/'
		api_path = api_path + str(dependency_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.FieldMapDependency.UpdateMapDependencyParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_map_dependency(self, dependency_id):
		"""
		The method to get map dependency

		Parameters:
			dependency_id (int) : An int representing the dependency_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(dependency_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: dependency_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/layouts/'
		api_path = api_path + str(self.__layout_id)
		api_path = api_path + '/map_dependency/'
		api_path = api_path + str(dependency_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.FieldMapDependency.GetMapDependencyParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def delete_map_dependency(self, dependency_id):
		"""
		The method to delete map dependency

		Parameters:
			dependency_id (int) : An int representing the dependency_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(dependency_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: dependency_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/layouts/'
		api_path = api_path + str(self.__layout_id)
		api_path = api_path + '/map_dependency/'
		api_path = api_path + str(dependency_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.FieldMapDependency.DeleteMapDependencyParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_map_dependency.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class CreateMapDependencyParam(object):
	pass


class CreateMapDependencyHeader(object):
	pass


class GetMapDependenciesParam(object):
	page = Param('page', 'com.zoho.crm.api.FieldMapDependency.GetMapDependenciesParam')
	per_page = Param('per_page', 'com.zoho.crm.api.FieldMapDependency.GetMapDependenciesParam')
	filters = Param('filters', 'com.zoho.crm.api.FieldMapDependency.GetMapDependenciesParam')


class UpdateMapDependencyParam(object):
	pass


class GetMapDependencyParam(object):
	pass


class DeleteMapDependencyParam(object):
	pass
