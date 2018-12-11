from src.authentication.session import Session
from src.authentication.signup_controller import SignupController
from src.authentication.login_controller import LoginController
from src.ui.authentication_ui import AuthenticationUI


class SessionInitializer(object):

    @staticmethod
    def initialize_session():
        return AuthenticationUI.select_option()








