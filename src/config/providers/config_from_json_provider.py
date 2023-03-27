import json
from  src.config.providers.base_config import BaseConfig

class ConfigFromJsonProvider(BaseConfig):
    """
    Configuration through JSON file.
    """
    def __init__(self, config_path):
        """
        : param config_path: Path to the JSON configuration file.
        """
        with open(config_path) as json_file:
            self._config_data = json.load(config_path)

    def get(self, key):
        """
        Returns config value for the given key.
        : param str key: Key to retrieve.
        """
        val = self._config_data.get(key)
        return val