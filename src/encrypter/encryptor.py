from abc import ABC, abstractmethod


class Encryptor(ABC):

    def __init__(self):
        """
        an Abstract base class that is the parent of all encrypting classes in the encrypter module and
        allows for all of them to have a similar interface
        """
        pass

    @abstractmethod
    def encrypt(self, message, key):
        pass
