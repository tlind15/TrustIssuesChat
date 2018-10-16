from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from os import urandom
from src.message.message import HMACHashedMessage


class HMAC(object):
    """
    Generates an HMAC integrity tag
    """

    @staticmethod
    def generate_tag(message_text, key=None):
        """
        Computes the HMAC integrity tag

        :param message_text: a byte String representing the ciphertext from which to compute the integrity tag
        :param key: a byte String representing a randomly generated 256-bit (32 byte) key
        :return: a HMACHashedMessage object containing the hashed integrity tag, the key, and hashing algorithm used
        """
        if isinstance(message_text, str):
            message_text.encode()

        elif not isinstance(message_text, bytes):
            raise TypeError("The argument 'message_text' is not of type 'bytes'")

        if key is None:
            key = HMAC.get_key()

        elif not isinstance(key, bytes):
            raise TypeError("The argument 'key' is not of type 'bytes'")

        tag_generator = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        tag_generator.update(message_text)  # hashes the message
        hashed_text = tag_generator.finalize()  # returns the hashed message data
        return HMACHashedMessage(hashed_text, key, hashes.SHA256())

    @staticmethod
    def get_key():
        """
        Randomly generates a 256-bit (32 byte) HMAC key

        :return: a byte String representing the HMAC key
        """
        return urandom(32)
