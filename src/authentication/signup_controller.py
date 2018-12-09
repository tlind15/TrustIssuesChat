from src.json_data.json_constructor import JsonConstructor
from src.json_data.json_constructor_strategy import SignupLoginJsonStrategy
from src.server.server_boundary import ServerBoundary
from src.server.server_command import SignupCommand
from src.configuration.jwt_config import JWTConfig


class SignupController(object):

    @staticmethod
    def signup(user):
        data = JsonConstructor.build_json(SignupLoginJsonStrategy(user))
        response = ServerBoundary.send_request(SignupCommand(data)).json()
        config = JWTConfig()
        config.create_configuration(user.username)
        return response["data"]


