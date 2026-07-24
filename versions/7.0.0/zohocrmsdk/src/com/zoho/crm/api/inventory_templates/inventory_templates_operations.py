try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class InventoryTemplatesOperations(object):
	def __init__(self):
		"""Creates an instance of InventoryTemplatesOperations"""
		pass

	def get_inventory_templates(self, param_instance=None):
		"""
		The method to get inventory templates

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
		api_path = api_path + '/crm/v8/settings/inventory_templates'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.inventory_templates.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_inventory_template(self, template):
		"""
		The method to get inventory template

		Parameters:
			template (int) : An int representing the template

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(template, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: template EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/inventory_templates/'
		api_path = api_path + str(template)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.inventory_templates.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetInventoryTemplatesParam(object):
	module = Param('module', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam')
	category = Param('category', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam')
	sort_by = Param('sort_by', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam')
	sort_order = Param('sort_order', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam')
	filters = Param('filters', 'com.zoho.crm.api.InventoryTemplates.GetInventoryTemplatesParam')
