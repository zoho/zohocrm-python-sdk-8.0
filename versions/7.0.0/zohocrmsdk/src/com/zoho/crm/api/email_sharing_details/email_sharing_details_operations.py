try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants


class EmailSharingDetailsOperations(object):
	def __init__(self, record_id, module):
		"""
		Creates an instance of EmailSharingDetailsOperations with the given parameters

		Parameters:
			record_id (int) : An int representing the record_id
			module (string) : A string representing the module
		"""

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		self.__record_id = record_id
		self.__module = module


	def get_email_sharing_details(self):
		"""
		The method to get email sharing details

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/__emails_sharing_details'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_sharing_details.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')
