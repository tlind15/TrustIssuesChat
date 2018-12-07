import abc
from abc import abstractmethod


class JsonConstructorStrategy(abc):
    @abstractmethod
    def construct_json(self):
        pass


class SignupJsonStrategy(JsonConstructorStrategy):
    def construct_json(self):
        pass


class LoginJsonStrategy(JsonConstructorStrategy):
    def construct_json(self):
        pass


class SendMessageJsonStrategy(JsonConstructorStrategy):
    def construct_json(self):
        pass


class CheckMessagesJsonStrategy(JsonConstructorStrategy):
    def construct_json(self):
        pass
