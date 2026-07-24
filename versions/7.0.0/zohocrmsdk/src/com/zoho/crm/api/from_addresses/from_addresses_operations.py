try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class FromAddressesOperations(object):
	def __init__(self, user_id=None):
		"""
		Creates an instance of FromAddressesOperations with the given parameters

		Parameters:
			user_id (string) : A string representing the user_id
		"""

		if user_id is not None and not isinstance(user_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_id EXPECTED TYPE: str', None, None)
		
		self.__user_id = user_id


	def get_from_addresses(self):
		"""
		The method to get from addresses

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v8/settings/emails/actions/from_addresses'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('user_id', 'com.zoho.crm.api.FromAddresses.GetFromAddressesParam'), self.__user_id)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.from_addresses.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetFromAddressesParam(object):
	pass
