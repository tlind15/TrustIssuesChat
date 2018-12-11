class Session:
    def __init__(self, user, token, rsa_config, user_config):
        self.user = user
        self.token = token
        self.rsa_config = rsa_config
        self.user_config = user_config
