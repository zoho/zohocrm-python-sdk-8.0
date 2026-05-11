try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants


class MailMergeOperations(object):
	def __init__(self, module, id):
		"""
		Creates an instance of MailMergeOperations with the given parameters

		Parameters:
			module (string) : A string representing the module
			id (string) : A string representing the id
		"""

		if not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		if not isinstance(id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: str', None, None)
		
		self.__module = module
		self.__id = id


	def send_mail_merge(self, request):
		"""
		The method to send mail merge

		Parameters:
			request (MailMergeWrapper) : An instance of MailMergeWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.mail_merge_wrapper import MailMergeWrapper
		except Exception:
			from .mail_merge_wrapper import MailMergeWrapper

		if request is not None and not isinstance(request, MailMergeWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: MailMergeWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module)
		api_path = api_path + '/'
		api_path = api_path + str(self.__id)
		api_path = api_path + '/actions/send_mail_merge'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def download_mail_merge(self, request):
		"""
		The method to download mail merge

		Parameters:
			request (DownloadMailMergeWrapper) : An instance of DownloadMailMergeWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.download_mail_merge_wrapper import DownloadMailMergeWrapper
		except Exception:
			from .download_mail_merge_wrapper import DownloadMailMergeWrapper

		if request is not None and not isinstance(request, DownloadMailMergeWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: DownloadMailMergeWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module)
		api_path = api_path + '/'
		api_path = api_path + str(self.__id)
		api_path = api_path + '/actions/download_mail_merge'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.download_response_handler import DownloadResponseHandler
		except Exception:
			from .download_response_handler import DownloadResponseHandler
		return handler_instance.api_call(DownloadResponseHandler.__module__, 'application/json')

	def sign_mail_merge(self, request):
		"""
		The method to sign mail merge

		Parameters:
			request (SignMailMergeWrapper) : An instance of SignMailMergeWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.sign_mail_merge_wrapper import SignMailMergeWrapper
		except Exception:
			from .sign_mail_merge_wrapper import SignMailMergeWrapper

		if request is not None and not isinstance(request, SignMailMergeWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: SignMailMergeWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(self.__module)
		api_path = api_path + '/'
		api_path = api_path + str(self.__id)
		api_path = api_path + '/actions/sign_mail_merge'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.mail_merge.sign_action_handler import SignActionHandler
		except Exception:
			from .sign_action_handler import SignActionHandler
		return handler_instance.api_call(SignActionHandler.__module__, 'application/json')
