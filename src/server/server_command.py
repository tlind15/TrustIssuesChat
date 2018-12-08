from abc import ABC, abstractmethod
import requests


class ServerCommand(ABC):
    def __init__(self, data):
        self.data = data
        self.base_url = "https://donttrustthisgroup.me/"

    @abstractmethod
    def execute(self):
        pass


class SendMessageCommand(ServerCommand):

    def __init__(self, data, token):
        super().__init__(data)
        self._token = token
        self.url = super().base_url + "/send-message"

    def execute(self):
        header = {"Authorization": "Bearer " + self._token}
        return requests.post(self.url, self.data, headers=header)


class CheckMessagesCommand(ServerCommand):
    def __init__(self, data, token):
        super().__init__(data)
        self._token = token
        self.url = super().base_url + "/check-messages"

    def execute(self):
        header = {"Authorization": "Bearer " + self._token}
        return requests.get(self.url, params=self.data, headers=header)


class SignupCommand(ServerCommand):
    def __init__(self, data):
        super().__init__(data)
        self.url = super().base_url + "/signup"

    def execute(self):
        requests.post(self.url, self.data)


class LoginCommand(ServerCommand):
    def __init__(self, data):
        super().__init__(data)
        self.url = super().base_url + "/login"

    def execute(self):
        requests.post(self.url, self.data)


class CheckTokenCommand(ServerCommand):
    def __init__(self, data):
        super().__init__(data)
        self.url = super().base_url + "/check-valid-token"

    def execute(self):
        return requests.get(self.url, params=self.data)
