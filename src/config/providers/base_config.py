class BaseConfig():
    """
    Base class for config providers,
    should not be used directly.
    """
    def get(self, key):
        raise NotImplementedError("BaseConfig() :: Not implemented yet.")