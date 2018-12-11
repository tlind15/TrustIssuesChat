from src.json_data.json_constructor import JsonConstructor
from src.json_data.json_constructor_strategy import SignupLoginJsonStrategy
from src.server.server_boundary import ServerBoundary
from src.server.server_command import SignupCommand
from src.configuration.rsa_config import RSAConfig
from src.configuration.user_config import UserConfig
from src.authentication.session import Session


class SignupController(object):

    @staticmethod
    def signup(user, user_directory):
        data = JsonConstructor.build_json(SignupLoginJsonStrategy(user))
        response = ServerBoundary.send_request(SignupCommand(data)).json()
        rsa_config = RSAConfig(user_directory)
        user_config = UserConfig(user_directory)
        return Session(user, response["data"], rsa_config, user_config)


