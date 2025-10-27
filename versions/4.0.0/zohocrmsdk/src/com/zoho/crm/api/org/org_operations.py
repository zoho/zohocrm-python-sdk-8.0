try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants


class OrgOperations(object):
	def __init__(self):
		"""Creates an instance of OrgOperations"""
		pass

	def get_organization(self):
		"""
		The method to get organization

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/org'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.org.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_org_photo(self):
		"""
		The method to get org photo

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/org/photo'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.org.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'image/png')

	def upload_organization_photo(self, request):
		"""
		The method to upload organization photo

		Parameters:
			request (FileBodyWrapper) : An instance of FileBodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.org.file_body_wrapper import FileBodyWrapper
		except Exception:
			from .file_body_wrapper import FileBodyWrapper

		if request is not None and not isinstance(request, FileBodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: FileBodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/org/photo'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('multipart/form-data')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.org.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_organization_photo(self):
		"""
		The method to delete organization photo

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/org/photo'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.org.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')


class GetOrganizationHeader(object):
	pass
