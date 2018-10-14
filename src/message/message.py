from abc import ABC, abstractmethod


class Message(ABC):

    @abstractmethod
    def get_text(self):
        pass


class PlaintextMessage(Message):

    def __init__(self, message_text):
        self.text = message_text

    def get_text(self):
        return self.text


class EncryptedMessage(Message):

    def __init__(self, key_ciphertext, message_ciphertext, message_authentication_tag=None):
        self.key_ciphertext = key_ciphertext
        self._message_ciphertext = message_ciphertext
        self.message_authentication_tag = message_authentication_tag

    def get_text(self):
        return self._message_ciphertext


class HashedMessage(Message):

    def __init__(self, hashed_text, key):
        self._hashed_text = hashed_text
        self.key = key

    def get_text(self):
        return self._hashed_text

    @abstractmethod
    def get_hashing_function(self):
        pass


class HMACHashedMessage(HashedMessage):

    def __init__(self, hashed_text, key, hashing_function):
        HashedMessage.__init__(self, hashed_text, key)
        self._hashing_function = hashing_function

    def get_mac_object(self):
        return self.hmac_object

    def get_hashing_function(self):
        return self._hashing_function
