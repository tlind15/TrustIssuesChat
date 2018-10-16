from abc import ABC, abstractmethod

class Decryptor(ABC):

    @abstractmethod
    def decrypt(self, ciphertext, key):
        pass