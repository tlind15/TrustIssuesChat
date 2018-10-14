from src.encrypter import aes_encrypt, rsa_encrypt, hmac_tag
from src.message.message import EncryptedMessage


class EncryptionController(object):

    def __init__(self, message_text, rsa_public_key_path):
        self.message_text = message_text
        self.rsa_public_key_path = rsa_public_key_path

    def encrypt_message(self):
        aes_encryptor = aes_encrypt.AESEncrypt()
        aes_ciphertext, aes_key = aes_encryptor.encrypt(self.message_text)

        hmac_tag_generator = hmac_tag.HMAC()
        hashed_message_obj = hmac_tag_generator.generate_tag(aes_ciphertext)

        rsa_encrytor = rsa_encrypt.RSAEncrypt()
        rsa_key = rsa_encrytor.get_key(self.rsa_public_key_path)
        rsa_ciphertext = rsa_encrytor.encrypt(aes_key + hashed_message_obj.key, rsa_key)

        return EncryptedMessage(key_ciphertext=rsa_ciphertext, message_ciphertext=aes_ciphertext,
                                message_authentication_tag=hashed_message_obj.get_text())
