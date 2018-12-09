from src.json_data.json_constructor import JsonConstructor
from src.json_data.json_constructor_strategy import SignupLoginJsonStrategy
from src.server.server_boundary import ServerBoundary
from src.server.server_command import LoginCommand
from src.configuration.jwt_config import JWTConfig


class LoginController(object):

    @staticmethod
    def login(user):
        data = JsonConstructor.build_json(SignupLoginJsonStrategy(user))
        response = ServerBoundary.send_request(LoginCommand(data)).json()
        print(response)
        config = JWTConfig()
        config.set_username(user.username).commit_changes()
        return response["data"]
