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
        while True:
            try:
                selection = int(input("\n(1) Send a new message \n\n(2) Exit\n "))
                if selection != 1 or selection != 2:
                    print("\nNot a valid selection\n")
                else:
                    break
            except TypeError:
                print("\nNot a valid input\n")

        options = {1: TrustIssuesChat._create_message(), 2: TrustIssuesChat._exit()}
        options.get(selection)

    @staticmethod
    def _create_message():
        message_text = MessageInput.read_message()
        TrustIssuesChat._confirm_message(message_text)


    @staticmethod
    def _confirm_message(message_text):
        while True:
            try:
                selection = str(input("Send message? (Y/N) "))
                if selection.upper() != "Y" or selection.upper() != "N":
                    print("\nNot a valid selection\n")
                else:
                    break
            except TypeError:
                print("\nNot a valid input\n")
        options = {"Y": TrustIssuesChat._send_message(message_text), "N": TrustIssuesChat._home_screen()}
        return options.get(selection.upper())

    @staticmethod
    def _send_message(message_text):

        if isinstance(message_text, str):
            message_text.encode()
        elif isinstance(message_text, bytes):
            raise TypeError("The argument 'message_text' is not of type 'str' or type 'bytes'")
    
        message_obj = PlaintextMessage(message_text)
        controller = EncryptionController(message_obj, "C:\\Users\\tlindblom\\RSAKeys\\public.pem")
        encrypted_message_obj = controller.encrypt_message()

        if encrypted_message_obj is None:
            print("\nUnable to send message")

        else:
            pass
            # send to output class or server

    @staticmethod
    def _exit():
        print("\nGoodbye!")

