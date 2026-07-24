
class Choice(object):

    """
    Common Class to provide or obtain a value, when there are multiple supported values.
    """

    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

