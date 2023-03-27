import os

from src.config.providers.config_from_env_provider import ConfigFromEnvProvider
from src.config.providers.config_from_json_provider import ConfigFromJsonProvider


class Config:
    default_config = "dev"

    def __init__(self):

        
        
        self.providers = [
            ConfigFromEnvProvider(),
            ConfigFromJsonProvider(json_path)
        ]

    def register(self, name):
        pass
    
    def set(self, key, val):
        pass
    
    def get(self, val):
        pass
    
# singletone
config = Config()