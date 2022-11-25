import abc
from dataclasses import asdict
import yaml
from box import Box
from os import path
import sys


# deprecate
def load_config(file_name=None):
    config_file = file_name if file_name is not None else get_main_name()
    with open(config_file, 'r') as stream:
        return yaml.safe_load(stream)


# deprecate
def has_main():
    try:
        get_main_name()
        return True
    except KeyError:
        return False


def get_main_name():
    app_name = sys.modules['__main__'].__file__.split('.')[0]
    return '{}.yaml'.format(app_name)


# deprecate
def init(file_name=None):
    return Box(load_config(file_name))


class Configuration(metaclass=abc.ABCMeta):

    @classmethod
    def init(cls, file_name=None):
        file_name = file_name if file_name is not None else get_main_name()
        if path.exists(file_name):
            config = cls.load(file_name)
            return config
        else:
            config = cls()
            config.save(file_name)
            return config

    @classmethod
    def load(cls, file_name):
        with open(file_name) as stream:
            params = yaml.safe_load(stream)
            return Box(params)

    def save(self, file_name):
        with open(file_name, 'w+') as file:
            file.write(yaml.dump(asdict(self)))
