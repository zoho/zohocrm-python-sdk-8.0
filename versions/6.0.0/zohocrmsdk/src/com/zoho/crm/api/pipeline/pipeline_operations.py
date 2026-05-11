try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class PipelineOperations(object):
	def __init__(self, layout_id=None):
		"""
		Creates an instance of PipelineOperations with the given parameters

		Parameters:
			layout_id (int) : An int representing the layout_id
		"""

		if layout_id is not None and not isinstance(layout_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: layout_id EXPECTED TYPE: int', None, None)
		
		self.__layout_id = layout_id


	def get_pipelines(self):
		"""
		The method to get pipelines

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/pipeline'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.GetPipelinesParam'), self.__layout_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_pipeline(self, request):
		"""
		The method to create pipeline

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/pipeline'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.CreatePipelineParam'), self.__layout_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_pipelines(self, request):
		"""
		The method to update pipelines

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/pipeline'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.UpdatePipelinesParam'), self.__layout_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_pipeline(self, id):
		"""
		The method to get pipeline

		Parameters:
			id (int) : An int representing the id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/pipeline/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.GetPipelineParam'), self.__layout_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_pipeline(self, id, request):
		"""
		The method to update pipeline

		Parameters:
			id (int) : An int representing the id
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/pipeline/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.UpdatePipelineParam'), self.__layout_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_pipeline(self, id, request):
		"""
		The method to delete pipeline

		Parameters:
			id (int) : An int representing the id
			request (DPipelineWrapper) : An instance of DPipelineWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.d_pipeline_wrapper import DPipelineWrapper
		except Exception:
			from .d_pipeline_wrapper import DPipelineWrapper

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, DPipelineWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: DPipelineWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/pipeline/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PATCH)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.DeletePipelineParam'), self.__layout_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def transfer_pipelines(self, request):
		"""
		The method to transfer pipelines

		Parameters:
			request (TransferPipelineWrapper) : An instance of TransferPipelineWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.transfer_pipeline_wrapper import TransferPipelineWrapper
		except Exception:
			from .transfer_pipeline_wrapper import TransferPipelineWrapper

		if request is not None and not isinstance(request, TransferPipelineWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: TransferPipelineWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/pipeline/actions/transfer'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.add_param(Param('layout_id', 'com.zoho.crm.api.Pipeline.TransferPipelinesParam'), self.__layout_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.pipeline.transfer_pipeline_action_handler import TransferPipelineActionHandler
		except Exception:
			from .transfer_pipeline_action_handler import TransferPipelineActionHandler
		return handler_instance.api_call(TransferPipelineActionHandler.__module__, 'application/json')


class GetPipelinesParam(object):
	pass


class CreatePipelineParam(object):
	pass


class UpdatePipelinesParam(object):
	pass


class GetPipelineParam(object):
	pass


class UpdatePipelineParam(object):
	pass


class DeletePipelineParam(object):
	pass


class TransferPipelinesParam(object):
	pass
