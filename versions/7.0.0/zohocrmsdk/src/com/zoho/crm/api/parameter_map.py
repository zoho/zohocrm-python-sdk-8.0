try:
    import logging
    from zohocrmsdk.src.com.zoho.crm.api.param import Param
    from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
    from zohocrmsdk.src.com.zoho.crm.api.util.datatype_converter import DataTypeConverter
    from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from zohocrmsdk.src.com.zoho.crm.api.util.header_param_validator import HeaderParamValidator
except Exception:
    import logging
    from .util.constants import Constants
    from .util.header_param_validator import HeaderParamValidator
    from .util.datatype_converter import DataTypeConverter
    from .param import Param
    from ..api.exception import SDKException


class ParameterMap(object):
    """
    This class represents the HTTP parameter name and value.
    """

    def __init__(self):
        """Creates an instance of ParameterMap Class"""

        self.request_parameters = dict()

    def add(self, param, value):

        """
        The method to add parameter name and value.

        Parameters:
            param (Param): A Param class instance.
            value (object): An object containing the parameter value.
        """

        if param is None:
            raise SDKException(Constants.PARAMETER_NONE_ERROR, Constants.PARAM_INSTANCE_NONE_ERROR)

        param_name = param.name

        if param_name is None:
            raise SDKException(Constants.PARAM_NAME_NONE_ERROR, Constants.PARAM_NAME_NONE_ERROR_MESSAGE)

        if value is None:
            raise SDKException(Constants.PARAMETER_NONE_ERROR, param_name + Constants.NONE_VALUE_ERROR_MESSAGE)

        try:
            class_name = param.class_name
            parsed_param_value = None
            if class_name is not None:
                parsed_param_value = HeaderParamValidator().validate(param_name, class_name, value)
            else:
                try:
                    parsed_param_value = DataTypeConverter.post_convert(value, value.__class__.__name__)
                except Exception as e:
                    parsed_param_value = str(value)
            if param_name not in self.request_parameters:
                self.request_parameters[param_name] = str(parsed_param_value)
            else:
                param_value = self.request_parameters[param_name]
                self.request_parameters[param_name] = param_value + ',' + str(parsed_param_value)
        except SDKException as e:
            logging.getLogger('SDKLogger').error(Constants.PARAM_EXCEPTION + e.__str__())
            raise e
        except Exception as e:
            sdk_exception = SDKException(cause=e)
            logging.getLogger('SDKLogger').error(Constants.PARAM_EXCEPTION + sdk_exception.__str__())
            raise sdk_exception
