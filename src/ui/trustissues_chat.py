from src.ui.input import MessageInput
from src.message.message import PlaintextMessage, EncryptedMessage
from src.encrypter.controller import EncryptionController


class TrustIssuesChat(object):

    @staticmethod
    def start():
        print("**********TrustIssues Chat**********")
        TrustIssuesChat._home_screen()

    @staticmethod
    def _home_screen():
        while True:
            try:
                selection = int(input("\nMain Menu\n(1) Send a new message\n(2) Exit\n\nSelection: "))
                if selection != 1 and selection != 2:
                    print("Not a valid selection\n")
                else:
                    break
            except ValueError:
                print("Not a valid input\n")

        # this dictionary has the function names
        options = {1: TrustIssuesChat._create_message, 2: TrustIssuesChat._exit}
        options[selection]()  # this calls the function using the '()' with the name selected from the dictionary

    @staticmethod
    def _create_message():
        message_text = MessageInput.read_message()
        TrustIssuesChat._confirm_message(message_text)


    @staticmethod
    def _confirm_message(message_text):
        selection = "N"
        while True:
            try:
                selection = str(input("Send message? (Y/N) "))
                if selection.upper() != "Y" and selection.upper() != "N":
                    print("Not a valid selection\n")
                else:
                    break
            except ValueError:
                print("Not a valid input\n")
            finally:
                if selection.upper() == "Y":
                    TrustIssuesChat._send_message(message_text)
                elif selection.upper() == "N":
                    TrustIssuesChat._home_screen()


    @staticmethod
    def _send_message(message_text):

        if isinstance(message_text, str):
            message_text = message_text.encode()
        elif isinstance(message_text, bytes):
            raise TypeError("The argument 'message_text' is not of type 'str' or type 'bytes'")

        message_obj = PlaintextMessage(message_text)
        controller = EncryptionController(message_obj, "C:\\Users\\tlindblom\\RSAKeys\\public.pem")
        encrypted_message_obj = controller.encrypt_message()

        if encrypted_message_obj is None:
            print("\nUnable to send message")

        else:
            print(encrypted_message_obj.get_text())
            # eventually pass to server, for now call the decryption controller and pass its output to the output class

    @staticmethod
    def _exit():
        print("\nGoodbye!")

