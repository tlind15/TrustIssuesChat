class ServerBoundary(object):

    @staticmethod
    def send_request(server_command):
        server_command.execute()
