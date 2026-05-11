try:
    import importlib
    import logging
    import re
    import json
    from zohocrmsdk.src.com.zoho.crm.api.util import Converter, Constants, JSONConverter
except Exception:
    import importlib
    import logging
    import re
    from .converter import Converter
    from .constants import Constants
    from .json_converter import JSONConverter


class Downloader(Converter):

    """
    This class to process the download file and stream response.
    """

    logger = logging.getLogger('SDKLogger')

    def __init__(self, common_api_handler):

        super().__init__(common_api_handler)
        self.unique_dict = {}
        self.common_api_handler = common_api_handler

    def form_request(self, request_instance, pack, instance_number, class_member_detail):

        return None

    def append_to_request(self, request_base, request_object):

        return

    def get_wrapped_response(self, response, pack):

        return [self.get_response(response, pack)]

    def get_response(self, response, pack):

        try:
            from zohocrmsdk.src.com.zoho.crm.api import Initializer

        except Exception:
            from ..initializer import Initializer

        path_split = str(pack).rpartition(".")
        class_name = self.module_to_class(path_split[-1])
        pack = path_split[0] + "." + class_name
        class_detail = dict(Initializer.json_details[str(pack)])

        if Constants.INTERFACE in class_detail and class_detail[Constants.INTERFACE] is not None:
            classes = class_detail[Constants.CLASSES]

            for each_class in classes:
                if Constants.FILE_BODY_WRAPPER in each_class:
                    return self.get_response(response, each_class)
        else:
            instance = self.get_class(class_name, path_split[0])()

            for member_name, member_detail in class_detail.items():
                data_type = member_detail[Constants.TYPE]
                instance_value = None

                if data_type == Constants.STREAM_WRAPPER_CLASS_PATH:
                    file_name = ''
                    content_disposition = response.headers[Constants.CONTENT_DISPOSITION]

                    if "'" in content_disposition:
                        start_index = content_disposition.rindex("'")
                        file_name = content_disposition[start_index + 1:]

                    elif '"' in content_disposition:
                        start_index = content_disposition.rindex('=')
                        file_name = content_disposition[start_index + 1:].replace('"', '')

                    stream_path_split = str(data_type).rpartition(".")
                    stream_class_name = self.module_to_class(stream_path_split[-1])
                    instance_value = self.get_class(stream_class_name, stream_path_split[0])(file_name, response)

                setattr(instance,
                        self.construct_private_member(class_name=class_name, member_name=member_name), instance_value)

            return instance

    @staticmethod
    def construct_private_member(class_name, member_name):
        return '_' + class_name + '__' + member_name

    @staticmethod
    def get_class(class_name, class_path):
        imported_module = importlib.import_module(class_path)
        class_holder = getattr(imported_module, class_name)
        return class_holder
