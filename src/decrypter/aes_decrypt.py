from src.decrypter.decryptor import Decryptor
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.backends import default_backend


class AESDecrypt(Decryptor):

    def decrypt(self, ciphertext, key, iv=None):
        decryptor = Cipher(AES(key), modes.CBC(iv), backend=default_backend()).decryptor()
        ciphertext_with_padding = decryptor.update(ciphertext) + decryptor.finalize()
        return self.unpad(ciphertext_with_padding)

    def unpad(self, ciphertext_with_padding):
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(ciphertext_with_padding) + unpadder.finalize()


