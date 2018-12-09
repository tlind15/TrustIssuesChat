from src.ui.input import MessageInput
from src.message.send_message_controller import SendMessageController
from src.authentication.session_initializer import SessionInitializer
from src.message.receive_message_controller import ReceiveMessageController
from src.temp_decrypt.controller import DecryptionController


class TrustIssuesChat(object):

    session = None

    @staticmethod
    def start():
        print("**********TrustIssues Chat**********")
        TrustIssuesChat.session = SessionInitializer.initialize_session()
        TrustIssuesChat._home_screen()

    @staticmethod
    def _home_screen():
        while True:
            try:
                selection = int(input("\nMain Menu\n(1) Send a new message\n(2) Check Messages\n(3) Exit\n\nSelection: "))
                if selection != 1 and selection != 2:
                    print("Not a valid selection\n")
                else:
                    break
            except ValueError:
                print("Not a valid input\n")

        # this dictionary has the function names
        options = {1: TrustIssuesChat._create_message, 2: TrustIssuesChat._check_messages, 3: TrustIssuesChat._exit}
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
            controller = SendMessageController(TrustIssuesChat.session)
            response = controller.send_message(message_text, MessageInput.read_recipient())
            TrustIssuesChat._home_screen()

    @staticmethod
    def _check_messages():
        data = ReceiveMessageController.get_messages(TrustIssuesChat.session.user.username,
                                                         TrustIssuesChat.session.jwt_token)
        controller = DecryptionController("C:\\Users\\tlindblom\\RSAKeys\\private.pem")
        plaintext_messages = []
        for entry in data:
            plaintext_messages.append(controller.decrypt_message(entry["message"]))
        for msg in plaintext_messages:
            print(msg.get_text().decode())
        TrustIssuesChat._home_screen()

    @staticmethod
    def _exit():
        print("\nGoodbye!")

