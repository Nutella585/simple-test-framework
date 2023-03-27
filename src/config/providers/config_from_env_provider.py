import os
from  src.config.providers.base_config import BaseConfig

class ConfigFromEnvProvider(BaseConfig):
    """
    Configuration through env variables.
    """
    def get(self, key):
        return os.environ.get(key)