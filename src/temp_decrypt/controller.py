from src.temp_decrypt.aes_decrypt import AESDecrypt
from src.temp_decrypt.rsa_decrypt import RSADecrypt
from src.temp_decrypt.message_authentication import AuthenticateMessage
from src.message.message import PlaintextMessage


class DecryptionController(object):

    def __init__(self, encrypted_message_obj, rsa_private_key_path):
        self.encrypted_message_obj = encrypted_message_obj
        self.rsa_private_key_path = rsa_private_key_path

    def decrypt_message(self):
        rsa_decrpyptor = RSADecrypt()
        key_plaintext = rsa_decrpyptor.decrypt(self.encrypted_message_obj.key_ciphertext,
                                               rsa_decrpyptor.get_priv_key(self.rsa_private_key_path))

        key_plaintext_length = len(key_plaintext)
        aes_key = key_plaintext[:key_plaintext_length//2]
        hmac_key = key_plaintext[key_plaintext_length//2:]
        is_message_authentic = AuthenticateMessage.authenticate(self.encrypted_message_obj.get_text(), hmac_key,
                                                                self.encrypted_message_obj.message_authentication_tag)
        if is_message_authentic:
            aes_decryptor = AESDecrypt()
            plaintext_message = aes_decryptor.decrypt(self.encrypted_message_obj.get_text(), aes_key,
                                                      self.encrypted_message_obj.initialization_vector)
            return PlaintextMessage(plaintext_message)
        else:
            return None

