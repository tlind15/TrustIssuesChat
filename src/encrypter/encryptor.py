from abc import ABC, abstractmethod


class Encryptor(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def encrypt(self, message, key):
        pass
