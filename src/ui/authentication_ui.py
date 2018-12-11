from src.authentication.user import User
from src.authentication.signup_controller import SignupController
from src.authentication.login_controller import LoginController

class AuthenticationUI(object):

    _user_directory = None

    @staticmethod
    def select_option():
        selection = int(input("What would you like to do? \n(1) Signup\n(2) Login\n\nSelection: "))
        actions = {1: AuthenticationUI.signup, 2: AuthenticationUI.login}
        return actions[selection]()


    @staticmethod
    def signup():
        print("*********Create New Account**********")
        return SignupController.signup(AuthenticationUI._get_credentials(), AuthenticationUI._user_directory)

    @staticmethod
    def login():
        print("*********Login**********")
        return LoginController.login(AuthenticationUI._get_credentials(), AuthenticationUI._user_directory)

    @staticmethod
    def _get_credentials():
        print("\nPlease input a username.")
        username = input("Username: ")
        print("Please enter a password")
        password = input("Password: ")
        AuthenticationUI._user_directory = "users/" + username
        return User(username, password)

