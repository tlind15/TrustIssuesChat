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
        self._message = encrypted_message
        self._recipient = recipient_username

    def construct_json(self):
            return {"sender": self._username, "recipient": self._recipient,
                    "message": self._message.get_text(), "key": self._message.key_ciphertext,
                    "tag": self._message.message_authentication_tag, "iv": self._message.initialization_vector}


class CheckMessagesJsonStrategy(JsonConstructorStrategy):
    def __init__(self, user):
        self._username = user.username

    def construct_json(self):
        return {"sender", self._username}


class CheckTokenJsonStrategy(JsonConstructorStrategy):
    def __init__(self, username):
        self._username = username

    def construct_json(self):
        return {"sender", self._username}
