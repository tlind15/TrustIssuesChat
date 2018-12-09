from abc import ABC, abstractmethod
from src.message.message import EncryptedMessage
from base64 import b64encode, b64decode

class JsonDeconstructor(object):
    @staticmethod
    def deconstruct_json(json_deconstructor):
        return json_deconstructor.deconstruct_json()


class JsonDeconstructorStrategy(ABC):
    @abstractmethod
    def deconstruct_json(self):
        pass


class ReceiveMessagesStrategy(JsonDeconstructorStrategy):
    def __init__(self, message_data):
        self._data = message_data

    def deconstruct_json(self):
        data_list = self._data["data"]
        message_list = []
        for entry in data_list:
            key = b64decode(entry['key'].encode())
            message = b64decode(entry['message'].encode())
            iv = b64decode(entry['iv'].encode())
            tag = b64decode(entry['tag'].encode())
            encrypted_msg = EncryptedMessage(key, message, iv, tag)
            message_list.append({"sender": entry["sender"], "message": encrypted_msg, "time": entry["time"]})
        return message_list

