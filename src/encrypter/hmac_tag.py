from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from os import urandom

class HMAC:

    def generate_tag(self, message, key=None):
        if key is None:
            key = self.get_key()

        tag_generator = hmac.HMAC(key, hashes=hashes.SHA256(), backend=default_backend())
        tag_generator.update(message)


    def get_key(self):
        return urandom(32)