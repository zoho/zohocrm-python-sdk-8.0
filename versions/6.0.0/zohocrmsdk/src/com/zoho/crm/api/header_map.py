try:
    import logging
    from zohocrmsdk.src.com.zoho.crm.api.header import Header
    from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
    from zohocrmsdk.src.com.zoho.crm.api.util.datatype_converter import DataTypeConverter
    from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zohocrmsdk.src.com.zoho.crm.api.util.header_param_validator import HeaderParamValidator
except Exception:
    import logging
    from .util.constants import Constants
    from .util.header_param_validator import HeaderParamValidator
    from .util.datatype_converter import DataTypeConverter
    from .header import Header
    from ..api.exception import SDKException


class HeaderMap(object):

    """
    This class represents the HTTP header name and value.
    """

    def __init__(self):
        """Creates an instance of HeaderMap Class"""

        self.request_headers = dict()

    def add(self, header, value):

        """
        The method to add the parameter name and value.

        Parameters:
            header (Header): A Header class instance.
            value (object): An object containing the header value.
        """

        if header is None:
            raise SDKException(Constants.HEADER_NONE_ERROR, Constants.HEADER_INSTANCE_NONE_ERROR)

        header_name = header.name

        if header_name is None:
            raise SDKException(Constants.HEADER_NAME_NONE_ERROR, Constants.HEADER_NAME_NULL_ERROR_MESSAGE)

        if value is None:
            raise SDKException(Constants.HEADER_NONE_ERROR, header_name + Constants.NONE_VALUE_ERROR_MESSAGE)
        try:
            class_name = header.class_name
            parsed_header_value = None
            if class_name is not None:
                parsed_header_value = HeaderParamValidator().validate(header_name, class_name, value)
            else:
                try:
                    parsed_header_value = DataTypeConverter.post_convert(value, value.__class__.__name__)
                except Exception as e:
                    parsed_header_value = str(value)
            if header_name not in self.request_headers:
                self.request_headers[header_name] = str(parsed_header_value)
            else:
                header_value = self.request_headers[header_name]
                self.request_headers[header_name] = header_value + ',' + str(parsed_header_value)
        except SDKException as e:
            logging.getLogger('SDKLogger').error(Constants.HEADER_EXCEPTION + e.__str__())
            raise e
        except Exception as e:
            sdk_exception = SDKException(cause=e)
            logging.getLogger('SDKLogger').error(Constants.HEADER_EXCEPTION + sdk_exception.__str__())
            raise sdk_exception
