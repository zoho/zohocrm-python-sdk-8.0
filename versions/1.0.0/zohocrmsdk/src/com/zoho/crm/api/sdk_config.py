class SDKConfig(object):
    """
    The class to configure the SDK.
    """

    def __init__(self, auto_refresh_fields=False, pick_list_validation=True, read_timeout=None, connect_timeout=None, update_api_domain=True):
        """
        Creates an instance of SDKConfig with the following parameters

        Parameters:
            auto_refresh_fields(bool): A bool representing auto_refresh_fields
            pick_list_validation(bool): A bool representing pick_list_validation
            read_timeout(float): A Float representing read_timeout
            connect_timeout(float): A Float representing connect_timeout
        """
        self.__auto_refresh_fields = auto_refresh_fields
        self.__pick_list_validation = pick_list_validation
        self.__read_timeout = read_timeout
        self.__connect_timeout = connect_timeout
        self.__update_api_domain = update_api_domain

    def get_auto_refresh_fields(self):
        """
        This is a getter method to get auto_refresh_fields.

        Returns:
            bool: A bool representing auto_refresh_fields
        """
        return self.__auto_refresh_fields

    def get_pick_list_validation(self):
        """
        This is a getter method to get pick_list_validation.

        Returns:
            bool: A bool representing pick_list_validation
        """
        return self.__pick_list_validation

    def get_read_timeout(self):
        """
        This is a getter method to get read_timeout.

        Returns:
            Float: A Float representing read_timeout
        """
        return self.__read_timeout

    def get_connect_timeout(self):
        """
        This is a getter method to get connect_timeout.

        Returns:
            Float: A Float representing connect_timeout
        """
        return self.__connect_timeout

    def apply_api_domain_update(self):
        return self.__update_api_domain
