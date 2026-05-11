try:
    from abc import ABC, abstractmethod
    import logging
    import sys
    import zlib
    import base64
    import re
    import os
    import importlib
    from zohocrmsdk.src.com.zoho.crm.api.util import Utility, Choice
    from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer

except Exception:
    from abc import ABC, abstractmethod
    import logging
    import sys
    import zlib
    import base64
    import re
    import os
    import importlib
    from .utility import Utility
    from .choice import Choice
    from ..initializer import Initializer

class Converter(ABC):
    """
    This abstract class is to construct API request and response.
    """

    logger = logging.getLogger('SDKLogger')

    def __init__(self, common_api_handler):

        """
        Creates a Converter class instance with the CommonAPIHandler class instance.
        :param common_api_handler: A CommonAPIHandler class instance.
        """

        self.common_api_handler = common_api_handler

    @abstractmethod
    def get_response(self, response, pack):

        """
        This abstract method to process the API response.
        :param response: A object containing the API response contents or response.
        :param pack: A str containing the expected method return type.
        :return: A object representing the POJO class instance.
        """

        pass

    @abstractmethod
    def form_request(self, request_instance, pack, instance_number, class_member_detail):

        """
        This abstract method to construct the API request.
        :param request_instance: A Object containing the POJO class instance.
        :param pack: A str containing the expected method return type.
        :param instance_number: An int containing the POJO class instance list number.
        :param class_member_detail : A dict representing the member details
        :return: A object representing the API request body object.
        """

        pass

    @abstractmethod
    def append_to_request(self, request_base, request_object):

        """
        This abstract method to construct the API request body.
        :param request_base: A HttpEntityEnclosingRequestBase class instance.
        :param request_object: A object containing the API request body object.
        """

        pass

    @abstractmethod
    def get_wrapped_response(self, response, pack):

        """
        This abstract method to process the API response.
        :param response: A object containing the HttpResponse class instance.
        :param pack: A str containing the expected method return type.
        :return: A object representing the POJO class instance.
        """
        pass

    def value_checker(self, class_name, member_name, key_details, value, unique_values_map, instance_number):

        """
        This method is to validate if the input values satisfy the constraints for the respective fields.
        :param class_name: A str containing the class name.
        :param member_name: A str containing the member name.
        :param key_details: A JSON object containing the key JSON details.
        :param value: A object containing the key value.
        :param unique_values_map: A list containing the construct objects.
        :param instance_number: An int containing the POJO class instance list number.
        :return: A bool representing the key value is expected pattern, unique, length, and values.
        """

        try:
            from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
            from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
            from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer

        except Exception:
            from ..exception import SDKException
            from .constants import Constants
            from ..initializer import Initializer

        details_jo = {}
        name = key_details[Constants.NAME]
        data_type = key_details[Constants.TYPE]
        check = True
        given_type = None

        if value is not None:
            if Constants.INTERFACE in key_details and key_details[Constants.INTERFACE]:
                interface_details = Initializer.get_initializer().json_details[key_details[Constants.STRUCTURE_NAME]]
                classes = interface_details[Constants.CLASSES]
                check = False
                for each_class in classes:
                    path_split = str(value.__class__.__module__).rpartition(".")
                    class_name = self.module_to_class(path_split[-1])
                    pack = path_split[0] + "." + class_name

                    if pack == each_class:
                        check = True
                        break
            else:
                given_type = value.__class__

        if data_type in Constants.DATA_TYPE:
            if value is not None and isinstance(value, list) and Constants.STRUCTURE_NAME in key_details:
                structure_name = key_details[Constants.STRUCTURE_NAME]
                index = 0
                path_split = str(structure_name).rpartition('.')
                imported_module = importlib.import_module(path_split[0])
                class_holder = getattr(imported_module, path_split[-1])

                for each_instance in value:
                    if not isinstance(each_instance, class_holder):
                        check = False
                        instance_number = index
                        data_type = Constants.LIST_KEY + '[' + structure_name + ']'
                        given_type = each_instance.__module__
                        break

                    index = index + 1
            elif value is not None and isinstance(value, list) and Constants.SUB_TYPE in key_details:
                index = 0
                sub_type1 = key_details[Constants.SUB_TYPE]
                sub_type = sub_type1[Constants.TYPE]
                if sub_type.lower() == Constants.OBJECT_KEY:
                    check = True
                else:
                    for each_instance in value:
                        if not Utility.check_data_type(each_instance, sub_type):
                            check = False
                            instance_number = index
                            if sub_type in Constants.DATA_TYPE:
                                sub_type = Constants.DATA_TYPE.get(sub_type).__name__
                            data_type = Constants.LIST_KEY + '[' + sub_type + ']'
                            given_type = Constants.LIST_KEY + '[' + each_instance.__class__.__name__ + ']'
                            break
                        index = index + 1
            else:
                check = Utility.check_data_type(value=value, data_type=data_type)

        elif value is not None and data_type.lower() != Constants.OBJECT_KEY:
            if data_type == "TimeZone":
                check = True
            else:
                path_split = str(data_type).rpartition('.')
                imported_module = importlib.import_module(path_split[0])
                class_holder = getattr(imported_module, path_split[-1])

                if not isinstance(value, class_holder):
                    check = False
        if not check and value is not None:
            details_jo[Constants.FIELD] = name
            details_jo[Constants.CLASS] = class_name
            details_jo[Constants.ACCEPTED_TYPE] = data_type
            details_jo[Constants.GIVEN_TYPE] = given_type
            if instance_number is not None:
                details_jo[Constants.INDEX] = instance_number

            raise SDKException(code=Constants.TYPE_ERROR, details=details_jo)

        if Constants.VALUES in key_details and \
                (Constants.PICKLIST not in key_details
                 or (key_details[Constants.PICKLIST]
                     and Initializer.get_initializer().sdk_config.get_pick_list_validation())):
            values_ja = key_details[Constants.VALUES]
            self.check_choice_value1(member_name, class_name, instance_number, values_ja, value, details_jo)

        if Constants.UNIQUE in key_details:
            if name not in unique_values_map:
                unique_values_map[name] = []

            values_array = unique_values_map[name]

            if value in values_array:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.FIRST_INDEX] = values_array.index(value) + 1
                details_jo[Constants.NEXT_INDEX] = instance_number

                raise SDKException(code=Constants.UNIQUE_KEY_ERROR, details=details_jo)

            else:
                unique_values_map[name].append(value)

        if Constants.MIN_LENGTH in key_details or Constants.MAX_LENGTH in key_details:
            count = len(str(value))

            if isinstance(value, list):
                count = len(value)

            if Constants.MAX_LENGTH in key_details and count > key_details[Constants.MAX_LENGTH]:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.GIVEN_LENGTH] = count
                details_jo[Constants.MAXIMUM_LENGTH] = key_details[Constants.MAX_LENGTH]

                raise SDKException(code=Constants.MAXIMUM_LENGTH_ERROR, details=details_jo)

            if Constants.MIN_LENGTH in key_details and count < key_details[Constants.MIN_LENGTH]:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.GIVEN_LENGTH] = count
                details_jo[Constants.MINIMUM_LENGTH] = key_details[Constants.MIN_LENGTH]

                raise SDKException(code=Constants.MINIMUM_LENGTH_ERROR, details=details_jo)

        return True

    def module_to_class(self, module_name):
        if "_" in module_name:
            class_name = ''
            module_split = str(module_name).split('_')
            for each_name in module_split:
                each_name = each_name.capitalize()
                class_name += each_name
        else:
            class_name = module_name[0].upper() + module_name[1:]

        return class_name

    def check_choice_value(self, class_name, key_details, value):
        try:
            from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
            from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
        except Exception:
            from .constants import Constants
            from ..initializer import Initializer
    
        name = key_details[Constants.NAME]
        if Constants.VALUES in key_details and name is not None and (Constants.PICKLIST not in key_details or (key_details[Constants.PICKLIST] and Initializer.get_initializer().sdk_config.get_pick_list_validation())):
            values_ja = key_details[Constants.VALUES]
            self.check_choice_value1(name, class_name, 0, values_ja, value, {})

    def check_choice_value1(self, member_name, class_name, instance_number, values_ja, value, details_jo):
        try:
            from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
            from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
        except Exception:
            from ..exception import SDKException
            from .constants import Constants

        if isinstance(value, list):
            value_1 = value
            for value_2 in value_1:
                if isinstance(value_2, Choice):
                    choice = value_2
                    value_2 = choice.get_value()
                if str(value_2) not in values_ja:
                    details_jo[Constants.FIELD] = member_name
                    details_jo[Constants.CLASS] = class_name
                    details_jo[Constants.GIVEN_VALUE] = value
                    details_jo[Constants.ACCEPTED_VALUES] = values_ja
                    if instance_number is not None:
                        details_jo[Constants.INDEX] = instance_number

                    raise SDKException(code=Constants.UNACCEPTED_VALUES_ERROR, details=details_jo)
        else:
            if isinstance(value, Choice):
                value = value.get_value()

            if value not in values_ja:
                details_jo[Constants.FIELD] = member_name
                details_jo[Constants.CLASS] = class_name
                details_jo[Constants.GIVEN_VALUE] = value
                details_jo[Constants.ACCEPTED_VALUES] = values_ja
                if instance_number is not None:
                    details_jo[Constants.INDEX] = instance_number

                raise SDKException(code=Constants.UNACCEPTED_VALUES_ERROR, details=details_jo)

    @classmethod
    def get_encoded_file_name(self):

        try:
            from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
        except:
            from ....api.authenticator.oauth_token import OAuthToken
        initializer = Initializer.get_initializer()
        token = initializer.token
        token_key = ""
        if isinstance(token, OAuthToken):
            oauth_token = token
            if oauth_token.get_user_signature() is not None:
                token_key = oauth_token.get_user_signature().get_name()
            else:
                refresh_token = oauth_token.get_refresh_token()
                if refresh_token is not None and len(refresh_token) > 0:
                    token_key = refresh_token[0:len(refresh_token) - 32]
                else:
                    access_token = oauth_token.get_access_token()
                    if access_token is not None and len(access_token) > 0:
                        token_key = access_token[0:len(access_token) - 32]

        file_name = initializer.environment.url
        if token_key is not None and len(token_key) > 0:
            file_name = file_name + token_key

        input_bytes = file_name.encode("UTF-8")
        encoded_string = base64.b64encode(input_bytes)
        encoded_string = str(encoded_string.decode("UTF-8"))
        return encoded_string + '.json'
