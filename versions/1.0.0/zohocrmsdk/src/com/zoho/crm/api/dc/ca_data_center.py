try:
    from zohocrmsdk.src.com.zoho.crm.api.dc.data_center import DataCenter
except Exception as e:
    from .data_center import DataCenter


class CADataCenter(DataCenter):

    """
    This class represents the properties of Zoho CRM in CA Domain.
    """

    @classmethod
    def PRODUCTION(cls):

        """
        This method represents the Zoho CRM Production environment in CA domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://www.zohoapis.ca", cls().get_iam_url(), cls().get_file_upload_url())

    @classmethod
    def SANDBOX(cls):

        """
        This method represents the Zoho CRM Sandbox environment in CA domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://sandbox.zohoapis.ca", cls().get_iam_url(), cls().get_file_upload_url())

    @classmethod
    def DEVELOPER(cls):

        """
        This method represents the Zoho CRM Developer environment in CA domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://developer.zohoapis.ca", cls().get_iam_url(), cls().get_file_upload_url())

    def get_iam_url(self):
        return "https://accounts.zohocloud.ca/oauth/v2/token"

    def get_file_upload_url(self):
        return "https://upload.zohocloud.ca"
