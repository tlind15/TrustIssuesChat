from src.server.server_boundary import ServerBoundary
from src.server.server_command import SendFriendRequestCommand, GetPendingFriendRequestsCommand, AddFriendCommand, \
    GetFriendsCommand
from src.json_data.json_constructor import JsonConstructor
from src.json_data.json_constructor_strategy import SendFriendRequestJsonStrategy, GetPendingFriendRequestsJsonStrategy,\
    AddFriendJsonStrategy, GetFriendsJsonStrategy
from src.email_action.send_email import SendEmail


class SendFriendRequestController(object):
    @staticmethod
    def send_friend_request(session, recipient_username):
        data = JsonConstructor.build_json(SendFriendRequestJsonStrategy(session.user, recipient_username))
        ServerBoundary.send_request(SendFriendRequestCommand(data, session.token))


class GetPendingFriendRequestController(object):
    @staticmethod
    def get_pending_friend_requests(session):
        data = JsonConstructor.build_json(GetPendingFriendRequestsJsonStrategy(session .user,
                                                                               session.user_config
                                                                               .config_data["request poll"]))
        session.user_config.update_request_poll()
        response = ServerBoundary.send_request(GetPendingFriendRequestsCommand(data, session.token)).json()
        requests = response["data"]

        if len(requests) > 0:
            for requester in requests:
                GetPendingFriendRequestController._accept_reject_requests(session, requester,
                                                                          session.rsa_config.my_rsa["public key"])
        else:
            print("\nYou have no pending friend requests!")

    @staticmethod
    def _accept_reject_requests(session, email_of_requester, rsa_public_key_path):
        print("\nYou have a friend request from: " + email_of_requester)
        selection = int(input("Would you like to accept?\n(1) Yes\n(2) No\n\nSelection: "))
        if selection == 1:
            SendEmail.send_email(email_of_requester, rsa_public_key_path)
            GetPendingFriendRequestController._add_friend(session.user, email_of_requester, session.token)

    @staticmethod
    def _add_friend(primary_user, email_of_requester, token):
        data = JsonConstructor.build_json(AddFriendJsonStrategy(primary_user, email_of_requester))
        response = ServerBoundary.send_request(AddFriendCommand(data, token))


