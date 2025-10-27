
class Param(object):

    """
    This class represents the HTTP parameter.
    """

    def __init__(self, name, class_name=None):

        """
        Creates an Param class instance with the following parameters

        Parameters:
            name (str) : A string containing the parameter name.
            class_name (str) : A string containing the parameter class name.
        """

        self.name = name
        self.class_name = class_name
