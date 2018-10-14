from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.backends import default_backend
from os import urandom
from cryptography.hazmat.primitives import padding
from src.encrypter.encryptor import Encryptor


class AESEncrypt(Encryptor):

    def encrypt(self, message_text, key=None):
        if key is None:
            key = self.get_key()

        algorithm = AES(key)
        cipher = Cipher(algorithm, mode=modes.CBC(self.get_iv()), backend=default_backend())
        encrypted_text = cipher.encryptor().update(self.pad_data(message_text)) + cipher.encryptor().finalize()
        return encrypted_text, key

    def get_key(self):
        return urandom(32)

    def get_iv(self):
        return urandom(16)

    def pad_data(self, message):
        encoded_message = message.encode()
        if len(encoded_message) % 16 == 0:
            return encoded_message
        else:
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(message.encode())
            padded_data += padder.finalize()
            return padded_data




