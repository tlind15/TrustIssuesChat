from src.authentication.session import Session
from src.configuration.jwt_config import JWTConfig
from src.json_data.json_constructor import JsonConstructor
from src.json_data.json_constructor_strategy import CheckTokenJsonStrategy
from src.server.server_boundary import ServerBoundary
from src.server.server_command import CheckTokenCommand


class SessionInitializer(object):

    @staticmethod
    def initialize_session():
        jwt_config = JWTConfig()
        if not jwt_config.does_configuration_exist():
            pass # send to signup

        else:
            if jwt_config.get_token() is None:
                pass # send to login

            else:
                data = JsonConstructor.build_json(CheckTokenJsonStrategy(jwt_config.get_username()))
                response = ServerBoundary.send_request(CheckTokenCommand(data))
                if not response["status"]:
                    pass # send to login

        return Session(jwt_config.get_username(), jwt_config.get_token())






