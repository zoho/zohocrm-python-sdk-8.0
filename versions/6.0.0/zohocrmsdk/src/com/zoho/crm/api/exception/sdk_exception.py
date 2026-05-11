import json


class SDKException(Exception):

    """
    This class is the common SDKException object.
    """

    message = 'Caused By: {code} - {message}'

    def __init__(self, code=None, message=None, details=None, cause=None):

        """
        Creates an SDKException class instance with the specified parameters.

        Parameters:
            code (str) : A string containing the Exception error code.
            message (str) : A string containing the Exception error message.
            details (dict) : A dict containing the error response.
            cause (Exception) : A Exception class instance.
        """

        self.code = code
        self.cause = cause
        self.details = details
        self.error_message = "" if message is None else message

        if self.details is not None:
            self.error_message = self.error_message + json.dumps(self.details,default=str)

        if self.cause is not None:
            self.error_message = self.error_message + str(self.cause)

        Exception.__init__(self, code, message)

    def __str__(self):
        return self.message.format(code=self.code, message=self.error_message)
