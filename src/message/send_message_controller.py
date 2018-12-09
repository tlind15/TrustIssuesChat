from src.json_data.json_constructor import JsonConstructor
from src.json_data.json_constructor_strategy import SendMessageJsonStrategy
from src.server.server_boundary import ServerBoundary
from src.server.server_command import SendMessageCommand
from src.message.message import PlaintextMessage
from src.encrypter.controller import EncryptionController


class SendMessageController(object):
    def __init__(self, session):
        self._session = session

    def send_message(self, message_text, recipient_username):

        if isinstance(message_text, str):
            message_text = message_text.encode("utf-8")
        elif isinstance(message_text, bytes):
            raise TypeError("The argument 'message_text' is not of type 'str' or type 'bytes'")

        message_obj = PlaintextMessage(message_text)
        controller = EncryptionController(message_obj, "C:\\Users\\tlindblom\\RSAKeys\\public.pem")
        encrypted_message_obj = controller.encrypt_message()

        if encrypted_message_obj is None:
            print("\nUnable to send message")

        else:
            json_data = JsonConstructor.build_json(SendMessageJsonStrategy(self._session.user,
                                                                           encrypted_message_obj, recipient_username))
            r = ServerBoundary.send_request(SendMessageCommand(json_data, self._session.jwt_token))
            print(r.text)
