from src.json_data.json_constructor_strategy import *


class JsonConstructor:

    def __init__(self, json_constructor_strategy):
        self._strategy = json_constructor_strategy

    def build_json(self):
        return self._strategy.construct_json()
