try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class TagsOperations(object):
	def __init__(self):
		"""Creates an instance of TagsOperations"""
		pass

	def get_tags(self, param_instance=None):
		"""
		The method to get tags

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
		api_path = api_path + '/crm/v8/settings/tags'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_tags(self, request, param_instance=None):
		"""
		The method to create tags

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/tags'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_tags(self, request, param_instance=None):
		"""
		The method to update tags

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/tags'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_tag(self, id, request, param_instance=None):
		"""
		The method to update tag

		Parameters:
			id (int) : An int representing the id
			request (BodyWrapper) : An instance of BodyWrapper
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/tags/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def delete_tag(self, id):
		"""
		The method to delete tag

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
		api_path = api_path + '/crm/v8/settings/tags/'
		api_path = api_path + str(id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_DELETE)
		handler_instance.set_category_method(Constants.REQUEST_METHOD_DELETE)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def merge_tags(self, id, request):
		"""
		The method to merge tags

		Parameters:
			id (int) : An int representing the id
			request (MergeWrapper) : An instance of MergeWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.merge_wrapper import MergeWrapper
		except Exception:
			from .merge_wrapper import MergeWrapper

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, MergeWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: MergeWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/tags/'
		api_path = api_path + str(id)
		api_path = api_path + '/actions/merge'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def add_tags(self, module_api_name, record_id, request, param_instance=None):
		"""
		The method to add tags

		Parameters:
			module_api_name (string) : A string representing the module_api_name
			record_id (int) : An int representing the record_id
			request (NewTagRequestWrapper) : An instance of NewTagRequestWrapper
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.new_tag_request_wrapper import NewTagRequestWrapper
		except Exception:
			from .new_tag_request_wrapper import NewTagRequestWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, NewTagRequestWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: NewTagRequestWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/actions/add_tags'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.record_action_handler import RecordActionHandler
		except Exception:
			from .record_action_handler import RecordActionHandler
		return handler_instance.api_call(RecordActionHandler.__module__, 'application/json')

	def remove_tags(self, module_api_name, record_id, request):
		"""
		The method to remove tags

		Parameters:
			module_api_name (string) : A string representing the module_api_name
			record_id (int) : An int representing the record_id
			request (ExistingTagRequestWrapper) : An instance of ExistingTagRequestWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.existing_tag_request_wrapper import ExistingTagRequestWrapper
		except Exception:
			from .existing_tag_request_wrapper import ExistingTagRequestWrapper

		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, ExistingTagRequestWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: ExistingTagRequestWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(module_api_name)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/actions/remove_tags'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.record_action_handler import RecordActionHandler
		except Exception:
			from .record_action_handler import RecordActionHandler
		return handler_instance.api_call(RecordActionHandler.__module__, 'application/json')

	def add_tags_to_multiple_records(self, module_api_name, request, param_instance=None):
		"""
		The method to add tags to multiple records

		Parameters:
			module_api_name (string) : A string representing the module_api_name
			request (NewTagRequestWrapper) : An instance of NewTagRequestWrapper
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.new_tag_request_wrapper import NewTagRequestWrapper
		except Exception:
			from .new_tag_request_wrapper import NewTagRequestWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		if request is not None and not isinstance(request, NewTagRequestWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: NewTagRequestWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(module_api_name)
		api_path = api_path + '/actions/add_tags'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.record_action_handler import RecordActionHandler
		except Exception:
			from .record_action_handler import RecordActionHandler
		return handler_instance.api_call(RecordActionHandler.__module__, 'application/json')

	def remove_tags_from_multiple_records(self, module_api_name, request, param_instance=None):
		"""
		The method to remove tags from multiple records

		Parameters:
			module_api_name (string) : A string representing the module_api_name
			request (ExistingTagRequestWrapper) : An instance of ExistingTagRequestWrapper
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.existing_tag_request_wrapper import ExistingTagRequestWrapper
		except Exception:
			from .existing_tag_request_wrapper import ExistingTagRequestWrapper

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if not isinstance(module_api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_api_name EXPECTED TYPE: str', None, None)
		
		if request is not None and not isinstance(request, ExistingTagRequestWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: ExistingTagRequestWrapper', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/'
		api_path = api_path + str(module_api_name)
		api_path = api_path + '/actions/remove_tags'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.record_action_handler import RecordActionHandler
		except Exception:
			from .record_action_handler import RecordActionHandler
		return handler_instance.api_call(RecordActionHandler.__module__, 'application/json')

	def get_record_count_for_tag(self, id, param_instance=None):
		"""
		The method to get record count for tag

		Parameters:
			id (int) : An int representing the id
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

		if not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/tags/'
		api_path = api_path + str(id)
		api_path = api_path + '/actions/records_count'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.tags.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetTagsParam(object):
	module = Param('module', 'com.zoho.crm.api.Tags.GetTagsParam')
	my_tags = Param('my_tags', 'com.zoho.crm.api.Tags.GetTagsParam')
	include = Param('include', 'com.zoho.crm.api.Tags.GetTagsParam')


class CreateTagsParam(object):
	module = Param('module', 'com.zoho.crm.api.Tags.CreateTagsParam')
	color_code = Param('color_code', 'com.zoho.crm.api.Tags.CreateTagsParam')


class UpdateTagsParam(object):
	module = Param('module', 'com.zoho.crm.api.Tags.UpdateTagsParam')


class UpdateTagParam(object):
	module = Param('module', 'com.zoho.crm.api.Tags.UpdateTagParam')


class AddTagsParam(object):
	over_write = Param('over_write', 'com.zoho.crm.api.Tags.AddTagsParam')


class AddTagsToMultipleRecordsParam(object):
	over_write = Param('over_write', 'com.zoho.crm.api.Tags.AddTagsToMultipleRecordsParam')


class RemoveTagsFromMultipleRecordsParam(object):
	ids = Param('ids', 'com.zoho.crm.api.Tags.RemoveTagsFromMultipleRecordsParam')


class GetRecordCountForTagParam(object):
	module = Param('module', 'com.zoho.crm.api.Tags.GetRecordCountForTagParam')
