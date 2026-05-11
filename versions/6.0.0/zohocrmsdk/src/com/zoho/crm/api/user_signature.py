try:
    import re
    from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants

except Exception:
    import re
    from zohocrmsdk.src.com.zoho.crm.api.exception.sdk_exception import SDKException
    from .util.constants import Constants


class UserSignature(object):

    """
    This class represents the Zoho CRM User.
    """

    def __init__(self, name):

        """
        Creates an UserSignature class instance with the specified user email.

        Parameters:
            email (str) : A string containing the CRM user email
        """
        self.__name = name

    def get_name(self):
        """
        This is a getter method to get __name.

        Returns:
            string: A string representing __name
        """

        return self.__name
