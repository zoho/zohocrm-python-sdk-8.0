from abc import abstractmethod, ABC


class DataCenter(ABC):
    """
    This class represents the properties of Zoho CRM DataCenter
    """

    @abstractmethod
    def get_iam_url(self):

        """
        The method to get the accounts URL.
        :return: A str representing the accounts URL.
        """

        pass

    @abstractmethod
    def get_file_upload_url(self):
        """
        The method to get the File Upload URL
        :return: A str representing the File Upload URL
        """

        pass

    class Environment(object):

        def __init__(self, url, accounts_url, file_upload_url):
            """
            Creates an Environment class instance with the specified parameters.
            :param url: A str representing the Zoho CRM API URL.
            :param accounts_url: A str representing the accounts URL.
            :param file_upload_url : A str representing the File Upload URL
            """

            self.url = url
            self.accounts_url = accounts_url
            self.file_upload_url = file_upload_url
            return

    @staticmethod
    def get(config):

        try:
            from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter, JPDataCenter, INDataCenter, EUDataCenter, \
                CNDataCenter, AUDataCenter, CADataCenter, SADataCenter
            from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
            from zohocrmsdk.src.com.zoho.crm.api.util import Constants
        except Exception:
            from ..dc import USDataCenter, JPDataCenter, INDataCenter, EUDataCenter, CNDataCenter, AUDataCenter, \
                CADataCenter, SADataCenter
            from ..exception import SDKException
            from ..util import Constants

        if config in Constants.US_DATACENTER:
            if Constants.SANDBOX in config:
                return USDataCenter.SANDBOX()
            if Constants.DEVELOPER in config:
                return USDataCenter.DEVELOPER()
            return USDataCenter.PRODUCTION()

        elif config in Constants.JP_DATACENTER:
            if Constants.SANDBOX in config:
                return JPDataCenter.SANDBOX()
            if Constants.DEVELOPER in config:
                return JPDataCenter.DEVELOPER()
            return JPDataCenter.PRODUCTION()

        elif config in Constants.IN_DATACENTER:
            if Constants.SANDBOX in config:
                return INDataCenter.SANDBOX()
            if Constants.DEVELOPER in config:
                return INDataCenter.DEVELOPER()
            return INDataCenter.PRODUCTION()

        elif config in Constants.EU_DATACENTER:
            if Constants.SANDBOX in config:
                return EUDataCenter.SANDBOX()
            if Constants.DEVELOPER in config:
                return EUDataCenter.DEVELOPER()
            return EUDataCenter.PRODUCTION()

        elif config in Constants.CN_DATACENTER:
            if Constants.SANDBOX in config:
                return CNDataCenter.SANDBOX()
            if Constants.DEVELOPER in config:
                return CNDataCenter.DEVELOPER()
            return CNDataCenter.PRODUCTION()

        elif config in Constants.AU_DATACENTER:
            if Constants.SANDBOX in config:
                return AUDataCenter.SANDBOX()
            if Constants.DEVELOPER in config:
                return AUDataCenter.DEVELOPER()
            return AUDataCenter.PRODUCTION()
        elif config in Constants.CA_DATACENTER:
            if Constants.SANDBOX in config:
                return CADataCenter.SANDBOX()
            if Constants.DEVELOPER in config:
                return CADataCenter.DEVELOPER()
            return CADataCenter.PRODUCTION()
        elif config in Constants.SA_DATACENTER:
            if Constants.SANDBOX in config:
                return SADataCenter.SANDBOX()
            if Constants.DEVELOPER in config:
                return SADataCenter.DEVELOPER()
            return SADataCenter.PRODUCTION()
        return None
