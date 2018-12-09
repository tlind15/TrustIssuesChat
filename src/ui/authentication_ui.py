from src.authentication.user import User

class AuthenticationUI(object):

    @staticmethod
    def signup():
        print("*********Create New Account**********")
        return AuthenticationUI._get_credentials()

    @staticmethod
    def login():
        print("*********Login**********")
        return AuthenticationUI._get_credentials()

    @staticmethod
    def _get_credentials():
        print("\nPlease input a username.")
        username = input("Username: ")

        print("Please enter a password")
        password = input("Password: ")
        return User(username, password)

