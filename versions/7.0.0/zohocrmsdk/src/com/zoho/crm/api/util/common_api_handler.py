try:
    import json
    import platform
    import urllib3
    import logging
    from zohocrmsdk.src.com.zoho.crm.api.util.api_http_connector import APIHTTPConnector
    from zohocrmsdk.src.com.zoho.crm.api.util.json_converter import JSONConverter
    from zohocrmsdk.src.com.zoho.crm.api.util.xml_converter import XMLConverter
    from zohocrmsdk.src.com.zoho.crm.api.util.form_data_converter import FormDataConverter
    from zohocrmsdk.src.com.zoho.crm.api.util.downloader import Downloader
    from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zohocrmsdk.src.com.zoho.crm.api.util.api_response import APIResponse
    from zohocrmsdk.src.com.zoho.crm.api.header_map import HeaderMap
    from zohocrmsdk.src.com.zoho.crm.api.header import Header
    from zohocrmsdk.src.com.zoho.crm.api.parameter_map import ParameterMap
    from zohocrmsdk.src.com.zoho.crm.api.param import Param
    from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException

except Exception:
    import json
    import platform
    import urllib3
    import logging
    from .api_http_connector import APIHTTPConnector
    from .json_converter import JSONConverter
    from .constants import Constants
    from .api_response import APIResponse
    from ..header_map import HeaderMap
    from ..header import Header
    from ..parameter_map import ParameterMap
    from ..param import Param
    from ..exception import SDKException


