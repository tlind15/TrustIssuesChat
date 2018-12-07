import abc
from abc import abstractmethod


class ServerCommand(abc):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def execute(self):
        pass


class SendMessageCommand(ServerCommand):
    def execute(self):
        pass


class CheckMessagesCommand(ServerCommand):
    def execute(self):
        pass


class SignupCommand(ServerCommand):
    def execute(self):
        pass


class LoginCommand(ServerCommand):
    def execute(self):
        pass
