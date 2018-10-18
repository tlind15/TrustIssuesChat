from src.encrypter import aes_encrypt, rsa_encrypt, hmac_tag
from src.message.message import Message, EncryptedMessage


class EncryptionController(object):

    def __init__(self, message_obj, rsa_public_key_path):
        """
        Class executes the use case for encrypting a message

        :param message_obj: an instance of the 'Message' class containing the message to be encrypted
        :param rsa_public_key_path: a String representing the file path to an RSA public key file on the user's local machine

        """
        if not isinstance(message_obj, Message):
            raise TypeError("The argument 'message_obj' is not of type 'Message'")

        if not isinstance(rsa_public_key_path, str):
            raise TypeError("The argument 'rsa_public_key_path' is not of type 'str'")

        self.message_obj = message_obj
        self.rsa_public_key_path = rsa_public_key_path

    def encrypt_message(self):
        """
        Encrypts a message

        :return: returns an instance of the 'EncryptedMessage' class that can be used by other modules
        """

        # we need to make sure the message_text parameter in the message_obj is of a correct type
        if isinstance(self.message_obj.get_text(), str):
            self.message_obj.get_text().encode()

        elif not isinstance(self.message_obj.get_text(), bytes):
            raise TypeError("The message text is not of type 'bytes'")

        # we don't have to check the type of the key path since that was done in the constructor

        aes_ciphertext, aes_key = self._perform_message_encrpytion(self.message_obj.get_text())
        hash_message_text, mac_key = self._generate_integrity_tag(aes_ciphertext)
        rsa_ciphertext = self._perform_rsa_encryption(aes_key + mac_key, self.rsa_public_key_path)

        if rsa_ciphertext is None:
            return None
        else:
            return EncryptedMessage(key_ciphertext=rsa_ciphertext, message_ciphertext=aes_ciphertext,
                                    message_authentication_tag=hash_message_text)

    def _perform_message_encrpytion(self, message_text):
        """
        Encrypts the message text from the 'message_obj' variable

        :param message_text: a byte String corresponding to the message text to be encrypted
        :return: a byte String representing the encrypted message text
        """
        aes_encryptor = aes_encrypt.AESEncrypt()
        return aes_encryptor.encrypt(message_text)

    def _generate_integrity_tag(self, message_ciphertext):
        """
        Computes a message integrity tag from the provided ciphertext

        :param message_ciphertext: a byte String representing an encrypted message
        :return: a byte String that represents the integrity tag of the 'message_ciphertext' variable
        """
        hashed_message_obj = hmac_tag.HMAC().generate_tag(message_ciphertext)
        return hashed_message_obj.get_text(), hashed_message_obj.key

    def _perform_rsa_encryption(self, message, key_path):
        """
        Encrypts the encryption key(s) used with RSA encryption

        :param message: a byte String representing the key(s) to be encrypted
        :param key_path: a String representing a file path to .pem RSA public key file on the user local machine
        :return: a byte String representing the encrypted key(s)
        """
        rsa_encryptor = rsa_encrypt.RSAEncrypt()
        rsa_key = rsa_encryptor.get_key(key_path)

        if rsa_key is None:
            return None
        return rsa_encryptor.encrypt(message, rsa_key)
