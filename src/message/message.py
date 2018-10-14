from abc import ABC, abstractmethod


class Message(ABC):

    def __init__(self, user):
        self.user = None

    @abstractmethod
    def get_text(self):
        pass


class CipherText:

    def __init__(self, ciphertext_string, aes_key, rsa_private_key):
        self.ciphertext_string = ciphertext_string
        self.aes_key = aes_key
        self.rsa_private_key = rsa_private_key


class PlaintextMessage(Message):

    def __init__(self, user, message_text):
        Message.__init__(user)
        self.text = message_text

    def get_text(self):
        return self.text


class EncryptedMessage(Message):

    def __init__(self, user, ciphertext):
        Message.__init__(user)
        self.ciphertext = ciphertext

    def get_text(self):
        return self.ciphertext.ciphertext_string
    
