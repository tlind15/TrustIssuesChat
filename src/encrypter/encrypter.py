from abc import ABC, abstractmethod


class Encrypter(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def encrypt(self, message, key):
        pass
