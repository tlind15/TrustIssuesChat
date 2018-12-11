from src.server.server_boundary import ServerBoundary
from src.server.server_command import GetFriendsCommand
from src.json_data.json_constructor import JsonConstructor
from src.json_data.json_constructor_strategy import GetFriendsJsonStrategy
from src.email_action.send_email import SendEmail


class AddRSADetailsOfFriendsController(object):

    @staticmethod
    def add_rsa_entries(session):
        friends = AddRSADetailsOfFriendsController._get_friends(session)
        session.rsa_config.read_friends_rsa()
        friend_dict = session.rsa_config.friends_rsa
        my_public_key = session.rsa_config.my_rsa["public key"]
        for friend in friends:
            if friend not in friend_dict:
                print('\nYou have a new friend: ' + friend)
                print('\nLet\' send them your RSA public key')
                session.rsa_config.add_to_friends_rsa(friend, None)
                SendEmail.send_email(friend, my_public_key)

        print(session.rsa_config.friends_rsa)

    @staticmethod
    def _get_friends(session):
        data = JsonConstructor.build_json(GetFriendsJsonStrategy(session.user))
        response = ServerBoundary.send_request(GetFriendsCommand(data, session.token)).json()
        return response["data"]

    @staticmethod
    def add_friends_rsa_keys(rsa_config):
        rsa_config.read_friends_rsa()
        rsa_friend_entries = rsa_config.friends_rsa
        for entry in rsa_friend_entries:
            if rsa_friend_entries[entry] is None or rsa_friend_entries[entry].strip() == "":
                rsa_config.add_to_friends_rsa(entry, AddRSADetailsOfFriendsController.prompt_for_missing_rsa_key(entry))

    @staticmethod
    def prompt_for_missing_rsa_key(friend):
        print("\nWe do not have a public key for: " + friend)

        selection = ""
        while selection.upper() != "Y" and selection.upper() != "N":
            selection = input("Would you like to add one? (Y/N)")
            if selection.upper() == "Y":
                return input("Add RSA public key path for: " + friend)
        return None





