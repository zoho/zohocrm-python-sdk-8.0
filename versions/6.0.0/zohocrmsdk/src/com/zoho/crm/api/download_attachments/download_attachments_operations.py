try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class DownloadAttachmentsOperations(object):
	def __init__(self):
		"""Creates an instance of DownloadAttachmentsOperations"""
		pass

	def get_download_attachments_details(self, record_id, module, param_instance=None):
		"""
		The method to get download attachments details

		Parameters:
			record_id (int) : An int representing the record_id
			module (string) : A string representing the module
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

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(module)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/Emails/actions/download_attachments'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.download_attachments.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'multipart/form-data')


class GetDownloadAttachmentsDetailsParam(object):
	user_id = Param('user_id', 'com.zoho.crm.api.DownloadAttachments.GetDownloadAttachmentsDetailsParam')
	message_id = Param('message_id', 'com.zoho.crm.api.DownloadAttachments.GetDownloadAttachmentsDetailsParam')
	id = Param('id', 'com.zoho.crm.api.DownloadAttachments.GetDownloadAttachmentsDetailsParam')
	name = Param('name', 'com.zoho.crm.api.DownloadAttachments.GetDownloadAttachmentsDetailsParam')
