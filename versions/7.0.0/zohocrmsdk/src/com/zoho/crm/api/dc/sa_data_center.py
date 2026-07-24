try:
    from zohocrmsdk.src.com.zoho.crm.api.dc.data_center import DataCenter
except Exception as e:
    from .data_center import DataCenter


class SADataCenter(DataCenter):

    """
    This class represents the properties of Zoho CRM in SA Domain.
    """

    @classmethod
    def PRODUCTION(cls):

        """
        This method represents the Zoho CRM Production environment in SA domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://www.zohoapis.sa", cls().get_iam_url(), cls().get_file_upload_url())

    @classmethod
    def SANDBOX(cls):

        """
        This method represents the Zoho CRM Sandbox environment in SA domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://sandbox.zohoapis.sa", cls().get_iam_url(), cls().get_file_upload_url())

    @classmethod
    def DEVELOPER(cls):

        """
        This method represents the Zoho CRM Developer environment in SA domain
        :return: An instance of Environment
        """

        return DataCenter.Environment("https://developer.zohoapis.sa", cls().get_iam_url(), cls().get_file_upload_url())

    def get_iam_url(self):
        return "https://accounts.zoho.sa/oauth/v2/token"

    def get_file_upload_url(self):
        return "https://files.zoho.sa"
