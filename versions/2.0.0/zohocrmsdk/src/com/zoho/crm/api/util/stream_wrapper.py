try:
    import os
    from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
    from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
    import os
    from ..exception import SDKException
    from .constants import Constants


class StreamWrapper(object):

    """
    This class handles the file stream and name.
    """

    def __init__(self, name=None, stream=None, file_path=None):

        """
        Creates a StreamWrapper class instance with the specified parameters.

        Parameters:
            name (str) : A string containing the file name.
            stream (stream) : A stream containing the file stream.
            file_path (str) : A string containing the absolute file path.
        """

        if file_path is not None:
            if not os.path.exists(file_path):
                raise SDKException(Constants.FILE_ERROR, Constants.FILE_DOES_NOT_EXISTS)

            self.__name = os.path.basename(file_path)
            self.__stream = open(file_path, 'rb')

        else:
            self.__name = name
            self.__stream = stream

    def get_name(self):

        """
        This is a getter method to get the file name.

        Returns:
            string : A string representing the file name.
        """

        return self.__name

    def get_stream(self):

        """
        This is a getter method to get the file input stream.

        Returns:
            stream :  A stream representing the file stream.
        """

        return self.__stream
