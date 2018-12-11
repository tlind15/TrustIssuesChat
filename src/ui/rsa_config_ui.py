class RSAConfigUI(object):

    @staticmethod
    def get_rsa_config_data():
        rsa_public_key_path = input("\nPlease input public key path: ")
        rsa_private_key_path = input("\nPlease input private key path: ")
        return rsa_public_key_path, rsa_private_key_path