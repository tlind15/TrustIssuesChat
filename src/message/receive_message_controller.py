from src.server.server_boundary import ServerBoundary
from src.server.server_command import CheckMessagesCommand
from src.json_data.json_constructor import JsonConstructor
from src.json_data.json_constructor_strategy import CheckMessagesJsonStrategy
from src.json_data.json_deconstructor import JsonDeconstructor, ReceiveMessagesStrategy


class ReceiveMessageController(object):
    @staticmethod
    def get_messages(session):
        data = JsonConstructor.build_json(CheckMessagesJsonStrategy(session.user,
                                                                    session.user_config.config_data["message poll"]))
        session.user_config.update_message_poll()
        response = ServerBoundary.send_request(CheckMessagesCommand(data, session.token)).json()
        return JsonDeconstructor.deconstruct_json(ReceiveMessagesStrategy(response))


