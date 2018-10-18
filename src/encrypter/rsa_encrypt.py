from src.encrypter.encryptor import Encryptor
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.backends import default_backend


class RSAEncrypt(Encryptor):

    def encrypt(self, message, key):
        """
        Encrypts a message using a 2048-bit RSA key

        :param message: a byte String containing the key (or key concatenated together) to be encrypted
        :param key: a byte String representing the RSA public key
        :return: a byte String representing the encrypted message
        """
        if isinstance(message, str):
            message.encode()

        elif not isinstance(message, bytes):
            raise TypeError("The argument 'message' is not of type 'bytes'")

        if not isinstance(key, rsa.RSAPublicKey):
            raise TypeError("The argument 'key' is not a valid RSA public key")

        return key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def get_key(self, key_path):
        """
        Loads the RSA public from the user's local machine

        :param key_path: a String representing the path on the user's local machine containing the RSA public key
        :return: an RSAPublicKey object from the Cryptography library to be used in the 'encrypt' method
        """

        if not isinstance(key_path, str):
            raise TypeError("The argument 'key_path' is not of type 'str'")

        public_key = None

        try:
            with open(key_path, "rb") as key_file:
                public_key = load_pem_public_key(
                    key_file.read(),
                    backend=default_backend()
                )
        except IOError:
            print("Could not find RSA key")

        return public_key

    '''def get_priv_key(self, key_path):
        with open(key_path, "rb") as key_file:
            private_key = load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key'''
