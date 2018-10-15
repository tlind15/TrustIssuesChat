from abc import ABC, abstractmethod


class Message(ABC):
    """
    the abstract base class that serves at the input to both the encrypter and decrypter modules
    """

    @abstractmethod
    def get_text(self):
        pass


class PlaintextMessage(Message):

    def __init__(self, message_text):
        """
        :param message_text: a String corresponding to the message text
        """
        self.text = message_text.encode()

    def get_text(self):
        """
        This method overrides the abstract method from the Message class so that all types of Messages
        have similar behavior and usage

        :return: the message text String
        """
        return self.text

class EncryptedMessage(Message):

    def __init__(self, key_ciphertext, message_ciphertext, message_authentication_tag=None):
        """
        Contains the encrypted ciphertext and the corresponding key which is itself encrypted

        :param key_ciphertext: a byte String that represents the encrypted keys
        :param message_ciphertext: a byte String that represents the encrypted message
        :param message_authentication_tag: a byte String that represents the message integrity tag
        """

        self.key_ciphertext = key_ciphertext
        self._message_ciphertext = message_ciphertext
        self.message_authentication_tag = message_authentication_tag

    def get_text(self):
        """
        This method overrides the abstract method from the Message class so that all types of Messages
        have similar behavior and usage

        :return: the message text String
        """
        return self._message_ciphertext


# holds a message that has been hashed and its corresponding key
class HashedMessage(Message):

    def __init__(self, hashed_text, key):
        """
        Class contained a hashed message that can be used as an integrity tag

        :param hashed_text: a byte String containing the hashed text
        :param key: a byte String containing the key for the message authentication tag
        """
        self._hashed_text = hashed_text
        self.key = key

    def get_text(self):
        """
        This method overrides the abstract method from the Message class so that all types of Messages
        have similar behavior and usage

        :return: the message text String
        """
        return self._hashed_text

    @abstractmethod
    def get_hashing_function(self):
        """
        :return: a HashingAlgorithm object from the Cryptography library denoting the hashing function
        that was used
        """
        pass


class HMACHashedMessage(HashedMessage):

    def __init__(self, hashed_text, key, hashing_function):

        """
        Defines HMAC integrity tag that has been hashed using the 'hashing_function' argument

        :param hashed_text: a byte String containing the hashed text
        :param key: a byte String containing the key for the message authentication tag
        :param hashing_function: a HashingAlgorithm object from the Cryptography library denoting the hashing function
        that was used
        """
        HashedMessage.__init__(self, hashed_text, key)
        self._hashing_function = hashing_function

    def get_hashing_function(self):
        """
        :return: a HsahingAlgorithm object from the Cryptography class
        """
        return self._hashing_function
