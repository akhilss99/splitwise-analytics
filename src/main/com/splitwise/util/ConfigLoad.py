import importlib.resources
import importlib.util
import json

import yaml

from src.main.com.splitwise.util import RESOURCE_MODULE


class ConfigUtil:

    @staticmethod
    def load_json(filename: str) -> dict[str, str]:
        data = importlib.resources.open_text(RESOURCE_MODULE, filename, 'utf-8')
        return json.loads(data.read())

    @staticmethod
    def get_queries(filename: str) -> dict[str, str]:
        stream = importlib.resources.open_binary(RESOURCE_MODULE, filename)
        return yaml.load(stream=stream, Loader=yaml.SafeLoader)
