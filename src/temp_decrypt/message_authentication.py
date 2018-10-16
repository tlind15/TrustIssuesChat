from src.encrypter.hmac_tag import HMAC


class AuthenticateMessage(object):

    @staticmethod
    def authenticate(ciphertext, key, tag):
        return HMAC.generate_tag(ciphertext, key).get_text() == tag


