try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.header import Header
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..header import Header


class BusinessHoursOperations(object):
	def __init__(self, x_crm_org=None):
		"""
		Creates an instance of BusinessHoursOperations with the given parameters

		Parameters:
			x_crm_org (string) : A string representing the x_crm_org
		"""

		if x_crm_org is not None and not isinstance(x_crm_org, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: x_crm_org EXPECTED TYPE: str', None, None)
		
		self.__x_crm_org = x_crm_org


	def create_business_hours(self, request):
		"""
		The method to create business hours

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.business_hours.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.BusinessHours.CreateBusinessHoursHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.business_hours.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_business_hours(self, request):
		"""
		The method to update business hours

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.business_hours.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.BusinessHours.UpdateBusinessHoursHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.business_hours.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_business_hours(self):
		"""
		The method to get business hours

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.BusinessHours.GetBusinessHoursHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.business_hours.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class CreateBusinessHoursHeader(object):
	pass


class UpdateBusinessHoursHeader(object):
	pass


class GetBusinessHoursHeader(object):
	pass
