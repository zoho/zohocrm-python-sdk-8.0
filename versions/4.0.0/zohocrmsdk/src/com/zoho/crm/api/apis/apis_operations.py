try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class APIsOperations(object):
	def __init__(self, filters=None):
		"""
		Creates an instance of ApisOperations with the given parameters

		Parameters:
			filters (string) : A string representing the filters
		"""

		if filters is not None and not isinstance(filters, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: filters EXPECTED TYPE: str', None, None)
		
		self.__filters = filters


	def get_supported_api(self):
		"""
		The method to get supported api

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/__apis'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('filters', 'com.zoho.crm.api.Apis.GetSupportedAPIParam'), self.__filters)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.apis.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetSupportedAPIParam(object):
	pass
