from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from os import urandom
from src.message.message import HMACHashedMessage


class HMAC(object):

    def generate_tag(self, message_text, key=None):
        if key is None:
            key = self.get_key()

        tag_generator = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        tag_generator.update(message_text)
        hashed_text = tag_generator.finalize()
        return HMACHashedMessage(hashed_text, key, hashes.SHA256())

    def get_key(self):
        return urandom(32)
