try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class RelatedListsOperations(object):
	def __init__(self, layout_id=None):
		"""
		Creates an instance of RelatedListsOperations with the given parameters

		Parameters:
			layout_id (int) : An int representing the layout_id
		"""

		if layout_id is not None and not isinstance(layout_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout_id EXPECTED TYPE: int', None, None)
		
		self.__layout_id = layout_id


	def get_related_lists(self, param_instance=None):
		"""
		The method to get related lists

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
		api_path = api_path + '/crm/v8/settings/related_lists'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.RelatedLists.GetRelatedListsParam'), self.__layout_id)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_lists.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_related_list(self, id, param_instance=None):
		"""
		The method to get related list

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
		api_path = api_path + '/crm/v8/settings/related_lists/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.RelatedLists.GetRelatedListParam'), self.__layout_id)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.related_lists.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetRelatedListsParam(object):
	module = Param('module', 'com.zoho.crm.api.RelatedLists.GetRelatedListsParam')


class GetRelatedListParam(object):
	module = Param('module', 'com.zoho.crm.api.RelatedLists.GetRelatedListParam')
