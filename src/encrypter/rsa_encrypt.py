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
        with open(key_path, "rb") as key_file:
            public_key = load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key

    '''def get_priv_key(self, key_path):
        with open(key_path, "rb") as key_file:
            private_key = load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key'''



'''r = RSAEncrypt()
plaintext = "hello"
print(plaintext)
ciphertext = r.encrypt(plaintext, r.get_key("C:\\Users\\tlindblom\\RSAKeys\\public.pem"))
print(ciphertext)
new_plaintext = r.get_priv_key("C:\\Users\\tlindblom\\RSAKeys\\private.pem").decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(new_plaintext.decode())
'''
