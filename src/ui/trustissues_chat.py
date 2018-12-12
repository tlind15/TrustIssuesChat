from src.ui.input import MessageInput
from src.ui.friends_ui import FriendRequestUI
from src.message.send_message_controller import SendMessageController
from src.authentication.session_initializer import SessionInitializer
from src.message.receive_message_controller import ReceiveMessageController
from src.decrypter.controller import DecryptionController
from src.friends.friend_requests import GetPendingFriendRequestController
from src.friends.add_friends import AddRSADetailsOfFriendsController


class TrustIssuesChat(object):

    session = None

    @staticmethod
    def start():
        print("**********TrustIssues Chat**********")
        TrustIssuesChat.session = SessionInitializer.initialize_session()
        GetPendingFriendRequestController.get_pending_friend_requests(TrustIssuesChat.session)
        AddRSADetailsOfFriendsController.add_rsa_entries(TrustIssuesChat.session)
        AddRSADetailsOfFriendsController.add_friends_rsa_keys(TrustIssuesChat.session.rsa_config)
        TrustIssuesChat._home_screen()

    @staticmethod
    def _home_screen():
        #print(TrustIssuesChat.session.user.username)
        #print(TrustIssuesChat.session.token)
        #print(TrustIssuesChat.session.rsa_config.my_rsa)
        #print(TrustIssuesChat.session.user_config.config_data)
        while True:
            try:
                selection = int(input("\nMain Menu\n(1) Send a new message\n(2) Check Messages\n(3) Send Friend Request\n(4) Exit\n\nSelection: "))
                if selection != 1 and selection != 2 and selection != 3 and selection != 4:
                    print("Not a valid selection\n")
                else:
                    break
            except ValueError:
                print("Not a valid input\n")

        # this dictionary has the function names
        options = {1: TrustIssuesChat._create_message, 2: TrustIssuesChat._check_messages,
                   3: TrustIssuesChat._send_friend_request, 4: TrustIssuesChat._exit}
        options[selection]()  # this calls the function using the '()' with the name selected from the dictionary

    @staticmethod
    def _create_message():
        message_text = MessageInput.read_message()
        recipient = MessageInput.read_recipient(TrustIssuesChat.session.rsa_config)
        TrustIssuesChat._confirm_message(message_text, recipient)


    @staticmethod
    def _confirm_message(message_text, recipient):
        selection = "N"
        while True:
            try:
                selection = str(input("Send message to " + recipient + "? (Y/N) "))
                if selection.upper() != "Y" and selection.upper() != "N":
                    print("Not a valid selection\n")
                else:
                    break
            except ValueError:
                print("Not a valid input\n")
            finally:
                if selection.upper() == "Y":
                    TrustIssuesChat._send_message(message_text, recipient)
                elif selection.upper() == "N":
                    TrustIssuesChat._home_screen()

    @staticmethod
    def _send_message(message_text, recipient):
            controller = SendMessageController(TrustIssuesChat.session)
            response = controller.send_message(message_text, recipient)
            TrustIssuesChat._home_screen()

    @staticmethod
    def _check_messages():
        data = ReceiveMessageController.get_messages(TrustIssuesChat.session)
        # "C:\\Users\\tlindblom\\RSAKeys\\private.pem"
        controller = DecryptionController(TrustIssuesChat.session.rsa_config.my_rsa["private key"])
        for entry in data:
            plaintext_message = controller.decrypt_message(entry["message"])
            sender = entry["sender"]
            time = entry["time"]
            print("\nMessage from: " + sender)
            print("Time sent:" + time)
            print("Message: " + plaintext_message.get_text().decode())
        TrustIssuesChat._home_screen()

    @staticmethod
    def _send_friend_request():
        FriendRequestUI.send_friend_request(TrustIssuesChat.session)

    @staticmethod
    def _exit():
        print("\nGoodbye!")

