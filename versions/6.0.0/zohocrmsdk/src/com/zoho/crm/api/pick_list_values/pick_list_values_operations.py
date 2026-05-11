try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class PickListValuesOperations(object):
	def __init__(self, field_id, module=None):
		"""
		Creates an instance of PickListValuesOperations with the given parameters

		Parameters:
			field_id (int) : An int representing the field_id
			module (string) : A string representing the module
		"""

		if not isinstance(field_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field_id EXPECTED TYPE: int', None, None)
		
		if module is not None and not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__field_id = field_id
		self.__module = module


	def get_pick_list_values(self):
		"""
		The method to get pick list values

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/fields/'
		api_path = api_path + str(self.__field_id)
		api_path = api_path + '/pick_list_values'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('module', 'com.zoho.crm.api.PickListValues.GetPickListValuesParam'), self.__module)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.pick_list_values.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetPickListValuesParam(object):
	pass
