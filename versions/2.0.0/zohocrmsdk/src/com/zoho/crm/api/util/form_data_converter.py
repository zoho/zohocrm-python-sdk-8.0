try:
    import importlib
    import logging
    import re
    import json
    from zohocrmsdk.src.com.zoho.crm.api.util import Utility,Converter, Constants, StreamWrapper
    from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException

except Exception:
    import importlib
    import logging
    import re
    from .converter import Converter
    from .constants import Constants
    from .utility import Utility
    from .stream_wrapper import StreamWrapper
    from ..exception import SDKException


class FormDataConverter(Converter):
    """
    This class to process the upload file and stream.
    """

    logger = logging.getLogger('SDKLogger')

    def __init__(self, common_api_handler):

        super().__init__(common_api_handler)
        self.unique_dict = {}
        self.common_api_handler = common_api_handler

    def append_to_request(self, request_base, request_object):
        form_data_request_body = []
        self.add_file_body(request_object, form_data_request_body)
        if not self.common_api_handler.get_api_path().endswith(Constants.FUNCTIONS_PATH) and \
                Constants.FUNCTIONS not in self.common_api_handler.get_api_path():
            request_base.file = True
        return form_data_request_body

    def add_file_body(self, request_object, request_body):
        for key_name, key_value in request_object.items():
            if isinstance(key_value, list):
                for each_object in key_value:
                    if isinstance(each_object, StreamWrapper):
                        request_body.append((key_name, each_object.get_stream()))
                    else:
                        request_body.append((key_name, key_value))
            elif isinstance(key_value, StreamWrapper):
                entry = (key_name, key_value.get_stream())
                request_body.append(entry)
            else:
                entry = (key_name, key_value)
                request_body.append(entry)

    def form_request(self, request_instance, pack, instance_number, class_member_detail):
        path_split = str(pack).rpartition(".")
        class_name = self.module_to_class(path_split[-1])
        pack = path_split[0] + "." + class_name

        try:
            from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
        except Exception:
            from ..initializer import Initializer

        class_detail = dict(Initializer.json_details[str(pack)])
        request = dict()

        if Constants.INTERFACE in class_detail and class_detail[Constants.INTERFACE] is not None:
            request_object_class_name = request_instance.__class__.__module__
            request_object_class_name = str(request_object_class_name)
            path_split = str(request_object_class_name).rpartition(".")
            request_class_name = self.module_to_class(path_split[-1])
            request_object_class_name = path_split[0] + "." + request_class_name
            classes = class_detail[Constants.CLASSES]

            for class_name in classes:
                class_name_interface_lower = str(class_name).lower()
                request_class_path_lower = request_object_class_name.lower()
                if class_name_interface_lower == request_class_path_lower:
                    class_detail = dict(Initializer.json_details[str(class_name)])
                    class_name = str(class_name).rpartition(".")
                    class_name = self.module_to_class(class_name[-1])
                    break

        for member_name, member_detail in class_detail.items():
            modification = None

            if (Constants.READ_ONLY in member_detail and bool(
                    member_detail[Constants.READ_ONLY])) or Constants.NAME not in member_detail:
                continue
            key_name = member_detail[Constants.NAME]
            try:
                modification = getattr(request_instance, Constants.IS_KEY_MODIFIED)(key_name)
            except Exception as e:
                raise SDKException(code=Constants.EXCEPTION_IS_KEY_MODIFIED, cause=e)

            if (modification is None or modification == 0) and Constants.REQUIRED in member_detail and bool(
                    member_detail[Constants.REQUIRED]):
                raise SDKException(Constants.MANDATORY_VALUE_ERROR,
                                   Constants.MANDATORY_KEY_ERROR + member_name)

            field_value = getattr(request_instance, self.construct_private_member(class_name=class_name, member_name=member_name))

            if modification is not None and modification != 0 and field_value is not None and  self.value_checker(
                    class_name=class_name,
                    member_name=member_name,
                    key_details=member_detail,
                    value=field_value,
                    unique_values_map=self.unique_dict,
                    instance_number=instance_number) is True:
                key_name = member_detail.get(Constants.NAME)
                data_type = member_detail.get(Constants.TYPE)

                if data_type == Constants.LIST_NAMESPACE:
                    request[key_name] = self.set_json_array(field_value, member_detail)

                elif data_type == Constants.MAP_NAMESPACE:
                    request[key_name] = self.set_json_object(field_value, member_detail)

                elif Constants.STRUCTURE_NAME in member_detail:
                    request[key_name] = \
                        self.form_request(field_value, member_detail.get(Constants.STRUCTURE_NAME), 0, member_detail)

                else:
                    request[key_name] = field_value

            return request

    def set_json_object(self, field_value, member_detail):
        json_object = {}
        request_object = dict(field_value)

        if member_detail is None:
            for key, value in request_object.items():
                json_object[key] = self.redirector_for_object_to_json(value)

        else:
            keys_detail = member_detail[Constants.KEYS]

            for key_detail in keys_detail:
                key_name = key_detail[Constants.NAME]
                key_value = None

                if key_name in request_object and request_object[key_name] is not None:
                    if Constants.STRUCTURE_NAME in key_detail:
                        key_value = self.form_request(field_value[key_name],
                                                      key_detail[Constants.STRUCTURE_NAME], 0, member_detail)

                    else:
                        key_value = self.redirector_for_object_to_json(field_value[key_name])

                    json_object[key_name] = key_value

        return json_object

    def set_json_array(self, field_value, member_detail):
        json_array = []
        request_objects = list(field_value)

        if member_detail is None:
            for request in request_objects:
                json_array.append(self.redirector_for_object_to_json(request))

        else:
            if Constants.STRUCTURE_NAME in member_detail:
                instance_count = 0
                pack = member_detail[Constants.STRUCTURE_NAME]

                for request in request_objects:
                    json_array.append(self.form_request(request, pack, instance_count, member_detail))
                    instance_count += 1

            else:
                for request in field_value:
                    json_array.append(self.redirector_for_object_to_json(request))

        return json_array

    def redirector_for_object_to_json(self, request):
        if isinstance(request, list):
            return self.set_json_array(request, None)

        if isinstance(request, dict):
            return self.set_json_object(request, None)

        else:
            return request

    def get_wrapped_response(self, response, pack):
        return None

    def get_response(self, response, pack):
        return None

    @staticmethod
    def construct_private_member(class_name, member_name):
        return '_' + class_name + '__' + member_name


