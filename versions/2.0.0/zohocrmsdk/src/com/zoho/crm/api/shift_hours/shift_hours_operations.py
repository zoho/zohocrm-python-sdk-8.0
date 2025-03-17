try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.header import Header
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..header import Header


class ShiftHoursOperations(object):
	def __init__(self, x_crm_org=None):
		"""
		Creates an instance of ShiftHoursOperations with the given parameters

		Parameters:
			x_crm_org (string) : A string representing the x_crm_org
		"""

		if x_crm_org is not None and not isinstance(x_crm_org, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: x_crm_org EXPECTED TYPE: str', None, None)
		
		self.__x_crm_org = x_crm_org


	def get_shift_hours(self):
		"""
		The method to get shift hours

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours/shift_hours'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.ShiftHours.GetShiftHoursHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_shifts_hours(self, request):
		"""
		The method to create shifts hours

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours/shift_hours'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.ShiftHours.CreateShiftsHoursHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_shift_hours(self, request):
		"""
		The method to update shift hours

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours/shift_hours'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.ShiftHours.UpdateShiftHoursHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_shift_hour(self, shift_id):
		"""
		The method to get shift hour

		Parameters:
			shift_id (int) : An int representing the shift_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(shift_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shift_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours/shift_hours/'
		api_path = api_path + str(shift_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.ShiftHours.GetShiftHourHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_shift_hour(self, shift_id, request):
		"""
		The method to update shift hour

		Parameters:
			shift_id (int) : An int representing the shift_id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(shift_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shift_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours/shift_hours/'
		api_path = api_path + str(shift_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.ShiftHours.UpdateShiftHourHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_shift_hour(self, shift_id):
		"""
		The method to delete shift hour

		Parameters:
			shift_id (int) : An int representing the shift_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(shift_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: shift_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/business_hours/shift_hours/'
		api_path = api_path + str(shift_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.add_header(Header('X-CRM-ORG', 'com.zoho.crm.api.ShiftHours.DeleteShiftHourHeader'), self.__x_crm_org)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.shift_hours.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetShiftHoursHeader(object):
	pass


class CreateShiftsHoursHeader(object):
	pass


class UpdateShiftHoursHeader(object):
	pass


class GetShiftHourHeader(object):
	pass


class UpdateShiftHourHeader(object):
	pass


class DeleteShiftHourHeader(object):
	pass
