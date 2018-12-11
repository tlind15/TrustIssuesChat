from abc import ABC, abstractmethod


class JsonConstructorStrategy(ABC):
    @abstractmethod
    def construct_json(self):
        pass


class SignupLoginJsonStrategy(JsonConstructorStrategy):
    def __init__(self, user):
        self._user = user

    def construct_json(self):
        return {'username': self._user.username, 'password': self._user.password}


class SendMessageJsonStrategy(JsonConstructorStrategy):
    def __init__(self, user, encrypted_message, recipient_username):
        self._username = user.username
        self._password = user.password
        self._message = encrypted_message
        self._recipient = recipient_username

    def construct_json(self):
            return {"sender": self._username, "password": self._password, "recipient": self._recipient,
                    "message": self._message.get_text(), "key": self._message.key_ciphertext,
                    "tag": self._message.message_authentication_tag, "iv": self._message.initialization_vector}


class CheckMessagesJsonStrategy(JsonConstructorStrategy):
    def __init__(self, user, msg_polling_timestamp):
        self._user = user
        self._timestamp = msg_polling_timestamp

    def construct_json(self):
        return {"username": self._user.username, "password": self._user.password, "timestamp": self._timestamp}


class SendFriendRequestJsonStrategy(JsonConstructorStrategy):
    def __init__(self, user, recipient):
        self._user = user
        self._recipient = recipient

    def construct_json(self):
        return {"sender": self._user.username, "password": self._user.password, "recipient": self._recipient}


class GetPendingFriendRequestsJsonStrategy(JsonConstructorStrategy):
    def __init__(self, user, polling_timestamp):
        self._user = user
        self._timestamp = polling_timestamp

    def construct_json(self):
        return {"username": self._user.username, "password": self._user.password, "timestamp": self._timestamp}


class AddFriendJsonStrategy(JsonConstructorStrategy):
    def __init__(self, user, recipient):
        self._user = user
        self._recipient = recipient

    def construct_json(self):
        return {"user1": self._user.username, "password": self._user.password, "user2": self._recipient}


class GetFriendsJsonStrategy(JsonConstructorStrategy):
    def __init__(self, user):
        self._user = user

    def construct_json(self):
        return {"username": self._user.username, "password": self._user.password}