class CommonAPIHandler(object):
    """
    This class to process the API request and its response.
    Construct the objects that are to be sent as parameters or request body with the API.
    The Request parameter, header and body objects are constructed here.
    Process the response JSON and converts it to relevant objects in the library.
    """
    logger = logging.getLogger('SDKLogger')

    def __init__(self):

        self.__api_path = None
        self.__header = HeaderMap()
        self.__param = ParameterMap()
        self.__request = None
        self.__http_method = None
        self.__module_api_name = None
        self.__content_type = None
        self.__category_method = None
        self.__mandatory_checker = None
    
    def set_content_type(self, content_type):
        """
        The method to set the Content Type

        Parameters:
            content_type(str):  A string containing the Content Type
        """

        self.__content_type = content_type

    def set_api_path(self, api_path):
        """
        The method to set the API Path

        Parameters:
            api_path(str) : A string containing the API Path
        """

        self.__api_path = api_path
    
    def add_param(self, param_instance, param_value):

        """
        The method to add an API request parameter.

        Parameters:
            param_instance (Param) : A Param instance containing the API request parameter.
            param_value (object) : An object containing the API request parameter value.
        """

        if param_value is None:
            return

        if self.__param is None:
            self.__param = ParameterMap()

        self.__param.add(param_instance, param_value)

    def add_header(self, header_instance, header_value):
        """
        The method to add an API request header.

        Parameters:
            header_instance (Header) : A Header instance containing the API request header.
            header_value (object) : An object containing the API request header value.
        """

        if header_value is None:
            return

        if self.__header is None:
            self.__header = HeaderMap()

        self.__header.add(header_instance, header_value)

    def set_param(self, param):
        """
        The method to set the API request parameter map.

        Parameters:
            param(ParameterMap) : A ParameterMap class instance containing the API request parameters
        """

        if param is None:
            return

        if self.__param.request_parameters is not None and self.__param.request_parameters:
            self.__param.request_parameters.update(param.request_parameters)
        else:
            self.__param = param

    def get_module_api_name(self):
        """
        The method to get the Module API Name

        Returns:
            string: A string representing the Module API Name
        """

        return self.__module_api_name

    def set_module_api_name(self, module_api_name):
        """
        The method to set the Module API Name

        Parameters:
            module_api_name(str):  A string containing the Module API Name
        """

        self.__module_api_name = module_api_name

    def set_header(self, header):
        """
        The method to set the API request header map.

        Parameters:
            header(HeaderMap): A HeaderMap class instance containing the API request headers
        """

        if header is None:
            return

        if self.__header.request_headers is not None and self.__header.request_headers:
            self.__header.request_headers.update(header.request_headers)
        else:
            self.__header = header

    def set_request(self, request):
        """
        The method to set the request instance.

        Parameters:
            request(object): An object containing the request body

        """
        self.__request = request

    def set_http_method(self, http_method):
        """
        The method to set the HTTP Method

        Parameters:
            http_method(str):  A string containing the HTTP method.
        """

        self.__http_method = http_method

    def api_call(self, class_name, encode_type):

        """
        The method to construct API request and response details. To make the Zoho CRM API calls.

        Parameters:
            class_name(str): A str containing the method return type.
            encode_type(str): A str containing the expected API response content type.

        Returns:
            APIResponse: An instance of APIResponse representing the Zoho CRM API response instance

        Raises:
            SDKException
        """

        try:
            from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        if Initializer.get_initializer() is None:
            raise SDKException(code=Constants.SDK_UNINITIALIZATION_ERROR,
                               message=Constants.SDK_UNINITIALIZATION_MESSAGE)

        connector = APIHTTPConnector()
        try:
            self.set_api_url(connector)
        except SDKException as e:
            CommonAPIHandler.logger.error(Constants.SET_API_URL_EXCEPTION + e.__str__())
            raise e
        except Exception as e:
            sdk_exception = SDKException(cause=e)
            CommonAPIHandler.logger.error(Constants.SET_API_URL_EXCEPTION + sdk_exception.__str__())
            raise sdk_exception

        connector.request_method = self.__http_method
        connector.content_type = self.__content_type

        if self.__header is not None and len(self.__header.request_headers) > 0:
            connector.headers = self.__header.request_headers

        if self.__param is not None and len(self.__param.request_parameters) > 0:
            connector.parameters = self.__param.request_parameters

        try:
            Initializer.get_initializer().token.authenticate(connector)
        except SDKException as e:
            CommonAPIHandler.logger.info(Constants.AUTHENTICATION_EXCEPTION + e.__str__())
            raise e
        except Exception as e:
            sdk_exception = SDKException(cause=e)
            CommonAPIHandler.logger.error(Constants.AUTHENTICATION_EXCEPTION + sdk_exception.__str__())
            raise sdk_exception

        convert_instance = None

        if self.__content_type is not None and \
                self.__http_method in [Constants.REQUEST_METHOD_PATCH, Constants.REQUEST_METHOD_POST,
                                       Constants.REQUEST_METHOD_PUT]:
            try:
                convert_instance = self.get_converter_class_instance(self.__content_type.lower())
                request = convert_instance.form_request(self.__request, self.__request.__class__.__module__, None, None)
            except SDKException as e:
                CommonAPIHandler.logger.info(Constants.FORM_REQUEST_EXCEPTION + e.__str__())
                raise e
            except Exception as e:
                sdk_exception = SDKException(cause=e)
                CommonAPIHandler.logger.error(Constants.FORM_REQUEST_EXCEPTION + sdk_exception.__str__())
                raise sdk_exception

            connector.request_body = request

        try:
            connector.headers[
                Constants.ZOHO_SDK] = platform.system() + "/" + \
                                      platform.release() + "/python-8.0/" + platform.python_version() + ":" + \
                                      Constants.SDK_VERSION
            response = connector.fire_request(convert_instance)
            return_object = None
            response_json = None

            if Constants.CONTENT_TYPE in response.headers:
                content_type = response.headers[Constants.CONTENT_TYPE]

                if ";" in content_type:
                    content_type = content_type.rpartition(";")[0]

                convert_instance = self.get_converter_class_instance(str(content_type).lower())
                response_object = convert_instance.get_wrapped_response(response, class_name)
                if response_object is not None:
                    if response_object[0] is not None:
                        return_object = response_object[0]
                    if len(response_object) == 2 and response_object[1] is not None:
                        response_json = response_object[1]
            else:
                CommonAPIHandler.logger.info(response.__str__())

            return APIResponse(response.headers, response.status_code, return_object, response_json)
        except SDKException as e:
            CommonAPIHandler.logger.info(Constants.API_CALL_EXCEPTION + e.__str__())
        except Exception as e:
            sdk_exception = SDKException(cause=e)
            CommonAPIHandler.logger.error(Constants.API_CALL_EXCEPTION + sdk_exception.__str__())
            raise sdk_exception

    def get_converter_class_instance(self, encode_type):

        """
        This method to get a Converter class instance.
        :param encode_type: A str containing the API response content type.
        :return: A Converter class instance.
        """

        switcher = {

            "application/json": JSONConverter(self),

            "text/plain": Downloader(self),

            "application/ld+json": JSONConverter(self),

            "application/xml": XMLConverter(self),

            "text/xml": XMLConverter(self),

            "multipart/form-data": FormDataConverter(self),

            "application/x-download": Downloader(self),

            "image/png": Downloader(self),

            "image/jpeg": Downloader(self),

            "image/gif": Downloader(self),

            "image/tiff": Downloader(self),

            "image/svg+xml": Downloader(self),

            "image/bmp": Downloader(self),

            "image/webp": Downloader(self),

            "text/html": Downloader(self),

            "text/css": Downloader(self),

            "text/javascript": Downloader(self),

            "text/calendar": Downloader(self),

            "application/zip": Downloader(self),

            "application/pdf": Downloader(self),

            "application/java-archive": Downloader(self),

            "application/javascript": Downloader(self),

            "application/xhtml+xml": Downloader(self),

            "application/x-bzip": Downloader(self),

            "application/msword": Downloader(self),

            "application/vnd.openxmlformats-officedocument.wordprocessingml.document": Downloader(self),

            "application/gzip": Downloader(self),

            "application/x-httpd-php": Downloader(self),

            "application/vnd.ms-powerpoint": Downloader(self),

            "application/vnd.rar": Downloader(self),

            "application/x-sh": Downloader(self),

            "application/x-tar": Downloader(self),

            "application/vnd.ms-excel": Downloader(self),

            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": Downloader(self),

            "application/x-7z-compressed": Downloader(self),

            "audio/mpeg": Downloader(self),

            "audio/x-ms-wma": Downloader(self),

            "audio/vnd.rn-realaudio": Downloader(self),

            "audio/x-wav": Downloader(self),

            "audio/3gpp": Downloader(self),

            "audio/3gpp2": Downloader(self),

            "video/mpeg": Downloader(self),

            "video/mp4": Downloader(self),

            "video/webm": Downloader(self),

            "video/3gpp": Downloader(self),

            "video/3gpp2": Downloader(self),

            "font/ttf": Downloader(self),

            "text/csv": Downloader(self),

            "application/octet-stream": Downloader(self),
        }

        return switcher.get(encode_type, None)

    def set_api_url(self, connector):
        try:
            from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        api_path = ''

        if Constants.HTTP in self.__api_path:
            if Constants.CONTENT_API_URL in self.__api_path:
                api_path = Initializer.get_initializer().environment.file_upload_url

                try:
                    url_parse = urllib3.util.parse_url(self.__api_path)
                    path = url_parse.path
                except Exception as ex:
                    raise SDKException(code=Constants.INVALID_URL_ERROR, cause=ex)

                api_path = api_path + path
            else:
                if str(self.__api_path)[:1].__eq__('/'):
                    self.__api_path = self.__api_path[1:]

                api_path = api_path + self.__api_path
        else:
            api_path = Initializer.get_initializer().environment.url
            api_path = api_path + self.__api_path

        connector.url = api_path
    
    def get_mandatory_checker(self):
        """
        The method to get the Mandatory Checker

        Returns:
            bool: A boolean representing the Mandatory Checker.
        """
        return self.__mandatory_checker
        
    def set_mandatory_checker(self, mandatory_checker):
        """
        The method to set the Mandatory Checker

        Parameters:
            mandatory_checker(bool): A boolean containing the Mandatory Checker.
        """

        self.__mandatory_checker = mandatory_checker

    def get_http_method(self):
        """
        The method to get the HTTP Method

        Returns:
            string: A string representing the HTTP Method
        """

        return self.__http_method
    
    def get_category_method(self):
        """
        The method to get the Category Method

        Returns:
            string: A string representing the Category method.
        """

        return self.__category_method

    def set_category_method(self, category_method):
        """
        The method to set the Category Method

        Parameters:
            category_method(str):  A string containing the Category method.
        """

        self.__category_method = category_method

    def get_api_path(self):
        """
        The method to get the API Path

        Returns:
            string: A string representing the API Path
        """
        return self.__api_path
