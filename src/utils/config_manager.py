import json
import os
from os import path
from types import SimpleNamespace

from src.utils.FileUtils import FileUtils


class Config(object):
    DEFAULT_ENV = 'qa.dev'

    def __init__(self):
        self.path = path.abspath(f'{__file__}/../../config/conf.json')
        with open(self.path, 'r') as json_file:
            self.data = json.load(json_file)

    def get_config(self):
        data_to_replace = self.resolve_env()

        new_data: SimpleNamespace = FileUtils.read_json_with_replace(
            self.path,
            data_to_replace,
        )
        return new_data

    def resolve_env(self):
        data_to_replace = {}
        if "ENV" in os.environ:
            data_to_replace['{env}'] = os.environ["ENV"]
        else:
            data_to_replace['{env}'] = self.DEFAULT_ENV
        return data_to_replace


__config = Config()
conf = __config.get_config()

if __name__ == '__main__':
    print(conf['boat']['boat_homepage_url'])
