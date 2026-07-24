try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.header import Header
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..header import Header


class BulkWriteOperations(object):
	def __init__(self):
		"""Creates an instance of BulkWriteOperations"""
		pass

	def upload_file(self, request, header_instance=None):
		"""
		The method to upload file

		Parameters:
			request (FileBodyWrapper) : An instance of FileBodyWrapper
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.file_body_wrapper import FileBodyWrapper
		except Exception:
			from .file_body_wrapper import FileBodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if request is not None and not isinstance(request, FileBodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: FileBodyWrapper', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + 'https://content.zohoapis.com/crm/v8/upload'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('multipart/form-data')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_header(header_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.action_response import ActionResponse
		except Exception:
			from .action_response import ActionResponse
		return handler_instance.api_call(ActionResponse.__module__, 'application/json')

	def create_bulk_write_job(self, request):
		"""
		The method to create bulk write job

		Parameters:
			request (RequestWrapper) : An instance of RequestWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.request_wrapper import RequestWrapper
		except Exception:
			from .request_wrapper import RequestWrapper

		if request is not None and not isinstance(request, RequestWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: RequestWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/bulk/v8/write'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.action_response import ActionResponse
		except Exception:
			from .action_response import ActionResponse
		return handler_instance.api_call(ActionResponse.__module__, 'application/json')

	def get_bulk_write_job_details(self, job_id):
		"""
		The method to get bulk write job details

		Parameters:
			job_id (string) : A string representing the job_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(job_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: job_id EXPECTED TYPE: str', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/bulk/v8/write/'
		api_path = api_path + str(job_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.response_wrapper import ResponseWrapper
		except Exception:
			from .response_wrapper import ResponseWrapper
		return handler_instance.api_call(ResponseWrapper.__module__, 'application/json')

	def download_bulk_write_result(self, download_url):
		"""
		The method to download bulk write result

		Parameters:
			download_url (string) : A string representing the download_url

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(download_url, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: download_url EXPECTED TYPE: str', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/'
		api_path = api_path + str(download_url)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.bulk_write.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/octet-stream')


class UploadFileHeader(object):
	feature = Header('feature', 'com.zoho.crm.api.BulkWrite.UploadFileHeader')
	x_crm_org = Header('X-CRM-ORG', 'com.zoho.crm.api.BulkWrite.UploadFileHeader')
