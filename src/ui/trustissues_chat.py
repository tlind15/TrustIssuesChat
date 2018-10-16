from src.ui.input import MessageInput
from src.message.message import PlaintextMessage, EncryptedMessage
from src.encrypter.controller import EncryptionController


class TrustIssuesChat(object):

    @staticmethod
    def start():
        print("***TrustIssues Chat***")
        TrustIssuesChat._home_screen()

    @staticmethod
    def _home_screen():
        selection = int(input("\n(1) Send a new message \n\n(2) Exit\n "))
        options = {1: TrustIssuesChat._create_message(), 2: TrustIssuesChat._exit()}
        options.get(selection, "\nInvalid Selection")

    @staticmethod
    def _create_message():
        message_text = MessageInput.read_message()
        options = {True: TrustIssuesChat._send_message(message_text), False: TrustIssuesChat._home_screen()}
        options.get(TrustIssuesChat._confirm_message())


    @staticmethod
    def _confirm_message():
        selection = str(input("Send message? (Y/N) "))
        options = {"Y": True, "N": False}
        return options.get(selection.upper(), "\nInvalid Selection")

    @staticmethod
    def _send_message(message_text):
        message_obj = PlaintextMessage(message_text)
        controller = EncryptionController(message_obj, "C:\\Users\\tlindblom\\RSAKeys\\public.pem")
        encrypted_message_obj = controller.encrypt_message()

        # send to output class or server

    @staticmethod
    def _exit():
        print("\nGoodbye!")

