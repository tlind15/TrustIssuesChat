import json
from src.ui.rsa_config_ui import RSAConfigUI
import os


class RSAConfig(object):
    def __init__(self, config_directory):
        self.my_rsa = {}
        self.friends_rsa = {}
        self._config_directory = config_directory
        self._my_rsa_file = config_directory + "/MyRSA.txt"
        self._friend_rsa_file = config_directory + "/FriendsRSA.txt"
        self.read_my_rsa()

    def read_my_rsa(self):
        try:
            with open(self._my_rsa_file, "r") as reader:
                self.my_rsa = json.loads(reader.read())
                reader.close()
        except FileNotFoundError:
            os.makedirs(self._config_directory)
            public_key, private_key = RSAConfigUI.get_rsa_config_data()
            self._write_my_rsa(public_key, private_key)

    def _write_my_rsa(self, my_rsa_public_key_path=None, my_rsa_private_key_path=None):
        self.my_rsa = {"public key": my_rsa_public_key_path, "private key": my_rsa_private_key_path}

        with open(self._my_rsa_file, "w") as writer:
            writer.write(json.dumps(self.my_rsa))
            writer.close()

    def read_friends_rsa(self):
        try:
            with open(self._friend_rsa_file, "r") as reader:
                self.friends_rsa = json.loads(reader.read())
                reader.close()
        except FileNotFoundError:
            pass

    def add_to_friends_rsa(self, friend_email, friend_rsa_path):
        self.read_friends_rsa()
        self.friends_rsa[friend_email] = friend_rsa_path
        with open(self._friend_rsa_file, "w") as writer:
            writer.write(json.dumps(self.friends_rsa))
            writer.close()
