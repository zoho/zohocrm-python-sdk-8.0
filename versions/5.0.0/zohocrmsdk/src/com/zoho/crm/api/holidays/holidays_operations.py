try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, Choice, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
	from zohocrmsdk.src.com.zoho.crm.api.header import Header
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, Choice, CommonAPIHandler, Constants
	from ..param import Param
	from ..header import Header


class HolidaysOperations(object):
	def __init__(self, x_crm_org=None):
		"""
		Creates an instance of HolidaysOperations with the given parameters

		Parameters:
			x_crm_org (string) : A string representing the x_crm_org
		"""

		if x_crm_org is not None and not isinstance(x_crm_org, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: x_crm_org EXPECTED TYPE: str', None, None)
		
		self.__x_crm_org = x_crm_org


	def get_holidays(self, param_instance=None):
		"""
		The method to get holidays

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
		api_path = api_path + '/crm/v8/settings/holidays'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.Holidays.GetHolidaysHeader'), self.__x_crm_org)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_holidays(self, request):
		"""
		The method to create holidays

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/holidays'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.Holidays.CreateHolidaysHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_holidays(self, request):
		"""
		The method to update holidays

		Parameters:
			request (Holidays) : An instance of Holidays

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.holidays import Holidays
		except Exception:
			from .holidays import Holidays

		if request is not None and not isinstance(request, Holidays):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: Holidays', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/holidays'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.Holidays.UpdateHolidaysHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_holiday(self, holiday_id, request):
		"""
		The method to update holiday

		Parameters:
			holiday_id (int) : An int representing the holiday_id
			request (Holidays) : An instance of Holidays

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.holidays import Holidays
		except Exception:
			from .holidays import Holidays

		if not isinstance(holiday_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: holiday_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, Holidays):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: Holidays', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/holidays/'
		api_path = api_path + str(holiday_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.Holidays.UpdateHolidayHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_holiday(self, holiday_id):
		"""
		The method to get holiday

		Parameters:
			holiday_id (int) : An int representing the holiday_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(holiday_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: holiday_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/holidays/'
		api_path = api_path + str(holiday_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.Holidays.GetHolidayHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def delete_holiday(self, holiday_id):
		"""
		The method to delete holiday

		Parameters:
			holiday_id (int) : An int representing the holiday_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(holiday_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: holiday_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/holidays/'
		api_path = api_path + str(holiday_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.Holidays.DeleteHolidayHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.holidays.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetHolidaysHeader(object):
	pass


class GetHolidaysParam(object):
	year = Param('year', 'com.zoho.crm.api.Holidays.GetHolidaysParam')
	type = Param('type', 'com.zoho.crm.api.Holidays.GetHolidaysParam')
	shift_id = Param('shift_id', 'com.zoho.crm.api.Holidays.GetHolidaysParam')


class CreateHolidaysHeader(object):
	pass


class UpdateHolidaysHeader(object):
	pass


class UpdateHolidayHeader(object):
	pass


class GetHolidayHeader(object):
	pass


class DeleteHolidayHeader(object):
	pass
