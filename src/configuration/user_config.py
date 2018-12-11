import json
import datetime


class UserConfig(object):
    def __init__(self, config_directory):
        self._config_directory = config_directory
        self.user_config_file = config_directory + "/UserConfig.txt"
        self.config_data = {}
        self.read_user_config()

    def read_user_config(self):
        try:
            with open(self.user_config_file, "r") as reader:
                self.config_data = json.loads(reader.read())
                reader.close()
        except FileNotFoundError:
            self._create_new_config()

    def _create_new_config(self):
        current_time = str(datetime.datetime.utcnow()).split('.')[0]
        self.config_data = {"message poll": current_time, "request poll": current_time}
        self.write_user_config()

    def write_user_config(self):
        with open(self.user_config_file, "w") as writer:
            writer.write(json.dumps(self.config_data))
            writer.close()

    def update_message_poll(self):
        self.read_user_config()
        current_time = str(datetime.datetime.utcnow()).split('.')[0]
        self.config_data["message poll"] = current_time
        self.write_user_config()

    def update_request_poll(self):
        self.read_user_config()
        current_time = str(datetime.datetime.utcnow()).split('.')[0]
        self.config_data["request poll"] = current_time
        self.write_user_config()
