try:
    import threading
    import os
    import json
    import logging
    import shutil
    from zohocrmsdk.src.com.zoho.crm.api.util import Constants, Converter, Utility
    from zohocrmsdk.src.com.zoho.crm.api.initializer import Initializer
    from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException

except Exception:
    import threading
    import os
    import json
    import logging
    import shutil
    from .constants import Constants
    from .converter import Converter
    from .utility import Utility
    from ..initializer import Initializer
    from ..exception import SDKException


class ModuleFieldsHandler(object):
    logger = logging.getLogger('SDKLogger')
    lock = threading.Lock()

    @staticmethod
    def __get_directory():

        """
        The method to obtain resources directory path.

        Returns:
            str: A String representing the directory's absolute path.
        """
        return os.path.join(Initializer.get_initializer().resource_path, Constants.FIELD_DETAILS_DIRECTORY)

    @staticmethod
    def delete_fields_file():
        """
        The method to delete fields JSON File of the current user.

        Raises:
            SDKException
        """

        with ModuleFieldsHandler.lock:
            try:
                record_field_details_path = os.path.join(ModuleFieldsHandler.__get_directory(), Converter.get_encoded_file_name())
                if os.path.exists(record_field_details_path):
                    os.remove(record_field_details_path)
            except Exception as e:
                sdk_exception = SDKException(cause=e)
                ModuleFieldsHandler.logger.info(Constants.DELETE_FIELD_FILE_ERROR + sdk_exception.__str__())
                raise sdk_exception

    @staticmethod
    def delete_all_field_files():
        """
        The method to delete all the field JSON files under resources directory.

        Raises:
            SDKException
        """

        with ModuleFieldsHandler.lock:
            try:
                record_field_details_directory = ModuleFieldsHandler.__get_directory()
                if os.path.exists(record_field_details_directory):
                    files_list = [os.path.join(record_field_details_directory, file) for file in os.listdir(record_field_details_directory) if os.path.isfile(os.path.join(record_field_details_directory, file))]
                    for each_file in files_list:
                        if Constants.JSON_FILE_EXTENSION in each_file:
                            os.remove(each_file)
            except Exception as e:
                sdk_exception = SDKException(cause=e)
                ModuleFieldsHandler.logger.info(Constants.DELETE_FIELD_FILES_ERROR + sdk_exception.__str__())
                raise sdk_exception

    @staticmethod
    def delete_fields(module):
        """
        The method to delete fields of the given module from the current user's fields JSON file.

        Parameters:
            module(str): A string representing the module.

        Raises:
            SDKException
        """

        try:
            if module is None:
                raise Exception("module should not be None")

            record_field_details_path = os.path.join(ModuleFieldsHandler.__get_directory(), Converter.get_encoded_file_name())
            if os.path.exists(record_field_details_path):
                record_field_details_json = Initializer.get_json(record_field_details_path)
                if module.lower() in record_field_details_json:
                    Utility.delete_fields(record_field_details_json, module)
                    with open(record_field_details_path, mode="w") as file:
                        json.dump(record_field_details_json, file)
                        file.flush()
                        file.close()

        except Exception as e:
            sdk_exception = SDKException(cause=e)
            ModuleFieldsHandler.logger.info(Constants.DELETE_MODULE_FROM_FIELDFILE_ERROR + sdk_exception.__str__())
            raise sdk_exception

    @staticmethod
    def refresh_fields(module):
        """
        The method to force-refresh fields of a module.

        Parameters:
            module(str): A string representing the module.

        Raises:
            SDKException
        """

        with ModuleFieldsHandler.lock:
            try:
                if module is None:
                    raise Exception("module should not be None")

                ModuleFieldsHandler.delete_fields(module)
                Utility.get_fields_info(module)
            except SDKException as ex:
                ModuleFieldsHandler.logger.info(Constants.REFRESH_SINGLE_MODULE_FIELDS_ERROR + module + ex.__str__())
                raise ex
            except Exception as e:
                sdk_exception = SDKException(cause=e)
                ModuleFieldsHandler.logger.info(Constants.REFRESH_SINGLE_MODULE_FIELDS_ERROR + sdk_exception.__str__())
                raise sdk_exception

    @staticmethod
    def refresh_all_modules():
        """
        The method to force-refresh fields of all the available modules.

        Raises:
            SDKException
        """

        with ModuleFieldsHandler.lock:
            try:
                Utility.refresh_modules()
            except SDKException as ex:
                ModuleFieldsHandler.logger.info(Constants.REFRESH_ALL_MODULE_FIELDS_ERROR + ex.__str__())
                raise ex
            except Exception as e:
                sdk_exception = SDKException(cause=e)
                ModuleFieldsHandler.logger.info(Constants.REFRESH_ALL_MODULE_FIELDS_ERROR + sdk_exception.__str__())
                raise sdk_exception
