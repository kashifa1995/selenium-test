import json
import os

from types import SimpleNamespace


class FileUtils:

    @staticmethod
    def read_json(file_path) -> dict:
        assert os.path.exists(file_path), f'No file found at {file_path}'

        with open(file_path, 'rb') as f:
            return json.load(f)

    @staticmethod
    def read_json_as_ns(file_path) -> SimpleNamespace:
        assert os.path.exists(file_path), f'No file found at {file_path}'

        with open(file_path, 'rb') as f:
            return json.load(f, object_hook=lambda d: SimpleNamespace(**d))

    @staticmethod
    def read_json_with_replace(file_path, data_to_replace: dict) -> SimpleNamespace:
        assert os.path.exists(file_path), f'No file found at {file_path}'

        with open(file_path, 'r') as f:
            data = f.read()

        for k, v in data_to_replace.items():
            data = data.replace(k, v)

        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))


