from src.server.server_command import *


class ServerBoundary:

    @staticmethod
    def send_request(server_command):
        server_command.execute()
