try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Utility, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Utility, Constants


class ConversionOptionOperations(object):
	def __init__(self, lead_id):
		"""
		Creates an instance of ConversionOptionOperations with the given parameters

		Parameters:
			lead_id (int) : An int representing the lead_id
		"""

		if not isinstance(lead_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lead_id EXPECTED TYPE: int', None, None)
		
		self.__lead_id = lead_id


	def lead_conversion_options(self):
		"""
		The method to lead conversion options

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Leads/'
		api_path = api_path + str(self.__lead_id)
		api_path = api_path + '/__conversion_options'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_module_api_name("Leads")
		Utility.get_fields("Leads,Contacts,Deals,Accounts", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.conversion_option.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')
