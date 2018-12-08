from src.configuration.jwt_config import JWTConfig


class Session:
    def __init__(self, user, token=None):
        self.user = user
        if token is None:
            config = JWTConfig()
            self.jwt_token = config.get_token()
        else:
            self.jwt_token = token
