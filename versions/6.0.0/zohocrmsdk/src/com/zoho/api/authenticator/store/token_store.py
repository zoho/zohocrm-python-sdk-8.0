try:
    from abc import ABC, abstractmethod

except Exception as e:
    from abc import ABC, abstractmethod


class TokenStore(ABC):

    """
    This class is to store user token details.
    """

    @abstractmethod
    def find_token(self, token):

        """
        The method to get user token details.

        Parameters:
            token (Token) : A Token class instance.

        Returns:
            Token : A Token class instance representing the user token details.
        """

        pass

    @abstractmethod
    def save_token(self, token):

        """
        The method to store user token details.

        Parameters:
            token (Token) : A Token class instance.

        """

        pass

    @abstractmethod
    def delete_token(self, id):

        """
        The method to delete user token details.

        Parameters:
            id (String) : A String representing Token id.
        """

        pass

    @abstractmethod
    def get_tokens(self):

        """
        The method to retrieve all the stored tokens.

        Returns:
            list : A List of Token instances
        """

        pass

    @abstractmethod
    def delete_tokens(self):

        """
        The method to delete all the stored tokens.
        """

    pass
    @abstractmethod
    def find_token_by_id(self, id):

        """
        The method to get id token details.

        Parameters:
            id (String) : A String id.
        Returns:
            Token : A Token class instance representing the id token details.
        """

    pass
