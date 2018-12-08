class JsonConstructor(object):

    @staticmethod
    def build_json(json_constructor_strategy):
        return json_constructor_strategy.construct_json()
