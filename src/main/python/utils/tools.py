from pyhocon import ConfigFactory


class Config(object):
    def __init__(self, conf_path):
        self._config = ConfigFactory.parse_file(conf_path)

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]

