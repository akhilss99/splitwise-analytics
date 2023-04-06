from dotenv import load_dotenv
from pkg_resources import resource_stream
from yaml import load, SafeLoader

import os


class ConfigUtil:

    @staticmethod
    def get_conf(filename: str) -> dict[str, str]:
        stream = resource_stream("resources", filename)
        load_dotenv(dotenv_path=stream.name)
        return {
            "consumer_key": os.environ.get("consumer_key"),
            "consumer_secret": os.environ.get("consumer_secret"),
            "api_key": os.environ.get("api_key"),
            "GROUP_ID": os.environ.get("GROUP_ID")
        }

    @staticmethod
    def get_queries(filename: str) -> dict[str, str]:
        stream = resource_stream("resources", filename)
        return load(stream=stream, Loader=SafeLoader)
