try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Utility, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Utility, Constants


class ConvertLeadOperations(object):
	def __init__(self, lead_id):
		"""
		Creates an instance of ConvertLeadOperations with the given parameters

		Parameters:
			lead_id (int) : An int representing the lead_id
		"""

		if not isinstance(lead_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lead_id EXPECTED TYPE: int', None, None)
		
		self.__lead_id = lead_id


	def convert_lead(self, request):
		"""
		The method to convert lead

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.convert_lead.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Leads/'
		api_path = api_path + str(self.__lead_id)
		api_path = api_path + '/actions/convert'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_module_api_name("Deals")
		Utility.get_fields("Deals", handler_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.convert_lead.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')
