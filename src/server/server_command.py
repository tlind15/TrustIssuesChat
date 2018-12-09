from abc import ABC, abstractmethod
import json
import requests
from base64 import b64encode, b64decode


class ServerCommand(ABC):
    def __init__(self, data):
        self.data = data
        self.base_url = "https://donttrustthisgroup.me"

    @abstractmethod
    def execute(self):
        pass


class SendMessageCommand(ServerCommand):

    def __init__(self, data, token):
        super().__init__(data)
        self._token = token
        self.url = self.base_url + "/send-message"

    def execute(self):
        header = {u'content-type': u'application/json', "Authorization": "Bearer " + self._token}
        self.data['tag'] = b64encode(self.data['tag']).decode()
        self.data["iv"] = b64encode(self.data["iv"]).decode()
        self.data["key"] = b64encode(self.data["key"]).decode()
        self.data["message"] = b64encode(self.data["message"]).decode()
        return requests.post(self.url, json.dumps(self.data), headers=header)


class CheckMessagesCommand(ServerCommand):
    def __init__(self, data, token):
        super().__init__(data)
        self._token = token
        self.url = self.base_url + "/check-messages"

    def execute(self):
        header = {u'content-type': u'application/json', "Authorization": "Bearer " + self._token}
        return requests.get(self.url, params=self.data, headers=header).json()


class SignupCommand(ServerCommand):
    def __init__(self, data):
        super().__init__(data)
        self.url = self.base_url + "/signup"

    def execute(self):
        headers = {u'content-type': u'application/json'}
        return requests.post(self.url, headers=headers, data=json.dumps(self.data))


class LoginCommand(ServerCommand):
    def __init__(self, data):
        super().__init__(data)
        self.url = self.base_url + "/login"

    def execute(self):
        headers = {u'content-type': u'application/json'}
        return requests.post(self.url, headers=headers, data=json.dumps(self.data))


class CheckTokenCommand(ServerCommand):
    def __init__(self, data):
        super().__init__(data)
        self.url = self.base_url + "/check-valid-token"

    def execute(self):
        return requests.get(self.url, params=self.data)
