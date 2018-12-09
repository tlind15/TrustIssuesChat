class ServerBoundary(object):

    @staticmethod
    def send_request(server_command):
        return server_command.execute()
