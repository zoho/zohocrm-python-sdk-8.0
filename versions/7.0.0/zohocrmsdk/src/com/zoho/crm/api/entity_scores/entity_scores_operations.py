try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
	from zohocrmsdk.src.com.zoho.crm.api.header import Header
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param
	from ..header import Header


class EntityScoresOperations(object):
	def __init__(self, fields=None, cvid=None):
		"""
		Creates an instance of EntityScoresOperations with the given parameters

		Parameters:
			fields (string) : A string representing the fields
			cvid (string) : A string representing the cvid
		"""

		if fields is not None and not isinstance(fields, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: str', None, None)
		
		if cvid is not None and not isinstance(cvid, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: cvid EXPECTED TYPE: str', None, None)
		
		self.__fields = fields
		self.__cvid = cvid


	def get_entity_score(self, record_id):
		"""
		The method to get entity score

		Parameters:
			record_id (int) : An int representing the record_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Entity_Scores__s/'
		api_path = api_path + str(record_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('fields', 'com.zoho.crm.api.EntityScores.GetEntityScoreParam'), self.__fields)
		handler_instance.add_param(Param('cvid', 'com.zoho.crm.api.EntityScores.GetEntityScoreParam'), self.__cvid)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.entity_scores.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_entity_scores(self, param_instance=None, header_instance=None):
		"""
		The method to get entity scores

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap
			header_instance (HeaderMap) : An instance of HeaderMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		try:
			from zohocrmsdk.src.com.zoho.crm.api import HeaderMap
		except Exception:
			from ..header_map import HeaderMap

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		if header_instance is not None and not isinstance(header_instance, HeaderMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: header_instance EXPECTED TYPE: HeaderMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/Entity_Scores__s'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('fields', 'com.zoho.crm.api.EntityScores.GetEntityScoresParam'), self.__fields)
		handler_instance.add_param(Param('cvid', 'com.zoho.crm.api.EntityScores.GetEntityScoresParam'), self.__cvid)
		handler_instance.set_param(param_instance)
		handler_instance.set_header(header_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.entity_scores.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetEntityScoreParam(object):
	pass


class GetEntityScoresParam(object):
	ids = Param('ids', 'com.zoho.crm.api.EntityScores.GetEntityScoresParam')
	sort_by = Param('sort_by', 'com.zoho.crm.api.EntityScores.GetEntityScoresParam')
	sort_order = Param('sort_order', 'com.zoho.crm.api.EntityScores.GetEntityScoresParam')
	page = Param('page', 'com.zoho.crm.api.EntityScores.GetEntityScoresParam')
	per_page = Param('per_page', 'com.zoho.crm.api.EntityScores.GetEntityScoresParam')
	page_token = Param('page_token', 'com.zoho.crm.api.EntityScores.GetEntityScoresParam')


class GetEntityScoresHeader(object):
	if_modified_since = Header('If-Modified-Since', 'com.zoho.crm.api.EntityScores.GetEntityScoresHeader')
