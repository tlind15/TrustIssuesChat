from abc import ABC
from encrypter import Encrypter
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.backends import default_backend


class RSAEncrypt(Encrypter):

    def __init__(self):
        pass

    def encrypt(self, message, key):
        return key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    def get_key(self, key_path):
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
