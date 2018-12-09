from src.authentication.session import Session
from src.configuration.jwt_config import JWTConfig
from src.authentication.signup_controller import SignupController
from src.authentication.login_controller import LoginController
from src.ui.authentication_ui import AuthenticationUI


class SessionInitializer(object):

    @staticmethod
    def initialize_session():
        jwt_config = JWTConfig()
        if not jwt_config.does_configuration_exist():
            user = AuthenticationUI.signup()
            token = SignupController.signup(user)

        else:
            user = AuthenticationUI.login()
            token = LoginController.login(user)

        '''else:
            if jwt_config.get_token() is None:
                pass # send to login

            else:
                data = JsonConstructor.build_json(CheckTokenJsonStrategy(jwt_config.get_username()))
                response = ServerBoundary.send_request(CheckTokenCommand(data))
                if not response["status"]:
                    pass # send to login'''
        jwt_config.set_token(token).commit_changes()
        return Session(user, token)






