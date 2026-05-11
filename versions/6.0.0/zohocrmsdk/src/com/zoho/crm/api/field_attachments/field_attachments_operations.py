try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class FieldAttachmentsOperations(object):
	def __init__(self, module_api_name, record_id, fields_attachment_id=None):
		"""
		Creates an instance of FieldAttachmentsOperations with the given parameters

		Parameters:
			module_api_name (string) : A string representing the module_api_name
			record_id (int) : An int representing the record_id
			fields_attachment_id (int) : An int representing the fields_attachment_id
		"""

		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if fields_attachment_id is not None and not isinstance(fields_attachment_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields_attachment_id EXPECTED TYPE: int', None, None)
		
		self.__module_api_name = module_api_name
		self.__record_id = record_id
		self.__fields_attachment_id = fields_attachment_id


	def get_field_attachments(self):
		"""
		The method to get field attachments

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/actions/download_fields_attachment'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('fields_attachment_id', 'com.zoho.crm.api.FieldAttachments.GetFieldAttachmentsParam'), self.__fields_attachment_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.field_attachments.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/x-download')


class GetFieldAttachmentsParam(object):
	pass
