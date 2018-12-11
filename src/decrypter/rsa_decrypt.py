from src.decrypter.decryptor import Decryptor
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


class RSADecrypt(Decryptor):

    def decrypt(self, ciphertext, key):
        return key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def get_priv_key(self, key_path):
        with open(key_path, "rb") as key_file:
            private_key = load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key
