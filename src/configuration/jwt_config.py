import json


class JWTConfig(object):
    def __init__(self):
        self._filename = "user.txt"
        self._configuration = None

    def create_configuration(self, username):
        self._configuration = {"username": username, "token": None}
        self._write_configuration()

    def does_configuration_exist(self):
        self._read_configuration()
        config_exists = self._configuration is not None
        print(config_exists)
        return config_exists

    def _read_configuration(self):
        try:
            with open(self._filename, "r+") as reader:
                self._configuration = json.loads(reader.read())
                reader.close()
        except FileNotFoundError:
            return

    def _write_configuration(self):
        with open(self._filename, "w") as writer:
            writer.write(json.dumps(self._configuration))
            writer.close()

    def set_token(self, token):
        if self._configuration is None:
            self._read_configuration()
        self._configuration["token"] = token
        return self

    def get_token(self):
        if self._configuration is None:
            self._read_configuration()
        return self._configuration["token"]

    def set_username(self, username):
        if self._configuration is None:
            self._read_configuration()
        self._configuration["username"] = username
        return self

    def get_username(self):
        if self._configuration is None:
            self._read_configuration()
        return self._configuration["username"]

    def commit_changes(self):
        self._write_configuration()
